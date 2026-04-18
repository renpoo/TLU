#!/usr/bin/env python3
# test_002_2_2_filter_micro_forensics.py
import unittest
import numpy as np
from src.filters._002_2_2_filter_micro_forensics import run_micro_forensics_analysis

class TestFilterMicroForensics(unittest.TestCase):
    def test_run_micro_forensics_analysis_shape(self):
        """
        [Red->Green] When T_slice with N=2 is passed,
        verification that 2 rows (N rows) of micro indicator records are returned without side effects.
        """
        N = 2
        T_slice = np.array([
            [0.0, 10.0],
            [0.0,  0.0]
        ])
        t_idx = 0
        
        # History mock (pass the latest 2 steps as a list)
        q_history = [np.array([-5.0, 5.0]), np.array([-8.0, 8.0])]
        P_history = [np.array([[0.0, 1.0], [0.0, 0.0]]), np.array([[0.0, 1.0], [0.0, 0.0]])]
        
        thresholds = {
            'kl_drift_thresh': 3.0,
            'z_score_thresh': 3.0
        }

        # Act
        records, q_current, P_current = run_micro_forensics_analysis(
            t_idx, T_slice, q_history, P_history, thresholds
        )

        # Assert: N rows of records
        self.assertEqual(len(records), N)
        self.assertEqual(q_current.shape, (N,))
        self.assertEqual(P_current.shape, (N, N))
        
        # Record structure: [t_idx, node_idx, node_kl_drift, node_univariate_z_score, micro_anomaly_flag]
        node0_rec = records[0]
        self.assertEqual(len(node0_rec), 5) 
        self.assertEqual(node0_rec[0], 0) # t_idx
        self.assertEqual(node0_rec[1], 0) # node_idx

        node1_rec = records[1]
        self.assertEqual(node1_rec[1], 1) # node_idx is sequential

        # Proof that the passed list did not mutate
        self.assertEqual(len(q_history), 2)
        self.assertEqual(len(P_history), 2)

    def test_micro_forensics_extreme_thresholds(self):
        """[Red->Green] Verify bounds constraints evaluate anomalies safely against absolute extreme float values"""
        N = 2
        T_slice = np.array([
            [0.0, 1000.0],
            [0.0, 0.0]
        ])
        t_idx = 0
        q_history = [np.array([5.0, -5.0]), np.array([10.0, -10.0])]
        P_history = [np.array([[0.0, 1.0], [0.0, 0.0]]), np.array([[0.0, 1.0], [0.0, 0.0]])]
        
        # Test with practically unreachable thresholds
        thresholds = {
            'kl_drift_thresh': 1e9,
            'z_score_thresh': 1e9
        }
        
        records, _, _ = run_micro_forensics_analysis(
            t_idx, T_slice, q_history, P_history, thresholds
        )
        
        # Anomaly flag should be strictly 0 despite massive inputs
        for rec in records:
            self.assertEqual(rec[4], 0)

if __name__ == '__main__':
    unittest.main()
