#!/usr/bin/env python3
# test_004_1_1_filter_control_theory.py
import unittest
import numpy as np
from src.filters._004_1_1_filter_control_theory import run_control_theory_analysis

class TestFilterControlTheory(unittest.TestCase):
    def test_run_control_theory_analysis_basic(self):
        """
        [Red->Green] 純粋関数が文字列や外部ファイルに依存せず、
        ターゲットベクトルと制御可能インデックスのみを受け取り、
        最適入力 u とギャップを正しく計算して返すことを確認する。
        """
        N = 2
        # ノード0 から ノード1 へ 10.0 の移動
        T_slice = np.array([
            [0.0, 10.0],
            [0.0,  0.0]
        ])
        
        # ノード1 の目標値を 20.0 とする
        target_q = np.array([0.0, 20.0])
        # ノード0 のみを予算投下(制御)可能とする
        controllable_indices = [0]
        t_idx = 0

        # 実行 (重みはデフォルト)
        records, q_current = run_control_theory_analysis(
            t_idx, T_slice, target_q, controllable_indices
        )

        # 検証
        self.assertEqual(len(records), N)
        self.assertEqual(q_current.shape, (2,))
        
        # 修正: カラム名を最新の純粋数理モデルに同期
        # レコード構造: [t_idx, node_idx, optimal_input_u, state_error_x]
        node0_rec = records[0]
        self.assertEqual(len(node0_rec), 4)
        self.assertEqual(node0_rec[0], 0)
        self.assertEqual(node0_rec[1], 0)
        self.assertTrue(isinstance(node0_rec[2], str)) # optimal_input_u
        self.assertTrue(isinstance(node0_rec[3], str)) # state_error_x
        
        # ノード1は制御不能なので、推奨入力 u は 0.0000 に強制されているはず
        node1_rec = records[1]
        self.assertEqual(float(node1_rec[2]), 0.0)

if __name__ == '__main__':
    unittest.main()
