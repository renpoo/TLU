#!/usr/bin/env python3
# test_core_control_theory.py
import unittest
import numpy as np

try:
    import scipy
    from src.core.core_control_theory import (
        build_state_space_matrices,
        build_QR_matrices,
        solve_lqr_gain,
        compute_optimal_input
    )
    SCIPY_AVAILABLE = True
except ImportError:
    SCIPY_AVAILABLE = False

@unittest.skipIf(not SCIPY_AVAILABLE, "Skipping test since scipy is unsupported")
class TestControlTheory(unittest.TestCase):
    def test_build_state_space_matrices(self):
        # 3-node system. Nodes 0 and 2 are controllable (resource dropable)
        P_matrix = np.array([
            [0.8, 0.2, 0.0],
            [0.1, 0.9, 0.0],
            [0.0, 0.0, 1.0]
        ])
        controllable_indices = [0, 2]
        
        A, B = build_state_space_matrices(P_matrix, controllable_indices)
        
        # A matrix should match P matrix (this time use P as is as LTI system)
        np.testing.assert_array_equal(A, P_matrix)
        
        # B matrix should be a (3 x 2) mapping matrix
        expected_B = np.array([
            [1.0, 0.0], # Input to Node 0
            [0.0, 0.0], # Node 1 is uncontrollable
            [0.0, 1.0]  # Input to Node 2
        ])
        np.testing.assert_array_equal(B, expected_B)

    def test_build_QR_matrices(self):
        N = 3
        num_inputs = 2
        weight_Q = 10.0
        weight_R = 1.0
        target_indices = [1] # Emphasize achieving the goal of Node 1
        
        Q, R = build_QR_matrices(N, num_inputs, weight_Q, weight_R, target_indices)
        
        # Q is (3 x 3). The weight of target Node 1 (index 1) becomes 10.0
        expected_Q = np.diag([0.0, 10.0, 0.0])
        # R is (2 x 2). Penalty for input is 1.0
        expected_R = np.diag([1.0, 1.0])
        
        np.testing.assert_array_equal(Q, expected_Q)
        np.testing.assert_array_equal(R, expected_R)

    def test_solve_lqr_gain_and_optimal_input(self):
        # Verification with a very simple 1D system
        # x(t+1) = 1.0 * x(t) + 1.0 * u(t)
        A = np.array([[1.0]])
        B = np.array([[1.0]])
        Q = np.array([[10.0]]) # Hate deviation from target very much
        R = np.array([[1.0]])  # Care a little bit about cost
        
        K_lqr = solve_lqr_gain(A, B, Q, R)
        
        # K based on exact solution of DARE is about 0.916
        self.assertEqual(K_lqr.shape, (1, 1))
        self.assertTrue(K_lqr[0, 0] > 0.0) # Positive feedback gain must be applied
        
        # When current state is 50.0 and target is 100.0
        current_state = np.array([50.0])
        target_state = np.array([100.0])
        
        u = compute_optimal_input(K_lqr, current_state, target_state)
        
        # u = -K * (current - target) = -K * (-50) = K * 50
        # Since the gain is about 0.9, the input should be about 45.0 (tries to close the gap at once)
        self.assertTrue(u[0] > 40.0)

if __name__ == '__main__':
    unittest.main()
