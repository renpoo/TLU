#!/usr/bin/env python3
# test_core_safe_linalg.py
import unittest
import numpy as np
from src.core.core_safe_linalg import compute_safe_pinv, compute_covariance_matrix

class TestSafeLinalg(unittest.TestCase):
    def test_compute_safe_pinv_singular(self):
        """
        完全にランク落ち（特異性）している行列に対し、
        例外を吐かずに安全な擬似逆行列が計算できるかのテスト。
        """
        # 意図的にランク落ちさせた行列（行2は行1の2倍なので、行列式は0）
        M_singular = np.array([
            [1.0, 2.0],
            [2.0, 4.0]
        ])
        
        
        # もし通常の np.linalg.inv(M_singular) を呼べば LinAlgError でクラッシュするが、
        # safe_pinv はクラッシュせずに結果（NumPy配列）を返すこと。
        # チコノフ正則化項（Ridgeペナルティ）
        # lambda_reg = 1e-4
        actual_pinv = compute_safe_pinv(M_singular, rcond=1e-15, lambda_reg=1e-4)
        
        # 結果が正しい形状 (2x2) であり、NaNなどが含まれていないことを確認
        self.assertEqual(actual_pinv.shape, (2, 2))
        self.assertFalse(np.isnan(actual_pinv).any())
        
    def test_compute_safe_pinv_zero_matrix(self):
        """
        すべての要素がゼロの行列（取引が一切ない完全な虚無）に対するテスト。
        """
        M_zero = np.zeros((3, 3))
        
        # ゼロ行列の擬似逆行列はゼロ行列になるべきだが、
        # lambda_reg (正則化項) が加わることでクラッシュを回避する。
        actual_pinv = compute_safe_pinv(M_zero, rcond=1e-15, lambda_reg=1e-4)
        
        self.assertEqual(actual_pinv.shape, (3, 3))
        self.assertFalse(np.isnan(actual_pinv).any())


    def test_compute_covariance_matrix_basic(self):
        """
        過去の状態変位ベクトル（dq_history）から、ノード間の共分散行列を正しく算出するテスト。
        """
        
        # dq_history: (Time_steps x Nodes) の行列
        # ここでは 3ステップ(T=3)、2ノード(N=2)の単純な履歴を想定
        # ノード0の履歴: [1, 3, 5] (平均=3)
        # ノード1の履歴: [2, 4, 6] (平均=4)
        dq_history = np.array([
            [1.0, 2.0],
            [3.0, 4.0],
            [5.0, 6.0]
        ])
        
        # 期待される共分散行列 (N x N)
        # ノード0の分散 (不偏分散): ((1-3)^2 + (3-3)^2 + (5-3)^2) / (3-1) = 8 / 2 = 4.0
        # ノード1の分散: ((2-4)^2 + (4-4)^2 + (6-4)^2) / 2 = 4.0
        # ノード0と1の共分散: ((-2)*(-2) + 0*0 + 2*2) / 2 = 8 / 2 = 4.0
        expected_cov = np.array([
            [4.0, 4.0],
            [4.0, 4.0]
        ])
        
        actual_cov = compute_covariance_matrix(dq_history)
        
        # 形状が (N, N) であることと、値の一致を確認
        self.assertEqual(actual_cov.shape, (2, 2))
        np.testing.assert_array_almost_equal(actual_cov, expected_cov)


    def test_compute_safe_pinv_exact_3x3_with_tikhonov(self):
        """
        波及エコーでは爆発してしまった 3x3 行列に対して、
        チコノフ正則化ルート (M^T M 経由) で正しい逆行列が求まるかどうかの検算テスト。
        """
        
        # 固有値にマイナスが含まれ、そのままエコーを回すと爆発する厄介な行列
        M_3x3 = np.array([
            [1.0, 2.0, 3.0],
            [3.0, 5.0, 4.0],
            [5.0, 6.0, 1.0]
        ])
        
        # 数学的に真の逆行列 (np.linalg.inv で直接求めた正確な値)
        # 19/6, -16/6, 7/6 ... の小数表現
        expected_inv_exact = np.array([
            [ 3.16666667, -2.66666667,  1.16666667],
            [-2.83333333,  2.33333333, -0.83333333],
            [ 1.16666667, -0.66666667,  0.16666667]
        ])
        
        # 1. ペナルティなし (lambda=0.0) のルート
        # 単純な SVD ベースの擬似逆行列なので、当然一致するはず。
        actual_inv_0 = compute_safe_pinv(M_3x3, rcond=1e-15, lambda_reg=0.0)
        np.testing.assert_array_almost_equal(actual_inv_0, expected_inv_exact, decimal=5)
        
        # 2. 微小なペナルティあり (lambda=1e-4) のチコノフ正則化ルート
        # M^T * M + lambda * I の計算を経由しても、真の逆行列の形が崩れていないことを証明する！
        actual_inv_reg = compute_safe_pinv(M_3x3, rcond=1e-15, lambda_reg=1e-4)

        np.testing.assert_array_almost_equal(actual_inv_reg, expected_inv_exact, decimal=2)


if __name__ == '__main__':
    unittest.main()