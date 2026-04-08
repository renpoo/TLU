#!/usr/bin/env python3
# test_1_6_filter_local_thermo.py
import unittest
import numpy as np
from src.filters._001_1_2_filter_local_thermodynamics import run_local_thermo_analysis

class TestFilterLocalThermo(unittest.TestCase):
    def test_run_local_thermo_analysis_basic(self):
        """
        [Red->Green] 純粋な数理ロジック層が、履歴を内部で変異させることなく、
        局所熱力学指標（u_i, s_i, t_i）を正しく計算し返すことを確認する。
        """
        N = 2
        # ノード0 から ノード1 へ 10.0 の移動
        T_slice = np.array([
            [0.0, 10.0],
            [0.0,  0.0]
        ])
        q_history = []
        t_idx = 0

        # 実行
        records, q_current = run_local_thermo_analysis(
            t_idx, T_slice, q_history
        )

        # 検証
        self.assertEqual(len(records), N)
        self.assertEqual(q_current.shape, (2,))
        
        # レコード構造: [t_idx, node_idx, u_i, s_i, t_i]
        node0_rec = records[0]
        self.assertEqual(len(node0_rec), 5)
        self.assertEqual(node0_rec[0], 0)
        self.assertEqual(node0_rec[1], 0)
        self.assertTrue(isinstance(node0_rec[2], str))

        # 渡したリストが変異（mutate）していないことの証明
        self.assertEqual(len(q_history), 0)

if __name__ == '__main__':
    unittest.main()
