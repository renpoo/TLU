#!/usr/bin/env python3
# test_core_topology.py
import unittest
import numpy as np
from src.core.core_topology import compute_edge_stress

class TestCoreTopology(unittest.TestCase):
    def test_compute_edge_stress_normal(self):
        """[Green] 通常の履歴から正しくZスコア（応力）が計算されること"""
        T_current = np.array([
            [0.0, 10.0],
            [0.0,  0.0]
        ])
        # 履歴の平均=4.0, 標準偏差=2.0 になるようなデータ
        T_history = [
            np.array([[0.0, 6.0], [0.0, 0.0]]),
            np.array([[0.0, 2.0], [0.0, 0.0]])
        ]
        
        stress = compute_edge_stress(T_current, T_history)
        
        # 期待値: |10.0 - 4.0| / 2.0 = 3.0
        self.assertEqual(stress.shape, (2, 2))
        self.assertAlmostEqual(stress[0, 1], 3.0)

    def test_compute_edge_stress_insufficient_history(self):
        """[Green] 履歴が2件未満の場合は安全にゼロ行列を返すこと"""
        T_current = np.array([[0.0, 10.0], [0.0, 0.0]])
        T_history = [np.array([[0.0, 5.0], [0.0, 0.0]])] # 1件のみ
        
        stress = compute_edge_stress(T_current, T_history)
        
        self.assertEqual(stress[0, 1], 0.0)
        self.assertTrue(np.all(stress == 0.0))

    def test_compute_edge_stress_zero_division(self):
        """[Green] 過去の標準偏差が0（一定の取引）の場合、ゼロ除算を回避して0.0を返すこと"""
        T_current = np.array([[0.0, 10.0], [0.0, 0.0]])
        # 履歴がすべて同じ値（標準偏差 = 0.0）
        T_history = [
            np.array([[0.0, 5.0], [0.0, 0.0]]),
            np.array([[0.0, 5.0], [0.0, 0.0]])
        ]
        
        stress = compute_edge_stress(T_current, T_history)
        
        # np.divide の where 句により、安全に 0.0 が返るはず
        self.assertEqual(stress[0, 1], 0.0)

if __name__ == '__main__':
    unittest.main()
