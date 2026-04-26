#!/usr/bin/env python3
# core_forensics.py
import numpy as np
from src.core.core_information_geometry import compute_kl_divergence

def check_conservation_law(q_current: np.ndarray, tolerance: float, leak_idx: int = -1) -> tuple[float, bool]:
    """!
    @brief Calculate the total sum of the pure flux across the entire network to detect conservation law residuals (leaks).
    @details Evaluates the closed-system integrity by summing the net flux. If leak_idx is provided, uses its accumulation as the residual.

    @param q_current Net flux vector for all nodes (shape: N).
    @param tolerance Floating point tolerance limit for leak detection.
    @param leak_idx Optional index of the UNKNOWN_LEAK node.

    @return A tuple (abs_residual, is_leaking) representing the absolute residual and leak status.
    """
    if leak_idx >= 0 and leak_idx < len(q_current):
        residual = float(q_current[leak_idx])
    else:
        # Total inflow and outflow of the entire system. For closed systems like double-entry bookkeeping, this should inherently be 0.
        residual = float(np.sum(q_current))
        
    abs_residual = abs(residual)
    
    # Determine as a "leak" if it exceeds the floating-point arithmetic error (tolerance)
    is_leaking = abs_residual > tolerance
    
    return abs_residual, is_leaking

def compute_structural_drift(P_current: np.ndarray, P_history: list[np.ndarray]) -> float:
    """!
    @brief Calculate the structural drift using KL divergence.
    @details Computes the baseline from the history of past transition matrices, and returns the total sum of KL divergence.

    @param P_current Current transition probability matrix (N x N).
    @param P_history List of historical transition probability matrices.

    @return The total sum of KL divergence for the entire network.

    @pre
        - `P_current` and matrices in `P_history` must be valid N x N matrices.
    @post
        - Returns 0.0 if `P_history` is empty.
        - Returns a non-negative float representing structural change.
    @invariant
        - Transition probabilities are non-negative and stable over time.
    """
    if not P_history:
        return 0.0
    
    # Take the average of the past history (multiple matrices) and set it as the "normal distribution rule (baseline)"
    P_baseline = np.mean(P_history, axis=0)
    
    # Extract KL divergence for each node using the shared library
    kl_div_array = compute_kl_divergence(P_current, P_baseline)
    
    # Sum all distances per node to represent the "magnitude of structural change" for the entire network
    return float(np.sum(kl_div_array))

def compute_multivariate_anomaly(q_current: np.ndarray, q_mean: np.ndarray, K_precision: np.ndarray) -> float:
    """!
    @brief Calculate the multivariate anomaly using Mahalanobis distance (Z-score).
    @details Calculates the Mahalanobis distance of the current state vector using the precision matrix.

    @param q_current Current state vector.
    @param q_mean Historical mean of the state vector.
    @param K_precision Precision matrix (inverse covariance).

    @return The Z-score (Mahalanobis distance) as a float.

    @pre
        - Dimensions of `q_current`, `q_mean`, and `K_precision` must match correctly.
        - `K_precision` must be safely calculated (e.g., via pseudoinverse) by the caller.
    @post
        - Returns a unconditionally non-negative float distance.
    @invariant
        - The distance metric strictly satisfies non-negativity.
    """
    # Deviation from the expected value (displacement vector)
    delta = q_current - q_mean
    
    # Calculate (q - μ)^T * K * (q - μ)
    # * Assumes K_precision has been safely calculated using compute_safe_pinv by the caller
    mahalanobis_sq = np.dot(delta.T, np.dot(K_precision, delta))
    
    # Take the square root since it is a distance. Protect with max(0, ...) to prevent negative cases due to numerical errors.
    z_score = np.sqrt(max(0.0, mahalanobis_sq))
    
    return float(z_score)

def evaluate_anomaly_flags(residual: float, kl_div: float, z_score: float, thresholds: dict) -> int:
    """!
    @brief Determine if the anomaly scores exceed given thresholds.
    @details Evaluates anomaly scores against explicit thresholds. Strict Fail-Fast on missing keys.

    @param residual Calculated leak residual.
    @param kl_div Calculated KL divergence drift.
    @param z_score Calculated Mahalanobis Z-score.
    @param thresholds Dictionary containing detection limits.

    @return 1 if an anomaly is detected, 0 otherwise (normal).

    @pre
        - `thresholds` MUST contain 'leak_tolerance', 'kl_drift_thresh', and 'z_score_thresh'.
    @post
        - Returns strictly an integer 0 or 1.
    @invariant
        - Scale invariance: no implicit default values are maintained internally.
    """
    # Intentional Fail-Fast: explicitly raise a KeyError if a key does not exist
    if residual > thresholds['leak_tolerance']:
        return 1
    if kl_div > thresholds['kl_drift_thresh']:
        return 1
    if z_score > thresholds['z_score_thresh']:
        return 1
    
    return 0
