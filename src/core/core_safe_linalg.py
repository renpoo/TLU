#!/usr/bin/env python3
# core_safe_linalg.py
import numpy as np

def compute_safe_pinv(M_singular, rcond, lambda_reg):
    """
    Safely calculate the pseudo-inverse of a singular matrix.
    Implementation based on true Tikhonov regularization (M^T * M + lambda*I)^(-1) * M^T.
    
    * To ensure scale invariance, rcond and lambda_reg do not have default values.
    * The caller (upper layer) must supply these according to the scale of the system.
    
    Args:
        M_singular: Singular matrix (N x M)
        rcond: Rank determination threshold (float)
        lambda_reg: Tikhonov regularization term (float)
        
    Returns:
        M_pinv: Safe pseudo-inverse matrix (M x N)
    """
    if lambda_reg > 0.0:
        M_singular_T = M_singular.T
        # Construct M^T M + lambda * I
        N_cols = M_singular.shape[1]
        M_reg = np.dot(M_singular_T, M_singular) + lambda_reg * np.eye(N_cols, dtype=float)
        
        # Apply additional safety using pinv with rcond instead of direct inverse
        pinv_reg = np.linalg.pinv(M_reg, rcond=rcond)
        
        # Finally, multiply by M^T
        return np.dot(pinv_reg, M_singular_T)
    else:
        # Standard SVD cutoff only if no regularization is applied
        return np.linalg.pinv(M_singular, rcond=rcond)

def compute_covariance_matrix(dq_history):
    """
    Calculate the covariance matrix between nodes from past displacement history.
    
    Args:
        dq_history: Past displacement history (Time_steps x Nodes)
        
    Returns:
        covariance_matrix: Covariance matrix (Nodes x Nodes)
    """
    # Uses numpy's np.cov. Calculates unbiased variance by default.
    # If dq_history is (T, N), np.cov's default behavior returns an (N, N) covariance matrix.
    # ddof=1 guarantees unbiased variance (denominator is N-1).
    covariance_matrix = np.cov(dq_history, rowvar=False, ddof=1)
    return covariance_matrix
