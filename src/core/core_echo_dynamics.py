#!/usr/bin/env python3
# core_echo_dynamics.py
import numpy as np

def compute_finite_echo(P_matrix, gamma, max_k):
    """!
    @brief Calculate the finite echo matrix sum (M_echo).
    @details Generates the mathematical power series approximation up to max_k.

    @param P_matrix Transition probability matrix (N x N).
    @param gamma Extinction damping factor scalar.
    @param max_k Propagation recurrence steps.

    @return The finite sum echo matrix (N x N).

    @pre
        - `P_matrix` size constraints (square array).
    @post
        - Unconditionally calculates bounds assuming a discrete Markov-chain step.
    @invariant
        - 0-th step implicitly defaults to the identity matrix.
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
    """!
    @brief Decompose the finite echo matrix by k-th propagation step.
    @details Returns a chronologically sequential list of the discrete matrix powers.

    @param P_matrix Transition probability matrix (N x N).
    @param gamma Extinction damping factor scalar.
    @param max_k Propagation recurrence steps.

    @return List of ordered k-th layer discrete transmission arrays.

    @pre
        - `P_matrix` size constraints (square array).
    @post
        - Yields a python list exactly `max_k` elements long.
    @invariant
        - Tracks strictly the sequential spread (gamma^k * P^k) mapping.
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
