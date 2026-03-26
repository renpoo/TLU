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

def build_QR_matrices(N: int, num_inputs: int, weight_Q: float, weight_R: float, target_indices: list[int]) -> tuple[np.ndarray, np.ndarray]:
    Q = np.zeros((N, N), dtype=float)
    for idx in target_indices:
        Q[idx, idx] = weight_Q
        
    safe_weight_R = max(weight_R, 1e-6)
    R = np.eye(num_inputs, dtype=float) * safe_weight_R
    
    return Q, R

def solve_lqr_gain(A: np.ndarray, B: np.ndarray, Q: np.ndarray, R: np.ndarray) -> np.ndarray:
    if B.shape[1] == 0 or np.all(B == 0):
        return np.zeros((0, A.shape[0]))

    try:
        S = la.solve_discrete_are(A, B, Q, R)
        Bp_S_B = np.dot(B.T, np.dot(S, B))
        
        # 修正: np.linalg.pinv を廃止し、SDL_04 のコア関数へ委譲
        R_plus_Bp_S_B_inv = compute_safe_pinv(R + Bp_S_B, rcond=1e-15, lambda_reg=1e-6)
        
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
