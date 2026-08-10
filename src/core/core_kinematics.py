#!/usr/bin/env python3
# core_kinematics.py
import numpy as np
from src.core.core_safe_linalg import compute_safe_pinv

def build_echo_matrix(P: np.ndarray, gamma: float, max_k: int) -> np.ndarray:
    """!
    @brief Build the finite echo matrix M_echo from the transition probability matrix P.
    @details Sums up k-th order propagations geometric series matrix.

    @param P Transition probability matrix (N x N).
    @param gamma Damping factor (scalar).
    @param max_k Maximum propagation step count.

    @return Unrolled finite echo matrix (N x N).

    @pre
        - `P` must be a square stochastic matrix.
        - `max_k` must be >= 0.
    @post
        - Returns an N x N numerically stable finite approximation array.
    @invariant
        - Series converges boundedly if gamma < 1.0.
    """
    N = P.shape[0]
    M_echo = np.eye(N)
    current_P = np.eye(N)
    for k in range(1, max_k + 1):
        current_P = np.dot(current_P, P)
        step_contrib = (gamma ** k) * current_P
        M_echo += step_contrib
        # A6: Stop rule for k >= 3 when propagation energy falls below numerical precision limit
        if k >= 3 and np.max(np.abs(step_contrib)) < 1e-12:
            break
    return M_echo

def run_forward_simulation(P, dq_input, gamma, max_k):
    """!
    @brief [Twin Swords 1: Propagation Simulation] Simulate forward wave propagation.
    @details Sequentially applies the finite propagation model M_echo = I + (gamma*P) + ... + (gamma*P)^max_k to input displacement.

    @param P Transition probability matrix (N x N).
    @param dq_input Initial displacement vector (1D array).
    @param gamma Damping coefficient.
    @param max_k Maximum step count of wave spread.

    @return The final aggregated displacement vector.

    @pre
        - Dimensions of `P` and `dq_input` must align.
    @post
        - Function resolves propagation analytically without recursive state mutations.
    @invariant
        - Energy is structurally damped per step by a factor of gamma.
    """
    total_dq = np.copy(dq_input)
    current_wave = np.copy(dq_input)
    
    for k in range(1, max_k + 1):
        # Optimize by multiplying (gamma * P) to the propagation from the previous step instead of calculating matrix powers directly
        current_wave = gamma * np.dot(current_wave, P)
        total_dq += current_wave
        
    return total_dq

def suggest_lambda(M: np.ndarray, lambda_ratio: float) -> float:
    """!
    @brief Propose a dynamic regularization parameter based on matrix scale.
    @details Enforces scale-invariance dynamically substituting fixed magic number thresholds.

    @param M Target singular matrix.
    @param lambda_ratio Scale-free regularization ratio scalar.

    @return Suggested lambda (float).

    @pre
        - `M` is a valid 2D numerical matrix.
    @post
        - Returns a non-negative float value.
    @invariant
        - Dynamically tracks matrix magnitude norm.
    """
    return float(np.linalg.norm(M) * lambda_ratio)

def solve_ik_with_safe_stiffness(J: np.ndarray, K_safe: np.ndarray, target_dr: float, lambda_ratio: float):
    """!
    @brief [Twin Swords 2: Inverse Kinematics and Strain Optimization] Solve node displacements minimizing strain energy.
    @details Calculates the total displacement dq_opt that minimizes U = 1/2 * dq^T * K_safe * dq.

    @param J Jacobian matrix constraint mapping.
    @param K_safe Stiffness scaling block matrix.
    @param target_dr Target distance scalar fluctuation.
    @param lambda_ratio Regularization magnitude ratio parameter.

    @return Optimal flattened displacement vector dq_opt.

    @pre
        - Valid dimensional alignment between `J` and `K_safe`.
    @post
        - The resulting vector intrinsically achieves pseudo inverse-based minimal norm projection.
    @invariant
        - Solves exact constrained least squares optimization.
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

def compute_higher_order_derivatives(v_history: np.ndarray):
    """!
    @brief Calculate the latest physical Jerk (j) and Snap (s) using discrete difference.
    @details Derives Jerk (3rd order time derivative of position) and Snap (4th order time derivative of position)
             from chronologically ordered velocity vector history.

    @param v_history Velocity (Flux) vector history (Time_steps x Nodes). Oldest first.

    @return Tuple of jerk (Nodes,) and snap (Nodes,).
    
    @pre
        - `v_history` must be a valid 2D array ordered chronologically.
    """
    T = v_history.shape[0]
    # Handle both 2D array (T x N) and 1D list of 1D arrays
    if isinstance(v_history, list):
        N = v_history[0].shape[0] if len(v_history) > 0 else 0
    else:
        N = v_history.shape[1] if v_history.ndim == 2 else 0

    jerk = np.zeros(N, dtype=float)
    snap = np.zeros(N, dtype=float)
    
    if T < 1:
        return jerk, snap

    # Convert to array for ease of multi-step indexing if it's a list
    v_arr = np.array(v_history)

    if T >= 3:
        # j(t) = v(t) - 2*v(t-1) + v(t-2)
        jerk = v_arr[-1] - 2 * v_arr[-2] + v_arr[-3]
    if T >= 4:
        # s(t) = v(t) - 3*v(t-1) + 3*v(t-2) - v(t-3)
        snap = v_arr[-1] - 3 * v_arr[-2] + 3 * v_arr[-3] - v_arr[-4]
        
    return jerk, snap

def compute_derivatives(v_history):
    """!
    @brief Calculate the latest physical velocity (v) and acceleration (a).
    @details Derives kinematics differentials from chronologically ordered velocity vector memory.

    @param v_history Velocity (Flux) vector history (Time_steps x Nodes). Oldest first.

    @return Tuple of velocity (Nodes,) and acceleration (Nodes,).

    @pre
        - `v_history` must be a valid 2D array ordered chronologically.
    @post
        - Safely returns zero-filled vectors if bounds assert insufficiently.
    @invariant
        - v(t) is directly the latest flux.
        - First order differentiation a(t) = v(t) - v(t-1)
    """
    T = v_history.shape[0]
    
    # Return zero vectors if history is insufficient
    if T < 1:
        N = v_history.shape[1] if v_history.ndim == 2 else 0
        return np.zeros(N, dtype=float), np.zeros(N, dtype=float)
        
    v_latest = v_history[-1]
    
    if T < 2:
        return v_latest, np.zeros_like(v_latest)
    
    v_prev = v_history[-2]
    a = v_latest - v_prev
    
    return v_latest, a
