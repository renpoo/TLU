#!/usr/bin/env python3
# ==========================================
# _002_2_2_filter_micro_forensics.py
# TLU System: Micro Forensics (Node-specific Anomalies)
# Version: 8.0.0 (Refactored with BaseFilter Architecture)
# ==========================================
import sys
import argparse
import numpy as np
from typing import List, Tuple, Dict, Any

from src.filters.base_filter import BaseFilter, HistoryBuffer
from src.core.core_tensor_ops import compute_net_flux, compute_transition_matrix

def compute_node_kl_divergence_vector(
        P_current: np.ndarray, 
        P_history_window: List[np.ndarray], 
        epsilon: float = 1e-9
) -> np.ndarray:
    N = P_current.shape[0]
    if len(P_history_window) == 0:
        return np.zeros(N)
    
    P_mean_hist = np.mean(P_history_window, axis=0)
    P_current_safe = P_current + epsilon
    P_mean_hist_safe = P_mean_hist + epsilon
    
    ratio = P_current_safe / P_mean_hist_safe
    kl_matrix = P_current_safe * np.log(ratio)
    kl_vector = np.sum(kl_matrix, axis=1) 
    
    return np.maximum(kl_vector, 0.0)

def compute_node_univariate_z_score_vector(
        q_current: np.ndarray, 
        q_history_window: List[np.ndarray]
) -> np.ndarray:
    N = len(q_current)
    if len(q_history_window) < 2:
        return np.zeros(N)
    
    q_history_mat = np.array(q_history_window)
    q_mean_hist = np.mean(q_history_mat, axis=0)
    q_std_hist = np.std(q_history_mat, axis=0)
    
    deviation = q_current - q_mean_hist
    z_scores = np.divide(deviation, q_std_hist, out=np.zeros_like(deviation), where=q_std_hist!=0)
    
    return np.abs(z_scores)

def evaluate_micro_anomaly_flags(
        kl_vector: np.ndarray, 
        z_vector_g: np.ndarray,
        z_vector_v: np.ndarray, 
        thresholds: Dict[str, float]
) -> List[int]:
    N = len(kl_vector)
    flags = []
    for i in range(N):
        is_kl_anomaly = kl_vector[i] > thresholds.get('kl_drift_thresh', 3.0)
        is_z_X_anomaly = z_vector_g[i] > thresholds.get('z_score_thresh', 3.0)
        is_z_v_anomaly = z_vector_v[i] > thresholds.get('z_score_thresh', 3.0)
        
        flags.append(1 if (is_kl_anomaly or is_z_X_anomaly or is_z_v_anomaly) else 0)
    return flags

def run_micro_forensics_analysis(
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
    @brief [Pure Orchestration Function] Run micro anomaly heuristics on individual active structures.
    @details Legacy interface retained for backward compatibility with integration tests.
    """
    N = T_slice.shape[0]
    v_current = compute_net_flux(T_slice)
    P_current = compute_transition_matrix(T_slice)

    if len(X_history_window) == 0:
        X_current = X_initial + v_current
        X_prev = X_initial
    else:
        X_current = X_history_window[-1] + v_current
        X_prev = X_history_window[-1]

    g_current = v_current / (np.abs(X_prev) + 1.0)

    node_kl = compute_node_kl_divergence_vector(P_current, P_history_window)
    node_z_v = compute_node_univariate_z_score_vector(v_current, v_history_window)
    node_z_g = compute_node_univariate_z_score_vector(g_current, g_history_window)

    anomaly_flags = evaluate_micro_anomaly_flags(node_kl, node_z_g, node_z_v, thresholds)

    records = []
    for i in range(N):
        records.append([
            t_idx, i, 
            f"{node_z_g[i]:.4f}", 
            f"{node_z_v[i]:.4f}", 
            f"{node_kl[i]:.4f}", 
            anomaly_flags[i]
        ])

    return records, v_current, X_current, g_current, P_current


class MicroForensicsFilter(BaseFilter):
    cli_description = "TLU Micro Forensics (Node Anomaly) Filter"
    output_header = ["t_idx", "node_idx", "z_score_X", "z_score_v", "local_kl_drift", "micro_anomaly_flag"]
    history_config = {"v": 12, "X": 12, "g": 12, "P": 12}

    def add_arguments(self, parser: argparse.ArgumentParser):
        parser.add_argument("--baseline_window", type=int, default=12, help="Baseline construction period")
        parser.add_argument("--kl_drift_thresh", type=float, default=3.0, help="Anomaly threshold for micro KL divergence")
        parser.add_argument("--z_score_thresh", type=float, default=3.0, help="Anomaly threshold for univariate Z-score")

    def process_slice(
        self, 
        t_idx: int, 
        T_slice: np.ndarray, 
        history: HistoryBuffer,
        X_initial: np.ndarray,
        args: argparse.Namespace
    ) -> Tuple[List[List[Any]], Dict[str, np.ndarray]]:
        
        thresholds = {
            'kl_drift_thresh': args.kl_drift_thresh,
            'z_score_thresh': args.z_score_thresh
        }

        v_hist = history.get("v")
        X_hist = history.get("X")
        g_hist = history.get("g")
        P_hist = history.get("P")

        records, v_current, X_current, g_current, P_current = run_micro_forensics_analysis(
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
    filter_app = MicroForensicsFilter()
    filter_app.run()

if __name__ == "__main__":
    main()
