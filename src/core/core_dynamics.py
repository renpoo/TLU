#!/usr/bin/env python3
# core_dynamics.py
import numpy as np

def compute_optimal_time_lag(signal_A: np.ndarray, signal_B: np.ndarray, max_lag: int) -> tuple[int, float]:
    """
    Calculate the cross-correlation between two time-series signals and identify the time lag that maximizes the correlation.
    
    Args:
        signal_A: Time-series array for the cause side (1D np.ndarray) ex: ad spend
        signal_B: Time-series array for the effect side (1D np.ndarray) ex: sales
        max_lag: Maximum number of time lag steps to search (int)
        
    Returns:
        best_lag: Time lag with the highest waveform match (int)
        max_corr: Correlation coefficient at that lag (float)
    """
    N = len(signal_A)
    best_lag = 0
    max_corr = -np.inf
    
    # Limit the upper bound of the lag to search by subtracting the minimum elements required for calculation (2) from the array length
    actual_max_lag = min(max_lag, N - 2)
    
    # Return zero immediately if the history is too short to calculate correlation
    if actual_max_lag < 0:
        return 0, 0.0

    for lag in range(actual_max_lag + 1):
        # Compare by using signal A as a baseline and pulling signal B back by `lag` (left shift)
        slice_A = signal_A[: N - lag]
        slice_B = signal_B[lag :]
        
        # Protect against zero division when the waveform is completely flat (variance is 0) and correlation cannot be calculated
        std_A = np.std(slice_A)
        std_B = np.std(slice_B)
        
        if std_A == 0.0 or std_B == 0.0:
            corr = 0.0
        else:
            # Get the off-diagonal element ([0, 1]) since np.corrcoef returns a 2x2 correlation matrix
            corr = np.corrcoef(slice_A, slice_B)[0, 1]
            
        if corr > max_corr:
            max_corr = corr
            best_lag = lag
            
    return best_lag, float(max_corr)


def estimate_virtual_mass_and_viscosity(q_history: np.ndarray, v_history: np.ndarray, base_epsilon: float, velocity_scale_ratio: float) -> tuple[np.ndarray, np.ndarray]:
    """
    Estimate the virtual mass (M) and viscosity (C) of each node from the past history.
    * Eliminate scale-dependent magic numbers and inject minute value parameters externally.
    
    Args:
        q_history: State vector history (Time_steps x Nodes)
        v_history: Velocity vector history (Time_steps x Nodes)
        base_epsilon: Absolute minute value to prevent zero division
        velocity_scale_ratio: Dynamic minute value ratio based on velocity scale
        
    Returns:
        M: Virtual mass per node (Nodes,)
        C: Viscous resistance per node (Nodes,)
    """
    # Mass M (Inertia): Assumed to be proportional to the accumulation of past activity (scale)
    M = np.mean(np.abs(q_history), axis=0)
    
    # Viscosity C (Friction): Assumed to be higher when velocity fluctuation is smaller (movement is fixed)
    if v_history.shape[0] <= 1:
        # Set all elements to zero if t_idx = 0 (history belongs to only 1 step)
        C = np.zeros(v_history.shape[1])
    else:
        # Take the reciprocal of the standard deviation (volatility) of velocity.
        v_std = np.std(v_history, axis=0)
        
        # Calculate a dynamic minute value to prevent zero division when completely still (standard deviation is 0)
        if (v_std == 0.0).all():
            global_v_scale = np.mean(v_std)
            # Use the externally injected ratio (velocity_scale_ratio)
            dynamic_epsilon = max(base_epsilon, global_v_scale * velocity_scale_ratio)
        else:
            dynamic_epsilon = 0.0

        C = 1.0 / (v_std + dynamic_epsilon)
    
    return M, C

def compute_external_force_residual(M: np.ndarray, C: np.ndarray, K: np.ndarray, a: np.ndarray, v: np.ndarray, dq: np.ndarray) -> np.ndarray:
    """
    Backcalculate the abnormal external shock (F_external) from the observed state of the system (M, C, K, a, v, dq).
    """
    # F_external = Ma + Cv + Kdq
    return M * a + C * v + K * dq
