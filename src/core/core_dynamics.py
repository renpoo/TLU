#!/usr/bin/env python3
# core_dynamics.py
import numpy as np

def compute_optimal_time_lag(signal_A: np.ndarray, signal_B: np.ndarray, max_lag: int) -> tuple[int, float]:
    """
    2つの時系列シグナル間の相互相関を計算し、最も相関が高くなるタイムラグ（遅延）を特定する。
    
    Args:
        signal_A: 原因側の時系列配列 (1D np.ndarray) 例: 広告費
        signal_B: 結果側の時系列配列 (1D np.ndarray) 例: 売上
        max_lag:  探索する最大のタイムラグステップ数 (int)
        
    Returns:
        best_lag: 最も波形が一致したタイムラグ (int)
        max_corr: その時の相関係数 (float)
    """
    N = len(signal_A)
    best_lag = 0
    max_corr = -np.inf
    
    # 探索するラグの上限は、配列の長さから最低限計算に必要な要素数(2)を引いたものにも制限する
    actual_max_lag = min(max_lag, N - 2)
    
    # 履歴が短すぎて相関が計算できない場合は即座にゼロを返す
    if actual_max_lag < 0:
        return 0, 0.0

    for lag in range(actual_max_lag + 1):
        # シグナルAを基準とし、シグナルBを lag 分だけ「過去に引き戻して（左シフトして）」比較する
        # 例 lag=2: Aは[0]〜[N-3]まで、Bは[2]〜[N-1]までを使用
        slice_A = signal_A[: N - lag]
        slice_B = signal_B[lag :]
        
        # 波形が完全に平坦（分散が0）な場合、相関係数は計算できない（ゼロ除算）ため保護する
        std_A = np.std(slice_A)
        std_B = np.std(slice_B)
        
        if std_A == 0.0 or std_B == 0.0:
            corr = 0.0
        else:
            # np.corrcoefは2x2の相関行列を返すため、非対角要素([0, 1])を取得する
            corr = np.corrcoef(slice_A, slice_B)[0, 1]
            
        if corr > max_corr:
            max_corr = corr
            best_lag = lag
            
    return best_lag, float(max_corr)


def estimate_virtual_mass_and_viscosity(q_history: np.ndarray, v_history: np.ndarray, base_epsilon: float = 1e-6) -> tuple[np.ndarray, np.ndarray]:
    """
    過去の履歴から、各ノードの仮想的な質量(M)と粘性(C)を推定する。
    
    Args:
        q_history: 状態ベクトルの履歴 (Time_steps x Nodes)
        v_history: 速度ベクトルの履歴 (Time_steps x Nodes)
        
    Returns:
        M: ノードごとの仮想質量 (Nodes,)
        C: ノードごとの粘性抵抗 (Nodes,)
    """
    # 質量 M (慣性): 過去の活動量の蓄積（スケール）に比例すると仮定
    # 単純に、q_historyの絶対値の時間平均を「動かしにくさ」の指標とする
    M = np.mean(np.abs(q_history), axis=0)
    
    # 粘性 C (摩擦): 速度の変動が少ないほど摩擦が大きい（動きが固定されている）と仮定
    if v_history.shape[0] <= 1:
        # t_idx = 0 の場合（履歴が1ステップしかない場合）、すべての要素をゼロにする
        C = np.zeros(v_history.shape[1])
    else:
        # 速度の標準偏差(ボラティリティ)の逆数をとる。
        v_std = np.std(v_history, axis=0)
        
        # 完全に凪いでいる（標準偏差が0の）場合のゼロ除算を防ぐため、微小値(epsilon)を加算
        if (v_std == 0.0).all():
            global_v_scale = np.mean(v_std)
            dynamic_epsilon = max(base_epsilon, global_v_scale * 1e-6)
        else:
            dynamic_epsilon = 0.0

        C = 1.0 / (v_std + dynamic_epsilon)
    
    return M, C

def compute_external_force_residual(M: np.ndarray, C: np.ndarray, K: np.ndarray, a: np.ndarray, v: np.ndarray, dq: np.ndarray) -> np.ndarray:
    """
    観測された系の状態(M, C, K, a, v, dq)から、
    外部からの異常なショック(F_external)を逆算する。
    """
    # F_external = Ma + Cv + Kdq
    return M * a + C * v + K * dq
