#!/usr/bin/env python3
# core_topology.py
import numpy as np

def compute_edge_stress(T_current: np.ndarray, T_history_window: list[np.ndarray]) -> np.ndarray:
    """
    過去の遷移確率(またはフラックス)行列の履歴から、現在のエッジごとの応力(Stress)を計算する。
    応力は、過去の平均からの逸脱度（単変量Zスコア）として定義される。
    
    Args:
        T_current: 現在の行列 (Nodes x Nodes)
        T_history_window: 過去の行列のリスト
        
    Returns:
        stress_matrix: エッジごとの応力行列 (Nodes x Nodes)
    """
    N = T_current.shape[0]
    if len(T_history_window) < 2:
        return np.zeros((N, N), dtype=float)
        
    hist_arr = np.array(T_history_window)
    mean_tensor = np.mean(hist_arr, axis=0)
    std_tensor = np.std(hist_arr, axis=0)
    
    # 逸脱度の計算
    deviation = np.abs(T_current - mean_tensor)
    
    # ゼロ除算の回避: 標準偏差が0のエッジ（常に一定額の取引）は、応力を0とする
    stress_matrix = np.divide(
        deviation, 
        std_tensor, 
        out=np.zeros_like(deviation), 
        where=(std_tensor != 0)
    )
    
    return stress_matrix
