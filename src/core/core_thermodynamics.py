#!/usr/bin/env python3
# core_thermodynamics.py
import numpy as np
from typing import List
from src.core.core_information_geometry import compute_shannon_entropy

# ==========================================
# Macro Thermodynamics (System-wide Indicators)
# ==========================================

def compute_internal_energy(T_slice: np.ndarray) -> float:
    """!
    @brief Calculate the macro internal energy (U) for the network.
    @details U is defined as the total sum of absolute values of the total transition slice.

    @param T_slice Current transition or flux matrix (Nodes x Nodes).

    @return Macro internal energy U.

    @pre
        - `T_slice` must be a valid numeric 2D numpy array.
    @post
        - Returns a unconditionally non-negative float.
    @invariant
        - U acts as a macroscopic scalar representation of system-wide activity.
    """
    return float(np.sum(np.abs(T_slice)))

def compute_work(q_vector: np.ndarray, work_indices: List[int]) -> float:
    """!
    @brief Calculate the effective work (W) extracted from the system.
    @details Work is defined as the sum of pure inflow to nodes designated as work_sink.

    @param q_vector Pure net flux vector (1D array).
    @param work_indices List of node indices designated to extract work.

    @return Extracted work W as a float.

    @pre
        - `work_indices` must be valid integer indices boundary-checked against `q_vector`.
    @post
        - Returns 0.0 if `work_indices` is empty.
    @invariant
        - Work represents energy physically removed from the system loop.
    """
    if not work_indices:
        return 0.0
    return float(np.sum(q_vector[work_indices]))

def compute_heat(q_vector: np.ndarray, heat_indices: List[int]) -> float:
    """!
    @brief Calculate the dissipated heat (Q) lost from the system.
    @details Heat is defined as the total pure inflow to nodes designated as heat_sink.

    @param q_vector Pure net flux vector (1D array).
    @param heat_indices List of node indices designated for dissipation.

    @return Dissipated heat Q as a float.

    @pre
        - `heat_indices` must be valid integer indices boundary-checked against `q_vector`.
    @post
        - Returns 0.0 if `heat_indices` is empty.
    @invariant
        - Heat represents energy irrecoverably lost to the environment.
    """
    if not heat_indices:
        return 0.0
    return float(np.sum(q_vector[heat_indices]))

def compute_macro_entropy(P: np.ndarray) -> float:
    """!
    @brief Calculate the macroscopic entropy S of the entire network.
    @details Sums the Shannon entropy of each individual node.

    @param P Transition probability matrix (Nodes x Nodes).

    @return Macroscopic entropy S.

    @pre
        - `P` must be a valid Markov-chain transition probability matrix.
    @post
        - Returns a non-negative float.
    @invariant
        - Entropy evaluates system stochasticity and degrees of freedom.
    """
    node_entropies = compute_shannon_entropy(P)
    S = float(np.sum(node_entropies))
    return S

def compute_helmholtz_free_energy(U: float, T: float, S: float) -> float:
    """!
    @brief Calculate the Helmholtz free energy F.
    @details Formula: F = U - TS. Represents the total useful work derivable from the system.

    @param U Internal energy.
    @param T Macroscopic temperature.
    @param S Macroscopic entropy.

    @return Helmholtz free energy F as a float.

    @pre
        - T must be corrected to a standard deviation scale that has the same dimension as U.
    @post
        - Returns a float. Can be negative depending on entropic expansion.
    @invariant
        - Follows fundamental classical thermodynamics laws.
    """
    return U - T * S

def compute_macro_temperature(q_history_window: np.ndarray) -> float:
    """!
    @brief Calculate the temperature T of the entire network.
    @details T is the sum of the standard deviation of pure flux across the network.

    @param q_history_window History window of flux vectors.

    @return Macroscopic temperature T.

    @pre
        - `q_history_window` must be an array of at least shape (m>=1, N).
    @post
        - Returns a strictly non-negative float.
    @invariant
        - Lowered to 1st degree order standard deviation to structurally align physical dimensions with U.
    """
    # Fix: Changed from np.var (variance) to np.std (standard deviation) to lower dimension to 1st degree (circle)
    node_std = np.std(q_history_window, axis=0, ddof=0)
    T = float(np.sum(node_std))
    return T

# ==========================================
# Local Thermodynamics (Node-specific Local Indicators)
# ==========================================

def compute_local_internal_energy(T_slice: np.ndarray) -> np.ndarray:
    """!
    @brief Calculate the node-specific local internal energy (u_i).
    @details Assesses absolute sums of inflows and outflows dimensionally constrained per node.

    @param T_slice Transition or flux matrix.

    @return A 1D numpy array of local internal energies.

    @pre
        - `T_slice` must be a 2D numpy array.
    @post
        - Result is unconditionally positive or zero.
    @invariant
        - Represents isolated local node activity, disregarding cross-network aggregation.
    """
    inflow = np.sum(np.abs(T_slice), axis=0)
    outflow = np.sum(np.abs(T_slice), axis=1)
    return inflow + outflow

def compute_local_temperature(q_history_window: np.ndarray) -> np.ndarray:
    """!
    @brief Calculate the local temperature T_i at each node in the network.
    @details Defines local T as the univariate standard deviation of pure flux for that node.

    @param q_history_window Historical net flux (Time_steps x Nodes).

    @return A 1D numpy array of node temperatures.

    @pre
        - `q_history_window` must be a valid 2D array.
    @post
        - Automatically returns zero vectors if historical depth is insufficient (< 2).
    @invariant
        - Satisfies zero sum baseline shifts under stationary limits.
    """
    # Return 0 if history is insufficient (only 1 step)
    if len(q_history_window) < 2:
        return np.zeros(q_history_window.shape[1], dtype=float)
        
    # Fix: Changed from np.var (variance) to np.std (standard deviation)
    return np.std(q_history_window, axis=0, ddof=0)

def compute_local_temperature_gradient(t_local: np.ndarray, T_slice: np.ndarray) -> np.ndarray:
    """!
    @brief Calculate the local spatial temperature gradient for each topological network node.
    @details Evaluates the sum of temperature differences between a node and its bounded neighbors tracking bottleneck constraints.

    @param t_local 1D array of extracted absolute local node temperatures.
    @param T_slice Transition flux interaction graph defining connectivity matrices.

    @return A 1D numpy array representing directional thermal gradient stress variables bounds.

    @pre
        - Length of `t_local` structurally identical to bounded dimensionality `N` representing columns and rows.
    @post
        - Extracts positive gradients indicating downstream sinks relative to heavily constrained isolated hot points.
    @invariant
        - Structurally derives completely unweighted geometric distance shifts mapped strictly topographically minimizing numeric scaling biases.
    """
    N = T_slice.shape[0]
    
    # Force undirected boundaries defining edge limits structurally bounded across isolated links
    A = ((T_slice + T_slice.T) > 0).astype(float)
    np.fill_diagonal(A, 0.0)
    
    # Compute topological degrees
    D = np.sum(A, axis=1)
    
    # Extract structural geometric limits representing relative thermal friction: (A * T) - (D * T)
    grad_t = A.dot(t_local) - D * t_local
    
    return grad_t
