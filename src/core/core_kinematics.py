#!/usr/bin/env python3
# core_kinematics.py
import numpy as np
from src.core.core_safe_linalg import compute_safe_pinv

def build_echo_matrix(P: np.ndarray, gamma: float, max_k: int) -> np.ndarray:
    """Build the finite echo matrix M_echo from the transition probability matrix P"""
    N = P.shape[0]
    M_echo = np.eye(N)
    current_P = np.eye(N)
    for k in range(1, max_k + 1):
        current_P = np.dot(current_P, P)
        M_echo += (gamma ** k) * current_P
    return M_echo

def run_forward_simulation(P, dq_input, gamma, max_k):
    """
    [Twin Swords 1: Propagation Simulation]
    Sequentially apply the finite propagation model M_echo = I + (gamma*P) + ... + (gamma*P)^max_k
    to the input displacement dq_input to calculate the final propagation impact.
    """
    total_dq = np.copy(dq_input)
    current_wave = np.copy(dq_input)
    
    for k in range(1, max_k + 1):
        # Optimize by multiplying (gamma * P) to the propagation from the previous step instead of calculating matrix powers directly
        current_wave = gamma * np.dot(current_wave, P)
        total_dq += current_wave
        
    return total_dq

def suggest_lambda(M: np.ndarray, lambda_ratio: float) -> float:
    """
    Propose a dynamic regularization parameter based on the scale of the matrix.
    * Use lambda_ratio from the outside instead of a fixed value like 1e-4.
    """
    return float(np.linalg.norm(M) * lambda_ratio)

def solve_ik_with_safe_stiffness(J: np.ndarray, K_safe: np.ndarray, target_dr: float, lambda_ratio: float):
    """
    [Twin Swords 2: Inverse Kinematics and Strain Optimization]
    Calculate the total displacement dq_opt that minimizes the strain energy U = 1/2 * dq^T * K_safe * dq 
    for the target fluctuation target_dr.
    
    * Receive lambda_ratio from the outside to perform scale-invariant regularization.
    """
    # 1. Calculate the pseudo-inverse (flexibility/covariance) of the stiffness matrix K
    K_inv = compute_safe_pinv(K_safe, rcond=1e-15, lambda_reg=suggest_lambda(K_safe, lambda_ratio))
    
    # 2. Adjust Jacobian J shape (treat 1D vector as a matrix)
    if J.ndim == 1:
        J = J.reshape(1, -1)
        
    # 3. Calculate Gram matrix A = J * K_inv * J.T in projection space
    A = np.dot(J, np.dot(K_inv, J.T))
    
    # 4. Calculate safe inverse of A
    A_inv = compute_safe_pinv(A, rcond=1e-15, lambda_reg=suggest_lambda(A, lambda_ratio))
    
    # 5. Calculate optimal displacement dq_opt
    dr_vec = np.array([target_dr]) if np.isscalar(target_dr) else np.array(target_dr)
    dq_opt = np.dot(K_inv, np.dot(J.T, np.dot(A_inv, dr_vec)))
    
    return dq_opt.flatten()

def compute_derivatives(q_history):
    """
    Calculate the latest velocity (v) and acceleration (a) from the time-series history of the state vector (q).    

    Args:
        q_history: Past state vector history (Time_steps x Nodes)
                   Must be in chronological order (oldest history first).
        
    Returns:
        v: Latest velocity vector (Nodes,)
        a: Latest acceleration vector (Nodes,)
    """
    T = q_history.shape[0]
    
    # Return zero vectors if history is insufficient (only 1 step)
    if T < 2:
        N = q_history.shape[1]
        return np.zeros(N, dtype=float), np.zeros(N, dtype=float)
    
    # Get the latest 2 steps
    q_latest = q_history[-1]   # t
    q_prev = q_history[-2]     # t-1
    
    # Velocity v(t) = q(t) - q(t-1)
    v = q_latest - q_prev
    
    # Acceleration a(t) = v(t) - v(t-1)
    # Calculate v(t-1)
    v_prev = q_prev - q_history[-3] if T >= 3 else v
    
    a = v - v_prev
    
    return v, a
