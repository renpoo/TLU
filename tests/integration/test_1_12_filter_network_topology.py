#!/usr/bin/env python3
# test_1_12_filter_network_topology.py
import unittest
import numpy as np
from src.filters._1_12_filter_network_topology import run_network_topology_analysis

class TestFilterNetworkTopology(unittest.TestCase):
    def test_run_network_topology_analysis_basic(self):
        """
        [Red->Green] 1タイムスライスを渡したとき、I/Oに依存せずに
        アクティブなエッジの重みと応力が計算されることを確認。
        """
        # t=3 の最新スライス
        T_slice = np.array([
            [0.0, 10.0, 5.0],  # 0->1, 0->2 のエッジが存在
            [0.0,  0.0, 0.0],
            [2.0,  0.0, 0.0]   # 2->0 のエッジが存在
        ])
        t_idx = 3
        
        # 過去2ステップ分の履歴
        T_history = [
            np.array([[0.0, 8.0, 5.0], [0.0, 0.0, 0.0], [2.0, 0.0, 0.0]]),
            np.array([[0.0, 12.0, 5.0], [0.0, 0.0, 0.0], [2.0, 0.0, 0.0]])
        ]

        # 実行
        records = run_network_topology_analysis(t_idx, T_slice, T_history)

        # 検証
        # weight > 0 のエッジは3つ (0->1, 0->2, 2->0) なので、3行返るはず
        self.assertEqual(len(records), 3)

        # 0 -> 1 のエッジを検証
        rec_0_1 = next(r for r in records if r[1] == 0 and r[2] == 1)
        self.assertEqual(rec_0_1[0], t_idx) # t_idx
        
        # 値が文字列としてフォーマットされているか
        self.assertTrue(isinstance(rec_0_1[3], str)) # weight
        self.assertTrue(isinstance(rec_0_1[4], str)) # stress

if __name__ == '__main__':
    unittest.main()
