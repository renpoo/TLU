#!/usr/bin/env python3
# core_information_geometry.py
import numpy as np

def compute_shannon_entropy(P_matrix):
    """
    Calculate the Shannon entropy per node from the transition probability matrix (P).
    
    Args:
        P_matrix: Transition probability matrix (Nodes x Nodes)
        
    Returns:
        entropy: Shannon entropy per node (Nodes,)
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
    """
    Calculate the KL divergence (Kullback-Leibler divergence: informational distance) per node 
    between the current transition probability (P_current) and the past baseline (P_baseline).
    
    Args:
        P_current: Current transition probability matrix (Nodes x Nodes)
        P_baseline: Past baseline transition probability matrix (Nodes x Nodes)
        
    Returns:
        kl_divergence: KL divergence per node (Nodes,)
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
    """
    Calculate the information curvature (absolute value of 2nd order difference, effectively acceleration distortion) 
    per node from the pure flux history.
    
    Args:
        q_history_window: (Steps x Nodes) array. Requires Steps >= 3.
        
    Returns:
        curvature: Curvature vector per node (Nodes,)
    """
    if q_history_window.shape[0] < 3:
        return np.zeros(q_history_window.shape[1], dtype=float)
    
    # 2nd order difference: a(t) = v(t) - v(t-1) = q(t) - 2q(t-1) + q(t-2)
    accel = q_history_window[-1, :] - 2 * q_history_window[-2, :] + q_history_window[-3, :]
    return np.abs(accel)

def compute_information_density(T_slice: np.ndarray) -> np.ndarray:
    """
    Calculate the information density (total sum of absolute inflows and outflows) per node 
    from the current transition slice.
    
    Args:
        T_slice: Current transition probability (or flux) matrix (Nodes x Nodes)
        
    Returns:
        density: Information density vector per node (Nodes,)
    """
    # Sum of outflows (axis=1) + Sum of inflows (axis=0)
    outflow = np.sum(np.abs(T_slice), axis=1)
    inflow = np.sum(np.abs(T_slice), axis=0)
    return outflow + inflow
