#!/usr/bin/env python3
# core_thermodynamics.py
import numpy as np
from typing import List
from src.core.core_information_geometry import compute_shannon_entropy

# ==========================================
# Macro Thermodynamics (System-wide Indicators)
# ==========================================

def compute_internal_energy(X_current: np.ndarray) -> float:
    """!
    @brief Calculate the macro internal energy (U) for the network.
    @details U is defined as the total sum of absolute values of the absolute balances.

    @param X_current Absolute balance (State) vector.

    @return Macro internal energy U.

    @pre
        - `X_current` must be a valid numeric 1D numpy array.
    @post
        - Returns a unconditionally non-negative float.
    @invariant
        - U acts as a macroscopic scalar representation of system-wide activity.
    """
    return float(np.sum(np.abs(X_current)))

def compute_work(q_vector: np.ndarray, work_indices: List[int]) -> float:
    """!
    @brief Calculate the effective work (W) extracted from the system.
    @details Work is defined as the sum of pure inflow to nodes designated as work_sink.

    @param q_vector Pure net flux vector (1D array).
    @param work_indices List of node indices designated to extract work.

    @return Extracted work W as a float.

    @pre
        - `work_indices` must be valid integer indices boundary-checked against `q_vector`.
    @post
        - Returns 0.0 if `work_indices` is empty.
    @invariant
        - Work represents energy physically removed from the system loop.
    """
    if not work_indices:
        return 0.0
    return float(np.sum(q_vector[work_indices]))

def compute_heat(q_vector: np.ndarray, heat_indices: List[int]) -> float:
    """!
    @brief Calculate the dissipated heat (Q) lost from the system.
    @details Heat is defined as the total pure inflow to nodes designated as heat_sink.

    @param q_vector Pure net flux vector (1D array).
    @param heat_indices List of node indices designated for dissipation.

    @return Dissipated heat Q as a float.

    @pre
        - `heat_indices` must be valid integer indices boundary-checked against `q_vector`.
    @post
        - Returns 0.0 if `heat_indices` is empty.
    @invariant
        - Heat represents energy irrecoverably lost to the environment.
    """
    if not heat_indices:
        return 0.0
    return float(np.sum(q_vector[heat_indices]))

def compute_macro_entropy(P: np.ndarray) -> float:
    """!
    @brief Calculate the macroscopic entropy S of the entire network.
    @details Sums the Shannon entropy of each individual node.

    @param P Transition probability matrix (Nodes x Nodes).

    @return Macroscopic entropy S.

    @pre
        - `P` must be a valid Markov-chain transition probability matrix.
    @post
        - Returns a non-negative float.
    @invariant
        - Entropy evaluates system stochasticity and degrees of freedom.
    """
    node_entropies = compute_shannon_entropy(P)
    S = float(np.sum(node_entropies))
    return S

def compute_helmholtz_free_energy(U: float, T: float, S: float) -> float:
    """!
    @brief Calculate the Helmholtz free energy F.
    @details Formula: F = U - TS. Represents the total useful work derivable from the system.

    @param U Internal energy.
    @param T Macroscopic temperature.
    @param S Macroscopic entropy.

    @return Helmholtz free energy F as a float.

    @pre
        - T must be corrected to a standard deviation scale that has the same dimension as U.
    @post
        - Returns a float. Can be negative depending on entropic expansion.
    @invariant
        - Follows fundamental classical thermodynamics laws.
    """
    return U - T * S

def compute_natural_parameter_temperature(
    history_window: np.ndarray, 
    lambda_reg: float = 1e-4
) -> tuple[float, np.ndarray]:
    """!
    @brief Calculate macro and local temperature based on Exponential Family Natural Parameters (theta) and Fisher Information.
    @details Implements SDL_001 natural parameter temperature redefinition T = 1 / ||theta||.
             Uses regularized precision matrix (Fisher Information) for robust shrinkage estimation.

    @param history_window Historical state or flux vectors (Time_steps x Nodes).
    @param lambda_reg Tikhonov regularization scalar for Fisher matrix inversion.

    @return Tuple of (macro_temperature_T: float, local_temperatures_T_i: np.ndarray).
    """
    if len(history_window) < 2:
        N = history_window.shape[1] if history_window.ndim == 2 else 1
        return 0.0, np.zeros(N, dtype=float)

    from src.core.core_safe_linalg import compute_safe_pinv, compute_covariance_matrix, DEFAULT_RCOND
    mean_vec = np.mean(history_window, axis=0)
    cov_mat = compute_covariance_matrix(history_window)
    
    K_precision = compute_safe_pinv(cov_mat, rcond=DEFAULT_RCOND, lambda_reg=lambda_reg)
    theta_local = np.abs(np.dot(K_precision, mean_vec))
    
    eps = 1e-8
    local_T = 1.0 / (theta_local + eps)
    macro_T = float(np.sum(local_T))
    
    return macro_T, local_T

