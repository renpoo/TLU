#!/usr/bin/env python3
# test_1_8_filter_forensics.py
import unittest
import numpy as np
from src.filters._1_8_filter_macro_forensics import run_forensics_analysis

class TestFilterForensics(unittest.TestCase):
    def test_run_forensics_analysis_basic(self):
        """
        [Red->Green] 1タイムスライスを渡したとき、I/Oに依存せずに
        システム全体のマクロ異常検知指標が計算されることを確認。
        """
        T_slice = np.array([
            [0.0, 10.0],
            [0.0,  0.0]
        ])
        t_idx = 0
        
        q_history = [np.array([-5.0, 5.0]), np.array([-8.0, 8.0])]
        P_history = [np.array([[0.0, 1.0], [0.0, 0.0]]), np.array([[0.0, 1.0], [0.0, 0.0]])]
        
        thresholds = {
            'leak_tolerance': 1e-5,
            'kl_drift_thresh': 3.0,
            'z_score_thresh': 3.0
        }

        records, q_current, P_current = run_forensics_analysis(
            t_idx, T_slice, q_history, P_history, thresholds
        )

        # 全体で1行のレコードが返る
        self.assertEqual(len(records), 1)
        
        # レコード構造: [t_idx, conservation_residual, kl_divergence_drift, mahalanobis_z_score, anomaly_flag]
        sys_rec = records[0]
        self.assertEqual(len(sys_rec), 5) 
        self.assertEqual(sys_rec[0], 0)
        self.assertTrue(isinstance(sys_rec[1], str))
        self.assertTrue(isinstance(sys_rec[2], str))
        self.assertTrue(isinstance(sys_rec[3], str))
        self.assertIn(sys_rec[4], [0, 1])

if __name__ == '__main__':
    unittest.main()
