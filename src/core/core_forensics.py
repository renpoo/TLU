#!/usr/bin/env python3
# core_forensics.py
import numpy as np
from src.core.core_information_geometry import compute_kl_divergence

def check_conservation_law(q_current: np.ndarray, tolerance: float) -> tuple[float, bool]:
    """
    ネットワーク全体の純フラックスの総和を計算し、保存則の残差（漏電）を検知する。
    ※ tolerance（許容誤差）は呼び出し元から明示的に注入されること。
    """
    # 系全体の流入・流出の総和。複式簿記等の閉鎖系であれば本来は0になる。
    residual = float(np.sum(q_current))
    abs_residual = abs(residual)
    
    # 浮動小数点演算の誤差（tolerance）を超えていれば「漏れ」と判定
    is_leaking = abs_residual > tolerance
    
    return abs_residual, is_leaking

def compute_structural_drift(P_current: np.ndarray, P_history: list[np.ndarray]) -> float:
    """
    過去の遷移確率行列の履歴からベースラインを算出し、現在の分布とのKLダイバージェンスの総和を返す。
    """
    if not P_history:
        return 0.0
    
    # 過去の履歴（複数の行列）の平均を取り、これを「平常時の配分ルール（ベースライン）」とする
    P_baseline = np.mean(P_history, axis=0)
    
    # 共有ライブラリを使用して、各ノードのKLダイバージェンスを計算
    kl_div_array = compute_kl_divergence(P_current, P_baseline)
    
    # ノードごとの距離をすべて足し合わせ、ネットワーク全体としての「構造変化の大きさ」とする
    return float(np.sum(kl_div_array))

def compute_multivariate_anomaly(q_current: np.ndarray, q_mean: np.ndarray, K_precision: np.ndarray) -> float:
    """
    精度行列（共分散行列の逆行列）を用いて、現在の状態ベクトルのマハラノビス距離（Zスコア）を計算する。
    """
    # 期待値からのズレ（変位ベクトル）
    delta = q_current - q_mean
    
    # (q - μ)^T * K * (q - μ) の計算
    # ※ K_precision は、呼び出し元で compute_safe_pinv を用いて安全に計算されている前提
    mahalanobis_sq = np.dot(delta.T, np.dot(K_precision, delta))
    
    # 距離なので平方根をとる。数値誤差で負になる微小なケースを防ぐため max(0, ...) で保護
    z_score = np.sqrt(max(0.0, mahalanobis_sq))
    
    return float(z_score)

def evaluate_anomaly_flags(residual: float, kl_div: float, z_score: float, thresholds: dict) -> int:
    """
    各種異常スコアが閾値を超過しているかを判定し、1（異常）または 0（正常）を返す。
    ※ スケール不変性を保つため、内部での暗黙のデフォルト値は持たない。
    ※ thresholds には必ず 'leak_tolerance', 'kl_drift_thresh', 'z_score_thresh' が含まれていること。
    """
    # 意図的なFail-Fast: キーが存在しない場合は明示的にKeyErrorを発生させる
    if residual > thresholds['leak_tolerance']:
        return 1
    if kl_div > thresholds['kl_drift_thresh']:
        return 1
    if z_score > thresholds['z_score_thresh']:
        return 1
    
    return 0
