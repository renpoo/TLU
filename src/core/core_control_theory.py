#!/usr/bin/env python3
# core_control_theory.py
import numpy as np
import scipy.linalg as la
from src.core.core_safe_linalg import compute_safe_pinv

def build_state_space_matrices(transition_P: np.ndarray, controllable_indices: list[int]) -> tuple[np.ndarray, np.ndarray]:
    N = transition_P.shape[0]
    A = transition_P.copy()
    
    num_inputs = len(controllable_indices)
    B = np.zeros((N, num_inputs), dtype=float)
    
    for j, node_idx in enumerate(controllable_indices):
        B[node_idx, j] = 1.0
        
    return A, B

def build_QR_matrices(N: int, num_inputs: int, weight_Q: float, weight_R: float, target_indices: list[int], min_weight_R: float = 0.0) -> tuple[np.ndarray, np.ndarray]:
    """
    LQR制御用の重み行列 Q, R を構築する。
    min_weight_R: ゼロ行列化を防ぐためのR行列要素の最小許容値。外部スケールに合わせて注入する。
    """
    Q = np.zeros((N, N), dtype=float)
    for idx in target_indices:
        Q[idx, idx] = weight_Q
        
    # 暗黙のマジックナンバー 1e-6 を排除し、外部から注入された min_weight_R を使用
    safe_weight_R = max(weight_R, min_weight_R)
    R = np.eye(num_inputs, dtype=float) * safe_weight_R
    
    return Q, R

def solve_lqr_gain(A: np.ndarray, B: np.ndarray, Q: np.ndarray, R: np.ndarray, rcond: float = 1e-15, lambda_reg: float = 0.0) -> np.ndarray:
    """
    離散時間LQRの最適フィードバックゲイン K を算出する。
    rcond, lambda_reg: 特異行列回避のためのパラメータ。対象系のスケールに合わせて外部から注入可能。
    """
    if B.shape[1] == 0 or np.all(B == 0):
        return np.zeros((0, A.shape[0]))

    try:
        S = la.solve_discrete_are(A, B, Q, R)
        Bp_S_B = np.dot(B.T, np.dot(S, B))
        
        # 内部にハードコードされていた 1e-15, 1e-6 を引数化
        R_plus_Bp_S_B_inv = compute_safe_pinv(R + Bp_S_B, rcond=rcond, lambda_reg=lambda_reg)
        
        K_lqr = np.dot(R_plus_Bp_S_B_inv, np.dot(B.T, np.dot(S, A)))
        return K_lqr
        
    except la.LinAlgError:
        return np.zeros((B.shape[1], A.shape[0]))

def compute_optimal_input(K_lqr: np.ndarray, current_state: np.ndarray, target_state: np.ndarray) -> np.ndarray:
    if K_lqr.shape[0] == 0:
        return np.array([])
        
    error_state = current_state - target_state
    u = -np.dot(K_lqr, error_state)
    
    return u
