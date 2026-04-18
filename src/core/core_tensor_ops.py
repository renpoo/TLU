#!/usr/bin/env python3
# core_tensor_ops.py
import numpy as np

def _compute_outflow(T_matrix):
    """!
    @brief Helper: compute total outflow for each node.
    
    @param T_matrix Transition tensor matrix (Nodes x Nodes).
    @return 1D array of outflow sums.
    """
    return np.sum(T_matrix, axis=1)

def _compute_inflow(T_matrix):
    """!
    @brief Helper: compute total inflow for each node.
    
    @param T_matrix Transition tensor matrix (Nodes x Nodes).
    @return 1D array of inflow sums.
    """
    return np.sum(T_matrix, axis=0)
    
def compute_net_flux(T_matrix):
    """!
    @brief Calculate pure flux from the given transition tensor (matrix).
    @details Pure flux is defined as Inflow - Outflow mathematically.

    @param T_matrix Adjacency matrix of transactions (Nodes x Nodes).

    @return A 1D array representing the net flux for each node.

    @pre
        - `T_matrix` must be a 2D square matrix.
    @post
        - Returns a 1D array of numerical flux values.
    @invariant
        - Total sum of the resulting net flux array theoretically sums to 0 for a closed graph.
    """
    return _compute_inflow(T_matrix) - _compute_outflow(T_matrix)

def compute_transition_matrix(T_matrix):
    """!
    @brief Calculate transition probability matrix (distribution ratio).
    @details Normalizes the transaction matrix by the total outflow of each source node.

    @param T_matrix Adjacency matrix of transactions (Nodes x Nodes).

    @return Formatted transition probability matrix (P_matrix).

    @pre
        - `T_matrix` must be a 2D square matrix of non-negative values.
    @post
        - Handles zero-division securely by enforcing 0.0 where outflow is 0.
        - Rows of the returned matrix sum strictly to 1.0 (if outflow > 0).
    @invariant
        - The resulting matrix behaves as a Markov stochastic matrix.
    """
    outflow = _compute_outflow(T_matrix)
    outflow_col = outflow[:, np.newaxis]
    P_matrix = np.zeros_like(T_matrix, dtype=float)
    return np.divide(T_matrix, outflow_col, out=P_matrix, where=outflow_col != 0)
