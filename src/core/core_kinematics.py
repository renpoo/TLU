#!/usr/bin/env python3
# core_kinematics.py
import numpy as np
from src.core.core_safe_linalg import compute_safe_pinv

def build_echo_matrix(P: np.ndarray, gamma: float, max_k: int) -> np.ndarray:
    """推移確率行列Pから、有限波及エコー行列 M_echo を構築する"""
    N = P.shape[0]
    M_echo = np.eye(N)
    current_P = np.eye(N)
    for k in range(1, max_k + 1):
        current_P = np.dot(current_P, P)
        M_echo += (gamma ** k) * current_P
    return M_echo

def run_forward_simulation(P, dq_input, gamma, max_k):
    """
    [双剣の1: 波及シミュレーション]
    有限波及モデル M_echo = I + (gamma*P) + ... + (gamma*P)^max_k を
    入力変位 dq_input に対して逐次適用し、最終的な波及影響を算出する。
    """
    total_dq = np.copy(dq_input)
    current_wave = np.copy(dq_input)
    
    for k in range(1, max_k + 1):
        # 行列累乗を直接計算せず、前ステップの波及分に (gamma * P) を掛ける (効率化)
        current_wave = gamma * np.dot(current_wave, P)
        total_dq += current_wave
        
    return total_dq

def solve_ik_with_safe_stiffness(J, K_safe, target_dr):
    """
    [双剣の2: 逆運動学とひずみ最適化]
    目標変動量 target_dr に対し、ひずみエネルギー U = 1/2 * dq^T * K_safe * dq 
    を最小化する全体変位 dq_opt を算出する。
    
    解法: 重み付き最小二乗（制約付き最適化）
    dq = K_safe_pinv * J.T * pinv(J * K_safe_pinv * J.T) * target_dr
    """
    # 1. 剛性行列 K の擬似逆行列（＝柔軟性/共分散）を計算
    # SDL_04: compute_safe_pinv を使用
    K_inv = compute_safe_pinv(K_safe, lambda_reg=1e-1)
    
    # 2. ヤコビアン J の形状調整 (1次元ベクトルの場合も行列として扱う)
    if J.ndim == 1:
        J = J.reshape(1, -1)
        
    # 3. 投影空間での Gram 行列 A = J * K_inv * J.T を計算
    A = np.dot(J, np.dot(K_inv, J.T))
    
    # 4. A の安全な逆行列を計算
    A_inv = compute_safe_pinv(A, lambda_reg=suggest_lambda(A))
    
    # 5. 最適変位 dq_opt の算出
    dr_vec = np.array([target_dr]) if np.isscalar(target_dr) else np.array(target_dr)
    dq_opt = np.dot(K_inv, np.dot(J.T, np.dot(A_inv, dr_vec)))
    
    return dq_opt.flatten()

def suggest_lambda(M):
    # 行列のノルム（大きさ）の 1e-3 倍程度を正則化の基準にするなど
    return np.linalg.norm(M) * 1e-3

def compute_derivatives(q_history):
    """
    状態ベクトル(q)の時系列履歴から、最新の速度(v)と加速度(a)を算出する。
    
    Args:
        q_history: 過去の状態ベクトル履歴 (Time_steps x Nodes)
                   時系列順に並んでいること（最も古い履歴が先頭）。
        
    Returns:
        v: 最新の速度ベクトル (Nodes,)
        a: 最新の加速度ベクトル (Nodes,)
    """
    T = q_history.shape[0]
    
    # 履歴が足りない場合（1ステップ分しかない場合）はゼロベクトルを返す
    if T < 2:
        N = q_history.shape[1]
        return np.zeros(N, dtype=float), np.zeros(N, dtype=float)
    
    # 最新の2ステップを取得
    q_latest = q_history[-1]   # t
    q_prev = q_history[-2]     # t-1
    
    # 速度 v(t) = q(t) - q(t-1)
    v = q_latest - q_prev
    
    # 加速度 a(t) = v(t) - v(t-1)
    # v(t-1) を計算
    v_prev = q_prev - q_history[-3] if T >= 3 else v
    
    a = v - v_prev
    
    return v, a
