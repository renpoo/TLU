#!/usr/bin/env python3
# test_1_9_filter_micro_forensics.py
import unittest
import numpy as np
from src.filters._1_9_filter_micro_forensics import run_micro_forensics_analysis

class TestFilterMicroForensics(unittest.TestCase):
    def test_run_micro_forensics_analysis_shape(self):
        """
        [Red->Green] N=2のT_sliceを渡したとき、
        副作用なしに2行(N行)のミクロ指標レコードが返ることを確認。
        """
        N = 2
        T_slice = np.array([
            [0.0, 10.0],
            [0.0,  0.0]
        ])
        t_idx = 0
        
        # 履歴のモック（直近の2ステップ分をリストとして渡す）
        q_history = [np.array([-5.0, 5.0]), np.array([-8.0, 8.0])]
        P_history = [np.array([[0.0, 1.0], [0.0, 0.0]]), np.array([[0.0, 1.0], [0.0, 0.0]])]
        
        thresholds = {
            'kl_drift_thresh': 3.0,
            'z_score_thresh': 3.0
        }

        # 実行
        records, q_current, P_current = run_micro_forensics_analysis(
            t_idx, T_slice, q_history, P_history, thresholds
        )

        # 検証: N行のレコード
        self.assertEqual(len(records), N)
        self.assertEqual(q_current.shape, (N,))
        self.assertEqual(P_current.shape, (N, N))
        
        # レコード構造: [t_idx, node_idx, node_kl_drift, node_univariate_z_score, micro_anomaly_flag]
        node0_rec = records[0]
        self.assertEqual(len(node0_rec), 5) 
        self.assertEqual(node0_rec[0], 0) # t_idx
        self.assertEqual(node0_rec[1], 0) # node_idx

        node1_rec = records[1]
        self.assertEqual(node1_rec[1], 1) # node_idx が連番になっていること

        # 渡したリストが変異（mutate）していないことの証明
        self.assertEqual(len(q_history), 2)
        self.assertEqual(len(P_history), 2)

if __name__ == '__main__':
    unittest.main()
