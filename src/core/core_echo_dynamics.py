#!/usr/bin/env python3
# core_echo_dynamics.py
import numpy as np

def compute_finite_echo(P_matrix, gamma, max_k):
    """
    有限波及行列（Echo）を計算する。
    
    Args:
        P_matrix: 遷移確率行列 (N x N)
        gamma: 減衰率 (スカラー)
        max_k: 波及ステップ数 (int)
        
    Returns:
        M_echo: 有限波及行列 (N x N)
    """
    N = P_matrix.shape[0]
    
    # 0次波及 (k=0): 単位行列
    M_echo = np.eye(N, dtype=float)
    
    # 1次からmax_k次までの波及を計算して加算
    P_k = P_matrix.copy()  # k=1の遷移行列
    for k in range(1, max_k + 1):
        M_echo += (gamma ** k) * P_k
        P_k = np.dot(P_k, P_matrix)  # 次の次数の遷移行列を計算
        
    return M_echo


def compute_decomposed_echoes(P_matrix, gamma, max_k):
    """
    有限波及行列（Echo）を、k次波及ごとに分解してリストとして返す。
    
    Args:
        P_matrix: 遷移確率行列 (N x N)
        gamma: 減衰率 (スカラー)
        max_k: 波及ステップ数 (int)
        
    Returns:
        echoes: k次波及行列のリスト (List[np.ndarray])
                インデックス0が1次波及、インデックス1が2次波及...
    """
    N = P_matrix.shape[0]
    echoes = []
    
    # 1次からmax_k次までの波及を計算
    P_k = P_matrix.copy()  # k=1の遷移行列
    for k in range(1, max_k + 1):
        # k次波及行列 = gamma^k * P^k
        echo_k = (gamma ** k) * P_k
        echoes.append(echo_k)
        
        # 次の次数の遷移行列を計算
        P_k = np.dot(P_k, P_matrix)
        
    return echoes
