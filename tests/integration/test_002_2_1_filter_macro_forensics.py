#!/usr/bin/env python3
# test_002_2_1_filter_macro_forensics.py
import unittest
import numpy as np
from src.filters._002_2_1_filter_macro_forensics import run_forensics_analysis

class TestFilterForensics(unittest.TestCase):
    def test_run_forensics_analysis_basic(self):
        """
        [Red->Green] When 1 time slice is passed, without depending on I/O,
        verification that macroeconomic anomaly detection indicators for the entire system are calculated.
        """
        T_slice = np.array([
            [0.0, 10.0],
            [0.0,  0.0]
        ])
        t_idx = 0
        
        v_history = [np.array([-5.0, 5.0]), np.array([-8.0, 8.0])]
        X_history = [np.array([100.0, 100.0]), np.array([92.0, 108.0])]
        P_history = [np.array([[0.0, 1.0], [0.0, 0.0]]), np.array([[0.0, 1.0], [0.0, 0.0]])]
        X_initial = np.array([105.0, 95.0])
        
        thresholds = {
            'leak_tolerance': 1e-5,
            'kl_drift_thresh': 3.0,
            'z_score_thresh': 3.0
        }

        records, v_current, X_current, P_current = run_forensics_analysis(
            t_idx, T_slice, v_history, X_history, P_history, X_initial, thresholds
        )

        # Returns 1 row of record in total
        self.assertEqual(len(records), 1)
        
        # Record structure: [t_idx, conservation_residual, kl_divergence_drift, z_score_X, z_score_v, anomaly_flag]
        sys_rec = records[0]
        self.assertEqual(len(sys_rec), 6) 
        self.assertEqual(sys_rec[0], 0)
        self.assertTrue(isinstance(sys_rec[1], str))
        self.assertTrue(isinstance(sys_rec[2], str))
        self.assertTrue(isinstance(sys_rec[3], str))
        self.assertTrue(isinstance(sys_rec[4], str))
        self.assertIn(sys_rec[5], [0, 1])

if __name__ == '__main__':
    unittest.main()
