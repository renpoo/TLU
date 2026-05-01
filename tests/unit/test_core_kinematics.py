#!/usr/bin/env python3
# test_core_kinematics.py
import unittest
import numpy as np
from src.core.core_kinematics import compute_derivatives

class TestKinematics(unittest.TestCase):
    def test_compute_derivatives_basic(self):
        """
        Test to calculate the latest velocity (v) and acceleration (a) from the time-series history of the state vector (q).
        """
        # v_history: Velocity vectors arranged in chronological order (Time_steps x Nodes)
        # Assuming 3 steps (T=3) and 2 nodes (N=2)
        v_history = np.array([
            [10.0, 100.0],  # t=0
            [15.0,  90.0],  # t=1
            [18.0,  80.0]   # t=2 (latest)
        ])
        
        # Expected velocity vector v (latest flux)
        expected_v = np.array([18.0, 80.0])
        
        # Expected acceleration vector a (Latest 1st order difference of v: v[t] - v[t-1])
        # Node 0: 18 - 15 = 3.0
        # Node 1: 80 - 90 = -10.0
        expected_a = np.array([3.0, -10.0])
        
        actual_v, actual_a = compute_derivatives(v_history)
        
        np.testing.assert_array_almost_equal(actual_v, expected_v)
        np.testing.assert_array_almost_equal(actual_a, expected_a)

    def test_compute_derivatives_insufficient_history(self):
        """
        Test when history is insufficient and velocity or acceleration cannot be calculated.
        Safely return a zero vector.
        """
        # T=1 (Latest only)
        v_history_short = np.array([[10.0, 100.0]])
        
        actual_v, actual_a = compute_derivatives(v_history_short)
        
        # Safe design to return latest velocity, but zero acceleration
        expected_v = np.array([10.0, 100.0])
        expected_a = np.array([0.0, 0.0])
        np.testing.assert_array_almost_equal(actual_v, expected_v)
        np.testing.assert_array_almost_equal(actual_a, expected_a)

if __name__ == '__main__':
    unittest.main()
