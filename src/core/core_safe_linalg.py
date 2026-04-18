#!/usr/bin/env python3
# core_safe_linalg.py
import numpy as np

def compute_safe_pinv(M_singular, rcond, lambda_reg):
    """!
    @brief Safely calculate the pseudo-inverse of a singular matrix.
    @details Implements true Tikhonov regularization (M^T * M + lambda*I)^(-1) * M^T to prevent singularity crashes. Scale invariance is enforced by injecting tuning parameters explicitly.

    @param M_singular Singular matrix (N x M).
    @param rcond Rank determination threshold constraint (float).
    @param lambda_reg Tikhonov regularization term constraint (float).

    @return Safe pseudo-inverse matrix M_pinv (M x N).

    @pre
        - `M_singular` must be a valid 2D numpy array.
        - `rcond` and `lambda_reg` must be non-negative floats provided by the caller based on system scale.
    @post
        - Returns a densely computed pseudo-inverse matrix even under severe collinearity.
    @invariant
        - Mathematical equivalent applies Tikhonov regularization for lambda > 0 or standard SVD pseudo-inverse for lambda = 0.
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
    """!
    @brief Calculate the covariance matrix between nodes from displacement history.
    @details Uses an unbiased variance estimator (ddof=1) to assess structural correlation.

    @param dq_history Past displacement history matrix (Time_steps x Nodes).

    @return Covariance matrix between nodes (Nodes x Nodes).

    @pre
        - `dq_history` must be a valid 2D numpy array with Time_steps > 1 for unbiased estimator.
    @post
        - Returns a positive semi-definite matrix.
    @invariant
        - Operates row-wise safely ensuring dimensions are resolved across steps.
    """
    # Uses numpy's np.cov. Calculates unbiased variance by default.
    # If dq_history is (T, N), np.cov's default behavior returns an (N, N) covariance matrix.
    # ddof=1 guarantees unbiased variance (denominator is N-1).
    covariance_matrix = np.cov(dq_history, rowvar=False, ddof=1)
    return covariance_matrix
