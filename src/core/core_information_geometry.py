#!/usr/bin/env python3
# core_information_geometry.py
import numpy as np

def compute_shannon_entropy(P_matrix):
    """
    遷移確率行列(P)から、ノードごとのシャノンエントロピーを計算する。
    
    Args:
        P_matrix: 遷移確率行列 (Nodes x Nodes)
        
    Returns:
        entropy: ノードごとのシャノンエントロピー (Nodes,)
    """
    # ゼロの扱い: 0 * log(0) は 0 として扱う
    # np.log2(0) は -inf になるため、事前にマスクして 0 を代入する
    
    # ゼロ行列のチェック（安全策）
    if np.all(P_matrix == 0):
        return np.zeros(P_matrix.shape[0], dtype=float)
    
    # ゼロをマスクして計算
    P_masked = np.where(P_matrix > 0, P_matrix, 1.0)
    entropy = -np.sum(P_masked * np.log2(P_masked), axis=1)
    
    return entropy

def compute_kl_divergence(P_current, P_baseline):
    """
    現在の遷移確率(P_current)と過去のベースライン(P_baseline)の間の、
    ノードごとのKLダイバージェンス（カルバック・ライブラー情報量：情報量的な距離）を計算する。
    
    Args:
        P_current: 現在の遷移確率行列 (Nodes x Nodes)
        P_baseline: 過去のベースライン遷移確率行列 (Nodes x Nodes)
        
    Returns:
        kl_divergence: ノードごとのKLダイバージェンス (Nodes,)
    """
    # ゼロの扱い: p=0 または q=0 の場合、p*log(p/q) は 0 として扱う
    # np.log2(0) は -inf になるため、事前にマスクして 0 を代入する
    
    # ゼロ行列のチェック（安全策）
    if np.all(P_current == 0) or np.all(P_baseline == 0):
        return np.zeros(P_current.shape[0], dtype=float)
    
    # ゼロをマスクして計算
    # 分母がゼロになる場合（P_baselineが0）は、その項は0として扱う
    # 分子がゼロになる場合（P_currentが0）は、その項は0として扱う
    mask = (P_current > 0) & (P_baseline > 0)
    
    kl_divergence = np.zeros(P_current.shape[0], dtype=float)
    P_masked = np.where(mask, P_current, 1.0)
    P_baseline_masked = np.where(mask, P_baseline, 1.0)
    kl_divergence = np.sum(P_current * np.log2(P_masked / P_baseline_masked), axis=1)
    
    return kl_divergence

def compute_information_curvature(q_history_window: np.ndarray) -> np.ndarray:
    """
    純フラックス履歴から、各ノードの情報曲率（2階差分の絶対値、すなわち加速度的歪み）を計算する。
    
    Args:
        q_history_window: (Steps x Nodes) の配列。Steps >= 3 が必要。
        
    Returns:
        curvature: ノードごとの曲率ベクトル (Nodes,)
    """
    if q_history_window.shape[0] < 3:
        return np.zeros(q_history_window.shape[1], dtype=float)
    
    # 2階差分: a(t) = v(t) - v(t-1) = q(t) - 2q(t-1) + q(t-2)
    accel = q_history_window[-1, :] - 2 * q_history_window[-2, :] + q_history_window[-3, :]
    return np.abs(accel)

def compute_information_density(T_slice: np.ndarray) -> np.ndarray:
    """
    現在の遷移スライスから、各ノードの情報密度（流入と流出の絶対値の総和）を計算する。
    
    Args:
        T_slice: 現在の遷移確率(またはフラックス)行列 (Nodes x Nodes)
        
    Returns:
        density: ノードごとの情報密度ベクトル (Nodes,)
    """
    # 流出の総和 (axis=1) + 流入の総和 (axis=0)
    outflow = np.sum(np.abs(T_slice), axis=1)
    inflow = np.sum(np.abs(T_slice), axis=0)
    return outflow + inflow
