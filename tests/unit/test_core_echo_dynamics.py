#!/usr/bin/env python3
# test_core_echo_dynamics.py
import unittest
import numpy as np
from src.core.core_echo_dynamics import compute_finite_echo, compute_decomposed_echoes

class TestEchoDynamics(unittest.TestCase):
    def test_compute_finite_echo_basic(self):
        """
        有限波及行列（Echo）の総和を計算するテスト。
        2ノード間で質量がピンポンする単純なモデルで、減衰率(gamma)とステップ数(k)を検証。
        """
        # P: 遷移確率行列 (ノード0は100%ノード1へ、ノード1は100%ノード0へ)
        P_matrix = np.array([
            [0.0, 1.0],
            [1.0, 0.0]
        ])
        
        gamma = 0.5  # 減衰率（摩擦係数）
        max_k = 2    # 波及ステップ数 (0次, 1次, 2次)

        # 期待される波及行列 M_echo
        # 0次波及 (k=0): 単位行列 I = [[1, 0], [0, 1]]
        # 1次波及 (k=1): gamma^1 * P = [[0, 0.5], [0.5, 0]]
        # 2次波及 (k=2): gamma^2 * P^2 = 0.25 * [[1, 0], [0, 1]] = [[0.25, 0], [0, 0.25]]
        # 合計 M_echo: [[1.25, 0.5], [0.5, 1.25]]
        expected_M_echo = np.array([
            [1.25, 0.5],
            [0.5,  1.25]
        ])

        actual_M_echo = compute_finite_echo(P_matrix, gamma, max_k)

        np.testing.assert_array_almost_equal(actual_M_echo, expected_M_echo)


    def test_compute_decomposed_echoes_basic(self):
        """
        波及を合算せず、k次波及ごとに分解してリストとして返すテスト。
        """
        P_matrix = np.array([
            [0.0, 1.0],
            [1.0, 0.0]
        ])
        
        gamma = 0.5
        max_k = 2

        # 期待される分解された波及エコーのリスト
        # インデックス0: 1次波及 (gamma^1 * P)
        # インデックス1: 2次波及 (gamma^2 * P^2)
        # ※0次波及（単位行列）は含まない仕様とする
        expected_echoes = [
            np.array([[0.0, 0.5], [0.5, 0.0]]),   # 1st order
            np.array([[0.25, 0.0], [0.0, 0.25]])  # 2nd order
        ]

        actual_echoes = compute_decomposed_echoes(P_matrix, gamma, max_k)

        # リストの長さが一致することを確認
        assert len(actual_echoes) == len(expected_echoes)
        
        # 各階層の行列が一致することを確認
        for actual, expected in zip(actual_echoes, expected_echoes):
            np.testing.assert_array_almost_equal(actual, expected)


    def test_compute_decomposed_echoes_identity_matrix(self):
        """
        波及を合算せず、k次波及ごとに分解してリストとして返すテスト。
        """
        P_matrix = np.array([
            [1.0, 0.0],
            [0.0, 1.0]
        ])
        
        gamma = 1.0
        max_k = 2

        # 期待される分解された波及エコーのリスト
        # インデックス0: 1次波及 (gamma^1 * P)
        # インデックス1: 2次波及 (gamma^2 * P^2)
        # ※0次波及（単位行列）は含まない仕様とする
        expected_echoes = [
            np.array([[1.0, 0.0], [0.0, 1.0]]),   # 1st order
            np.array([[1.0, 0.0], [0.0, 1.0]])   # 2nd order
        ]

        actual_echoes = compute_decomposed_echoes(P_matrix, gamma, max_k)

        # リストの長さが一致することを確認
        assert len(actual_echoes) == len(expected_echoes)
        
        # 各階層の行列が一致することを確認
        for actual, expected in zip(actual_echoes, expected_echoes):
            np.testing.assert_array_almost_equal(actual, expected)


    def test_compute_finite_echo_native_2x2(self):
        """
        純粋な波及エコー関数の正常系テスト（2x2）。
        """
        P_matrix = np.array([
            [0.5, 0.5],
            [1.0, 0.0]
        ])
        gamma = 0.5
        max_k = 50  # 50回もループさせれば、無限等比級数の極限にほぼ到達する

        # 期待される無限波及行列（手計算での厳密な極限値）
        expected_M_echo = np.array([
            [1.6, 0.4],
            [0.8, 1.2]
        ])

        actual_M_echo = compute_finite_echo(P_matrix, gamma, max_k)

        # 50回の有限ループで、無限極限に「6桁の精度で」近似できているかをテストする
        np.testing.assert_array_almost_equal(actual_M_echo, expected_M_echo, decimal=5)

    def test_compute_finite_echo_native_3x3(self):
        """
        純粋な波及エコー関数の正常系テスト（3x3）。
        """
        P_matrix = np.array([
            [0.0, 0.5, 0.5],
            [0.5, 0.0, 0.5],
            [0.5, 0.5, 0.0]
        ])
        gamma = 0.5
        max_k = 50

        expected_M_echo = np.array([
            [1.2, 0.4, 0.4],
            [0.4, 1.2, 0.4],
            [0.4, 0.4, 1.2]
        ])

        actual_M_echo = compute_finite_echo(P_matrix, gamma, max_k)

        np.testing.assert_array_almost_equal(actual_M_echo, expected_M_echo, decimal=5)


    def test_compute_finite_echo_as_inverse_matrix(self):
        """
        一般的な行列 M の逆行列 M^-1 を、
        波及エコー関数(compute_finite_echo)の無限級数近似を利用して求めるテスト。
        """
        # 1. 解きたい一般的な行列 M
        M = np.array([
            [4.0, 7.0],
            [2.0, 6.0]
        ])
        
        # 期待される真の逆行列 (行列式=10)
        expected_M_inv = np.array([
            [ 0.6, -0.7],
            [-0.2,  0.4]
        ])

        # --------------------------------------------------------
        # 2. 波及エコー形式 ( I - P ) への「翻訳」プロセス
        # --------------------------------------------------------
        # M をそのまま P にすると波及が爆発するため、
        # 行列全体をすっぽり包み込む仮想の「枠の大きさ (c)」を定義します。
        # ここでは M の要素より少し大きい c = 10.0 とします。
        c = 10.0
        
        # M = c * (I - P) となるような、仮想の遷移確率行列 P を逆算します。
        # P = I - (M / c)
        I = np.eye(2)
        P_matrix = I - (M / c)
        
        # 3. エコーの実行
        # 摩擦なし(gamma=1.0) で、波及を100ステップ(max_k=100)回します。
        gamma = 1.0
        max_k = 100
        
        # エコー関数が計算するのは (I - P)^-1 の近似値です。
        echo_result = compute_finite_echo(P_matrix, gamma, max_k)
        
        # 4. 翻訳の巻き戻し
        # M = c * (I - P) なので、M^-1 = (1/c) * (I - P)^-1 です。
        # したがって、エコーの結果を c で割れば、Mの逆行列が復元されます。
        actual_M_inv_approx = echo_result / c
        
        # --------------------------------------------------------
        # 5. 検証
        # --------------------------------------------------------
        # エコー(足し算と掛け算のループ)だけで求めた近似値が、
        # 真の逆行列と「小数点以下5桁まで」完全に一致することを証明します。
        np.testing.assert_array_almost_equal(actual_M_inv_approx, expected_M_inv, decimal=5)


if __name__ == '__main__':
    unittest.main()
