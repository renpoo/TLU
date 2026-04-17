#!/usr/bin/env python3
# test_core_dynamics.py
import unittest
import numpy as np

# これから実装する純粋数学関数をインポート
from src.core.core_dynamics import compute_optimal_time_lag, estimate_virtual_mass_and_viscosity, compute_external_force_residual

class TestCoreDynamics(unittest.TestCase):
    
    def test_compute_optimal_time_lag_simple_shift(self):
        """
        [Red] 投資(signal_A)と効果発現(signal_B)の間に、
        明確な2ステップの時間遅れ（タイムラグ）が存在する場合のテスト。
        """
        # 時刻t=0でのみ大きな活動(10.0)があったシグナルA
        signal_A = np.array([10.0, 0.0, 0.0, 0.0, 0.0])
        
        # 時刻t=2でのみ大きな反応(10.0)があったシグナルB (Aから2ステップ遅れ)
        signal_B = np.array([0.0, 0.0, 10.0, 0.0, 0.0])
        
        max_lag = 3

        # 実行 (Act)
        lag, max_corr = compute_optimal_time_lag(signal_A, signal_B, max_lag)

        # 検証 (Assert)
        # BはAに対して「2ステップ」遅れているため、最適なラグは 2 であるべき
        self.assertEqual(lag, 2)
        # 形状が完全に一致しているため、相関係数は 1.0 に近いはず
        self.assertGreater(max_corr, 0.9)

    def test_virtual_estimate_mass_and_viscosity_relative(self):
        """
        [Red] ノードの質量(M)と粘性(C)の相対的な振る舞いを推定するテスト。
        具体的な計算式の実装前に、期待される物理的特性（大小関係）を定義する。
        """

        # 3時点、2ノードの履歴データ
        # Node 0 (左列): 活動量スケールが大きく、速度も激しく変動している（質量大、粘性小）
        # Node 1 (右列): 活動量スケールが小さく、速度が全く変化していない（質量小、粘性大）
        q_history = np.array([
            [100.0, 10.0],
            [120.0, 10.0],
            [90.0,  10.0]
        ])
        v_history = np.array([
            [20.0, 0.0],
            [20.0, 0.0],
            [-30.0, 0.0]
        ])

        # 実行 (Act)
        M, C = estimate_virtual_mass_and_viscosity(q_history, v_history, base_epsilon=1e-10, velocity_scale_ratio=0.1)

        # 検証 (Assert)
        # 1. 質量 M: 活動スケールが大きい Node 0 の方が、Node 1 より大きいはず
        self.assertGreater(M[0], M[1])
        
        # 2. 粘性 C: 摩擦で完全に動きが固定されている Node 1 の方が、自由に動く Node 0 より大きいはず
        self.assertGreater(C[1], C[0])
    
    def test_compute_external_force_residual(self):
        """
        [Red] 観測された系の状態(M, C, K, a, v, dq)から、
        外部からの異常なショック(F_external)を逆算するテスト。
        """
        
        # 認知負荷を下げるため、単一ノード（要素数1の配列）でテストする
        # 仮想質量 M = 10.0, 粘性 C = 2.0, 剛性(バネ定数) K = 5.0
        M = np.array([10.0])
        C = np.array([2.0])
        K = np.array([5.0])
        
        # 観測された現在の状態
        # 加速度 a = 1.0, 速度 v = 3.0, 変位 dq = 2.0
        a = np.array([1.0])
        v = np.array([3.0])
        dq = np.array([2.0])
        
        # 実行 (Act)
        F_ext = compute_external_force_residual(M, C, K, a, v, dq)
        
        # 検証 (Assert)
        # F_ext = Ma + Cv + K*dq
        # F_ext = (10.0 * 1.0) + (2.0 * 3.0) + (5.0 * 2.0)
        #       = 10.0 + 6.0 + 10.0 = 26.0
        self.assertEqual(F_ext[0], 26.0)

if __name__ == '__main__':
    unittest.main()
