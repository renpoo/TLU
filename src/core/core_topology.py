#!/usr/bin/env python3
# core_topology.py
import numpy as np

def compute_edge_stress(T_current: np.ndarray, T_history_window: list[np.ndarray]) -> np.ndarray:
    """
    Calculate the current edge-wise stress from the history of past transition probability (or flux) matrices.
    Stress is defined as the degree of deviation (univariate Z-score) from the past average.
    
    Args:
        T_current: Current matrix (Nodes x Nodes)
        T_history_window: List of past matrices
        
    Returns:
        stress_matrix: Edge-wise stress matrix (Nodes x Nodes)
    """
    N = T_current.shape[0]
    if len(T_history_window) < 2:
        return np.zeros((N, N), dtype=float)
        
    hist_arr = np.array(T_history_window)
    mean_tensor = np.mean(hist_arr, axis=0)
    std_tensor = np.std(hist_arr, axis=0)
    
    # Calculate deviation
    deviation = np.abs(T_current - mean_tensor)
    
    # Avoid zero division: Stress is 0 for edges with a standard deviation of 0 (always constant transaction amount)
    stress_matrix = np.divide(
        deviation, 
        std_tensor, 
        out=np.zeros_like(deviation), 
        where=(std_tensor != 0)
    )
    
    return stress_matrix
