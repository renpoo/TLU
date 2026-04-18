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
        # q_history: State vectors arranged in chronological order (Time_steps x Nodes)
        # Assuming 3 steps (T=3) and 2 nodes (N=2)
        # Node 0: [10, 15, 18] -> Speed is gradually decreasing
        # Node 1: [100, 90, 80] -> Decreasing at a constant speed
        q_history = np.array([
            [10.0, 100.0],  # t=0
            [15.0,  90.0],  # t=1
            [18.0,  80.0]   # t=2 (latest)
        ])
        
        # Expected velocity vector v (Latest 1st order difference: q[t] - q[t-1])
        # Node 0: 18 - 15 = 3.0
        # Node 1: 80 - 90 = -10.0
        expected_v = np.array([3.0, -10.0])
        
        # Expected acceleration vector a (Latest 2nd order difference: v[t] - v[t-1])
        # Calculate previous velocity v[t-1] -> Node 0: 15-10=5.0, Node 1: 90-100=-10.0
        # Acceleration a = Latest velocity - Previous velocity
        # Node 0: 3.0 - 5.0 = -2.0 (Decelerating)
        # Node 1: -10.0 - (-10.0) = 0.0 (Constant velocity motion)
        expected_a = np.array([-2.0, 0.0])
        
        actual_v, actual_a = compute_derivatives(q_history)
        
        np.testing.assert_array_almost_equal(actual_v, expected_v)
        np.testing.assert_array_almost_equal(actual_a, expected_a)

    def test_compute_derivatives_insufficient_history(self):
        """
        Test when history is insufficient and velocity or acceleration cannot be calculated.
        Safely return a zero vector.
        """
        # T=1 (Latest only)
        q_history_short = np.array([[10.0, 100.0]])
        
        actual_v, actual_a = compute_derivatives(q_history_short)
        
        # Safe design to return a zero vector if history is insufficient
        expected_zeros = np.array([0.0, 0.0])
        np.testing.assert_array_almost_equal(actual_v, expected_zeros)
        np.testing.assert_array_almost_equal(actual_a, expected_zeros)

if __name__ == '__main__':
    unittest.main()
