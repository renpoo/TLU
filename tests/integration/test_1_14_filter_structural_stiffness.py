#!/usr/bin/env python3
# test_1_14_filter_structural_stiffness.py
import unittest
import numpy as np
from src.filters._1_14_filter_structural_stiffness import run_structural_stiffness_analysis

class TestFilterStructuralStiffness(unittest.TestCase):
    def setUp(self):
        self.N = 3
        # ノード間の移動スライス
        self.T_slice = np.array([
            [0.0, 10.0, 0.0],
            [0.0,  0.0, 5.0],
            [0.0,  0.0, 0.0]
        ])
        self.t_idx = 1
        # K_safeを計算できるよう、最低3件の履歴をモック（差分をとるため）
        self.q_history = [
            np.array([-5.0, 5.0, 0.0]),
            np.array([-8.0, 3.0, 5.0]),
            np.array([-10.0, 5.0, 5.0])
        ]

    def test_run_structural_stiffness_analysis(self):
        """[Red->Green] 剛性行列 (K) が N x N のレコードとして出力されることを確認"""
        
        records, q_current = run_structural_stiffness_analysis(
            t_idx=self.t_idx,
            T_slice=self.T_slice,
            q_history=self.q_history
        )

        # 1タイムステップにつき N * N = 9 行のレコードが返ること
        self.assertEqual(len(records), self.N * self.N)
        
        # 現在の純フラックスが返されていること
        self.assertEqual(q_current.shape, (self.N,))
        
        # レコードの構造チェック: [t_idx, src_idx, tgt_idx, stiffness_k]
        first_record = records[0]
        self.assertEqual(len(first_record), 5)
        self.assertEqual(first_record[0], self.t_idx)
        self.assertEqual(first_record[1], 0) # src_idx
        self.assertEqual(first_record[2], 0) # tgt_idx
        
        # stiffness は文字列としてフォーマットされていること
        self.assertTrue(isinstance(first_record[3], str))

    def test_run_structural_stiffness_short_history(self):
        """履歴が不足している場合、ゼロ行列として安全にフォールバックすること"""
        records, _ = run_structural_stiffness_analysis(
            t_idx=self.t_idx,
            T_slice=self.T_slice,
            q_history=[] # 履歴なし
        )
        
        # すべての剛性が 0.000000 になるはず
        for rec in records:
            self.assertEqual(float(rec[3]), 0.0)

if __name__ == '__main__':
    unittest.main()
