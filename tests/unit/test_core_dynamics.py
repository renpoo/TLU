#!/usr/bin/env python3
# test_core_dynamics.py
import unittest
import numpy as np

# Import the pure math functions to be implemented
from src.core.core_dynamics import compute_optimal_time_lag, estimate_virtual_mass_and_viscosity, compute_external_force_residual

class TestCoreDynamics(unittest.TestCase):
    
    def test_compute_optimal_time_lag_simple_shift(self):
        """
        [Red] Test when there is a clear 2-step time delay (lag)
        between investment (signal_A) and effect manifestation (signal_B).
        """
        # Signal A with large activity (10.0) only at time t=0
        signal_A = np.array([10.0, 0.0, 0.0, 0.0, 0.0])
        
        # Signal B with large reaction (10.0) only at time t=2 (2 steps behind A)
        signal_B = np.array([0.0, 0.0, 10.0, 0.0, 0.0])
        
        max_lag = 3

        # Act
        lag, max_corr = compute_optimal_time_lag(signal_A, signal_B, max_lag)

        # Assert
        # Since B is "2 steps" delayed with respect to A, the optimal lag should be 2
        self.assertEqual(lag, 2)
        # Since the shapes match perfectly, the correlation coefficient should be close to 1.0
        self.assertGreater(max_corr, 0.9)

    def test_virtual_estimate_mass_and_viscosity_relative(self):
        """
        [Red] Test to estimate relative behavior of node mass (M) and viscosity (C).
        Verify that Viscosity scales proportionally with Mass (Rayleigh damping).
        """
        # Node 0 (Left col): Large mass
        # Node 1 (Right col): Small mass
        X_history = np.array([
            [100.0, 10.0],
            [120.0, 10.0],
            [90.0,  10.0]
        ])

        # Act
        M, C = estimate_virtual_mass_and_viscosity(X_history, damping_ratio=0.1)

        # Assert
        # 1. Mass M: Node 0 with larger absolute balance should have larger mass
        self.assertGreater(M[0], M[1])
        
        # 2. Viscosity C: Since C = M * damping_ratio, Node 0 should have proportionally larger viscosity
        self.assertGreater(C[0], C[1])
        self.assertAlmostEqual(C[0], M[0] * 0.1)
        self.assertAlmostEqual(C[1], M[1] * 0.1)
    
    def test_compute_external_force_residual(self):
        """
        [Red] Test to reverse-calculate anomalous external shock (F_external)
        from the observed state of the system (M, C, K, a, v, dq).
        """
        
        # Test with a single node (array of length 1) to lower cognitive load
        # Virtual mass M = 10.0, Viscosity C = 2.0, Stiffness (spring const) K = 5.0
        M = np.array([10.0])
        C = np.array([2.0])
        K = np.array([5.0])
        
        # Observed current state
        # Acceleration a = 1.0, Velocity v = 3.0, Displacement dq = 2.0
        a = np.array([1.0])
        v = np.array([3.0])
        dq = np.array([2.0])
        
        # Act
        F_ext = compute_external_force_residual(M, C, K, a, v, dq)
        
        # Assert
        # F_ext = Ma + Cv + K*dq
        # F_ext = (10.0 * 1.0) + (2.0 * 3.0) + (5.0 * 2.0)
        #       = 10.0 + 6.0 + 10.0 = 26.0
        self.assertEqual(F_ext[0], 26.0)

if __name__ == '__main__':
    unittest.main()
