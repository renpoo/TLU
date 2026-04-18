#!/usr/bin/env python3
# core_forensics.py
import numpy as np
from src.core.core_information_geometry import compute_kl_divergence

def check_conservation_law(q_current: np.ndarray, tolerance: float) -> tuple[float, bool]:
    """
    Calculate the total sum of the pure flux across the entire network to detect conservation law residuals (leaks).
    * tolerance must be explicitly injected by the caller.
    """
    # Total inflow and outflow of the entire system. For closed systems like double-entry bookkeeping, this should inherently be 0.
    residual = float(np.sum(q_current))
    abs_residual = abs(residual)
    
    # Determine as a "leak" if it exceeds the floating-point arithmetic error (tolerance)
    is_leaking = abs_residual > tolerance
    
    return abs_residual, is_leaking

def compute_structural_drift(P_current: np.ndarray, P_history: list[np.ndarray]) -> float:
    """
    Calculate the baseline from the history of past transition probability matrices, and return the total sum of KL divergence against the current distribution.
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
    """
    Calculate the Mahalanobis distance (Z-score) of the current state vector using the precision matrix (inverse of the covariance matrix).
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
    """
    Determine if the various anomaly scores exceed the thresholds and return 1 (anomaly) or 0 (normal).
    * To maintain scale invariance, no implicit default values are held internally.
    * thresholds MUST contain 'leak_tolerance', 'kl_drift_thresh', 'z_score_thresh'.
    """
    # Intentional Fail-Fast: explicitly raise a KeyError if a key does not exist
    if residual > thresholds['leak_tolerance']:
        return 1
    if kl_div > thresholds['kl_drift_thresh']:
        return 1
    if z_score > thresholds['z_score_thresh']:
        return 1
    
    return 0
