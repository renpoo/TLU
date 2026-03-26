#!/usr/bin/env python3
# ==========================================
# _1_12_filter_network_topology.py
# TLU System: Network Topology & Edge Stress Filter
# ==========================================
import sys
import argparse
import numpy as np
from typing import List, Tuple

from src.filters.cli_parser import get_base_parser
from src.filters.stream_processor import setup_pipeline, yield_time_slices
from src.core.core_topology import compute_edge_stress

def run_network_topology_analysis(
        t_idx: int, 
        T_slice: np.ndarray, 
        T_history_window: List[np.ndarray]
) -> List[list]:
    """ [Pure Orchestration Function] """
    N = T_slice.shape[0]
    
    # エッジの応力(Zスコア)を計算
    stress_matrix = compute_edge_stress(T_slice, T_history_window)
    
    records = []
    # すべてのノードペアについて、取引(weight)がゼロより大きいエッジのみを抽出
    for i in range(N):
        for j in range(N):
            weight = T_slice[i, j]
            if weight > 0:
                stress = stress_matrix[i, j]
                # 出力フォーマット: [t_idx, src_idx, tgt_idx, weight, stress]
                records.append([
                    t_idx, i, j, 
                    f"{weight:.4f}", f"{stress:.4f}"
                ])
                
    return records

def main():
    parser = get_base_parser("TLU Network Topology & Edge Stress Filter")
    parser.add_argument("--baseline_window", type=int, default=12, help="応力計算のベースライン期間")
    
    output_header = ["t_idx", "src_idx", "tgt_idx", "weight", "stress"]
    args, N, reader, writer = setup_pipeline(parser, output_header)

    T_history_window = []

    for t_idx, T_slice in yield_time_slices(reader, N):
        records = run_network_topology_analysis(t_idx, T_slice, T_history_window)
        
        # 履歴の安全な更新
        T_history_window.append(T_slice.copy())
        if len(T_history_window) > args.baseline_window:
            T_history_window.pop(0)
            
        for rec in records:
            writer.writerow(rec)

if __name__ == "__main__":
    main()
