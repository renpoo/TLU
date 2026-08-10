#!/usr/bin/env python3
# ==========================================
# _002_2_1_filter_macro_forensics.py
# TLU System: Macro Forensics & Anomaly Detection Pipeline Filter
# Version: 8.0.0 (Refactored with BaseFilter Architecture)
# ==========================================
import sys
import argparse
import numpy as np
import pandas as pd
from typing import List, Tuple, Dict, Any

from src.filters.base_filter import BaseFilter, HistoryBuffer
from src.core.core_tensor_ops import compute_net_flux, compute_transition_matrix
from src.core.core_safe_linalg import compute_covariance_matrix, compute_safe_pinv, DEFAULT_RCOND, DEFAULT_LAMBDA_REG
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
) -> Tuple[List[list], np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """!
    @brief [Pure Orchestration Function] Run macroscopic forensics evaluation bounds.
    @details Legacy interface retained for backward compatibility with integration tests.
    """
    v_current = compute_net_flux(T_slice)
    P_current = compute_transition_matrix(T_slice)

    if len(X_history_window) == 0:
        X_current = X_initial + v_current
        X_prev = X_initial
    else:
        X_current = X_history_window[-1] + v_current
        X_prev = X_history_window[-1]
        
    g_current = v_current / (np.abs(X_prev) + 1.0)

    abs_residual, _ = check_conservation_law(
        v_current, 
        thresholds.get('leak_tolerance', 1e-5),
        thresholds.get('leak_idx', -1)
    )

    kl_drift = compute_structural_drift(P_current, P_history_window)

    if len(v_history_window) > 1:
        v_mean = np.mean(v_history_window, axis=0)
        v_cov_matrix = compute_covariance_matrix(np.array(v_history_window))
        v_K_precision = compute_safe_pinv(v_cov_matrix, rcond=DEFAULT_RCOND, lambda_reg=DEFAULT_LAMBDA_REG)
        z_score_v = compute_multivariate_anomaly(v_current, v_mean, v_K_precision)
        
        g_mean = np.mean(g_history_window, axis=0)
        g_cov_matrix = compute_covariance_matrix(np.array(g_history_window))
        g_K_precision = compute_safe_pinv(g_cov_matrix, rcond=DEFAULT_RCOND, lambda_reg=DEFAULT_LAMBDA_REG)
        z_score_X = compute_multivariate_anomaly(g_current, g_mean, g_K_precision)
    else:
        z_score_v = 0.0
        z_score_X = 0.0

    flag = evaluate_anomaly_flags(abs_residual, kl_drift, z_score_X, z_score_v, thresholds)

    record = [
        t_idx, 
        f"{abs_residual:.4f}", 
        f"{kl_drift:.4f}", 
        f"{z_score_X:.4f}", 
        f"{z_score_v:.4f}", 
        flag
    ]

    return [record], v_current, X_current, g_current, P_current


class MacroForensicsFilter(BaseFilter):
    cli_description = "TLU Forensics & Anomaly Detection Filter"
    output_header = ["t_idx", "conservation_residual", "kl_divergence_drift", "z_score_X", "z_score_v", "anomaly_flag"]
    history_config = {"v": 12, "X": 12, "g": 12, "P": 12}

    def add_arguments(self, parser: argparse.ArgumentParser):
        parser.add_argument("--baseline_window", type=int, default=12, help="Baseline construction period")
        parser.add_argument("--leak_tolerance", type=float, default=1e-5, help="Tolerance error for conservation law")
        parser.add_argument("--kl_drift_thresh", type=float, default=3.0, help="Anomaly threshold for structural change")
        parser.add_argument("--z_score_thresh", type=float, default=3.0, help="Anomaly threshold for Z-score")

    def process_slice(
        self, 
        t_idx: int, 
        T_slice: np.ndarray, 
        history: HistoryBuffer,
        X_initial: np.ndarray,
        args: argparse.Namespace
    ) -> Tuple[List[List[Any]], Dict[str, np.ndarray]]:
        
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

        v_hist = history.get("v")
        X_hist = history.get("X")
        g_hist = history.get("g")
        P_hist = history.get("P")

        records, v_current, X_current, g_current, P_current = run_forensics_analysis(
            t_idx, T_slice, v_hist, X_hist, g_hist, P_hist, X_initial, thresholds
        )

        state_updates = {
            "v": v_current,
            "X": X_current,
            "g": g_current,
            "P": P_current
        }

        return records, state_updates

def main():
    filter_app = MacroForensicsFilter()
    filter_app.run()

if __name__ == "__main__":
    main()
