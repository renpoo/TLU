#!/usr/bin/env python3
# ==========================================
# _003_1_3_filter_jacobian_trajectory.py
# TLU System: Jacobian Trajectory Extraction Filter
# ==========================================
import sys
import csv
import argparse
import numpy as np
import pandas as pd
from typing import List, Tuple

from src.filters.cli_parser import get_base_parser
from src.filters.stream_processor import setup_pipeline, yield_time_slices

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
    
    @param t_idx Sequence timestep index.
    @param T_slice Raw matrix bounding interactions.
    @param target_ids Constraint destination node indices (optional).
    @param gamma Damping coefficient.
    @param max_k Propagation step count.
    @param order Explicit propagation path order (1st, 2nd, 3rd matrix power, or 0 for full echo).
    
    @return List of records [t_idx, src_idx, dst_idx, jacobian_value].
    """
    N = T_slice.shape[0]
    records = []
    
    P_current = cto.compute_transition_matrix(T_slice)
    
    # Calculate target matrix based on requested order
    if order == 1:
        M = gamma * P_current
    elif order == 2:
        M = (gamma ** 2) * np.dot(P_current, P_current)
    elif order == 3:
        M = (gamma ** 3) * np.dot(np.dot(P_current, P_current), P_current)
    else:
        M = ck.build_echo_matrix(P_current, gamma, max_k)
    
    # Determine which target destination nodes to output
    dst_nodes = target_ids if (target_ids is not None and len(target_ids) > 0) else list(range(N))
    
    # M[i, j] represents sensitivity of node j (dst) with respect to input at node i (src)
    for src in range(N):
        for dst in dst_nodes:
            val = M[src, dst]
            records.append([
                t_idx, src, dst, f"{val:.6f}"
            ])
            
    return records

def main():
    parser = get_base_parser("TLU Jacobian Trajectory Filter")
    parser.add_argument("--target_labels", type=str, default="", help="Target output nodes (e.g.: 'DPT_HR,DPT_Sales')")
    parser.add_argument("--gamma", type=float, default=0.85)
    parser.add_argument("--max_k", type=int, default=5)
    parser.add_argument("--order", type=int, choices=[0, 1, 2, 3], default=0, help="Order of propagation path (1, 2, 3, or 0 for cumulative)")
    
    output_header = ["t_idx", "src_idx", "dst_idx", "jacobian_value"]
    args, N, reader, writer = setup_pipeline(parser, output_header)
    
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
            
    for t_idx, T_slice in yield_time_slices(reader, N):
        records = run_jacobian_trajectory_analysis(
            t_idx=t_idx,
            T_slice=T_slice,
            target_ids=target_ids_list,
            gamma=args.gamma,
            max_k=args.max_k,
            order=args.order
        )
        for rec in records:
            writer.writerow(rec)

if __name__ == "__main__":
    main()
