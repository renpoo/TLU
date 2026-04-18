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
        Define expected physical properties (magnitude relationship) before implementing specific formulas.
        """

        # History data for 3 time points and 2 nodes
        # Node 0 (Left col): Large activity scale, wildly fluctuating velocity (Large mass, small viscosity)
        # Node 1 (Right col): Small activity scale, velocity not changing at all (Small mass, large viscosity)
        q_history = np.array([
            [100.0, 10.0],
            [120.0, 10.0],
            [90.0,  10.0]
        ])
        v_history = np.array([
            [20.0, 0.0],
            [20.0, 0.0],
            [-30.0, 0.0]
        ])

        # Act
        M, C = estimate_virtual_mass_and_viscosity(q_history, v_history, base_epsilon=1e-10, velocity_scale_ratio=0.1)

        # Assert
        # 1. Mass M: Node 0 with larger activity scale should be larger than Node 1
        self.assertGreater(M[0], M[1])
        
        # 2. Viscosity C: Node 1 completely fixed by friction should be larger than freely moving Node 0
        self.assertGreater(C[1], C[0])
    
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
