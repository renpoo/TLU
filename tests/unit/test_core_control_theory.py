#!/usr/bin/env python3
# test_core_control_theory.py
import unittest
import numpy as np
from src.core.core_control_theory import (
    build_state_space_matrices,
    build_QR_matrices,
    solve_lqr_gain,
    compute_optimal_input
)

class TestControlTheory(unittest.TestCase):
    def test_build_state_space_matrices(self):
        # 3ノードのシステム。ノード0と2が制御可能（リソース投下可能）
        P_matrix = np.array([
            [0.8, 0.2, 0.0],
            [0.1, 0.9, 0.0],
            [0.0, 0.0, 1.0]
        ])
        controllable_indices = [0, 2]
        
        A, B = build_state_space_matrices(P_matrix, controllable_indices)
        
        # A行列はP行列と一致するはず（今回はLTIシステムとしてPをそのまま使用）
        np.testing.assert_array_equal(A, P_matrix)
        
        # B行列は (3 x 2) のマッピング行列になるはず
        expected_B = np.array([
            [1.0, 0.0], # Node 0 への入力
            [0.0, 0.0], # Node 1 は制御不可
            [0.0, 1.0]  # Node 2 への入力
        ])
        np.testing.assert_array_equal(B, expected_B)

    def test_build_QR_matrices(self):
        N = 3
        num_inputs = 2
        weight_Q = 10.0
        weight_R = 1.0
        target_indices = [1] # Node 1 の目標達成を重視
        
        Q, R = build_QR_matrices(N, num_inputs, weight_Q, weight_R, target_indices)
        
        # Q は (3 x 3)。ターゲットである Node 1 (インデックス1) の重みが 10.0 になる
        expected_Q = np.diag([0.0, 10.0, 0.0])
        # R は (2 x 2)。入力に対するペナルティが 1.0
        expected_R = np.diag([1.0, 1.0])
        
        np.testing.assert_array_equal(Q, expected_Q)
        np.testing.assert_array_equal(R, expected_R)

    def test_solve_lqr_gain_and_optimal_input(self):
        # 非常に単純な1次元システムでの検算
        # x(t+1) = 1.0 * x(t) + 1.0 * u(t)
        A = np.array([[1.0]])
        B = np.array([[1.0]])
        Q = np.array([[10.0]]) # 目標とのズレを非常に嫌う
        R = np.array([[1.0]])  # コストは少しだけ気にする
        
        K_lqr = solve_lqr_gain(A, B, Q, R)
        
        # DAREの厳密解に基づく K は約 0.916 程度になる
        self.assertEqual(K_lqr.shape, (1, 1))
        self.assertTrue(K_lqr[0, 0] > 0.0) # 正のフィードバックゲインが掛かること
        
        # 現在状態が 50.0、目標が 100.0 の場合
        current_state = np.array([50.0])
        target_state = np.array([100.0])
        
        u = compute_optimal_input(K_lqr, current_state, target_state)
        
        # u = -K * (current - target) = -K * (-50) = K * 50
        # ゲインが約 0.9 なので、入力は約 45.0 程度になるはず（一気に埋めようとする）
        self.assertTrue(u[0] > 40.0)

if __name__ == '__main__':
    unittest.main()
