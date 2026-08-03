#!/usr/bin/env python3
# ==========================================
# src/core/core_contracts.py
# TLU Core: Design by Contract (DbC) Math Assertions
# ==========================================
"""!
@file core_contracts.py
@brief Design by Contract (DbC) assertions and decorators for mathematical core operations.
@details Enforces invariants such as stochasticity, symmetry, and positive semi-definiteness.
"""

import functools
import numpy as np
from typing import Callable, Any

def assert_stochastic_matrix(mat: np.ndarray, tol: float = 1e-4):
    """!
    @brief DbC Invariant: Assert matrix is a valid Markov transition matrix (row sum = 1.0 for active rows).
    """
    if not isinstance(mat, np.ndarray):
        raise TypeError(f"DbC Violation: Expected numpy.ndarray, got {type(mat)}")
    if mat.ndim != 2 or mat.shape[0] != mat.shape[1]:
        raise ValueError(f"DbC Violation: Expected square matrix, got shape {mat.shape}")
    if np.isnan(mat).any() or np.isinf(mat).any():
        raise ValueError("DbC Violation: Matrix contains NaN or Inf values")
    
    row_sums = np.sum(mat, axis=1)
    active_mask = row_sums > tol
    if np.any(active_mask):
        active_sums = row_sums[active_mask]
        if not np.allclose(active_sums, 1.0, atol=tol):
            raise ValueError(f"DbC Violation: Active row sums must equal 1.0, got sums: {active_sums}")

def assert_symmetric_matrix(mat: np.ndarray, tol: float = 1e-4):
    """!
    @brief DbC Invariant: Assert matrix is symmetric (A = A.T).
    """
    if not isinstance(mat, np.ndarray):
        raise TypeError(f"DbC Violation: Expected numpy.ndarray, got {type(mat)}")
    if mat.ndim != 2 or mat.shape[0] != mat.shape[1]:
        raise ValueError(f"DbC Violation: Expected square matrix, got shape {mat.shape}")
    if not np.allclose(mat, mat.T, atol=tol):
        raise ValueError("DbC Violation: Matrix is not symmetric (A != A.T)")

def assert_positive_semi_definite(mat: np.ndarray, tol: float = 1e-7):
    """!
    @brief DbC Invariant: Assert matrix is positive semi-definite (eigenvalues >= -tol).
    """
    assert_symmetric_matrix(mat, tol=tol)
    eigvals = np.linalg.eigvalsh(mat)
    if np.any(eigvals < -tol):
        raise ValueError(f"DbC Violation: Matrix is not positive semi-definite, min eigenvalue = {np.min(eigvals):.6e}")
