#!/usr/bin/env python3
# core_information_geometry.py
import numpy as np

def compute_shannon_entropy(P_matrix):
    """!
    @brief Calculate the Shannon entropy per node from the transition probability matrix (P).
    @details Handles zero values gracefully to avoid numerical instability.

    @param P_matrix Transition probability matrix (Nodes x Nodes).

    @return Shannon entropy vector per node (Nodes,).

    @pre
        - `P_matrix` must be a valid 2D numpy array of probabilities.
    @post
        - Returns a 1D numpy array of non-negative entropy values.
    @invariant
        - Values in `P_matrix` are bounded between 0 and 1.
    """
    # Handling zero: 0 * log(0) is treated as 0
    # np.log2(0) produces -inf, so mask it beforehand and substitute 0
    
    # Zero matrix check (safety fallback)
    if np.all(P_matrix == 0):
        return np.zeros(P_matrix.shape[0], dtype=float)
    
    # Mask zeros beforehand to avoid log2(0) numerical warnings
    P_masked = np.where(P_matrix > 0, P_matrix, 1.0)
    entropy_terms = np.where(P_matrix > 0, P_matrix * np.log2(P_masked), 0.0)
    entropy = -np.sum(entropy_terms, axis=1)
    
    return np.maximum(0.0, entropy)

def detect_novel_routes(P_current: np.ndarray, P_baseline: np.ndarray) -> np.ndarray:
    """!
    @brief Detect novel routes (P_baseline == 0 and P_current > 0).
    @details Identifies unprecedented flow transitions that represent potential anomalies.
    
    @param P_current Current transition probability matrix (Nodes x Nodes).
    @param P_baseline Baseline transition probability matrix (Nodes x Nodes).
    
    @return Boolean matrix (Nodes x Nodes) where True indicates a novel route.
    """
    return (P_baseline == 0) & (P_current > 0)

def compute_alpha_divergence(P_current: np.ndarray, P_baseline: np.ndarray, alpha: float = 0.0) -> np.ndarray:
    """!
    @brief Calculate generalized alpha-divergence (default alpha=0.0, Hellinger-type bounded divergence).
    @details Solves the support mismatch bug (P_baseline=0, P_current>0).
             For alpha=0.0 (Hellinger type), D_alpha = sum((sqrt(P) - sqrt(Q))^2, axis=1).
             Always remains non-negative (>= 0.0) and bounded <= 2.0 per row.

    @param P_current Current transition probability matrix (Nodes x Nodes).
    @param P_baseline Baseline transition probability matrix (Nodes x Nodes).
    @param alpha Divergence order parameter (default 0.0).

    @return Alpha divergence vector per node (Nodes,).
    """
    if np.all(P_current == 0) and np.all(P_baseline == 0):
        return np.zeros(P_current.shape[0], dtype=float)

    if alpha == 0.0:
        sqrt_P = np.sqrt(np.maximum(P_current, 0.0))
        sqrt_Q = np.sqrt(np.maximum(P_baseline, 0.0))
        return np.sum((sqrt_P - sqrt_Q) ** 2, axis=1)
    else:
        P_safe = np.maximum(P_current, 0.0)
        Q_safe = np.maximum(P_baseline, 0.0)
        term = (alpha * P_safe + (1.0 - alpha) * Q_safe - (P_safe ** alpha) * (Q_safe ** (1.0 - alpha)))
        return np.sum(term, axis=1) / (alpha * (1.0 - alpha))

def compute_kl_divergence(P_current: np.ndarray, P_baseline: np.ndarray, use_alpha_zero: bool = True) -> np.ndarray:
    """!
    @brief Calculate divergence between current transition probability and baseline.
    @details By default (use_alpha_zero=True), delegates to compute_alpha_divergence(alpha=0.0)
             to avoid support mismatch masking bugs and negative values.
             If use_alpha_zero=False, computes standard KL divergence with epsilon smoothing for zero-support entries.

    @param P_current Current transition probability matrix (Nodes x Nodes).
    @param P_baseline Past baseline transition probability matrix (Nodes x Nodes).
    @param use_alpha_zero Whether to use bounded alpha=0.0 divergence (default True).

    @return Divergence vector per node (Nodes,).
    """
    if use_alpha_zero:
        return compute_alpha_divergence(P_current, P_baseline, alpha=0.0)
    
    if np.all(P_current == 0) or np.all(P_baseline == 0):
        return np.zeros(P_current.shape[0], dtype=float)

    eps = 1e-12
    Q_safe = np.where(P_baseline > 0, P_baseline, eps)
    P_safe = np.where(P_current > 0, P_current, 1.0)
    
    kl_terms = np.where(P_current > 0, P_current * np.log2(P_safe / Q_safe), 0.0)
    return np.maximum(0.0, np.sum(kl_terms, axis=1))

def compute_information_curvature(q_history_window: np.ndarray) -> np.ndarray:
    """!
    @brief Calculate the information curvature from pure flux history.
    @details Represents acceleration distortion by computing the absolute value of the 2nd order difference.

    @param q_history_window History window of flux (Steps x Nodes array).

    @return Curvature vector per node (Nodes,).

    @pre
        - `q_history_window` must be a 2D numpy array.
        - Requires at least 3 historical steps (Steps >= 3) to compute 2nd order difference.
    @post
        - Returns 0 for all nodes if history length < 3.
        - Returns a 1D numpy array of absolute curvature values.
    @invariant
        - Physical interpretation adheres to classical kinematics formulation: a(t) = v(t) - v(t-1).
    """
    if q_history_window.shape[0] < 3:
        return np.zeros(q_history_window.shape[1], dtype=float)
    
    # 2nd order difference: a(t) = v(t) - v(t-1) = q(t) - 2q(t-1) + q(t-2)
    accel = q_history_window[-1, :] - 2 * q_history_window[-2, :] + q_history_window[-3, :]
    return np.abs(accel)

def compute_information_density(T_slice: np.ndarray) -> np.ndarray:
    """!
    @brief Calculate the information density per node.
    @details Computes the total sum of absolute inflows and outflows for each node.

    @param T_slice Current transition or flux matrix (Nodes x Nodes).

    @return Information density vector per node (Nodes,).

    @pre
        - `T_slice` must be a valid 2D numpy array.
    @post
        - Returns a 1D numpy array of non-negative values.
    @invariant
        - Density is purely additive based on graph edges.
    """
    # Sum of outflows (axis=1) + Sum of inflows (axis=0)
    outflow = np.sum(np.abs(T_slice), axis=1)
    inflow = np.sum(np.abs(T_slice), axis=0)
    return outflow + inflow
