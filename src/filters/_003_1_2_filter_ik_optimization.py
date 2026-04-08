#!/usr/bin/env python3
# ==========================================
# _003_1_2_filter_ik_optimization.py
# TLU System: Inverse Kinematics (IK) Optimization Filter
# Version: 7.5.0 (Stiffness Override Injection Added)
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
import src.core.core_safe_linalg as csl

def run_ik_analysis(
        t_idx: int, 
        T_slice: np.ndarray, 
        q_history: List[np.ndarray],
        target_ids: List[int], 
        target_dr_values: np.ndarray,
        gamma: float, 
        max_k: int,
        penalty_arr: np.ndarray = None  # 追加: 外部からのペナルティ注入
) -> Tuple[List[list], np.ndarray]:
    """ [Pure Orchestration Function] """    
    N = T_slice.shape[0]
    records = []

    q_current = cto.compute_net_flux(T_slice)
    P_current = cto.compute_transition_matrix(T_slice)
    
    temp_history = q_history + [q_current]
    q_hist_arr = np.array(temp_history)
    
    # 1. ベースラインとなる剛性行列（K_safe）の算出
    if len(q_hist_arr) > 2:
        dq_history = np.diff(q_hist_arr, axis=0)
        covariance = csl.compute_covariance_matrix(dq_history)
        K_safe = csl.compute_safe_pinv(covariance, lambda_reg=1e-1)
    else:
        K_safe = np.eye(N)

    # 2. 外部ペナルティ（ハード制約）の合成
    if penalty_arr is not None and np.any(penalty_arr > 0):
        # K_safeの対角成分にペナルティを加算し、指定ノードを物理的に「固定」する
        np.fill_diagonal(K_safe, K_safe.diagonal() + penalty_arr)

    M_echo = ck.build_echo_matrix(P_current, gamma, max_k)
    J = M_echo[:, target_ids].T 
    
    suggested_ik_dq = ck.solve_ik_with_safe_stiffness(J, K_safe, target_dr_values)
    strain_energy = 0.5 * np.dot(suggested_ik_dq.T, np.dot(K_safe, suggested_ik_dq))

    for i in range(N):
        records.append([
            t_idx, i, 
            f"{suggested_ik_dq[i]:.4f}", f"{strain_energy:.4f}"
        ])
        
    return records, q_current

def main():
    parser = get_base_parser("TLU Inverse Kinematics Filter")
    parser.add_argument("--target_labels", type=str, default="", help="目標変位 (例: 'DPT_HR:100.0,DPT_Sales:200.0')")
    parser.add_argument("--stiffness_penalties", type=str, default="", help="特定のノードを固定する剛性ペナルティ (例: 'DPT_Legal:1e9')") # 追加
    parser.add_argument("--gamma", type=float, default=0.85)
    parser.add_argument("--max_k", type=int, default=5)
    
    output_header = ["t_idx", "node_idx", "ik_suggested_delta", "ik_strain_energy"]
    args, N, reader, writer = setup_pipeline(parser, output_header)
    
    target_ids_list = []
    target_dr_list = []
    penalty_arr = np.zeros(N) # 追加
    
    if args.target_labels or args.stiffness_penalties:
        try:
            df_map = pd.read_csv(args.node_map)
            label_to_idx = dict(zip(df_map['node_label'], df_map['node_idx']))
            
            # Targetのパース
            if args.target_labels:
                for pair in args.target_labels.split(','):
                    if ':' in pair:
                        lbl, val = pair.split(':', 1)
                        lbl = lbl.strip()
                        if lbl in label_to_idx:
                            target_ids_list.append(int(label_to_idx[lbl]))
                            target_dr_list.append(float(val))
                            
            # ペナルティのパース (追加)
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
    q_history_window = []

    for t_idx, T_slice in yield_time_slices(reader, N):
        records, q_current = run_ik_analysis(
            t_idx=t_idx, T_slice=T_slice, q_history=q_history_window,
            target_ids=target_ids_list, target_dr_values=target_dr_arr,
            gamma=args.gamma, max_k=args.max_k,
            penalty_arr=penalty_arr  # 追加
        )
        
        q_history_window.append(q_current)
        for rec in records:
            writer.writerow(rec)

if __name__ == "__main__":
    main()
