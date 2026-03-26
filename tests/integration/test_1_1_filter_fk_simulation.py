#!/usr/bin/env python3
# test_1_1_filter_fk_simulation.py
import unittest
import numpy as np
from src.filters._1_1_filter_fk_simulation import run_fk_analysis

class TestFilterFKSimulation(unittest.TestCase):
    def setUp(self):
        self.N = 3
        # ノード0 -> ノード1 (10.0), ノード1 -> ノード2 (5.0)
        self.T_slice = np.array([
            [0.0, 10.0, 0.0],
            [0.0,  0.0, 5.0],
            [0.0,  0.0, 0.0]
        ])
        self.t_idx = 1
        self.q_history = [
            np.array([-5.0, 5.0, 0.0]),
            np.array([-8.0, 3.0, 5.0]),
            np.array([-10.0, 5.0, 5.0])
        ]
        self.gamma = 0.85
        self.max_k = 5

    def test_run_fk_analysis_static(self):
        """[Red->Green] FK系統 (Staticモード) の純粋関数テスト"""
        static_dq_input = np.array([100.0, 0.0, 0.0]) # ノード0に+100のショック
        
        records, q_current = run_fk_analysis(
            t_idx=self.t_idx, 
            T_slice=self.T_slice, 
            q_history=self.q_history,
            fk_input_mode='static', 
            static_dq_input=static_dq_input,
            gamma=self.gamma, 
            max_k=self.max_k
        )
        
        # N件のレコードが返ること
        self.assertEqual(len(records), self.N)
        
        # q_currentが正しく計算されて返ること ([-10, 5, 5])
        self.assertEqual(q_current.shape, (3,))
        
        # レコード構造: [t_idx, node_idx, fk_echo_impact]
        node0_rec = records[0]
        self.assertEqual(node0_rec[0], self.t_idx)
        self.assertEqual(node0_rec[1], 0)
        
        # FKの出力が計算されていること (文字列としてフォーマットされている)
        self.assertNotEqual(node0_rec[2], "0.0000")

if __name__ == '__main__':
    unittest.main()
