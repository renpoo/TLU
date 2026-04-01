#!/usr/bin/env python3
# core_safe_linalg.py
import numpy as np

def compute_safe_pinv(M_singular, rcond=1e-6, lambda_reg=1e-1):
    """
    特異行列の擬似逆行列を安全に計算する。
    真のチコノフ正則化 (M^T * M + lambda*I)^(-1) * M^T に基づく実装。
    
    Args:
        M_singular: 特異行列 (N x M)
        rcond: ランク判定の閾値 (float)
        lambda_reg: チコノフ正則化項 (float)
        
    Returns:
        M_pinv: 安全な擬似逆行列 (M x N)
    """
    if lambda_reg > 0.0:
        M_singular_T = M_singular.T
        # M^T M + lambda * I の構築
        N_cols = M_singular.shape[1]
        M_reg = np.dot(M_singular_T, M_singular) + lambda_reg * np.eye(N_cols, dtype=float)
        
        # 逆行列の代わりに、rcondを用いたpinvでさらなる安全保障をかける
        pinv_reg = np.linalg.pinv(M_reg, rcond=rcond)
        
        # 最後に M^T を掛ける
        return np.dot(pinv_reg, M_singular_T)
    else:
        # 正則化なしの場合は標準のSVDカットオフのみ
        return np.linalg.pinv(M_singular, rcond=rcond)

def compute_covariance_matrix(dq_history):
    """
    過去の変位履歴から、ノード間の共分散行列を計算する。
    
    Args:
        dq_history: 過去の変位履歴 (Time_steps x Nodes)
        
    Returns:
        covariance_matrix: 共分散行列 (Nodes x Nodes)
    """
    # numpyのnp.covを使用。デフォルトでは不偏分散を計算してくれる。
    # dq_historyが (T, N) の場合、np.covのデフォルト動作では (N, N) の共分散行列が返る。
    # ddof=1で不偏分散（分母がN-1）が保証される。
    covariance_matrix = np.cov(dq_history, rowvar=False, ddof=1)
    return covariance_matrix
