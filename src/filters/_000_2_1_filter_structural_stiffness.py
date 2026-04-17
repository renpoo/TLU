#!/usr/bin/env python3
# ==========================================
# _000_2_1_filter_structural_stiffness.py
# TLU System: Structural Stiffness Matrix Filter
# Version: 7.6.0 (Partial Correlation Normalization Added)
# ==========================================
import sys
import argparse
import numpy as np
import pandas as pd
from typing import List, Tuple

from src.filters.cli_parser import get_base_parser
from src.filters.stream_processor import setup_pipeline, yield_time_slices

import src.core.core_tensor_ops as cto
import src.core.core_safe_linalg as csl

def compute_partial_correlation(K_precision: np.ndarray) -> np.ndarray:
    """ 
    [Pure Math] 精度行列 (K) から偏相関行列 (Partial Correlation) を算出する。
    値は常に -1.0 (完全な直接的逆相関/強い束縛) から 1.0 の範囲に正規化される。
    """
    N = K_precision.shape[0]
    R_partial = np.zeros((N, N), dtype=float)
    
    # 対角成分 (自己剛性)
    diag_K = np.diag(K_precision)
    # ゼロ割や負の平方根を防ぐための安全処理
    safe_diag = np.where(diag_K > 0, diag_K, 1e-15)
    
    for i in range(N):
        for j in range(N):
            if i == j:
                R_partial[i, j] = 1.0  # 自己の偏相関は定義上1.0とする
            else:
                # 偏相関係数の公式: r_ij = -K_ij / sqrt(K_ii * K_jj)
                val = -K_precision[i, j] / np.sqrt(safe_diag[i] * safe_diag[j])
                R_partial[i, j] = val
                
    # 数値計算上の微小な誤差で [-1.0, 1.0] を超えないようクリップ
    return np.clip(R_partial, -1.0, 1.0)

def run_structural_stiffness_analysis(
        t_idx: int, 
        T_slice: np.ndarray, 
        q_history: List[np.ndarray]
) -> Tuple[List[list], np.ndarray]:
    """ [Pure Orchestration Function] """    
    N = T_slice.shape[0]
    records = []

    q_current = cto.compute_net_flux(T_slice)
    
    temp_history = q_history + [q_current]
    q_hist_arr = np.array(temp_history)

    if len(q_hist_arr) > 2:
        dq_history = np.diff(q_hist_arr, axis=0)
        covariance = csl.compute_covariance_matrix(dq_history)
        K_safe = csl.compute_safe_pinv(covariance, rcond=1e-15, lambda_reg=1e-4)
        # ★ 追加: 偏相関行列への変換（人間界向けの正規化）
        R_partial = compute_partial_correlation(K_safe)
    else:
        K_safe = np.zeros((N, N))
        R_partial = np.zeros((N, N))

    for i in range(N):
        for j in range(N):
            records.append([
                t_idx, i, j, 
                f"{K_safe[i, j]:.12f}",
                f"{R_partial[i, j]:.4f}" # ★ 追加: 偏相関係数（-1.0 ~ 1.0）
            ])
            
    return records, q_current

def main():
    parser = get_base_parser("TLU Structural Stiffness Matrix Filter")
    parser.add_argument("--history_window", type=int, default=12, help="共分散計算に用いる履歴の長さ")
    
    # ★ 修正: ヘッダーに partial_corr を追加
    output_header = ["t_idx", "src_idx", "tgt_idx", "stiffness_k", "partial_corr"]
    args, N, reader, writer = setup_pipeline(parser, output_header)
    
    q_history_window = []

    for t_idx, T_slice in yield_time_slices(reader, N):
        records, q_current = run_structural_stiffness_analysis(
            t_idx=t_idx, 
            T_slice=T_slice, 
            q_history=q_history_window
        )
        
        q_history_window.append(q_current)
        if len(q_history_window) > args.history_window:
            q_history_window.pop(0)
            
        for rec in records:
            writer.writerow(rec)

if __name__ == "__main__":
    main()
