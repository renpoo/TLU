#!/usr/bin/env python3
# test_1_4_filter_time_lag.py
import unittest
import numpy as np
from src.filters._1_4_filter_time_lag import run_time_lag_analysis

class TestFilterTimeLag(unittest.TestCase):
    def test_run_time_lag_analysis_basic(self):
        """[Red->Green] 全履歴を用いたタイムラグ解析が一括処理されることを確認"""
        # Node 0の活動が、2ステップ遅れてNode 1に波及している履歴
        q_history = np.array([
            [10.0, 0.0],
            [0.0,  0.0],
            [0.0, 10.0],
            [0.0,  0.0]
        ])
        target_pairs = [(0, 1)]
        max_lag = 3

        records = run_time_lag_analysis(q_history, target_pairs, max_lag)

        self.assertEqual(len(records), 1)
        
        # レコード構造: [node_a_idx, node_b_idx, optimal_lag, correlation]
        result = records[0]
        self.assertEqual(result[0], 0)
        self.assertEqual(result[1], 1)
        self.assertEqual(result[2], 2) # 最適ラグは2ステップであるはず
        
        # 相関が算出されていること
        self.assertTrue(isinstance(result[3], str))

if __name__ == '__main__':
    unittest.main()