def compute_macro_temperature(X_history_window: np.ndarray, use_natural_parameter: bool = False) -> float:
    """!
    @brief Calculate the temperature T of the entire network.
    @details If use_natural_parameter=True, computes T using Fisher information natural parameters.
             Otherwise, computes T as the sum of standard deviations across the network.

    @param X_history_window History window of absolute balance vectors.
    @param use_natural_parameter Whether to use natural parameter theta estimation (default False for backward compatibility).

    @return Macroscopic temperature T.
    """
    if use_natural_parameter:
        macro_T, _ = compute_natural_parameter_temperature(X_history_window)
        return macro_T

    node_std = np.std(X_history_window, axis=0, ddof=0)
    T = float(np.sum(node_std))
    return T

# ==========================================
# Local Thermodynamics (Node-specific Local Indicators)
# ==========================================

def compute_local_internal_energy(X_current: np.ndarray) -> np.ndarray:
    """!
    @brief Calculate the node-specific local internal energy (u_i).
    @details Assesses absolute sums of absolute balances dimensionally constrained per node.

    @param X_current Absolute balance (State) vector.

    @return A 1D numpy array of local internal energies.

    @pre
        - `X_current` must be a 1D numpy array.
    @post
        - Result is unconditionally positive or zero.
    @invariant
        - Represents isolated local node activity, disregarding cross-network aggregation.
    """
    return np.abs(X_current)

def compute_local_temperature(X_history_window: np.ndarray, use_natural_parameter: bool = False) -> np.ndarray:
    """!
    @brief Calculate the local temperature T_i at each node in the network.
    @details If use_natural_parameter=True, computes local T using Fisher information natural parameters.
             Otherwise, computes local T as the univariate standard deviation for that node.

    @param X_history_window Historical absolute balances (Time_steps x Nodes).
    @param use_natural_parameter Whether to use natural parameter theta estimation (default False).

    @return A 1D numpy array of node temperatures.
    """
    if len(X_history_window) < 2:
        N = X_history_window.shape[1] if X_history_window.ndim == 2 else 1
        return np.zeros(N, dtype=float)

    if use_natural_parameter:
        _, local_T = compute_natural_parameter_temperature(X_history_window)
        return local_T

    return np.std(X_history_window, axis=0, ddof=0)

def compute_local_temperature_gradient(t_local: np.ndarray, T_slice: np.ndarray) -> np.ndarray:
    """!
    @brief Calculate the local spatial temperature gradient for each topological network node.
    @details Evaluates the sum of temperature differences between a node and its bounded neighbors tracking bottleneck constraints.

    @param t_local 1D array of extracted absolute local node temperatures.
    @param T_slice Transition flux interaction graph defining connectivity matrices.

    @return A 1D numpy array representing directional thermal gradient stress variables bounds.

    @pre
        - Length of `t_local` structurally identical to bounded dimensionality `N` representing columns and rows.
    @post
        - Extracts positive gradients indicating downstream sinks relative to heavily constrained isolated hot points.
    @invariant
        - Structurally derives completely unweighted geometric distance shifts mapped strictly topographically minimizing numeric scaling biases.
    """
    N = T_slice.shape[0]
    
    # Force undirected boundaries defining edge limits structurally bounded across isolated links
    A = ((T_slice + T_slice.T) > 0).astype(float)
    np.fill_diagonal(A, 0.0)
    
    # Compute topological degrees
    D = np.sum(A, axis=1)
    
    # Extract structural geometric limits representing relative thermal friction: (A * T) - (D * T)
    grad_t = A.dot(t_local) - D * t_local
    
    return grad_t
