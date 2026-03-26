#!/usr/bin/env python3
# test_core_kinematics.py
import unittest
import numpy as np
from src.core.core_kinematics import compute_derivatives

class TestKinematics(unittest.TestCase):
    def test_compute_derivatives_basic(self):
        """
        状態ベクトル(q)の時系列履歴から、最新の速度(v)と加速度(a)を算出するテスト。
        """
        # q_history: 時系列順に並んだ状態ベクトル (Time_steps x Nodes)
        # 3ステップ(T=3)、2ノード(N=2)を想定
        # ノード0: [10, 15, 18] -> 速度は徐々に落ちている
        # ノード1: [100, 90, 80] -> 一定の速度で減少している
        q_history = np.array([
            [10.0, 100.0],  # t=0
            [15.0,  90.0],  # t=1
            [18.0,  80.0]   # t=2 (最新)
        ])
        
        # 期待される速度ベクトル v (最新の1階差分: q[t] - q[t-1])
        # ノード0: 18 - 15 = 3.0
        # ノード1: 80 - 90 = -10.0
        expected_v = np.array([3.0, -10.0])
        
        # 期待される加速度ベクトル a (最新の2階差分: v[t] - v[t-1])
        # 直前の速度 v[t-1] を計算 -> ノード0: 15-10=5.0, ノード1: 90-100=-10.0
        # 加速度 a = 最新の速度 - 直前の速度
        # ノード0: 3.0 - 5.0 = -2.0 (減速している)
        # ノード1: -10.0 - (-10.0) = 0.0 (等速運動)
        expected_a = np.array([-2.0, 0.0])
        
        actual_v, actual_a = compute_derivatives(q_history)
        
        np.testing.assert_array_almost_equal(actual_v, expected_v)
        np.testing.assert_array_almost_equal(actual_a, expected_a)

    def test_compute_derivatives_insufficient_history(self):
        """
        履歴が足りず、速度や加速度が計算できない場合のテスト。
        安全にゼロベクトルを返すこと。
        """
        # T=1 (最新のみ)
        q_history_short = np.array([[10.0, 100.0]])
        
        actual_v, actual_a = compute_derivatives(q_history_short)
        
        # 履歴が足りない場合はゼロベクトルを返す安全設計
        expected_zeros = np.array([0.0, 0.0])
        np.testing.assert_array_almost_equal(actual_v, expected_zeros)
        np.testing.assert_array_almost_equal(actual_a, expected_zeros)

if __name__ == '__main__':
    unittest.main()
