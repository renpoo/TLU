#!/usr/bin/env python3
# core_thermodynamics.py
import numpy as np
from typing import List
from src.core.core_information_geometry import compute_shannon_entropy

# ==========================================
# Macro Thermodynamics (System-wide Indicators)
# ==========================================

def compute_internal_energy(T_slice: np.ndarray) -> float:
    """
    Calculate the internal energy (U) for one time slice of the network.
    U = Total activity of the entire system (sum of absolute values of total flux)
    """
    return float(np.sum(np.abs(T_slice)))

def compute_work(q_vector: np.ndarray, work_indices: List[int]) -> float:
    """
    Calculate the effective work (W) extracted from the system.
    W = Total pure inflow to nodes designated as work_sink
    """
    if not work_indices:
        return 0.0
    return float(np.sum(q_vector[work_indices]))

def compute_heat(q_vector: np.ndarray, heat_indices: List[int]) -> float:
    """
    Calculate the dissipated heat (Q) lost from the system.
    Q = Total pure inflow to nodes designated as heat_sink
    """
    if not heat_indices:
        return 0.0
    return float(np.sum(q_vector[heat_indices]))

def compute_macro_entropy(P: np.ndarray) -> float:
    """
    Calculate the macroscopic entropy S of the entire network.
    """
    node_entropies = compute_shannon_entropy(P)
    S = float(np.sum(node_entropies))
    return S

def compute_helmholtz_free_energy(U: float, T: float, S: float) -> float:
    """
    Calculate the Helmholtz free energy F.
    F = U - TS
    (* T must be corrected to a standard deviation scale that has the same dimension as U)
    """
    return U - T * S

def compute_macro_temperature(q_history_window: np.ndarray) -> float:
    """
    Calculate the temperature T of the entire network.
    T = Sum of the "standard deviation" of the pure flux of the entire system (adjusted to match dimensions)
    """
    # Fix: Changed from np.var (variance) to np.std (standard deviation) to lower dimension to 1st degree (circle)
    node_std = np.std(q_history_window, axis=0, ddof=0)
    T = float(np.sum(node_std))
    return T

# ==========================================
# Local Thermodynamics (Node-specific Local Indicators)
# ==========================================

def compute_local_internal_energy(T_slice: np.ndarray) -> np.ndarray:
    """
    Calculate the node-specific local internal energy (u_i) in one time slice of the network.
    u_i = Sum of the absolute values of all inflows and outflows for that node
    
    Returns:
        np.ndarray: Local internal energy array of shape (N,)
    """
    inflow = np.sum(np.abs(T_slice), axis=0)
    outflow = np.sum(np.abs(T_slice), axis=1)
    return inflow + outflow

def compute_local_temperature(q_history_window: np.ndarray) -> np.ndarray:
    """
    Calculate the local temperature T_i at each node in the network.
    T_i = "Standard deviation" of the pure flux of each node (within a time window)
    
    Returns:
        np.ndarray: Local temperature array of shape (N,)
    """
    # Return 0 if history is insufficient (only 1 step)
    if len(q_history_window) < 2:
        return np.zeros(q_history_window.shape[1], dtype=float)
        
    # Fix: Changed from np.var (variance) to np.std (standard deviation)
    return np.std(q_history_window, axis=0, ddof=0)
