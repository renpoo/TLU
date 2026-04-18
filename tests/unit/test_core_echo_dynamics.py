#!/usr/bin/env python3
# test_core_echo_dynamics.py
import unittest
import numpy as np
from src.core.core_echo_dynamics import compute_finite_echo, compute_decomposed_echoes

class TestEchoDynamics(unittest.TestCase):
    def test_compute_finite_echo_basic(self):
        """
        Test to calculate the sum of finite ripple matrix (Echo).
        Verify decay rate (gamma) and step count (k) in a simple model where mass ping-pongs between 2 nodes.
        """
        # P: Transition probability matrix (Node 0 goes 100% to Node 1, Node 1 goes 100% to Node 0)
        P_matrix = np.array([
            [0.0, 1.0],
            [1.0, 0.0]
        ])
        
        gamma = 0.5  # Decay rate (friction coefficient)
        max_k = 2    # Ripple step count (0th order, 1st order, 2nd order)

        # Expected ripple matrix M_echo
        # 0th order ripple (k=0): Identity matrix I = [[1, 0], [0, 1]]
        # 1st order ripple (k=1): gamma^1 * P = [[0, 0.5], [0.5, 0]]
        # 2nd order ripple (k=2): gamma^2 * P^2 = 0.25 * [[1, 0], [0, 1]] = [[0.25, 0], [0, 0.25]]
        # Total M_echo: [[1.25, 0.5], [0.5, 1.25]]
        expected_M_echo = np.array([
            [1.25, 0.5],
            [0.5,  1.25]
        ])

        actual_M_echo = compute_finite_echo(P_matrix, gamma, max_k)

        np.testing.assert_array_almost_equal(actual_M_echo, expected_M_echo)


    def test_compute_decomposed_echoes_basic(self):
        """
        Test to return decomposed k-th order ripples as a list without summing them up.
        """
        P_matrix = np.array([
            [0.0, 1.0],
            [1.0, 0.0]
        ])
        
        gamma = 0.5
        max_k = 2

        # Expected list of decomposed ripple echoes
        # Index 0: 1st order ripple (gamma^1 * P)
        # Index 1: 2nd order ripple (gamma^2 * P^2)
        # * Specification does not include 0th order ripple (identity matrix)
        expected_echoes = [
            np.array([[0.0, 0.5], [0.5, 0.0]]),   # 1st order
            np.array([[0.25, 0.0], [0.0, 0.25]])  # 2nd order
        ]

        actual_echoes = compute_decomposed_echoes(P_matrix, gamma, max_k)

        # Verify that the lengths of the lists match
        assert len(actual_echoes) == len(expected_echoes)
        
        # Verify that the matrices at each level match
        for actual, expected in zip(actual_echoes, expected_echoes):
            np.testing.assert_array_almost_equal(actual, expected)


    def test_compute_decomposed_echoes_identity_matrix(self):
        """
        Test to return decomposed k-th order ripples as a list without summing them up.
        """
        P_matrix = np.array([
            [1.0, 0.0],
            [0.0, 1.0]
        ])
        
        gamma = 1.0
        max_k = 2

        # Expected list of decomposed ripple echoes
        # Index 0: 1st order ripple (gamma^1 * P)
        # Index 1: 2nd order ripple (gamma^2 * P^2)
        # * Specification does not include 0th order ripple (identity matrix)
        expected_echoes = [
            np.array([[1.0, 0.0], [0.0, 1.0]]),   # 1st order
            np.array([[1.0, 0.0], [0.0, 1.0]])   # 2nd order
        ]

        actual_echoes = compute_decomposed_echoes(P_matrix, gamma, max_k)

        # Verify that the lengths of the lists match
        assert len(actual_echoes) == len(expected_echoes)
        
        # Verify that the matrices at each level match
        for actual, expected in zip(actual_echoes, expected_echoes):
            np.testing.assert_array_almost_equal(actual, expected)


    def test_compute_finite_echo_native_2x2(self):
        """
        Normal system test of pure ripple echo function (2x2).
        """
        P_matrix = np.array([
            [0.5, 0.5],
            [1.0, 0.0]
        ])
        gamma = 0.5
        max_k = 50  # Looping 50 times almost reaches the limit of infinite geometric series

        # Expected infinite ripple matrix (exact limit value by hand calculation)
        expected_M_echo = np.array([
            [1.6, 0.4],
            [0.8, 1.2]
        ])

        actual_M_echo = compute_finite_echo(P_matrix, gamma, max_k)

        # Test if it can approximate to the infinite limit "with 6 digits accuracy" in 50 finite loops
        np.testing.assert_array_almost_equal(actual_M_echo, expected_M_echo, decimal=5)

    def test_compute_finite_echo_native_3x3(self):
        """
        Normal system test of pure ripple echo function (3x3).
        """
        P_matrix = np.array([
            [0.0, 0.5, 0.5],
            [0.5, 0.0, 0.5],
            [0.5, 0.5, 0.0]
        ])
        gamma = 0.5
        max_k = 50

        expected_M_echo = np.array([
            [1.2, 0.4, 0.4],
            [0.4, 1.2, 0.4],
            [0.4, 0.4, 1.2]
        ])

        actual_M_echo = compute_finite_echo(P_matrix, gamma, max_k)

        np.testing.assert_array_almost_equal(actual_M_echo, expected_M_echo, decimal=5)


    def test_compute_finite_echo_as_inverse_matrix(self):
        """
        Test to find the inverse matrix M^-1 of a general matrix M
        by using infinite series approximation of ripple echo function (compute_finite_echo).
        """
        # 1. General matrix M to solve
        M = np.array([
            [4.0, 7.0],
            [2.0, 6.0]
        ])
        
        # Expected true inverse matrix (determinant=10)
        expected_M_inv = np.array([
            [ 0.6, -0.7],
            [-0.2,  0.4]
        ])

        # --------------------------------------------------------
        # 2. Process of "translation" to ripple echo format ( I - P )
        # --------------------------------------------------------
        # If M is used as P exactly, the ripple will explode,
        # so define a virtual "frame size (c)" that completely wraps the entire matrix.
        # Here, let's say c = 10.0 is slightly larger than the elements of M.
        c = 10.0
        
        # Back-calculate virtual transition probability matrix P such that M = c * (I - P).
        # P = I - (M / c)
        I = np.eye(2)
        P_matrix = I - (M / c)
        
        # 3. Execute echo
        # Loop ripple 100 steps (max_k=100) without friction (gamma=1.0).
        gamma = 1.0
        max_k = 100
        
        # The echo function calculates an approximation of (I - P)^-1.
        echo_result = compute_finite_echo(P_matrix, gamma, max_k)
        
        # 4. Rewind translation
        # Since M = c * (I - P), M^-1 = (1/c) * (I - P)^-1.
        # Therefore, dividing the echo result by c restores the inverse matrix of M.
        actual_M_inv_approx = echo_result / c
        
        # --------------------------------------------------------
        # 5. Verification
        # --------------------------------------------------------
        # Verify that the approximate value obtained only by echo (addition and multiplication loops)
        # perfectly matches the true inverse matrix "up to 5 decimal places".
        np.testing.assert_array_almost_equal(actual_M_inv_approx, expected_M_inv, decimal=5)


if __name__ == '__main__':
    unittest.main()
