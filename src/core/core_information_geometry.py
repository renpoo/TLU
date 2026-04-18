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
    
    # Mask zeros before calculation
    P_masked = np.where(P_matrix > 0, P_matrix, 1.0)
    entropy = -np.sum(P_masked * np.log2(P_masked), axis=1)
    
    return entropy

def compute_kl_divergence(P_current, P_baseline):
    """!
    @brief Calculate the KL divergence between the current transition probability and the past baseline.
    @details Computes the informational distance. Handles zeroes via masking.

    @param P_current Current transition probability matrix (Nodes x Nodes).
    @param P_baseline Past baseline transition probability matrix (Nodes x Nodes).

    @return KL divergence vector per node (Nodes,).

    @pre
        - Both `P_current` and `P_baseline` must be valid 2D numpy arrays.
        - Shapes of `P_current` and `P_baseline` must match perfectly.
    @post
        - Returns a 1D numpy array of non-negative KL divergence values.
    @invariant
        - Information distance is robust to zero-probability states via masking.
    """
    # Handling zero: If p=0 or q=0, p*log(p/q) is treated as 0
    # np.log2(0) produces -inf, so mask it beforehand and substitute 0
    
    # Zero matrix check (safety fallback)
    if np.all(P_current == 0) or np.all(P_baseline == 0):
        return np.zeros(P_current.shape[0], dtype=float)
    
    # Mask zeros before calculation
    # If the denominator becomes zero (P_baseline is 0), that term is treated as 0
    # If the numerator becomes zero (P_current is 0), that term is treated as 0
    mask = (P_current > 0) & (P_baseline > 0)
    
    kl_divergence = np.zeros(P_current.shape[0], dtype=float)
    P_masked = np.where(mask, P_current, 1.0)
    P_baseline_masked = np.where(mask, P_baseline, 1.0)
    kl_divergence = np.sum(P_current * np.log2(P_masked / P_baseline_masked), axis=1)
    
    return kl_divergence

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
