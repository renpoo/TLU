#!/usr/bin/env python3
# test_1_6_filter_local_thermo.py
import unittest
import numpy as np
from src.filters._001_1_2_filter_local_thermodynamics import run_local_thermo_analysis

class TestFilterLocalThermo(unittest.TestCase):
    def test_run_local_thermo_analysis_basic(self):
        """
        [Red->Green] Verify that the pure mathematical logic layer correctly calculates and returns
        the local thermodynamic indicators (u_i, s_i, t_i) without internally mutating the history.
        """
        N = 2
        # Transfer of 10.0 from Node 0 to Node 1
        T_slice = np.array([
            [0.0, 10.0],
            [0.0,  0.0]
        ])
        q_history = []
        t_idx = 0

        # Act
        records, q_current = run_local_thermo_analysis(
            t_idx, T_slice, q_history
        )

        # Assert
        self.assertEqual(len(records), N)
        self.assertEqual(q_current.shape, (2,))
        
        # Record structure: [t_idx, node_idx, u_i, s_i, t_i]
        node0_rec = records[0]
        self.assertEqual(len(node0_rec), 5)
        self.assertEqual(node0_rec[0], 0)
        self.assertEqual(node0_rec[1], 0)
        self.assertTrue(isinstance(node0_rec[2], str))

        # Proof that the passed list did not mutate
        self.assertEqual(len(q_history), 0)

    def test_local_thermo_isolated_node(self):
        """[Red->Green] Test metrics evaluation safely returning limits mapping totally isolated topologies without NaN exceptions"""
        N = 3
        # Node 2 is absolutely disconnected
        T_slice = np.array([
            [0.0, 10.0, 0.0],
            [0.0,  0.0, 0.0],
            [0.0,  0.0, 0.0]
        ])
        t_idx = 0
        records, q_current = run_local_thermo_analysis(t_idx, T_slice, [])
        self.assertEqual(len(records), N)
        node2_rec = records[2]
        self.assertEqual(node2_rec[1], 2)
        # Should gracefully return float representations without NaN
        self.assertFalse('nan' in node2_rec[2].lower())
        self.assertFalse('nan' in node2_rec[3].lower())

if __name__ == '__main__':
    unittest.main()
