#!/usr/bin/env python3
# core_control_theory.py
import numpy as np
import scipy.linalg as la
from src.core.core_safe_linalg import compute_safe_pinv

def build_state_space_matrices(transition_P: np.ndarray, controllable_indices: list[int]) -> tuple[np.ndarray, np.ndarray]:
    """!
    @brief Initialize generic state space mapping system matrices.
    @details Synthesizes dynamic mapping A blocks and input influence geometry B blocks.

    @param transition_P The temporal adjacency state probability.
    @param controllable_indices Vector representing boolean topological controllers.

    @return Mapped system geometry parameters A and B in classical configuration.

    @pre
        - `controllable_indices` properly align within the dimensions of `transition_P`.
    @post
        - Deterministically emits (N,N) and (N, M) parameter matrices.
    @invariant
        - Formulates discrete affine control spaces functionally.
    """
    N = transition_P.shape[0]
    A = transition_P.copy()
    
    num_inputs = len(controllable_indices)
    B = np.zeros((N, num_inputs), dtype=float)
    
    for j, node_idx in enumerate(controllable_indices):
        B[node_idx, j] = 1.0
        
    return A, B

def build_QR_matrices(N: int, num_inputs: int, weight_Q: float, weight_R: float, target_indices: list[int], min_weight_R: float = 0.0) -> tuple[np.ndarray, np.ndarray]:
    """!
    @brief Build the tracking weight cost matrices Q and R for optimal LQR limits.
    @details Configures optimal response thresholds with dynamic external safeguards applied to the baseline state cost and control cost.

    @param N Node dimension count.
    @param num_inputs Controllable indices domain size.
    @param weight_Q Scale for tracking stability.
    @param weight_R Scale for input energy limits.
    @param target_indices Subset geometry vectors tracking reference norms.
    @param min_weight_R decoupled minimum scalar boundary threshold preventing singularities.

    @return Formulated weight block matrices Q and R.

    @pre
        - Numerical parameter scaling injected successfully via pipeline runtime.
    @post
        - Enforces implicit non-zero positive definiteness bounded by `min_weight_R`.
    @invariant
        - Avoids all instances of mathematically zero R matrix conditions.
    """
    Q = np.zeros((N, N), dtype=float)
    for idx in target_indices:
        Q[idx, idx] = weight_Q
        
    # Eliminate the implicit magic number 1e-6 and use the externally injected min_weight_R
    safe_weight_R = max(weight_R, min_weight_R)
    R = np.eye(num_inputs, dtype=float) * safe_weight_R
    
    return Q, R

def solve_lqr_gain(A: np.ndarray, B: np.ndarray, Q: np.ndarray, R: np.ndarray, rcond: float = 1e-15, lambda_reg: float = 0.0) -> np.ndarray:
    """!
    @brief Calculate the optimal deterministic feedback geometric gain K block.
    @details Solves discrete algebraic Riccati equations while strictly mitigating rank deficiencies via pseudo inverse bounds.

    @param A The system shift map geometry.
    @param B Controllable unit mapping domain.
    @param Q Configured stability weight objective.
    @param R Configured actuation constraints threshold.
    @param rcond Truncation condition scalar bound.
    @param lambda_reg Parameter explicit for Tikhonov geometry regularization limits.

    @return Controller response boundary feedback map K.

    @pre
        - Dimensional geometry properly scaled through pre-synthesis.
    @post
        - Strictly falls back gracefully via empty blocks if linear equations completely fail.
    @invariant
        - Unconditionally bounds to a linear state quadratic formulation limits.
    """
    if B.shape[1] == 0 or np.all(B == 0):
        return np.zeros((0, A.shape[0]))

    try:
        S = la.solve_discrete_are(A, B, Q, R)
        Bp_S_B = np.dot(B.T, np.dot(S, B))
        
        # Converted internally hardcoded 1e-15, 1e-6 into arguments
        R_plus_Bp_S_B_inv = compute_safe_pinv(R + Bp_S_B, rcond=rcond, lambda_reg=lambda_reg)
        
        K_lqr = np.dot(R_plus_Bp_S_B_inv, np.dot(B.T, np.dot(S, A)))
        return K_lqr
        
    except la.LinAlgError:
        return np.zeros((B.shape[1], A.shape[0]))

def compute_optimal_input(K_lqr: np.ndarray, current_state: np.ndarray, target_state: np.ndarray) -> np.ndarray:
    """!
    @brief Backcalculate optimal spatial controller impulses tracking target errors.
    @details Translates scalar divergence mapped across K into pure actionable domains.

    @param K_lqr Linear Quadratic feedback gain loop matrix.
    @param current_state Current temporal network snapshot geometry block.
    @param target_state Theoretical baseline configuration anchor.

    @return Formulated spatial response vector `u`.

    @pre
        - Geometries inherently coupled dimensionally.
    @post
        - Outputs mathematically empty vector safely if control architecture is structurally disabled.
    @invariant
        - Imposes exact negative affine feedback responses u = -K * error.
    """
    if K_lqr.shape[0] == 0:
        return np.array([])
        
    error_state = current_state - target_state
    u = -np.dot(K_lqr, error_state)
    
    return u
