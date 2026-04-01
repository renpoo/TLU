#!/usr/bin/env python3
# ==========================================
# _1_13_filter_sensitivity.py
# TLU System: Meta-Analysis Layer (Sensitivity & Trade-off Matrix)
# ==========================================
import sys
import argparse
import numpy as np
import pandas as pd
from typing import List, Tuple

from src.filters.cli_parser import get_base_parser
from src.filters.stream_processor import setup_pipeline, yield_time_slices

import src.core.core_kinematics as ck
import src.core.core_tensor_ops as cto
import src.core.core_safe_linalg as csl

def run_sensitivity_analysis(
        t_idx: int, 
        T_slice: np.ndarray, 
        q_history: List[np.ndarray],
        delta: float,
        gamma: float, 
        max_k: int
) -> Tuple[List[list], np.ndarray]:
    """ 
    [Pure Orchestration Function]
    全ノードに対して「仮想投資(FK)」と「仮想目標(IK)」を総当たりで適用し、
    組織全体の感度（波及効果とひずみエネルギー）を算出する。
    """    
    N = T_slice.shape[0]
    records = []

    # 現在の状態と推移確率の計算
    q_current = cto.compute_net_flux(T_slice)
    P_current = cto.compute_transition_matrix(T_slice)
    M_echo = ck.build_echo_matrix(P_current, gamma, max_k)
    
    # 共分散と剛性行列 (K_safe) の計算
    temp_history = q_history + [q_current]
    q_hist_arr = np.array(temp_history)
    if len(q_hist_arr) > 2:
        dq_history = np.diff(q_hist_arr, axis=0)
        covariance = csl.compute_covariance_matrix(dq_history)
        K_safe = csl.compute_safe_pinv(covariance, lambda_reg=1e-1)
    else:
        K_safe = np.eye(N)

    # 全ノードに対して総当たりシミュレーション
    for i in range(N):
        # ------------------------------------------------
        # 1. FK Sensitivity (波及効率のテスト)
        # ノードi に delta の投資（ショック）を与えたら、全体がどう動くか？
        # ------------------------------------------------
        static_dq = np.zeros(N)
        static_dq[i] = delta
        echo_impact = ck.run_forward_simulation(P_current, static_dq, gamma, max_k)
        
        fk_total_ripple = np.sum(np.abs(echo_impact))  # 全体への波及量総和
        fk_impact_others = np.copy(echo_impact)
        fk_impact_others[i] = 0.0  # 自分自身への影響は除外
        fk_max_node = int(np.argmax(np.abs(fk_impact_others)))
        fk_max_impact = fk_impact_others[fk_max_node]

        # ------------------------------------------------
        # 2. IK Sensitivity (目標達成のひずみテスト)
        # ノードi を無理やり delta だけ押し上げたら、全体にどれだけの負荷がかかるか？
        # ------------------------------------------------
        J = M_echo[:, [i]].T 
        dq_opt = ck.solve_ik_with_safe_stiffness(J, K_safe, [delta])
        
        strain_energy = 0.5 * np.dot(dq_opt.T, np.dot(K_safe, dq_opt))  # 組織全体への摩擦/負荷
        ik_adjust_others = np.copy(dq_opt)
        ik_adjust_others[i] = 0.0  # 自分自身の変動は除外
        ik_max_node = int(np.argmax(np.abs(ik_adjust_others)))
        ik_max_adjust = ik_adjust_others[ik_max_node]

        records.append([
            t_idx, i, 
            f"{fk_total_ripple:.4f}", f"{fk_max_impact:.4f}", fk_max_node,
            f"{strain_energy:.4f}", f"{ik_max_adjust:.4f}", ik_max_node
        ])
        
    return records, q_current

def main():
    parser = get_base_parser("TLU Sensitivity & Trade-off Meta-Filter")
    parser.add_argument("--delta", type=float, default=10.0, help="仮想投資量 / 仮想目標変位量")
    parser.add_argument("--gamma", type=float, default=0.85)
    parser.add_argument("--max_k", type=int, default=5)
    parser.add_argument("--history_window", type=int, default=100)
    
    output_header = [
        "t_idx", "node_idx", 
        "fk_total_ripple", "fk_max_impact", "fk_max_impact_node",
        "ik_strain_energy", "ik_max_adjust", "ik_max_adjust_node"
    ]
    args, N, reader, writer = setup_pipeline(parser, output_header)
    
    q_history_window = []

    for t_idx, T_slice in yield_time_slices(reader, N):
        records, q_current = run_sensitivity_analysis(
            t_idx=t_idx, T_slice=T_slice, q_history=q_history_window,
            delta=args.delta, gamma=args.gamma, max_k=args.max_k
        )
        
        q_history_window.append(q_current)
        if len(q_history_window) > args.history_window:
            q_history_window.pop(0)
        
        for rec in records:
            writer.writerow(rec)

if __name__ == "__main__":
    main()
