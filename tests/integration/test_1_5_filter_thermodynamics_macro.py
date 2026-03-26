#!/usr/bin/env python3
# test_1_5_filter_thermodynamics_macro.py
import unittest
import numpy as np
from src.filters._1_5_filter_thermodynamics_macro import run_thermodynamics_analysis

class TestFilterThermodynamicsMacro(unittest.TestCase):
    def test_run_thermodynamics_analysis_basic(self):
        """
        [Red->Green] 純粋な数理ロジック層が、I/Oから完全に独立して
        熱力学指標（U, S, T, W, Q, F）を正しく計算し返すことを確認する。
        """
        # 準備 (Arrange)
        # ノード0 から ノード1 へ 10.0 の移動
        T_slice = np.array([
            [0.0, 10.0],
            [0.0,  0.0]
        ])
        q_history = []
        work_indices = [1] # ノード1への流入を「仕事」とする
        heat_indices = [0] # ノード0への流入を「散逸熱」とする
        t_idx = 0

        # 実行 (Act)
        records, q_current = run_thermodynamics_analysis(
            t_idx, T_slice, q_history, work_indices, heat_indices
        )

        # 検証 (Assert)
        # マクロ熱力学指標なので、出力レコードはシステム全体で1行のみ
        self.assertEqual(len(records), 1)
        self.assertEqual(q_current.shape, (2,))
        
        # レコード構造: [t_idx, U, S, T, W, Q, gradT, F]
        rec = records[0]
        self.assertEqual(len(rec), 8)
        self.assertEqual(rec[0], 0)
        self.assertTrue(isinstance(rec[1], str)) # Uなどが文字列フォーマットされているか

        # 具体的な値の簡単な検算 (T_sliceの総活動量 U = 10.0 になるはず)
        self.assertEqual(float(rec[1]), 10.0)

if __name__ == '__main__':
    unittest.main()
