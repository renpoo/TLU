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
    Build the weight matrices Q, R for LQR control.
    min_weight_R: Minimum allowable value for R matrix elements to prevent zero-matrix formation. Inject based on external scale.
    """
    Q = np.zeros((N, N), dtype=float)
    for idx in target_indices:
        Q[idx, idx] = weight_Q
        
    # Eliminate the implicit magic number 1e-6 and use the externally injected min_weight_R
    safe_weight_R = max(weight_R, min_weight_R)
    R = np.eye(num_inputs, dtype=float) * safe_weight_R
    
    return Q, R

def solve_lqr_gain(A: np.ndarray, B: np.ndarray, Q: np.ndarray, R: np.ndarray, rcond: float = 1e-15, lambda_reg: float = 0.0) -> np.ndarray:
    """
    Calculate the optimal feedback gain K for discrete-time LQR.
    rcond, lambda_reg: Parameters to avoid singular matrices. Can be injected externally based on the target system scale.
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
    if K_lqr.shape[0] == 0:
        return np.array([])
        
    error_state = current_state - target_state
    u = -np.dot(K_lqr, error_state)
    
    return u
