#!/usr/bin/env python3
# test_core_information_geometry.py
import unittest
import numpy as np
from src.core.core_information_geometry import compute_shannon_entropy, compute_kl_divergence

class TestInformationGeometry(unittest.TestCase):
    def test_compute_shannon_entropy_basic(self):
        """
        遷移確率行列(P)から、ノードごとのシャノンエントロピーを計算するテスト。
        """
        # P: 遷移確率行列 (N x N)
        # ノード0: [1.0, 0.0, 0.0] -> 1つのノードに100%集中 (エントロピーは0になるべき)
        # ノード1: [0.5, 0.5, 0.0] -> 2つのノードに均等に分散
        # ノード2: [0.0, 0.0, 0.0] -> どこにも流出しない孤立ノード (安全に0を返すこと)
        P_matrix = np.array([
            [1.0, 0.0, 0.0],
            [0.5, 0.5, 0.0],
            [0.0, 0.0, 0.0]
        ])
        
        # シャノンエントロピー H = - sum(p * log2(p))
        # 0*log2(0) は極限をとって 0 として扱う。
        # ノード0: -(1 * 0) = 0.0
        # ノード1: -(0.5 * -1 + 0.5 * -1) = 1.0
        # ノード2: すべて0なので 0.0
        expected_entropy = np.array([0.0, 1.0, 0.0])
        
        actual_entropy = compute_shannon_entropy(P_matrix)
        
        np.testing.assert_array_almost_equal(actual_entropy, expected_entropy)


    def test_compute_shannon_entropy_2(self):
        # Node 0: 完全に確定的（1つのルートに100%集中 -> エントロピー 0）
        # Node 1: 2つのルートに完全に等確率で分散 -> エントロピー最大 (底が2なら 1.0)
        # Node 2: 全要素ゼロ（流量なしのノードに対する安全確認 -> エントロピー 0.0 を返すこと）
        P = np.array([
            [1.0, 0.0],
            [0.5, 0.5],
            [0.0, 0.0]
        ])
        
        entropy = compute_shannon_entropy(P)
        
        self.assertAlmostEqual(entropy[0], 0.0)
        self.assertAlmostEqual(entropy[1], 1.0)
        self.assertAlmostEqual(entropy[2], 0.0)


    def test_compute_kl_divergence_basic(self):
        """
        現在の遷移確率(P_current)と過去のベースライン(P_baseline)の間の、
        ノードごとのKLダイバージェンス（情報量的な距離）を計算するテスト。
        """
        
        # P_current: 現在の分布
        P_current = np.array([
            [0.5, 0.5],  # ノード0: 均等に分散
            [1.0, 0.0]   # ノード1: ノード0に100%集中
        ])
        
        # P_baseline: 過去の平均的な分布
        P_baseline = np.array([
            [0.5, 0.5],  # ノード0: 過去も同じく均等だった（変化なし）
            [0.5, 0.5]   # ノード1: 過去は均等だった（激変している！）
        ])
        
        # 期待されるKLダイバージェンス
        # ノード0: 0.5*log2(0.5/0.5) + 0.5*log2(0.5/0.5) = 0.0 (変化なし)
        # ノード1: 1.0*log2(1.0/0.5) + 0.0*log2(...) = 1.0*log2(2.0) + 0 = 1.0
        expected_kl = np.array([0.0, 1.0])
        
        actual_kl = compute_kl_divergence(P_current, P_baseline)
        
        np.testing.assert_array_almost_equal(actual_kl, expected_kl)


    def test_compute_kl_divergence_2(self):
        # 現在の遷移確率と、過去のベースラインの比較
        P_current = np.array([
            [0.5, 0.5], # Node 0: 変化なし
            [0.5, 0.5], # Node 1: ベースラインから変化あり
            [1.0, 0.0], # Node 2: 現在は0を含む（分子のゼロ除算耐性テスト）
            [0.0, 0.0]  # Node 3: 全要素ゼロ（安全確認）
        ])
        
        P_baseline = np.array([
            [0.5, 0.5], # Node 0: 変化なし
            [0.8, 0.2], # Node 1: 過去は[0.8, 0.2]の偏りがあった
            [0.5, 0.5], # Node 2: 過去は分散していた
            [0.0, 0.0]  # Node 3: 過去もゼロ
        ])
        
        kl_div = compute_kl_divergence(P_current, P_baseline)
        
        # Node 0: 分布が完全に一致しているため、距離はゼロ
        self.assertAlmostEqual(kl_div[0], 0.0)
        
        # Node 1: 分布が異なるため、距離は正の値を持つ
        # 計算: 0.5*log2(0.5/0.8) + 0.5*log2(0.5/0.2) ≒ 0.3219
        self.assertGreater(kl_div[1], 0.0)
        self.assertAlmostEqual(kl_div[1], 0.321928, places=4)
        
        # Node 2: P_currentの要素が0の場合でも、安全に計算され距離が出る
        # 計算: 1.0*log2(1.0/0.5) + 0.0 = 1.0
        self.assertAlmostEqual(kl_div[2], 1.0)
        
        # Node 3: ゼロ行列同士はゼロを返す
        self.assertAlmostEqual(kl_div[3], 0.0)


if __name__ == '__main__':
    unittest.main()
