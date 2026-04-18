#!/usr/bin/env python3
# test_core_safe_linalg.py
import unittest
import numpy as np
from src.core.core_safe_linalg import compute_safe_pinv, compute_covariance_matrix

class TestSafeLinalg(unittest.TestCase):
    def test_compute_safe_pinv_singular(self):
        """
        Verify that a safe pseudo-inverse matrix can be calculated
        without throwing an exception for a completely rank-deficient (singular) matrix.
        """
        # Intentionally rank-deficient matrix (row 2 is twice row 1, so determinant is 0)
        M_singular = np.array([
            [1.0, 2.0],
            [2.0, 4.0]
        ])
        
        
        # If normal np.linalg.inv(M_singular) is called, it will crash with LinAlgError,
        # but safe_pinv should return the result (NumPy array) without crashing.
        # Tikhonov regularization term (Ridge penalty)
        # lambda_reg = 1e-4
        actual_pinv = compute_safe_pinv(M_singular, rcond=1e-15, lambda_reg=1e-4)
        
        # Verify that the result has the correct shape (2x2) and does not contain NaN, etc.
        self.assertEqual(actual_pinv.shape, (2, 2))
        self.assertFalse(np.isnan(actual_pinv).any())
        
    def test_compute_safe_pinv_zero_matrix(self):
        """
        Test for a matrix where all elements are zero (complete nothingness with no transactions at all).
        """
        M_zero = np.zeros((3, 3))
        
        # The pseudo-inverse matrix of a zero matrix should be a zero matrix,
        # but adding lambda_reg (regularization term) avoids crashing.
        actual_pinv = compute_safe_pinv(M_zero, rcond=1e-15, lambda_reg=1e-4)
        
        self.assertEqual(actual_pinv.shape, (3, 3))
        self.assertFalse(np.isnan(actual_pinv).any())


    def test_compute_covariance_matrix_basic(self):
        """
        Test to correctly calculate the covariance matrix between nodes from the past state displacement vector (dq_history).
        """
        
        # dq_history: (Time_steps x Nodes) matrix
        # Assuming a simple history of 3 steps (T=3) and 2 nodes (N=2) here
        # Node 0 history: [1, 3, 5] (mean=3)
        # Node 1 history: [2, 4, 6] (mean=4)
        dq_history = np.array([
            [1.0, 2.0],
            [3.0, 4.0],
            [5.0, 6.0]
        ])
        
        # Expected covariance matrix (N x N)
        # Node 0 variance (unbiased variance): ((1-3)^2 + (3-3)^2 + (5-3)^2) / (3-1) = 8 / 2 = 4.0
        # Node 1 variance: ((2-4)^2 + (4-4)^2 + (6-4)^2) / 2 = 4.0
        # Covariance of nodes 0 and 1: ((-2)*(-2) + 0*0 + 2*2) / 2 = 8 / 2 = 4.0
        expected_cov = np.array([
            [4.0, 4.0],
            [4.0, 4.0]
        ])
        
        actual_cov = compute_covariance_matrix(dq_history)
        
        # Verify that the shape is (N, N) and the values match
        self.assertEqual(actual_cov.shape, (2, 2))
        np.testing.assert_array_almost_equal(actual_cov, expected_cov)


    def test_compute_safe_pinv_exact_3x3_with_tikhonov(self):
        """
        Verification test to see if the correct inverse matrix can be found via the Tikhonov regularization route (via M^T M)
        for a 3x3 matrix that exploded in the ripple echo.
        """
        
        # Troublesome matrix that contains negative eigenvalues and explodes if the echo is processed as is
        M_3x3 = np.array([
            [1.0, 2.0, 3.0],
            [3.0, 5.0, 4.0],
            [5.0, 6.0, 1.0]
        ])
        
        # Mathematically true inverse matrix (exact value obtained directly with np.linalg.inv)
        # Decimal representation of 19/6, -16/6, 7/6 ...
        expected_inv_exact = np.array([
            [ 3.16666667, -2.66666667,  1.16666667],
            [-2.83333333,  2.33333333, -0.83333333],
            [ 1.16666667, -0.66666667,  0.16666667]
        ])
        
        # 1. Route without penalty (lambda=0.0)
        # Since it is a simple SVD-based pseudo-inverse matrix, it should naturally match.
        actual_inv_0 = compute_safe_pinv(M_3x3, rcond=1e-15, lambda_reg=0.0)
        np.testing.assert_array_almost_equal(actual_inv_0, expected_inv_exact, decimal=5)
        
        # 2. Tikhonov regularization route with a minute penalty (lambda=1e-4)
        # Prove that the shape of the true inverse matrix is not corrupted even through the calculation of M^T * M + lambda * I!
        actual_inv_reg = compute_safe_pinv(M_3x3, rcond=1e-15, lambda_reg=1e-4)

        np.testing.assert_array_almost_equal(actual_inv_reg, expected_inv_exact, decimal=2)


if __name__ == '__main__':
    unittest.main()