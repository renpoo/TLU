#!/usr/bin/env python3
# test_core_tensor_ops.py
import unittest
import numpy as np
from src.core.core_tensor_ops import compute_net_flux, compute_transition_matrix


class TestStreamProcessor(unittest.TestCase):
    def test_compute_net_flux_basic(self):
        """
        3x3の単純な遷移テンソル（行列）における純フラックスを計算するテスト。
        ドメイン（科目や部門）の意味は一切持たない、純粋な質量移動の観測。
        """
        # 3ノード間の質量移動 (T_matrix[src, tgt] = value)
        # ノード0 -> ノード1: 10
        # ノード1 -> ノード2: 5
        # ノード2 -> ノード0: 2
        T_matrix = np.array([
            [0, 10,  0],
            [0,  0,  5],
            [2,  0,  0]
        ])
    
        # 期待される純フラックス q (流入 - 流出)
        # ノード0: 流入(2) - 流出(10) = -8
        # ノード1: 流入(10) - 流出(5) = 5
        # ノード2: 流入(5) - 流出(2) = 3
        expected_q = np.array([-8, 5, 3])
    
        actual_q = compute_net_flux(T_matrix)
    
        np.testing.assert_array_equal(actual_q, expected_q)


    def test_compute_transition_matrix_basic_and_zero_div(self):
        """
        遷移確率行列（分配比率）の計算と、ゼロ除算の回避テスト。
        """
        T_matrix = np.array([
            [0, 8, 2],  # ノード0: 総流出10 (ノード1へ80%, ノード2へ20%)
            [0, 0, 0],  # ノード1: 総流出0 (ゼロ除算の危機！)
            [5, 5, 0]   # ノード2: 総流出10 (ノード0へ50%, ノード1へ50%)
        ])
        
        # 期待される遷移行列 P
        # 割り算が不可能なノード1の行は、すべて0のまま安全に処理されること。
        expected_P = np.array([
            [0.0, 0.8, 0.2],
            [0.0, 0.0, 0.0],
            [0.5, 0.5, 0.0]
        ])
        
        actual_P = compute_transition_matrix(T_matrix)
        
        np.testing.assert_array_almost_equal(actual_P, expected_P)


    def test_compute_net_flux_basic(self):
        """
        3ノードの単純な系での純フラックス算出テスト
        Node 0 -> Node 1: 100
        Node 1 -> Node 2: 30
        
        期待される純フラックス q:
        Node 0: -100 (流出のみ)
        Node 1: +100 - 30 = 70
        Node 2: +30 (流入のみ)
        """
        # 隣接行列 T (行: src, 列: tgt)
        T = np.array([
            [0, 100,   0],
            [0,   0,  30],
            [0,   0,   0]
        ])
        
        expected_q = np.array([-100, 70, 30])
        
        # 実行
        actual_q = compute_net_flux(T)
        
        # 検証
        np.testing.assert_array_almost_equal(actual_q, expected_q)


if __name__ == '__main__':
    unittest.main()
