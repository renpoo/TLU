#!/usr/bin/env python3
# test_002_1_1_filter_info_curvature.py
import unittest
import numpy as np
from src.filters._002_1_1_filter_info_curvature import run_info_curvature_analysis

class TestFilterInfoCurvature(unittest.TestCase):
    def test_run_info_curvature_analysis_logic(self):
        """
        [Red->Green] When 1 time slice is passed, without depending on I/O,
        verification that the Curvature and Density of each node are calculated.
        """
        N = 3
        t_idx = 3
        T_slice = np.array([
            [0.0, 10.0, 5.0],
            [0.0,  0.0, 0.0],
            [2.0,  0.0, 0.0]
        ])
        
        # History of the past 2 steps (combined with the latest T_slice, it becomes 3 steps)
        q_history = [
            np.array([10.0, 5.0, 2.0]),   # t=1
            np.array([12.0, 8.0, 5.0])    # t=2
        ]

        # Act
        records, q_current = run_info_curvature_analysis(t_idx, T_slice, q_history)

        # Assert
        self.assertEqual(len(records), N)
        self.assertEqual(q_current.shape, (N,))

        # Record structure: [t_idx, node_idx, curvature, density]
        rec0 = records[0]
        self.assertEqual(rec0[0], t_idx)
        self.assertEqual(rec0[1], 0)
        
        # Check if the value is formatted as a string
        self.assertTrue(isinstance(rec0[2], str)) # curvature
        self.assertTrue(isinstance(rec0[3], str)) # density

        # Proof that the passed list did not mutate
        self.assertEqual(len(q_history), 2)

if __name__ == '__main__':
    unittest.main()
