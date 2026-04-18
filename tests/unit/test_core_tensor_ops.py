#!/usr/bin/env python3
# test_core_tensor_ops.py
import unittest
import numpy as np
from src.core.core_tensor_ops import compute_net_flux, compute_transition_matrix


class TestStreamProcessor(unittest.TestCase):
    def test_compute_net_flux_basic(self):
        """
        Test to calculate the net flux in a simple 3x3 transition tensor (matrix).
        Pure observation of mass transfer, without any meaning of domains (accounts or departments).
        """
        # Mass transfer between 3 nodes (T_matrix[src, tgt] = value)
        # Node 0 -> Node 1: 10
        # Node 1 -> Node 2: 5
        # Node 2 -> Node 0: 2
        T_matrix = np.array([
            [0, 10,  0],
            [0,  0,  5],
            [2,  0,  0]
        ])
    
        # Expected net flux q (Inflow - Outflow)
        # Node 0: Inflow(2) - Outflow(10) = -8
        # Node 1: Inflow(10) - Outflow(5) = 5
        # Node 2: Inflow(5) - Outflow(2) = 3
        expected_q = np.array([-8, 5, 3])
    
        actual_q = compute_net_flux(T_matrix)
    
        np.testing.assert_array_equal(actual_q, expected_q)


    def test_compute_transition_matrix_basic_and_zero_div(self):
        """
        Test of calculating the transition probability matrix (distribution ratio) and avoiding zero division.
        """
        T_matrix = np.array([
            [0, 8, 2],  # Node 0: Total outflow 10 (80% to Node 1, 20% to Node 2)
            [0, 0, 0],  # Node 1: Total outflow 0 (Zero division crisis!)
            [5, 5, 0]   # Node 2: Total outflow 10 (50% to Node 0, 50% to Node 1)
        ])
        
        # Expected transition matrix P
        # The row for node 1, which cannot be divided, should be safely processed as all 0s.
        expected_P = np.array([
            [0.0, 0.8, 0.2],
            [0.0, 0.0, 0.0],
            [0.5, 0.5, 0.0]
        ])
        
        actual_P = compute_transition_matrix(T_matrix)
        
        np.testing.assert_array_almost_equal(actual_P, expected_P)


    def test_compute_net_flux_basic(self):
        """
        Test of calculating net flux in a simple system of 3 nodes
        Node 0 -> Node 1: 100
        Node 1 -> Node 2: 30
        
        Expected net flux q:
        Node 0: -100 (Outflow only)
        Node 1: +100 - 30 = 70
        Node 2: +30 (Inflow only)
        """
        # Adjacency matrix T (Rows: src, Columns: tgt)
        T = np.array([
            [0, 100,   0],
            [0,   0,  30],
            [0,   0,   0]
        ])
        
        expected_q = np.array([-100, 70, 30])
        
        # Act
        actual_q = compute_net_flux(T)
        
        # Assert
        np.testing.assert_array_almost_equal(actual_q, expected_q)


if __name__ == '__main__':
    unittest.main()
