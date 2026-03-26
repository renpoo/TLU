#!/usr/bin/env python3
# ==========================================
# _1_4_filter_time_lag.py
# TLU System: Time Lag Analysis Batch Filter
# ==========================================
import sys
import csv
import argparse
import numpy as np
import pandas as pd
from typing import List, Tuple

from src.filters.cli_parser import get_base_parser
from src.filters.stream_processor import setup_pipeline, yield_time_slices
from src.core.core_tensor_ops import compute_net_flux
from src.core.core_dynamics import compute_optimal_time_lag

def run_time_lag_analysis(q_hist_arr: np.ndarray, target_pairs: List[Tuple[int, int]], max_lag: int) -> List[list]:
    """ [Pure Orchestration Function] """
    records = []
    for idx_A, idx_B in target_pairs:
        sig_A = q_hist_arr[:, idx_A]
        sig_B = q_hist_arr[:, idx_B]
        
        best_lag, max_corr = compute_optimal_time_lag(sig_A, sig_B, max_lag)
        records.append([idx_A, idx_B, best_lag, f"{max_corr:.4f}"])
        
    return records

def main():
    parser = get_base_parser("TLU Time Lag Analysis Filter")
    parser.add_argument("--signal_pairs_labels", type=str, default="", help="Format: 'LabelA:LabelB,LabelC:LabelD'")
    parser.add_argument("--max_lag", type=int, default=6)
    
    output_header = ["node_a_idx", "node_b_idx", "optimal_lag", "correlation"]
    args, N, reader, writer = setup_pipeline(parser, output_header)

    # [I/O層でのドメイン解決] 最新の _node_map.csv を用いて文字列からペアのインデックスを抽出
    target_pairs = []
    if args.signal_pairs_labels:
        try:
            df_map = pd.read_csv(args.node_map)
            label_to_idx = dict(zip(df_map['node_label'], df_map['node_idx']))
            for pair_str in args.signal_pairs_labels.split(','):
                if ':' in pair_str:
                    lbl_A, lbl_B = pair_str.split(':')
                    lbl_A, lbl_B = lbl_A.strip(), lbl_B.strip()
                    if lbl_A in label_to_idx and lbl_B in label_to_idx:
                        target_pairs.append((int(label_to_idx[lbl_A]), int(label_to_idx[lbl_B])))
        except Exception as e:
            print(f"[WARN] Failed to parse labels: {e}", file=sys.stderr)

    # 1. すべてのタイムスライスから q_current を計算して蓄積
    q_history_list = []
    for t_idx, T_slice in yield_time_slices(reader, N):
        q_current = compute_net_flux(T_slice)
        q_history_list.append(q_current)

    # 2. ストリーム完了後、一括で解析を実行
    if len(target_pairs) > 0 and len(q_history_list) > 2:
        q_hist_arr = np.array(q_history_list)
        records = run_time_lag_analysis(q_hist_arr, target_pairs, args.max_lag)
        
        # 相関が高い順にソートして出力
        records.sort(key=lambda x: abs(float(x[3])), reverse=True)
        for rec in records:
            writer.writerow(rec)

if __name__ == "__main__":
    main()
