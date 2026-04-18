#!/usr/bin/env python3
# test_000_1_1_filter_dynamics_state.py
import unittest
import numpy as np
from src.filters._000_1_1_filter_dynamics_state import run_dynamics_state_analysis

class TestFilterDynamicsState(unittest.TestCase):
    def test_run_dynamics_state_analysis_basic(self):
        """[Red->Green] Verify that the dynamic parameters of 1 step are returned from the pure function"""
        N = 2
        T_slice = np.array([
            [0.0, 10.0],
            [0.0,  0.0]
        ])
        q_history = []
        v_history = []
        t_idx = 0

        records, q_current, v_current = run_dynamics_state_analysis(
            t_idx, T_slice, q_history, v_history
        )

        self.assertEqual(len(records), N)
        self.assertEqual(q_current.shape, (2,))
        self.assertEqual(v_current.shape, (2,))

        # Record structure: [t_idx, node_idx, net_flux_q, v, a, M, C, F_ext]
        node0_record = records[0]
        self.assertEqual(len(node0_record), 8) # Verify that the number of elements has become 8
        self.assertEqual(node0_record[0], 0)
        self.assertEqual(node0_record[1], 0)
        
        # Verify that it is a formatted string (q, v, a...)
        self.assertTrue(isinstance(node0_record[2], str))
        self.assertTrue(isinstance(node0_record[3], str))

    def test_run_dynamics_state_analysis_empty_history(self):
        """[Red->Green] Verify safe boundary constraints mapping zero initialized histories safely"""
        N = 2
        T_slice = np.array([
            [0.0, 5.0],
            [0.0, 0.0]
        ])
        t_idx = 0
        records, q_current, v_current = run_dynamics_state_analysis(
            t_idx, T_slice, [], []
        )
        self.assertEqual(len(records), N)
        self.assertEqual(q_current.shape, (2,)) 
        self.assertEqual(v_current.shape, (2,))
        node1_record = records[1]
        self.assertEqual(len(node1_record), 8)
        self.assertEqual(node1_record[0], 0)

if __name__ == '__main__':
    unittest.main()
