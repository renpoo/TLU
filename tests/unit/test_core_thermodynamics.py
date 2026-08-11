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
    compute_local_temperature,
    compute_local_temperature_gradient,
    compute_natural_parameter_temperature
)

class TestCoreThermodynamics(unittest.TestCase):
    # --- Macro Thermodynamics Tests ---
    def test_compute_internal_energy(self):
        X_current = np.array([10.0, -20.0, 30.0])
        U = compute_internal_energy(X_current)
        self.assertEqual(U, 60.0)

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
        
        expected_std = np.std([10.0, 15.0, 20.0]) + np.std([-10.0, -15.0, -20.0])
        self.assertAlmostEqual(T, expected_std)

    # --- Local Thermodynamics Tests (Newly added) ---
    def test_compute_local_internal_energy(self):
        X_current = np.array([30.0, -25.0, 15.0])
        expected_u_local = np.array([30.0, 25.0, 15.0])
        u_local = compute_local_internal_energy(X_current)
        self.assertEqual(u_local.shape, (3,))
        np.testing.assert_array_equal(u_local, expected_u_local)

    def test_compute_local_temperature(self):
        q_history = np.array([
            [10.0, -5.0,  0.0],
            [10.0, -5.0,  0.0],
            [10.0, 10.0, -5.0],
            [10.0, 10.0,  5.0]
        ])
        
        expected_t_local = np.std(q_history, axis=0, ddof=0)
        
        t_local = compute_local_temperature(q_history)
        self.assertEqual(t_local.shape, (3,))
        np.testing.assert_array_almost_equal(t_local, expected_t_local)

    def test_compute_local_temperature_gradient(self):
        T_slice = np.array([
            [0.0, 10.0,  0.0],
            [5.0,  0.0, 20.0],
            [0.0,  0.0,  0.0]
        ])
        t_local = np.array([1.0, 5.0, 2.0])
        
        # Node 0 connects to 1. t_1 - t_0 = 5.0 - 1.0 = 4.0
        # Node 1 connects to 0 and 2. (t_0 - t_1) + (t_2 - t_1) = (1.0 - 5.0) + (2.0 - 5.0) = -4.0 - 3.0 = -7.0
        # Node 2 connects to 1. t_1 - t_2 = 5.0 - 2.0 = 3.0
        expected_grad_t = np.array([4.0, -7.0, 3.0])
        
        grad_t = compute_local_temperature_gradient(t_local, T_slice)
        np.testing.assert_array_almost_equal(grad_t, expected_grad_t)

    def test_compute_natural_parameter_temperature(self):
        q_history = np.array([
            [10.0, -5.0],
            [12.0, -4.0],
            [11.0, -6.0]
        ])
        macro_T, local_T = compute_natural_parameter_temperature(q_history)
        self.assertGreater(macro_T, 0.0)
        self.assertEqual(len(local_T), 2)
        self.assertTrue(np.all(local_T > 0.0))

        # Test macro and local temperature with use_natural_parameter=True
        T_macro_nat = compute_macro_temperature(q_history, use_natural_parameter=True)
        self.assertAlmostEqual(T_macro_nat, macro_T)

        T_local_nat = compute_local_temperature(q_history, use_natural_parameter=True)
        np.testing.assert_array_almost_equal(T_local_nat, local_T)

    def test_filter_wiring_use_natural_parameter(self):
        """Verify that macro and local thermodynamics filter orchestration functions respect use_natural_parameter=True"""
        from src.filters._001_1_1_filter_macro_thermodynamics import run_thermodynamics_analysis
        from src.filters._001_1_2_filter_local_thermodynamics import run_local_thermo_analysis

        T_slice = np.array([[0.0, 10.0], [0.0, 0.0]])
        X_hist = [np.array([10.0, -5.0]), np.array([12.0, -4.0])]
        v_hist = [np.array([5.0, -5.0]), np.array([6.0, -6.0])]
        X_init = np.array([5.0, 0.0])

        rec_default, _, _ = run_thermodynamics_analysis(0, T_slice, v_hist, X_hist, X_init, [], [], use_natural_parameter=False)
        rec_nat, _, _ = run_thermodynamics_analysis(0, T_slice, v_hist, X_hist, X_init, [], [], use_natural_parameter=True)
        
        # Temperature (index 3 in record) should differ when using natural parameter
        self.assertNotEqual(rec_default[0][3], rec_nat[0][3])

        rec_local_default, _, _ = run_local_thermo_analysis(0, T_slice, v_hist, X_hist, X_init, use_natural_parameter=False)
        rec_local_nat, _, _ = run_local_thermo_analysis(0, T_slice, v_hist, X_hist, X_init, use_natural_parameter=True)

        # Local temperature (index 4 in node 0 record) should differ
        self.assertNotEqual(rec_local_default[0][4], rec_local_nat[0][4])


if __name__ == '__main__':
    unittest.main()
