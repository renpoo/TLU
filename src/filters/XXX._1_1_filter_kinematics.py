#!/usr/bin/env python3
# ==========================================
# _03_filter_kinematics.py
# TLU System: Phase B (Mathematical Filter)
# Category: Kinematics (Forward/Inverse Echo Analysis)
# Version: 7.4.0 (Refactored & Testable)
# ==========================================

import sys
import csv
import argparse
import numpy as np
import pandas as pd
from typing import List, Tuple

# 共有トポロジー演算ライブラリとストリームジェネレータ
from src.core.core_tensor_ops import compute_net_flux, compute_transition_matrix
from src.core.core_safe_linalg import compute_covariance_matrix, compute_safe_pinv
from src.core.core_kinematics import run_forward_simulation, solve_ik_with_safe_stiffness
from src.filters.stream_processor import yield_time_slices

def parse_args():
    parser = argparse.ArgumentParser(description="Kinematics and Mechanics Filter")
    parser.add_argument("--mode", type=str, choices=['fk', 'ik'], required=True, help="'fk' or 'ik'")
    parser.add_argument("--fk_input_mode", type=str, choices=['static', 'actual', 'impulse'], default='static', 
                        help="FK時の入力基準 (static: 固定仮想ショック, actual: 実質貢献度, impulse: 異常ショックの波及)")
    parser.add_argument("--input_dq", type=str, default="", help="For FK (static): Label-Value pairs (e.g., 'DPT_HR:1000,DPT_Marketing:500')")
    parser.add_argument("--target_dr", type=str, default="", help="For IK: Label-Value pairs (e.g., 'ACC_Sales:1000,ACC_COGS:-200')")
    parser.add_argument("--gamma", type=float, default=0.85, help="Damping factor")
    parser.add_argument("--max_k", type=int, default=5, help="Max echo steps")
    parser.add_argument("--node_map", type=str, default="_node_map.csv", help="Node map dictionary")
    return parser.parse_args()

def build_echo_matrix(P: np.ndarray, gamma: float, max_k: int) -> np.ndarray:
    """推移確率行列Pから、有限波及エコー行列 M_echo を構築する"""
    N = P.shape[0]
    M_echo = np.eye(N)
    current_P = np.eye(N)
    for k in range(1, max_k + 1):
        current_P = np.dot(current_P, P)
        M_echo += (gamma ** k) * current_P
    return M_echo

def resolve_inputs(args, node_map_path: str) -> Tuple[np.ndarray, List[int], np.ndarray, int, dict]:
    try:
        df_map = pd.read_csv(node_map_path)
        label_to_idx = dict(zip(df_map['node_label'], df_map['node_idx']))
        idx_to_label = dict(zip(df_map['node_idx'], df_map['node_label']))
        N = len(df_map)
    except Exception as e:
        print(f"Error loading node_map: {e}", file=sys.stderr)
        sys.exit(1)

    static_dq_input = np.zeros(N)
    target_ids = []
    target_dr_values = []

    if args.mode == 'fk' and args.input_dq:
        for pair in args.input_dq.split(','):
            if ':' in pair:
                lbl, val = pair.split(':')
                if lbl.strip() in label_to_idx:
                    static_dq_input[label_to_idx[lbl.strip()]] = float(val)

    if args.mode == 'ik' and args.target_dr:
        for pair in args.target_dr.split(','):
            if ':' in pair:
                lbl, val = pair.split(':')
                if lbl.strip() in label_to_idx:
                    target_ids.append(label_to_idx[lbl.strip()])
                    target_dr_values.append(float(val))

    if args.mode == 'ik' and not target_ids:
        print("Error: No valid target nodes specified for IK mode.", file=sys.stderr)
        sys.exit(1)

    return static_dq_input, target_ids, np.array(target_dr_values), N, idx_to_label

# --- 純粋関数 (テストの標的) ---
def run_kinematics_analysis(
    t_idx: int, T_slice: np.ndarray, q_history_list: List[np.ndarray],
    mode: str, fk_input_mode: str, static_dq_input: np.ndarray,
    target_ids: List[int], target_dr_values: np.ndarray,
    gamma: float, max_k: int
) -> Tuple[List[list], List[np.ndarray]]:
    
    N = T_slice.shape[0]
    q_current = compute_net_flux(T_slice)
    q_history_list.append(q_current)
    P_current = compute_transition_matrix(T_slice)
    
    # 剛性（K_safe）の動的学習
    q_hist_arr = np.array(q_history_list)
    if len(q_hist_arr) > 2:
        dq_history = np.diff(q_hist_arr, axis=0)
        covariance = compute_covariance_matrix(dq_history)
        K_safe = compute_safe_pinv(covariance, lambda_reg=1e-6)
    else:
        K_safe = np.eye(N)
        
    echo_impact_dq = np.zeros(N)
    suggested_ik_dq = np.zeros(N)
    strain_energy = 0.0
    
    # FK / IK の分岐
    if mode == 'fk':
        if fk_input_mode == 'static':
            current_input_dq = static_dq_input
        elif fk_input_mode == 'actual':
            current_input_dq = q_current
        elif fk_input_mode == 'impulse':
            if len(q_hist_arr) > 1:
                q_baseline = np.mean(q_hist_arr[:-1], axis=0)
                current_input_dq = q_current - q_baseline
            else:
                current_input_dq = np.zeros(N)

        echo_impact_dq = run_forward_simulation(P_current, current_input_dq, gamma, max_k)
        
    elif mode == 'ik':
        M_echo = build_echo_matrix(P_current, gamma, max_k)
        J = M_echo[:, target_ids].T 
        suggested_ik_dq = solve_ik_with_safe_stiffness(J, K_safe, target_dr_values)
        strain_energy = 0.5 * np.dot(suggested_ik_dq.T, np.dot(K_safe, suggested_ik_dq))

    # レコードの構築
    records = []
    for i in range(N):
        records.append([
            t_idx, i, f"{echo_impact_dq[i]:.4f}", f"{suggested_ik_dq[i]:.4f}", f"{strain_energy:.4f}"
        ])
        
    return records, q_history_list

# --- 極薄の I/O ラッパー層 ---
def main():
    args = parse_args()
    static_dq_input, target_ids, target_dr_values, N, idx_to_label = resolve_inputs(args, args.node_map)

    writer = csv.writer(sys.stdout)
    writer.writerow(["t_idx", "node_idx", "node_label", "fk_echo_impact", "ik_suggested_delta", "ik_strain_energy"])

    q_history_list = []
    reader = csv.reader(sys.stdin)
    
    # ジェネレータによる美しい I/O ループ
    for t_idx, T_slice in yield_time_slices(reader, N):
        records, q_history_list = run_kinematics_analysis(
            t_idx, T_slice, q_history_list,
            args.mode, args.fk_input_mode, static_dq_input,
            target_ids, target_dr_values,
            args.gamma, args.max_k
        )
        
        # ラベルを挿入して出力
        for rec in records:
            node_idx = rec[1]
            label = idx_to_label.get(node_idx, f"Node_{node_idx}")
            out_record = [rec[0], rec[1], label] + rec[2:]
            writer.writerow(out_record)

if __name__ == '__main__':
    main()
