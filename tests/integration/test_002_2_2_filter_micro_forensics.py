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
        v_history = [np.array([-5.0, 5.0]), np.array([-8.0, 8.0])]
        X_history = [np.array([100.0, 100.0]), np.array([92.0, 108.0])]
        P_history = [np.array([[0.0, 1.0], [0.0, 0.0]]), np.array([[0.0, 1.0], [0.0, 0.0]])]
        X_initial = np.array([105.0, 95.0])
        g_history = [np.array([-0.05, 0.05]), np.array([-0.08, 0.08])]
        
        thresholds = {
            'kl_drift_thresh': 3.0,
            'z_score_thresh': 3.0
        }

        # Act
        records, v_current, X_current, g_current, P_current = run_micro_forensics_analysis(
            t_idx, T_slice, v_history, X_history, g_history, P_history, X_initial, thresholds
        )

        # Assert: N rows of records
        self.assertEqual(len(records), N)
        self.assertEqual(v_current.shape, (N,))
        self.assertEqual(X_current.shape, (N,))
        self.assertEqual(P_current.shape, (N, N))
        
        # Record structure: [t_idx, node_idx, z_score_X, z_score_v, node_kl_drift, micro_anomaly_flag]
        node0_rec = records[0]
        self.assertEqual(len(node0_rec), 6) 
        self.assertEqual(node0_rec[0], 0) # t_idx
        self.assertEqual(node0_rec[1], 0) # node_idx

        node1_rec = records[1]
        self.assertEqual(node1_rec[1], 1) # node_idx is sequential

        # Proof that the passed list did not mutate
        self.assertEqual(len(v_history), 2)
        self.assertEqual(len(X_history), 2)
        self.assertEqual(len(P_history), 2)

    def test_micro_forensics_extreme_thresholds(self):
        """[Red->Green] Verify bounds constraints evaluate anomalies safely against absolute extreme float values"""
        N = 2
        T_slice = np.array([
            [0.0, 1000.0],
            [0.0, 0.0]
        ])
        t_idx = 0
        v_history = [np.array([5.0, -5.0]), np.array([10.0, -10.0])]
        X_history = [np.array([100.0, 100.0]), np.array([110.0, 90.0])]
        P_history = [np.array([[0.0, 1.0], [0.0, 0.0]]), np.array([[0.0, 1.0], [0.0, 0.0]])]
        X_initial = np.array([95.0, 105.0])
        
        g_history = [np.array([-0.05, 0.05]), np.array([-0.08, 0.08])]
        
        # Test with practically unreachable thresholds
        thresholds = {
            'kl_drift_thresh': 1e9,
            'z_score_thresh': 1e9
        }
        
        records, _, _, _, _ = run_micro_forensics_analysis(
            t_idx, T_slice, v_history, X_history, g_history, P_history, X_initial, thresholds
        )
        
        # Anomaly flag should be strictly 0 despite massive inputs
        for rec in records:
            self.assertEqual(rec[5], 0)

    def test_evaluate_micro_anomaly_flags_fail_fast(self):
        """Verify that evaluate_micro_anomaly_flags raises KeyError when required thresholds are missing"""
        from src.filters._002_2_2_filter_micro_forensics import evaluate_micro_anomaly_flags

        kl_vec = np.array([0.5, 1.2])
        z_g_vec = np.array([0.1, 0.2])
        z_v_vec = np.array([0.1, 0.2])

        # Missing 'kl_drift_thresh'
        with self.assertRaises(KeyError):
            evaluate_micro_anomaly_flags(kl_vec, z_g_vec, z_v_vec, {'z_score_thresh': 3.0})

        # Missing 'z_score_thresh'
        with self.assertRaises(KeyError):
            evaluate_micro_anomaly_flags(kl_vec, z_g_vec, z_v_vec, {'kl_drift_thresh': 3.0})

if __name__ == '__main__':
    unittest.main()
