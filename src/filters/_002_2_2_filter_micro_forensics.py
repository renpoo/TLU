#!/usr/bin/env python3
# ==========================================
# _002_2_2_filter_micro_forensics.py
# TLU System: Micro Forensics (Node-specific Anomalies)
# ==========================================
import sys
import argparse
import numpy as np
from typing import List, Tuple, Dict

from src.filters.cli_parser import get_base_parser
from src.filters.stream_processor import setup_pipeline, yield_time_slices

from src.core.core_tensor_ops import compute_net_flux, compute_transition_matrix

# 数理ユーティリティ (純粋関数)
def compute_node_kl_divergence_vector(
        P_current: np.ndarray, 
        P_history_window: List[np.ndarray], 
        epsilon: float = 1e-9
) -> np.ndarray:
    """ [Pure Math] 各ノード(行)ごとのKL情報量(構造変化度)ベクトルを計算 """
    N = P_current.shape[0]
    if len(P_history_window) == 0:
        return np.zeros(N)
    
    P_mean_hist = np.mean(P_history_window, axis=0)
    
    P_current_safe = P_current + epsilon
    P_mean_hist_safe = P_mean_hist + epsilon
    
    # 修正: compute_safe_divide を廃止し、単純な割り算に変更（epsilonのおかげで安全）
    ratio = P_current_safe / P_mean_hist_safe
    
    kl_matrix = P_current_safe * np.log(ratio)
    kl_vector = np.sum(kl_matrix, axis=1) 
    
    return np.maximum(kl_vector, 0.0)

def compute_node_univariate_z_score_vector(
        q_current: np.ndarray, 
        q_history_window: List[np.ndarray]
) -> np.ndarray:
    """ [Pure Math] 各ノードごとの単変量Zスコア(活動量ショック)ベクトルを計算 """
    N = len(q_current)
    if len(q_history_window) < 2:
        return np.zeros(N)
    
    q_history_mat = np.array(q_history_window)
    q_mean_hist = np.mean(q_history_mat, axis=0)
    q_std_hist = np.std(q_history_mat, axis=0)
    
    deviation = q_current - q_mean_hist
    
    # 修正: numpy の標準機能でゼロ除算を安全に回避
    z_scores = np.divide(deviation, q_std_hist, out=np.zeros_like(deviation), where=q_std_hist!=0)
    
    return np.abs(z_scores)

def evaluate_micro_anomaly_flags(
        kl_vector: np.ndarray, 
        z_vector: np.ndarray, 
        thresholds: Dict[str, float]
) -> List[int]:
    """ [Pure Logic] KLまたはZが閾値を超えた場合にフラグを立てる """
    N = len(kl_vector)
    flags = []
    for i in range(N):
        is_kl_anomaly = kl_vector[i] > thresholds.get('kl_drift_thresh', 3.0)
        is_z_anomaly = z_vector[i] > thresholds.get('z_score_thresh', 3.0)
        
        flags.append(1 if (is_kl_anomaly or is_z_anomaly) else 0)
    return flags

# オーケストレーション関数 (純粋関数)
def run_micro_forensics_analysis(
        t_idx: int, 
        T_slice: np.ndarray, 
        q_history_window: List[np.ndarray],
        P_history_window: List[np.ndarray],
        thresholds: Dict[str, float]
) -> Tuple[List[list], np.ndarray, np.ndarray]:
    """ [Pure Orchestration] """
    N = T_slice.shape[0]
    q_current = compute_net_flux(T_slice)
    P_current = compute_transition_matrix(T_slice)

    # 1. ミクロKL情報量 (ノードごとの構造変化)
    node_kl = compute_node_kl_divergence_vector(P_current, P_history_window)

    # 2. ミクロZスコア (ノードごとの単変量活動ショック)
    node_z = compute_node_univariate_z_score_vector(q_current, q_history_window)

    # 3. 異常フラグの評価
    anomaly_flags = evaluate_micro_anomaly_flags(node_kl, node_z, thresholds)

    # 4. レコードのフォーマット (N行のレコードを生成)
    records = []
    for i in range(N):
        records.append([
            t_idx, i, 
            f"{node_kl[i]:.4f}", 
            f"{node_z[i]:.4f}", 
            anomaly_flags[i]
        ])

    return records, q_current, P_current

def main():
    parser = get_base_parser("TLU Micro Forensics (Node Anomaly)")
    parser.add_argument("--baseline_window", type=int, default=12, help="ベースライン構築期間")
    parser.add_argument("--kl_drift_thresh", type=float, default=3.0, help="ミクロKL情報量の異常閾値")
    parser.add_argument("--z_score_thresh", type=float, default=3.0, help="単変量Zスコアの異常閾値")
    
    # 修正: node_idx を復活させ、ノードごとの指標ヘッダーに
    output_header = [
        "t_idx", "node_idx", "node_kl_drift", "node_univariate_z_score", "micro_anomaly_flag"
    ]
    args, N, reader, writer = setup_pipeline(parser, output_header)

    thresholds = {
        'kl_drift_thresh': args.kl_drift_thresh,
        'z_score_thresh': args.z_score_thresh
    }

    q_history_window = []
    P_history_window = []

    for t_idx, T_slice in yield_time_slices(reader, N):
        records, q_current, P_current = run_micro_forensics_analysis(
            t_idx, T_slice, q_history_window, P_history_window, thresholds
        )
        
        # 履歴の安全な更新
        q_history_window.append(q_current)
        P_history_window.append(P_current)
        if len(q_history_window) > args.baseline_window:
            q_history_window.pop(0)
            P_history_window.pop(0)
            
        for rec in records:
            writer.writerow(rec)

if __name__ == "__main__":
    main()
