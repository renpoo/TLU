#!/usr/bin/env python3
# test_1_10_filter_lag_matrix.py
import unittest
import numpy as np
from src.filters._1_10_filter_lag_matrix import run_lag_matrix_analysis

class TestFilterLagMatrix(unittest.TestCase):
    def test_run_lag_matrix_analysis_basic(self):
        """
        [Red->Green] 蓄積された履歴を渡したとき、I/Oに依存せずに
        N x N 全ペアのタイムラグと相関係数が計算されることを確認。
        """
        # 準備 (Arrange)
        q_history_list = [
            np.array([10.0,  0.0]), # t=0
            np.array([ 0.0, 10.0]), # t=1
            np.array([ 0.0,  0.0]), # t=2
            np.array([ 0.0,  0.0])  # t=3
        ]
        max_lag = 2

        # 実行 (Act)
        records = run_lag_matrix_analysis(q_history_list, max_lag)

        # 検証 (Assert)
        self.assertEqual(len(records), 4)

        # レコード構造: [src_idx, tgt_idx, optimal_lag, max_correlation]
        # Node 0 から Node 1 への波及関係をテスト
        record_0_to_1 = next(r for r in records if r[0] == 0 and r[1] == 1)
        
        self.assertEqual(len(record_0_to_1), 4)
        self.assertEqual(record_0_to_1[2], 1) # 1ステップ遅れている
        self.assertTrue(isinstance(record_0_to_1[3], str))
        self.assertIn("1.0", record_0_to_1[3])

if __name__ == '__main__':
    unittest.main()
