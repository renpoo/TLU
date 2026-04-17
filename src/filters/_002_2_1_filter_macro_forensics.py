#!/usr/bin/env python3
# ==========================================
# _1_8_filter_forensics.py
# TLU System: Forensics & Anomaly Detection Pipeline Filter
# ==========================================
import sys
import argparse
import numpy as np
from typing import List, Tuple, Dict

from src.filters.cli_parser import get_base_parser
from src.filters.stream_processor import setup_pipeline, yield_time_slices

from src.core.core_tensor_ops import compute_net_flux, compute_transition_matrix
from src.core.core_safe_linalg import compute_covariance_matrix, compute_safe_pinv
# 修正: core_forensics.py の純粋な関数群を個別にインポート
from src.core.core_forensics import (
    check_conservation_law,
    compute_structural_drift,
    compute_multivariate_anomaly,
    evaluate_anomaly_flags
)

def run_forensics_analysis(
        t_idx: int, 
        T_slice: np.ndarray, 
        q_history_window: List[np.ndarray],
        P_history_window: List[np.ndarray],
        thresholds: Dict[str, float]
) -> Tuple[List[list], np.ndarray, np.ndarray]:
    """ [Pure Orchestration Function] """
    q_current = compute_net_flux(T_slice)
    P_current = compute_transition_matrix(T_slice)

    # 1. 質量保存則のチェック (システム全体の残差)
    abs_residual, _ = check_conservation_law(q_current, thresholds.get('leak_tolerance', 1e-5))

    # 2. 構造ドリフト (KL情報量の総和)
    kl_drift = compute_structural_drift(P_current, P_history_window)

    # 3. 多変量異常検知 (マハラノビス Zスコア)
    if len(q_history_window) > 1:
        # 履歴から期待値(平均)と精度行列(共分散の逆行列)を計算
        q_mean = np.mean(q_history_window, axis=0)
        cov_matrix = compute_covariance_matrix(np.array(q_history_window))
        K_precision = compute_safe_pinv(cov_matrix, rcond=1e-15, lambda_reg=1e-4)
        
        z_score = compute_multivariate_anomaly(q_current, q_mean, K_precision)
    else:
        z_score = 0.0

    # 4. 総合異常フラグ
    flag = evaluate_anomaly_flags(abs_residual, kl_drift, z_score, thresholds)

    # システム全体のマクロ指標なので、1タイムスライスにつき1行のみ出力 (node_idx は廃止)
    record = [
        t_idx, 
        f"{abs_residual:.4f}", 
        f"{kl_drift:.4f}", 
        f"{z_score:.4f}", 
        flag
    ]

    return [record], q_current, P_current

def main():
    parser = get_base_parser("TLU Forensics & Anomaly Detection Filter")
    parser.add_argument("--baseline_window", type=int, default=12, help="ベースライン構築期間")
    parser.add_argument("--leak_tolerance", type=float, default=1e-5, help="保存則の許容誤差")
    parser.add_argument("--kl_drift_thresh", type=float, default=3.0, help="構造変化の異常閾値")
    parser.add_argument("--z_score_thresh", type=float, default=3.0, help="Zスコアの異常閾値")
    
    # 修正: node_idx を取り除き、全体指標としてのヘッダーに
    output_header = [
        "t_idx", "conservation_residual", 
        "kl_divergence_drift", "mahalanobis_z_score", "anomaly_flag"
    ]
    args, N, reader, writer = setup_pipeline(parser, output_header)

    thresholds = {
        'leak_tolerance': args.leak_tolerance,
        'kl_drift_thresh': args.kl_drift_thresh,
        'z_score_thresh': args.z_score_thresh
    }

    q_history_window = []
    P_history_window = []

    for t_idx, T_slice in yield_time_slices(reader, N):
        records, q_current, P_current = run_forensics_analysis(
            t_idx, T_slice, q_history_window, P_history_window, thresholds
        )
        
        q_history_window.append(q_current)
        P_history_window.append(P_current)
        if len(q_history_window) > args.baseline_window:
            q_history_window.pop(0)
            P_history_window.pop(0)
            
        for rec in records:
            writer.writerow(rec)

if __name__ == "__main__":
    main()
