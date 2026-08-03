#!/usr/bin/env python3
# ==========================================
# _004_1_1_filter_control_theory.py
# TLU System: Control Theory Pipeline Filter (LQR)
# Version: 8.0.0 (Refactored with BaseFilter Architecture)
# ==========================================
import sys
import argparse
import numpy as np
import pandas as pd
from typing import List, Tuple, Dict, Any

from src.filters.base_filter import BaseFilter, HistoryBuffer
from src.core.core_tensor_ops import compute_net_flux, compute_transition_matrix
from src.core.core_control_theory import solve_lqr_gain, compute_optimal_input

def run_control_theory_analysis(
        t_idx: int, 
        T_slice: np.ndarray, 
        target_q: np.ndarray,
        controllable_indices: List[int],
        Q_weight: float = 1.0,
        R_weight: float = 0.1
) -> Tuple[List[list], np.ndarray]:
    """!
    @brief [Pure Orchestration Function] Run linear quadratic regulator feedback bounds.
    @details Legacy interface retained for backward compatibility with integration tests.
    """
    q_current = compute_net_flux(T_slice)
    N = len(q_current)

    A_matrix = compute_transition_matrix(T_slice)

    B_matrix = np.zeros((N, N))
    for idx in controllable_indices:
        if 0 <= idx < N:
            B_matrix[idx, idx] = 1.0

    Q_mat = np.eye(N) * Q_weight
    R_mat = np.eye(N) * R_weight

    K = solve_lqr_gain(A_matrix, B_matrix, Q_mat, R_mat)
    u_input = compute_optimal_input(K, q_current, target_q)

    x_error = q_current - target_q
    abs_x_error = np.abs(x_error)

    records = []
    for i in range(N):
        val_u = u_input[i] if i in controllable_indices else 0.0
        records.append([
            t_idx, i, 
            f"{val_u:.4f}", f"{abs_x_error[i]:.4f}"
        ])

    return records, q_current


class ControlTheoryFilter(BaseFilter):
    cli_description = "TLU Control Theory Filter (LQR)"
    output_header = ["t_idx", "node_idx", "optimal_input_u", "state_error_x"]

    def add_arguments(self, parser: argparse.ArgumentParser):
        parser.add_argument("--controllable_labels", type=str, default="", help="Controllable node labels")
        parser.add_argument("--target_state", type=str, default="", help="Target state vector")
        parser.add_argument("--q_weight", type=float, default=1.0, help="State error penalty weight (Q)")
        parser.add_argument("--r_weight", type=float, default=0.1, help="Input cost penalty weight (R)")

    def process_slice(
        self, 
        t_idx: int, 
        T_slice: np.ndarray, 
        history: HistoryBuffer,
        X_initial: np.ndarray,
        args: argparse.Namespace
    ) -> Tuple[List[List[Any]], Dict[str, np.ndarray]]:
        
        N = T_slice.shape[0]
        controllable_indices = []
        target_q = np.zeros(N)
        
        try:
            df_map = pd.read_csv(args.node_map)
            label_to_idx = dict(zip(df_map['node_label'], df_map['node_idx']))
            
            if args.controllable_labels:
                for lbl in args.controllable_labels.split(','):
                    lbl = lbl.strip()
                    if lbl in label_to_idx:
                        controllable_indices.append(int(label_to_idx[lbl]))
                        
            if args.target_state:
                for item in args.target_state.split(','):
                    parts = item.split(':')
                    if len(parts) == 2:
                        lbl = parts[0].strip()
                        val = float(parts[1].strip())
                        if lbl in label_to_idx:
                            target_q[int(label_to_idx[lbl])] = val
                            
        except Exception as e:
            print(f"[WARN] Failed to parse labels or targets: {e}", file=sys.stderr)

        records, q_current = run_control_theory_analysis(
            t_idx, T_slice, target_q, controllable_indices, args.q_weight, args.r_weight
        )

        return records, {}

def main():
    filter_app = ControlTheoryFilter()
    filter_app.run()

if __name__ == "__main__":
    main()
