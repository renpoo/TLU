#!/usr/bin/env python3
# ==========================================
# _1_8_filter_forensics.py
# TLU System: Forensics & Anomaly Detection Pipeline Filter
# ==========================================
import sys
import argparse
import numpy as np
from typing import List, Tuple, Dict

from src.filters.cli_parser import get_base_parser
from src.filters.stream_processor import setup_pipeline, yield_time_slices

from src.core.core_tensor_ops import compute_net_flux, compute_transition_matrix
from src.core.core_safe_linalg import compute_covariance_matrix, compute_safe_pinv
# Fix: Individually import pure functions from core_forensics.py
from src.core.core_forensics import (
    check_conservation_law,
    compute_structural_drift,
    compute_multivariate_anomaly,
    evaluate_anomaly_flags
)

def run_forensics_analysis(
        t_idx: int, 
        T_slice: np.ndarray, 
        q_history_window: List[np.ndarray],
        P_history_window: List[np.ndarray],
        thresholds: Dict[str, float]
) -> Tuple[List[list], np.ndarray, np.ndarray]:
    """ [Pure Orchestration Function] """
    q_current = compute_net_flux(T_slice)
    P_current = compute_transition_matrix(T_slice)

    # 1. Check conservation of mass (System-wide residual)
    abs_residual, _ = check_conservation_law(q_current, thresholds.get('leak_tolerance', 1e-5))

    # 2. Structural drift (Sum of KL divergence)
    kl_drift = compute_structural_drift(P_current, P_history_window)

    # 3. Multivariate anomaly detection (Mahalanobis Z-score)
    if len(q_history_window) > 1:
        # Calculate expected value (mean) and precision matrix (inverse of covariance) from history
        q_mean = np.mean(q_history_window, axis=0)
        cov_matrix = compute_covariance_matrix(np.array(q_history_window))
        K_precision = compute_safe_pinv(cov_matrix, rcond=1e-15, lambda_reg=1e-4)
        
        z_score = compute_multivariate_anomaly(q_current, q_mean, K_precision)
    else:
        z_score = 0.0

    # 4. Comprehensive anomaly flag
    flag = evaluate_anomaly_flags(abs_residual, kl_drift, z_score, thresholds)

    # Because it's a macro indicator for the entire system, output only 1 row per time slice (node_idx is deprecated)
    record = [
        t_idx, 
        f"{abs_residual:.4f}", 
        f"{kl_drift:.4f}", 
        f"{z_score:.4f}", 
        flag
    ]

    return [record], q_current, P_current

def main():
    parser = get_base_parser("TLU Forensics & Anomaly Detection Filter")
    parser.add_argument("--baseline_window", type=int, default=12, help="Baseline construction period")
    parser.add_argument("--leak_tolerance", type=float, default=1e-5, help="Tolerance error for conservation law")
    parser.add_argument("--kl_drift_thresh", type=float, default=3.0, help="Anomaly threshold for structural change")
    parser.add_argument("--z_score_thresh", type=float, default=3.0, help="Anomaly threshold for Z-score")
    
    # Fix: Removed node_idx, updated header as an overall indicator
    output_header = [
        "t_idx", "conservation_residual", 
        "kl_divergence_drift", "mahalanobis_z_score", "anomaly_flag"
    ]
    args, N, reader, writer = setup_pipeline(parser, output_header)

    thresholds = {
        'leak_tolerance': args.leak_tolerance,
        'kl_drift_thresh': args.kl_drift_thresh,
        'z_score_thresh': args.z_score_thresh
    }

    q_history_window = []
    P_history_window = []

    for t_idx, T_slice in yield_time_slices(reader, N):
        records, q_current, P_current = run_forensics_analysis(
            t_idx, T_slice, q_history_window, P_history_window, thresholds
        )
        
        q_history_window.append(q_current)
        P_history_window.append(P_current)
        if len(q_history_window) > args.baseline_window:
            q_history_window.pop(0)
            P_history_window.pop(0)
            
        for rec in records:
            writer.writerow(rec)

if __name__ == "__main__":
    main()
