#!/usr/bin/env python3
# core_thermodynamics.py
import numpy as np
from typing import List
from src.core.core_information_geometry import compute_shannon_entropy

# ==========================================
# Macro Thermodynamics (システム全体の指標)
# ==========================================

def compute_internal_energy(T_slice: np.ndarray) -> float:
    """
    ネットワークの1タイムスライスにおける内部エネルギー (U) を算出する。
    U = 系全体の総活動量 (総フラックスの絶対値和)
    """
    return float(np.sum(np.abs(T_slice)))

def compute_work(q_vector: np.ndarray, work_indices: List[int]) -> float:
    """
    系から取り出された有効仕事 (W) を算出する。
    W = work_sink に指定されたノードへの純流入の合計
    """
    if not work_indices:
        return 0.0
    return float(np.sum(q_vector[work_indices]))

def compute_heat(q_vector: np.ndarray, heat_indices: List[int]) -> float:
    """
    系から失われた散逸熱 (Q) を算出する。
    Q = heat_sink に指定されたノードへの純流入の合計
    """
    if not heat_indices:
        return 0.0
    return float(np.sum(q_vector[heat_indices]))

def compute_macro_entropy(P: np.ndarray) -> float:
    """
    ネットワーク全体のマクロなエントロピー S を算出する。
    """
    node_entropies = compute_shannon_entropy(P)
    S = float(np.sum(node_entropies))
    return S

def compute_helmholtz_free_energy(U: float, T: float, S: float) -> float:
    """
    ヘルムホルツの自由エネルギー F を算出する。
    F = U - TS
    (※ T は U と同次元である標準偏差スケールに矯正されていること)
    """
    return U - T * S

def compute_macro_temperature(q_history_window: np.ndarray) -> float:
    """
    ネットワーク全体の温度 T を算出する。
    T = 系全体の純フラックスの「標準偏差」の総和 (次元を合わせるための修正)
    """
    # 修正: np.var(分散) から np.std(標準偏差) へ変更し、次元を1次(円)に引き下げる
    node_std = np.std(q_history_window, axis=0, ddof=0)
    T = float(np.sum(node_std))
    return T

# ==========================================
# Local Thermodynamics (ノードごとの局所指標)
# ==========================================

def compute_local_internal_energy(T_slice: np.ndarray) -> np.ndarray:
    """
    ネットワークの1タイムスライスにおける、ノードごとの局所内部エネルギー (u_i) を算出する。
    u_i = そのノードの全流入量と全流出量の絶対値の和
    
    Returns:
        np.ndarray: 形状 (N,) の局所内部エネルギー配列
    """
    inflow = np.sum(np.abs(T_slice), axis=0)
    outflow = np.sum(np.abs(T_slice), axis=1)
    return inflow + outflow

def compute_local_temperature(q_history_window: np.ndarray) -> np.ndarray:
    """
    ネットワークの各ノードにおける局所温度 T_i を算出する。
    T_i = 各ノードの純フラックスの「標準偏差」（タイムウィンドウ内）
    
    Returns:
        np.ndarray: 形状 (N,) の局所温度配列
    """
    # 履歴が不足している（1ステップしかない）場合は0を返す
    if len(q_history_window) < 2:
        return np.zeros(q_history_window.shape[1], dtype=float)
        
    # 修正: np.var(分散) から np.std(標準偏差) へ変更
    return np.std(q_history_window, axis=0, ddof=0)
