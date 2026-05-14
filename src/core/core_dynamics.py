#!/usr/bin/env python3
# core_dynamics.py
import numpy as np

def compute_optimal_time_lag(signal_A: np.ndarray, signal_B: np.ndarray, max_lag: int) -> tuple[int, float]:
    """!
    @brief Calculate the cross-correlation and optimal time lag between two signals.
    @details Identifies the time lag that maximizes the Pearson correlation between signal A (cause) and signal B (effect).

    @param signal_A Time-series array for the cause side (1D array).
    @param signal_B Time-series array for the effect side (1D array).
    @param max_lag Maximum number of time lag steps to search.

    @return A tuple (best_lag, max_corr).

    @pre
        - `signal_A` and `signal_B` must be 1D numpy arrays of the same length.
        - `max_lag` must be a non-negative integer.
    @post
        - Returns (0, 0.0) if the array length is too short to compute correlation.
        - `best_lag` is guaranteed to be in the range [0, min(max_lag, N-2)].
    @invariant
        - The correlation coefficient is always bounded within [-1.0, 1.0].
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


def estimate_virtual_mass_and_viscosity(X_history: np.ndarray, damping_ratio: float = 0.1) -> tuple[np.ndarray, np.ndarray]:
    """!
    @brief Estimate the virtual mass (M) and viscosity (C) of each node.
    @details Derives structural inertia (mass) based on historical state.
             Viscosity is modeled as mass-proportional structural damping (Rayleigh damping).
             This eliminates volatile division-by-zero hacks and provides stable physical continuity.

    @param X_history Absolute balance (State) vector history (Time_steps x Nodes).
    @param damping_ratio Proportional constant relating mass to friction.

    @return A tuple of (M, C) arrays.

    @pre
        - `X_history` must be a 2D array-like struct.
        - `damping_ratio` must be a positive float.
    @post
        - Both `M` and `C` arrays are strictly non-negative.
    @invariant
        - M is strictly proportional to the accumulation of past scale.
        - C scales linearly with M (C = M * damping_ratio).
    """
    # Mass M (Inertia): Assumed to be proportional to the accumulation of past activity (scale)
    M = np.mean(np.abs(X_history), axis=0)
    
    # Viscosity C (Friction): Mass-proportional structural damping
    C = M * damping_ratio
    
    return M, C

def compute_external_force_residual(M: np.ndarray, C: np.ndarray, K: np.ndarray, a: np.ndarray, v: np.ndarray, dq: np.ndarray) -> np.ndarray:
    """!
    @brief Backcalculate the abnormal external shock (F_external).
    @details Resolves the second-order physical dynamics equation: F = Ma + Cv + Kdq

    @param M Virtual mass array.
    @param C Viscosity array.
    @param K Stiffness matrix or vector equivalent.
    @param a Acceleration vector.
    @param v Velocity vector.
    @param dq State difference vector.

    @return Formatted external force array.

    @pre
        - All input tensors must be geometrically compatible in shape.
    @post
        - Returns a numerical tensor without side-effects.
    @invariant
        - Computes standard Newtonian equilibrium: Sum of internal forces + residual = external force.
    """
    # F_external = Ma + Cv + Kdq
    return M * a + C * v + K * dq
