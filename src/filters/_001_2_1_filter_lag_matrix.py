#!/usr/bin/env python3
# ==========================================
# _001_2_filter_lag_matrix.py
# TLU System: Time-Lag (Cross-Correlation) Matrix Filter
# ==========================================
import sys
import argparse
import numpy as np
from typing import List

from src.filters.cli_parser import get_base_parser
from src.filters.stream_processor import setup_pipeline, yield_time_slices
from src.core.core_tensor_ops import compute_net_flux
from src.core.core_dynamics import compute_optimal_time_lag

def run_lag_matrix_analysis(q_history_list: List[np.ndarray], max_lag: int) -> List[list]:
    """ [Pure Orchestration Function] """
    if not q_history_list:
        return []

    q_hist_arr = np.array(q_history_list)
    N = q_hist_arr.shape[1]
    
    records = []
    
    for i in range(N):
        for j in range(N):
            sig_A = q_hist_arr[:, i]
            sig_B = q_hist_arr[:, j]
            
            # sig_A に対して sig_B がどれくらい遅れている(lag)か、またその時の相関係数
            best_lag, max_corr = compute_optimal_time_lag(sig_A, sig_B, max_lag)
            
            # ラベルは排除し、純粋なインデックスと数値のみを返す
            records.append([
                i, j, best_lag, f"{max_corr:.4f}"
            ])
            
    return records

def main():
    parser = get_base_parser("TLU Full Matrix Time-Lag Filter")
    parser.add_argument("--max_lag", type=int, default=6, help="探索する最大タイムラグ（ステップ数）")
    
    output_header = ["src_idx", "tgt_idx", "optimal_lag", "max_correlation"]
    args, N, reader, writer = setup_pipeline(parser, output_header)

    q_history_list = []
    
    # 1. ストリームから全期間の純フラックスを蓄積
    for _, T_slice in yield_time_slices(reader, N):
        q_current = compute_net_flux(T_slice)
        q_history_list.append(q_current)

    # 2. 全データが揃った後に一括で N x N の相関マトリクスを計算
    records = run_lag_matrix_analysis(q_history_list, args.max_lag)

    # 3. 結果の出力
    for rec in records:
        writer.writerow(rec)

if __name__ == "__main__":
    main()
