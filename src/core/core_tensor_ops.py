#!/usr/bin/env python3
# core_tensor_ops.py
import numpy as np

def _compute_outflow(T_matrix):
    return np.sum(T_matrix, axis=1)

def _compute_inflow(T_matrix):
    return np.sum(T_matrix, axis=0)
    
def compute_net_flux(T_matrix):
    """
    与えられた遷移テンソル（行列）から純フラックスを計算する。
    """
    return _compute_inflow(T_matrix) - _compute_outflow(T_matrix)

def compute_transition_matrix(T_matrix):
    """
    与えられた遷移テンソル（行列）から遷移確率行列（分配比率）を計算する。
    """
    outflow = _compute_outflow(T_matrix)
    outflow_col = outflow[:, np.newaxis]
    P_matrix = np.zeros_like(T_matrix, dtype=float)
    return np.divide(T_matrix, outflow_col, out=P_matrix, where=outflow_col != 0)
