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
        X_history = []
        v_history = []
        t_idx = 0
        X_initial = np.array([0.0, 0.0])

        records, X_current, v_current = run_dynamics_state_analysis(
            t_idx, T_slice, X_history, v_history, X_initial
        )

        self.assertEqual(len(records), N)
        self.assertEqual(X_current.shape, (2,))
        self.assertEqual(v_current.shape, (2,))

        # Record structure: [t_idx, node_idx, net_flux_q, v, a, M, C, F_ext]
        node0_record = records[0]
        self.assertEqual(len(node0_record), 10) # Verify elements have increased to 10 (including jerk, snap)
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
        X_initial = np.array([0.0, 0.0])
        records, X_current, v_current = run_dynamics_state_analysis(
            t_idx, T_slice, [], [], X_initial
        )
        self.assertEqual(len(records), N)
        self.assertEqual(X_current.shape, (2,)) 
        self.assertEqual(v_current.shape, (2,))
        node1_record = records[1]
        self.assertEqual(len(node1_record), 10)
        self.assertEqual(node1_record[0], 0)

    def test_run_dynamics_state_analysis_jerk_snap(self):
        """Verify that jerk and snap are calculated correctly over multiple timesteps."""
        N = 2
        # Set up a historical flux sequence for node 0: v = [2.0, 5.0, 9.0, 14.0]
        # v(t) = 14.0, v(t-1) = 9.0, v(t-2) = 5.0, v(t-3) = 2.0
        # a(t) = 14.0 - 9.0 = 5.0, a(t-1) = 9.0 - 5.0 = 4.0
        # j(t) = a(t) - a(t-1) = 5.0 - 4.0 = 1.0 (jerk)
        # s(t) = j(t) - j(t-1) -> need j(t-1) -> j(t-1) = a(t-1) - a(t-2) = 4.0 - (5.0 - 2.0) = 4.0 - 3.0 = 1.0
        # s(t) = 1.0 - 1.0 = 0.0 (snap)
        
        X_history = [np.array([2.0, 0.0]), np.array([7.0, 0.0]), np.array([16.0, 0.0])]
        v_history = [np.array([2.0, 0.0]), np.array([5.0, 0.0]), np.array([9.0, 0.0])]
        X_initial = np.array([0.0, 0.0])
        
        # Current timestep flux: node 1 sends 14.0 to node 0 (net flux for node 0 is +14.0)
        T_slice = np.array([
            [0.0, 0.0],
            [14.0, 0.0]
        ])
        t_idx = 3
        
        records, X_current, v_current = run_dynamics_state_analysis(
            t_idx, T_slice, X_history, v_history, X_initial
        )
        
        # Record output columns: [t_idx, node_idx, X, v, a, j, s, M, C, F_ext]
        # jerk should be index 5, snap index 6
        rec = records[0]
        self.assertEqual(len(rec), 10)
        
        jerk_val = float(rec[5])
        snap_val = float(rec[6])
        
        self.assertAlmostEqual(jerk_val, 1.0, places=4)
        self.assertAlmostEqual(snap_val, 0.0, places=4)

if __name__ == '__main__':
    unittest.main()

