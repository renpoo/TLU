#!/usr/bin/env python3
# ==========================================
# _003_1_3_filter_jacobian_trajectory.py
# TLU System: Jacobian Trajectory Extraction Filter
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

def run_jacobian_trajectory_analysis(
        t_idx: int, 
        T_slice: np.ndarray, 
        target_ids: List[int], 
        gamma: float, 
        max_k: int,
        order: int = 0
) -> List[list]:
    """!
    @brief Extract Jacobian elements from transition probability matrix propagation echo.
    @details Legacy interface retained for backward compatibility with unit tests.
    """
    N = T_slice.shape[0]
    records = []
    
    P_current = cto.compute_transition_matrix(T_slice)
    
    if order == 1:
        M = gamma * P_current
    elif order == 2:
        M = (gamma ** 2) * np.dot(P_current, P_current)
    elif order == 3:
        M = (gamma ** 3) * np.dot(np.dot(P_current, P_current), P_current)
    else:
        M = ck.build_echo_matrix(P_current, gamma, max_k)
    
    dst_nodes = target_ids if (target_ids is not None and len(target_ids) > 0) else list(range(N))
    
    for src in range(N):
        for dst in dst_nodes:
            val = M[src, dst]
            records.append([
                t_idx, src, dst, f"{val:.6f}"
            ])
            
    return records


class JacobianTrajectoryFilter(BaseFilter):
    cli_description = "TLU Jacobian Trajectory Filter"
    output_header = ["t_idx", "src_idx", "dst_idx", "jacobian_value"]

    def add_arguments(self, parser: argparse.ArgumentParser):
        parser.add_argument("--target_labels", type=str, default="", help="Target output nodes")
        parser.add_argument("--gamma", type=float, default=0.85)
        parser.add_argument("--max_k", type=int, default=5)
        parser.add_argument("--order", type=int, choices=[0, 1, 2, 3], default=0, help="Order of propagation path")

    def process_slice(
        self, 
        t_idx: int, 
        T_slice: np.ndarray, 
        history: HistoryBuffer,
        X_initial: np.ndarray,
        args: argparse.Namespace
    ) -> Tuple[List[List[Any]], Dict[str, np.ndarray]]:
        
        target_ids_list = []
        if args.target_labels:
            try:
                df_map = pd.read_csv(args.node_map)
                label_to_idx = dict(zip(df_map['node_label'], df_map['node_idx']))
                for lbl in args.target_labels.split(','):
                    lbl = lbl.strip()
                    if lbl in label_to_idx:
                        target_ids_list.append(int(label_to_idx[lbl]))
            except Exception as e:
                print(f"[WARN] Failed to parse target labels: {e}", file=sys.stderr)

        records = run_jacobian_trajectory_analysis(
            t_idx=t_idx,
            T_slice=T_slice,
            target_ids=target_ids_list,
            gamma=args.gamma,
            max_k=args.max_k,
            order=args.order
        )

        return records, {}

def main():
    filter_app = JacobianTrajectoryFilter()
    filter_app.run()

if __name__ == "__main__":
    main()
