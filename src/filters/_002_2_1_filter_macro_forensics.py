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
        v_history_window: List[np.ndarray],
        X_history_window: List[np.ndarray],
        g_history_window: List[np.ndarray],
        P_history_window: List[np.ndarray],
        X_initial: np.ndarray,
        thresholds: Dict[str, float]
) -> Tuple[List[list], np.ndarray, np.ndarray, np.ndarray]:
    """!
    @brief [Pure Orchestration Function] Run macroscopic forensics evaluation bounds.
    @details Identifies graph-wide global anomaly conditions using multi-metric covariance tracking.

    @param t_idx Frame boundary index.
    @param T_slice Unfiltered interaction weight slice matrix.
    @param q_history_window Bounded tracking tensor for absolute shifts over temporal domains.
    @param P_history_window Tracking domains mapping stochastic baseline boundaries.
    @param thresholds Externally injected bounds mitigating explicit rigid parameters.

    @return Tuple (Flattened indicator rows list, pure flux vector, extracted P matrix).

    @pre
        - System strictly implements `leak_tolerance`, `kl_drift_thresh`, `z_score_thresh` definitions dynamically.
    @post
        - Degrades mathematically mitigating calculation bugs outputting safe zero boundaries implicitly.
    @invariant
        - Generates strict 1:1 scalar diagnostic mappings tracking network scale states.
    """
    v_current = compute_net_flux(T_slice)
    P_current = compute_transition_matrix(T_slice)

    # Calculate Absolute Balance X
    if len(X_history_window) == 0:
        X_current = X_initial + v_current
        X_prev = X_initial
    else:
        X_current = X_history_window[-1] + v_current
        X_prev = X_history_window[-1]
        
    # Calculate Relative Growth Rate g (Detrended Manifold)
    # epsilon=1.0 prevents division by zero and stabilizes tiny balances
    g_current = v_current / (np.abs(X_prev) + 1.0)

    # 1. Check conservation of mass (System-wide residual)
    abs_residual, _ = check_conservation_law(
        v_current, 
        thresholds.get('leak_tolerance', 1e-5),
        thresholds.get('leak_idx', -1)
    )

    # 2. Structural drift (Sum of KL divergence)
    kl_drift = compute_structural_drift(P_current, P_history_window)

    # 3. Multivariate anomaly detection (Mahalanobis Z-score)
    if len(v_history_window) > 1:
        # For velocity v
        v_mean = np.mean(v_history_window, axis=0)
        v_cov_matrix = compute_covariance_matrix(np.array(v_history_window))
        v_K_precision = compute_safe_pinv(v_cov_matrix, rcond=1e-15, lambda_reg=1e-4)
        z_score_v = compute_multivariate_anomaly(v_current, v_mean, v_K_precision)
        
        # For relative growth rate g (State Detrended Manifold)
        g_mean = np.mean(g_history_window, axis=0)
        g_cov_matrix = compute_covariance_matrix(np.array(g_history_window))
        g_K_precision = compute_safe_pinv(g_cov_matrix, rcond=1e-15, lambda_reg=1e-4)
        z_score_X = compute_multivariate_anomaly(g_current, g_mean, g_K_precision)
    else:
        z_score_v = 0.0
        z_score_X = 0.0

    # 4. Comprehensive anomaly flag
    flag = evaluate_anomaly_flags(abs_residual, kl_drift, z_score_X, z_score_v, thresholds)

    # Because it's a macro indicator for the entire system, output only 1 row per time slice (node_idx is deprecated)
    record = [
        t_idx, 
        f"{abs_residual:.4f}", 
        f"{kl_drift:.4f}", 
        f"{z_score_X:.4f}", 
        f"{z_score_v:.4f}", 
        flag
    ]

    return [record], v_current, X_current, g_current, P_current

def main():
    parser = get_base_parser("TLU Forensics & Anomaly Detection Filter")
    parser.add_argument("--baseline_window", type=int, default=12, help="Baseline construction period")
    parser.add_argument("--leak_tolerance", type=float, default=1e-5, help="Tolerance error for conservation law")
    parser.add_argument("--kl_drift_thresh", type=float, default=3.0, help="Anomaly threshold for structural change")
    parser.add_argument("--z_score_thresh", type=float, default=3.0, help="Anomaly threshold for Z-score")
    
    # Fix: Removed node_idx, updated header as an overall indicator
    output_header = [
        "t_idx", "conservation_residual", 
        "kl_divergence_drift", "z_score_X", "z_score_v", "anomaly_flag"
    ]
    args, N, reader, writer = setup_pipeline(parser, output_header)

    import pandas as pd
    leak_idx = -1
    try:
        df_map = pd.read_csv(args.node_map)
        leak_row = df_map[df_map['node_label'].isin(['UNKNOWN_LEAK', 'Unknown_Leak', 'ACC_Unknown_Leak'])]
        if not leak_row.empty:
            leak_idx = int(leak_row['node_idx'].iloc[0])
    except Exception as e:
        print(f"Warning: could not read leak node index: {e}", file=sys.stderr)

    thresholds = {
        'leak_tolerance': args.leak_tolerance,
        'kl_drift_thresh': args.kl_drift_thresh,
        'z_score_thresh': args.z_score_thresh,
        'leak_idx': leak_idx
    }

    from src.filters.stream_processor import load_initial_state
    import os
    env_dir = os.environ.get("TARGET_ENV", "workspace")
    X_initial = load_initial_state(env_dir, N)

    v_history_window = []
    X_history_window = []
    g_history_window = []
    P_history_window = []

    for t_idx, T_slice in yield_time_slices(reader, N):
        records, v_current, X_current, g_current, P_current = run_forensics_analysis(
            t_idx, T_slice, v_history_window, X_history_window, g_history_window, P_history_window, X_initial, thresholds
        )
        
        v_history_window.append(v_current)
        X_history_window.append(X_current)
        g_history_window.append(g_current)
        P_history_window.append(P_current)
        if len(v_history_window) > args.baseline_window:
            v_history_window.pop(0)
            X_history_window.pop(0)
            g_history_window.pop(0)
            P_history_window.pop(0)
            
        for rec in records:
            writer.writerow(rec)

if __name__ == "__main__":
    main()
