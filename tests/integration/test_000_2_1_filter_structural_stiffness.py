#!/usr/bin/env python3
# test_1_14_filter_structural_stiffness.py
import unittest
import numpy as np
from src.filters._000_2_1_filter_structural_stiffness import run_structural_stiffness_analysis

class TestFilterStructuralStiffness(unittest.TestCase):
    def setUp(self):
        self.N = 3
        # Movement slice between nodes
        self.T_slice = np.array([
            [0.0, 10.0, 0.0],
            [0.0,  0.0, 5.0],
            [0.0,  0.0, 0.0]
        ])
        self.t_idx = 1
        # Mock at least 3 history records to allow calculation of K_safe (to take the difference)
        self.q_history = [
            np.array([-5.0, 5.0, 0.0]),
            np.array([-8.0, 3.0, 5.0]),
            np.array([-10.0, 5.0, 5.0])
        ]

    def test_run_structural_stiffness_analysis(self):
        """[Red->Green] Verify that the stiffness matrix (K) is output as an N x N record"""
        
        records, q_current = run_structural_stiffness_analysis(
            t_idx=self.t_idx,
            T_slice=self.T_slice,
            q_history=self.q_history
        )

        # N * N = 9 rows of records are returned per time step
        self.assertEqual(len(records), self.N * self.N)
        
        # The current net flux is returned
        self.assertEqual(q_current.shape, (self.N,))
        
        # Record structure check: [t_idx, src_idx, tgt_idx, stiffness_k]
        first_record = records[0]
        self.assertEqual(len(first_record), 5)
        self.assertEqual(first_record[0], self.t_idx)
        self.assertEqual(first_record[1], 0) # src_idx
        self.assertEqual(first_record[2], 0) # tgt_idx
        
        # stiffness should be formatted as a string
        self.assertTrue(isinstance(first_record[3], str))

    def test_run_structural_stiffness_short_history(self):
        """If history is insufficient, safely fallback as a zero matrix"""
        records, _ = run_structural_stiffness_analysis(
            t_idx=self.t_idx,
            T_slice=self.T_slice,
            q_history=[] # No history
        )
        
        # All stiffness should be 0.000000
        for rec in records:
            self.assertEqual(float(rec[3]), 0.0)

if __name__ == '__main__':
    unittest.main()
