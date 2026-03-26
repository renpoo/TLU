#!/usr/bin/env python3
# test_core_thermodynamics.py
import unittest
import numpy as np
from src.core.core_thermodynamics import (
    compute_internal_energy, 
    compute_work, 
    compute_heat, 
    compute_macro_entropy, 
    compute_helmholtz_free_energy, 
    compute_macro_temperature,
    compute_local_internal_energy,
    compute_local_temperature
)

class TestCoreThermodynamics(unittest.TestCase):
    # --- Macro Thermodynamics Tests ---
    def test_compute_internal_energy(self):
        T_slice = np.array([
            [0.0, 100.0, 50.0],
            [0.0,   0.0,  0.0],
            [0.0,   0.0,  0.0]
        ])
        U = compute_internal_energy(T_slice)
        self.assertEqual(U, 150.0)

    def test_compute_work(self):
        q_vector = np.array([-150.0, 100.0, 50.0])
        work_indices = [1]
        W = compute_work(q_vector, work_indices)
        self.assertEqual(W, 100.0)

    def test_compute_heat(self):
        q_vector = np.array([-150.0, 100.0, 50.0])
        heat_indices = [2]
        Q = compute_heat(q_vector, heat_indices)
        self.assertEqual(Q, 50.0)

    def test_compute_macro_entropy(self):
        P = np.array([
            [1.0, 0.0],
            [0.5, 0.5]
        ])
        S = compute_macro_entropy(P)
        self.assertAlmostEqual(S, 1.0, places=4)

    def test_compute_helmholtz_free_energy(self):
        U, T, S = 100.0, 2.0, 10.0
        F = compute_helmholtz_free_energy(U, T, S)
        self.assertEqual(F, 80.0)

    def test_compute_macro_temperature(self):
        q_history = np.array([
            [10.0, -10.0],
            [15.0, -15.0],
            [20.0, -20.0]
        ])
        T = compute_macro_temperature(q_history)
        expected_var = np.var([10.0, 15.0, 20.0]) + np.var([-10.0, -15.0, -20.0])
        self.assertAlmostEqual(T, expected_var)

    # --- Local Thermodynamics Tests (新規追加) ---
    def test_compute_local_internal_energy(self):
        T_slice = np.array([
            [0.0, 20.0, 10.0],
            [0.0,  0.0,  5.0],
            [0.0,  0.0,  0.0]
        ])
        expected_u_local = np.array([30.0, 25.0, 15.0])
        u_local = compute_local_internal_energy(T_slice)
        self.assertEqual(u_local.shape, (3,))
        np.testing.assert_array_equal(u_local, expected_u_local)

    def test_compute_local_temperature(self):
        q_history = np.array([
            [10.0, -5.0,  0.0],
            [10.0, -5.0,  0.0],
            [10.0, 10.0, -5.0],
            [10.0, 10.0,  5.0]
        ])
        expected_t_local = np.array([0.0, 56.25, 12.5])
        t_local = compute_local_temperature(q_history)
        self.assertEqual(t_local.shape, (3,))
        np.testing.assert_array_almost_equal(t_local, expected_t_local)

if __name__ == '__main__':
    unittest.main()
