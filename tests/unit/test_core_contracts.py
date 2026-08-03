#!/usr/bin/env python3
# ==========================================
# tests/unit/test_core_contracts.py
# Unit tests for DbC math contracts in core_contracts.py
# ==========================================
import unittest
import numpy as np

from src.core.core_contracts import (
    assert_stochastic_matrix,
    assert_symmetric_matrix,
    assert_positive_semi_definite
)

class TestCoreContracts(unittest.TestCase):
    def test_assert_stochastic_matrix_pass(self):
        # Valid stochastic matrix (rows sum to 1.0)
        P = np.array([
            [0.5, 0.5],
            [0.2, 0.8]
        ])
        assert_stochastic_matrix(P)

    def test_assert_stochastic_matrix_invalid_sums(self):
        # Row sums do not equal 1.0
        P = np.array([
            [0.5, 0.9],
            [0.2, 0.8]
        ])
        with self.assertRaises(ValueError):
            assert_stochastic_matrix(P)

    def test_assert_symmetric_matrix_pass(self):
        S = np.array([
            [1.0, 2.0],
            [2.0, 3.0]
        ])
        assert_symmetric_matrix(S)

    def test_assert_symmetric_matrix_fail(self):
        S = np.array([
            [1.0, 2.0],
            [0.0, 3.0]
        ])
        with self.assertRaises(ValueError):
            assert_symmetric_matrix(S)

    def test_assert_positive_semi_definite_pass(self):
        # Covariance matrix is PSD
        A = np.array([[2.0, -1.0], [-1.0, 2.0]])
        assert_positive_semi_definite(A)

    def test_assert_positive_semi_definite_fail(self):
        # Symmetric but has negative eigenvalue (-1)
        A = np.array([[0.0, 1.0], [1.0, 0.0]])
        with self.assertRaises(ValueError):
            assert_positive_semi_definite(A)

if __name__ == '__main__':
    unittest.main()
