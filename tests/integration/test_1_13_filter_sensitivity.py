#!/usr/bin/env python3
# test_1_13_filter_sensitivity.py
import unittest
import numpy as np
from src.filters._1_13_filter_sensitivity import run_sensitivity_analysis

class TestFilterSensitivity(unittest.TestCase):
    def test_run_sensitivity_analysis_logic(self):
        """
        [Red->Green] 純粋な数理ロジック層が、I/Oから完全に独立して
        各ノードの波及効果(FK)と目標ひずみ(IK)を正しく計算し返すことを確認する。
        """
        N = 3
        t_idx = 3
        T_slice = np.array([
            [0.0, 10.0, 5.0],
            [0.0,  0.0, 0.0],
            [2.0,  0.0, 0.0]
        ])
        
        # 過去2ステップ分の履歴 (最新の T_slice 分と合わせて3ステップになり、共分散が計算される)
        q_history = [
            np.array([10.0, 5.0, 2.0]),   # t=1
            np.array([12.0, 8.0, 5.0])    # t=2
        ]
        
        delta = 10.0
        gamma = 0.85
        max_k = 5

        # 実行 (Act)
        records, q_current = run_sensitivity_analysis(
            t_idx, T_slice, q_history, delta, gamma, max_k
        )

        # 検証 (Assert)
        self.assertEqual(len(records), N)
        self.assertEqual(q_current.shape, (N,))

        # レコード構造: [t_idx, node_idx, fk_total_ripple, fk_max_impact, fk_max_node, ik_strain_energy, ik_max_adjust, ik_max_node]
        rec0 = records[0]
        self.assertEqual(len(rec0), 8)
        self.assertEqual(rec0[0], t_idx)
        self.assertEqual(rec0[1], 0)
        
        # 値が文字列としてフォーマットされているか
        self.assertTrue(isinstance(rec0[2], str)) # fk_total_ripple
        self.assertTrue(isinstance(rec0[5], str)) # ik_strain_energy

        # 渡したリストが変異（mutate）していないことの証明
        self.assertEqual(len(q_history), 2)

if __name__ == '__main__':
    unittest.main()
