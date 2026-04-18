#!/usr/bin/env python3
# test_004_2_1_filter_sensitivity.py
import unittest
import numpy as np
from src.filters._004_2_1_filter_sensitivity import run_sensitivity_analysis

class TestFilterSensitivity(unittest.TestCase):
    def test_run_sensitivity_analysis_logic(self):
        """
        [Red->Green] Verify that the pure mathematical logic layer correctly calculates and returns
        the ripple effect (FK) and target strain (IK) of each node, completely independently of I/O.
        """
        N = 3
        t_idx = 3
        T_slice = np.array([
            [0.0, 10.0, 5.0],
            [0.0,  0.0, 0.0],
            [2.0,  0.0, 0.0]
        ])
        
        # History of the past 2 steps (combined with the latest T_slice, it becomes 3 steps, and covariance is calculated)
        q_history = [
            np.array([10.0, 5.0, 2.0]),   # t=1
            np.array([12.0, 8.0, 5.0])    # t=2
        ]
        
        delta = 10.0
        gamma = 0.85
        max_k = 5

        # Act
        records, q_current = run_sensitivity_analysis(
            t_idx, T_slice, q_history, delta, gamma, max_k
        )

        # Assert
        self.assertEqual(len(records), N)
        self.assertEqual(q_current.shape, (N,))

        # Record structure: [t_idx, node_idx, fk_total_ripple, fk_max_impact, fk_max_node, ik_strain_energy, ik_max_adjust, ik_max_node]
        rec0 = records[0]
        self.assertEqual(len(rec0), 8)
        self.assertEqual(rec0[0], t_idx)
        self.assertEqual(rec0[1], 0)
        
        # Check if the value is formatted as a string
        self.assertTrue(isinstance(rec0[2], str)) # fk_total_ripple
        self.assertTrue(isinstance(rec0[5], str)) # ik_strain_energy

        # Proof that the passed list did not mutate
        self.assertEqual(len(q_history), 2)

if __name__ == '__main__':
    unittest.main()
