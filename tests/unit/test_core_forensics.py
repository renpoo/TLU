#!/usr/bin/env python3
# test_core_forensics.py
import unittest
import numpy as np
from src.core.core_forensics import (
    check_conservation_law,
    compute_structural_drift,
    compute_multivariate_anomaly,
    evaluate_anomaly_flags
)

class TestCoreForensics(unittest.TestCase):
    def test_check_conservation_law(self):
        # ネットワーク全体の純フラックスの総和がゼロ（保存則）を満たしているか
        q_balanced = np.array([100.0, -50.0, -50.0])
        residual, is_leaking = check_conservation_law(q_balanced)
        self.assertAlmostEqual(residual, 0.0)
        self.assertFalse(is_leaking)

        # 保存則が壊れている（5.0 の漏電が発生）
        q_leaking = np.array([100.0, -50.0, -45.0])
        residual_leak, is_leaking_leak = check_conservation_law(q_leaking, tolerance=1e-3)
        self.assertAlmostEqual(residual_leak, 5.0)
        self.assertTrue(is_leaking_leak)

    def test_compute_structural_drift(self):
        # 過去の履歴（ベースライン）と現在の遷移確率を比較し、KLダイバージェンスの総和（ネットワーク全体のドリフト）を測る
        P_history = [
            np.array([[0.5, 0.5], [0.8, 0.2]]),
            np.array([[0.5, 0.5], [0.8, 0.2]])
        ]
        
        P_current_stable = np.array([[0.5, 0.5], [0.8, 0.2]])
        drift_stable = compute_structural_drift(P_current_stable, P_history)
        self.assertAlmostEqual(drift_stable, 0.0)

        # 構造が変化した（ドリフト発生）
        P_current_shifted = np.array([[1.0, 0.0], [0.5, 0.5]])
        drift_shifted = compute_structural_drift(P_current_shifted, P_history)
        self.assertGreater(drift_shifted, 0.0)

    def test_compute_multivariate_anomaly(self):
        # マハラノビス距離を用いた多次元の異常検知 (Zスコア)
        q_current = np.array([10.0, -10.0])
        q_mean = np.array([0.0, 0.0])
        
        # 完全に無相関で分散1の精度行列（単位行列）
        K_precision_identity = np.eye(2)
        
        z_score = compute_multivariate_anomaly(q_current, q_mean, K_precision_identity)
        # 期待値: sqrt(10^2 + (-10)^2) = sqrt(200) ≒ 14.14
        self.assertAlmostEqual(z_score, 14.1421, places=4)

    def test_evaluate_anomaly_flags(self):
        # 閾値辞書
        thresholds = {
            'leak_tolerance': 1.0,
            'kl_drift_thresh': 2.0,
            'z_score_thresh': 3.0
        }
        
        # 1. すべて正常
        flag_normal = evaluate_anomaly_flags(residual=0.1, kl_div=0.5, z_score=1.5, thresholds=thresholds)
        self.assertEqual(flag_normal, 0)
        
        # 2. 漏電（保存則違反）のみ異常
        flag_leak = evaluate_anomaly_flags(residual=5.0, kl_div=0.5, z_score=1.5, thresholds=thresholds)
        self.assertEqual(flag_leak, 1)
        
        # 3. Zスコアのみ異常
        flag_z = evaluate_anomaly_flags(residual=0.0, kl_div=0.5, z_score=4.0, thresholds=thresholds)
        self.assertEqual(flag_z, 1)

if __name__ == '__main__':
    unittest.main()
