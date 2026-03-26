#!/usr/bin/env python3
# test_1_11_filter_info_curvature.py
import unittest
import numpy as np
from src.filters._1_11_filter_info_curvature import run_info_curvature_analysis

class TestFilterInfoCurvature(unittest.TestCase):
    def test_run_info_curvature_analysis_logic(self):
        """
        [Red->Green] 1タイムスライスを渡したとき、I/Oに依存せずに
        各ノードの曲率(Curvature)と密度(Density)が計算されることを確認。
        """
        N = 3
        t_idx = 3
        T_slice = np.array([
            [0.0, 10.0, 5.0],
            [0.0,  0.0, 0.0],
            [2.0,  0.0, 0.0]
        ])
        
        # 過去2ステップ分の履歴 (最新の T_slice 分と合わせて3ステップになる)
        q_history = [
            np.array([10.0, 5.0, 2.0]),   # t=1
            np.array([12.0, 8.0, 5.0])    # t=2
        ]

        # 実行
        records, q_current = run_info_curvature_analysis(t_idx, T_slice, q_history)

        # 検証
        self.assertEqual(len(records), N)
        self.assertEqual(q_current.shape, (N,))

        # レコード構造: [t_idx, node_idx, curvature, density]
        rec0 = records[0]
        self.assertEqual(rec0[0], t_idx)
        self.assertEqual(rec0[1], 0)
        
        # 値が文字列としてフォーマットされているか
        self.assertTrue(isinstance(rec0[2], str)) # curvature
        self.assertTrue(isinstance(rec0[3], str)) # density

        # 渡したリストが変異（mutate）していないことの証明
        self.assertEqual(len(q_history), 2)

if __name__ == '__main__':
    unittest.main()
