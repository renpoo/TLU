#!/usr/bin/env python3
# ==========================================
# src/core/core_safe_linalg.py
# TLU Core: Safe Linear Algebra Utilities
# ==========================================
"""!
@file core_safe_linalg.py
@brief Safe linear algebra utilities for pseudo-inversion and covariance estimation.
"""

import numpy as np

# Standardized TLU System Regularization Constants
DEFAULT_RCOND: float = 1e-15
DEFAULT_LAMBDA_REG: float = 1e-4

def compute_safe_pinv(
    M_singular: np.ndarray, 
    rcond: float = DEFAULT_RCOND, 
    lambda_reg: float = DEFAULT_LAMBDA_REG
) -> np.ndarray:
    """!
    @brief Safely calculate the pseudo-inverse of a singular matrix.
    @details Implements Tikhonov regularization (M^T * M + lambda*I)^(-1) * M^T to prevent singularity crashes.

    @param M_singular Singular matrix (N x M).
    @param rcond Rank determination threshold constraint.
    @param lambda_reg Tikhonov regularization term constraint.

    @return Safe pseudo-inverse matrix M_pinv (M x N).
    """
    if lambda_reg > 0.0:
        M_singular_T = M_singular.T
        N_cols = M_singular.shape[1]
        M_reg = np.dot(M_singular_T, M_singular) + lambda_reg * np.eye(N_cols, dtype=float)
        pinv_reg = np.linalg.pinv(M_reg, rcond=rcond)
        return np.dot(pinv_reg, M_singular_T)
    else:
        return np.linalg.pinv(M_singular, rcond=rcond)

def compute_covariance_matrix(dq_history: np.ndarray) -> np.ndarray:
    """!
    @brief Calculate the covariance matrix between nodes from displacement history.
    @details Uses an unbiased variance estimator (ddof=1) to assess structural correlation.

    @param dq_history Past displacement history matrix (Time_steps x Nodes).

    @return Covariance matrix between nodes (Nodes x Nodes).
    """
    return np.cov(dq_history, rowvar=False, ddof=1)
