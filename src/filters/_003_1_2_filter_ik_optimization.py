#!/usr/bin/env python3
# ==========================================
# _003_1_2_filter_ik_optimization.py
# TLU System: Inverse Kinematics (IK) Optimization Filter
# Version: 8.0.0 (Refactored with BaseFilter Architecture)
# ==========================================
import sys
import argparse
import numpy as np
import pandas as pd
from typing import List, Tuple, Dict, Any

from src.filters.base_filter import BaseFilter, HistoryBuffer
import src.core.core_kinematics as ck
import src.core.core_tensor_ops as cto
import src.core.core_safe_linalg as csl

def run_ik_analysis(
        t_idx: int, 
        T_slice: np.ndarray, 
        q_history: List[np.ndarray],
        target_ids: List[int], 
        target_dr_values: np.ndarray,
        gamma: float, 
        max_k: int,
        penalty_arr: np.ndarray = None
) -> Tuple[List[list], np.ndarray]:
    """!
    @brief [Pure Orchestration Function] Run inverse kinematics optimization.
    @details Legacy interface retained for backward compatibility with integration tests.
    """    
    N = T_slice.shape[0]
    records = []

    q_current = cto.compute_net_flux(T_slice)
    P_current = cto.compute_transition_matrix(T_slice)
    
    temp_history = q_history + [q_current]
    q_hist_arr = np.array(temp_history)
    
    if len(q_hist_arr) > 2:
        dq_history = np.diff(q_hist_arr, axis=0)
        covariance = csl.compute_covariance_matrix(dq_history)
        K_safe = csl.compute_safe_pinv(covariance, rcond=csl.DEFAULT_RCOND, lambda_reg=csl.DEFAULT_LAMBDA_REG)
    else:
        K_safe = np.eye(N)

    if penalty_arr is not None and np.any(penalty_arr > 0):
        np.fill_diagonal(K_safe, K_safe.diagonal() + penalty_arr)

    M_echo = ck.build_echo_matrix(P_current, gamma, max_k)
    J = M_echo[:, target_ids].T 
    
    suggested_ik_dq = ck.solve_ik_with_safe_stiffness(J, K_safe, target_dr_values, lambda_ratio=1e-4)
    strain_energy = 0.5 * np.dot(suggested_ik_dq.T, np.dot(K_safe, suggested_ik_dq))

    for i in range(N):
        records.append([
            t_idx, i, 
            f"{suggested_ik_dq[i]:.4f}", f"{strain_energy:.4f}"
        ])
        
    return records, q_current


class InverseKinematicsFilter(BaseFilter):
    cli_description = "TLU Inverse Kinematics Filter"
    output_header = ["t_idx", "node_idx", "ik_suggested_delta", "ik_strain_energy"]
    history_config = {"q": 100}

    def add_arguments(self, parser: argparse.ArgumentParser):
        parser.add_argument("--target_labels", type=str, default="", help="Target displacement")
        parser.add_argument("--stiffness_penalties", type=str, default="", help="Stiffness penalty to fix specific nodes")
        parser.add_argument("--gamma", type=float, default=0.85)
        parser.add_argument("--max_k", type=int, default=5)

    def process_slice(
        self, 
        t_idx: int, 
        T_slice: np.ndarray, 
        history: HistoryBuffer,
        X_initial: np.ndarray,
        args: argparse.Namespace
    ) -> Tuple[List[List[Any]], Dict[str, np.ndarray]]:
        
        N = T_slice.shape[0]
        target_ids_list = []
        target_dr_list = []
        penalty_arr = np.zeros(N)
        
        if args.target_labels or args.stiffness_penalties:
            try:
                df_map = pd.read_csv(args.node_map)
                label_to_idx = dict(zip(df_map['node_label'], df_map['node_idx']))
                
                if args.target_labels:
                    for pair in args.target_labels.split(','):
                        if ':' in pair:
                            lbl, val = pair.split(':', 1)
                            lbl = lbl.strip()
                            if lbl in label_to_idx:
                                target_ids_list.append(int(label_to_idx[lbl]))
                                target_dr_list.append(float(val))
                                
                if args.stiffness_penalties:
                    for pair in args.stiffness_penalties.split(','):
                        if ':' in pair:
                            lbl, val = pair.split(':', 1)
                            lbl = lbl.strip()
                            if lbl in label_to_idx:
                                idx = int(label_to_idx[lbl])
                                penalty_arr[idx] = float(val)
                                
            except Exception as e:
                print(f"[WARN] Failed to parse labels: {e}", file=sys.stderr)
                
        target_dr_arr = np.array(target_dr_list, dtype=float)
        q_hist = history.get("q")

        records, q_current = run_ik_analysis(
            t_idx=t_idx, T_slice=T_slice, q_history=q_hist,
            target_ids=target_ids_list, target_dr_values=target_dr_arr,
            gamma=args.gamma, max_k=args.max_k,
            penalty_arr=penalty_arr
        )

        return records, {"q": q_current}

def main():
    filter_app = InverseKinematicsFilter()
    filter_app.run()

if __name__ == "__main__":
    main()
