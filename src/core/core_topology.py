#!/usr/bin/env python3
# core_topology.py
import numpy as np
from typing import List, Union

def compute_univariate_z_score(
    current_data: np.ndarray, 
    history_window: List[np.ndarray],
    absolute_deviation: bool = True
) -> np.ndarray:
    """!
    @brief Calculate univariate Z-score for tensors (1D node vectors, 2D edge matrices, or higher-D tensors).
    @details Evaluates absolute or signed standard deviation normalized metrics against history.
             Prevents division-by-zero crashes when standard deviation is zero.

    @param current_data Current slice or vector (arbitrary dimensional tensor).
    @param history_window List of historical array snapshots with matching shape.
    @param absolute_deviation If True, returns absolute magnitude of Z-score. Default True.

    @return Z-score tensor matching current_data shape.
    """
    shape = current_data.shape
    if len(history_window) < 2:
        return np.zeros(shape, dtype=float)
        
    hist_arr = np.array(history_window)
    mean_tensor = np.mean(hist_arr, axis=0)
    std_tensor = np.std(hist_arr, axis=0)
    
    deviation = current_data - mean_tensor
    if absolute_deviation:
        deviation = np.abs(deviation)
    
    z_scores = np.divide(
        deviation, 
        std_tensor, 
        out=np.zeros_like(deviation, dtype=float), 
        where=(std_tensor != 0)
    )
    
    return z_scores

def compute_edge_stress(T_current: np.ndarray, T_history_window: list[np.ndarray]) -> np.ndarray:
    """!
    @brief Calculate the current edge-wise stress from historical transition matrices.
    @details Stress is defined dimensionally as an absolute univariate Z-score against the temporal average.
             Consolidated wrapper around `compute_univariate_z_score`.

    @param T_current Current transition or flux matrix (Nodes x Nodes).
    @param T_history_window List of temporal matrix histories.

    @return Edge-wise stress matrix (Nodes x Nodes).

    @pre
        - All elements inside `T_history_window` must structurally match `T_current` sizes.
    @post
        - Z-score strictly resolves to 0.0 if standard deviation hits zero to prevent crashes.
    @invariant
        - Yields unitless standard variation indices.
    """
    return compute_univariate_z_score(T_current, T_history_window, absolute_deviation=True)
