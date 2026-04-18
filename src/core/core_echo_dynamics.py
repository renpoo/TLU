#!/usr/bin/env python3
# core_echo_dynamics.py
import numpy as np

def compute_finite_echo(P_matrix, gamma, max_k):
    """
    Calculate the finite echo matrix (Echo).
    
    Args:
        P_matrix: Transition probability matrix (N x N)
        gamma: Damping factor (scalar)
        max_k: Propagation step count (int)
        
    Returns:
        M_echo: Finite echo matrix (N x N)
    """
    N = P_matrix.shape[0]
    
    # 0-th order propagation (k=0): Identity matrix
    M_echo = np.eye(N, dtype=float)
    
    # Calculate and sum propagations from 1st to max_k-th order
    P_k = P_matrix.copy()  # Transition matrix for k=1
    for k in range(1, max_k + 1):
        M_echo += (gamma ** k) * P_k
        P_k = np.dot(P_k, P_matrix)  # Calculate the transition matrix for the next order
        
    return M_echo


def compute_decomposed_echoes(P_matrix, gamma, max_k):
    """
    Decompose the finite echo matrix (Echo) by k-th propagation and return as a list.
    
    Args:
        P_matrix: Transition probability matrix (N x N)
        gamma: Damping factor (scalar)
        max_k: Propagation step count (int)
        
    Returns:
        echoes: List of k-th order propagation matrices (List[np.ndarray])
                Index 0 is 1st order propagation, index 1 is 2nd order...
    """
    N = P_matrix.shape[0]
    echoes = []
    
    # Calculate propagation from 1st to max_k-th order
    P_k = P_matrix.copy()  # Transition matrix for k=1
    for k in range(1, max_k + 1):
        # k-th order propagation matrix = gamma^k * P^k
        echo_k = (gamma ** k) * P_k
        echoes.append(echo_k)
        
        # Calculate the transition matrix for the next order
        P_k = np.dot(P_k, P_matrix)
        
    return echoes
