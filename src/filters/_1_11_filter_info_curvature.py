#!/usr/bin/env python3
# ==========================================
# _1_11_filter_info_curvature.py
# TLU System: Information Curvature Pipeline Filter
# ==========================================
import sys
import argparse
import numpy as np
from typing import List, Tuple

from src.filters.cli_parser import get_base_parser
from src.filters.stream_processor import setup_pipeline, yield_time_slices

from src.core.core_tensor_ops import compute_net_flux
from src.core.core_information_geometry import (
    compute_information_curvature, 
    compute_information_density
)

def run_info_curvature_analysis(
        t_idx: int, 
        T_slice: np.ndarray, 
        q_history_window: List[np.ndarray]
) -> Tuple[List[list], np.ndarray]:
    """ [Pure Orchestration Function] """
    N = T_slice.shape[0]
    
    # 1. 最新の純フラックスを算出
    q_current = compute_net_flux(T_slice)
    
    # 曲率計算のため、現在状態を含めたテンポラリな履歴を作成
    temp_hist = np.array(q_history_window + [q_current])
    
    # 2. 曲率(Curvature) と 密度(Density) の計算
    curvature_vec = compute_information_curvature(temp_hist)
    density_vec = compute_information_density(T_slice)
    
    # 3. レコードのフォーマット (ラベルは排除し、純粋なテンソルデータにする)
    records = []
    for i in range(N):
        records.append([
            t_idx, i, 
            f"{curvature_vec[i]:.6f}", 
            f"{density_vec[i]:.4f}"
        ])
        
    return records, q_current

def main():
    parser = get_base_parser("TLU Information Curvature Filter")
    parser.add_argument("--window", type=int, default=3, help="曲率計算用のタイムウィンドウ幅（最小3）")
    
    output_header = ["t_idx", "node_idx", "curvature", "density"]
    args, N, reader, writer = setup_pipeline(parser, output_header)

    q_history_window = []

    for t_idx, T_slice in yield_time_slices(reader, N):
        records, q_current = run_info_curvature_analysis(
            t_idx, T_slice, q_history_window
        )
        
        # 履歴の安全な更新
        q_history_window.append(q_current)
        # 呼び出し元で temp_hist に q_current を足すため、ウィンドウサイズ-1 を保持する
        if len(q_history_window) > max(args.window, 3) - 1:
            q_history_window.pop(0)
            
        for rec in records:
            writer.writerow(rec)

if __name__ == "__main__":
    main()
