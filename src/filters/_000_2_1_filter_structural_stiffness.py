#!/usr/bin/env python3
# ==========================================
# _000_2_1_filter_structural_stiffness.py
# TLU System: Structural Stiffness Matrix Filter
# Version: 7.6.0 (Partial Correlation Normalization Added)
# ==========================================
import sys
import argparse
import numpy as np
import pandas as pd
from typing import List, Tuple

from src.filters.cli_parser import get_base_parser
from src.filters.stream_processor import setup_pipeline, yield_time_slices

import src.core.core_tensor_ops as cto
import src.core.core_safe_linalg as csl

def compute_partial_correlation(K_precision: np.ndarray) -> np.ndarray:
    """!
    @brief [Pure Math] Calculate Partial Correlation matrix from Precision matrix.
    @details Resolves independent correlations mathematically mitigating false structural influences.

    @param K_precision Precision matrix (Inverse covariance).

    @return Formatted Partial Correlation Matrix.

    @pre
        - `K_precision` resolves to a mathematically robust inverted matrix.
    @post
        - Unconditionally yields values clipped exactly between [-1.0, 1.0].
    @invariant
        - Self partial correlation perfectly evaluates to 1.0.
    """
    N = K_precision.shape[0]
    R_partial = np.zeros((N, N), dtype=float)
    
    # Diagonal components (Self-stiffness)
    diag_K = np.diag(K_precision)
    # Safety handling to prevent zero division and negative square roots
    safe_diag = np.where(diag_K > 0, diag_K, 1e-15)
    
    for i in range(N):
        for j in range(N):
            if i == j:
                R_partial[i, j] = 1.0  # Self partial correlation is 1.0 by definition
            else:
                # Partial correlation coefficient formula: r_ij = -K_ij / sqrt(K_ii * K_jj)
                val = -K_precision[i, j] / np.sqrt(safe_diag[i] * safe_diag[j])
                R_partial[i, j] = val
                
    # Clip to prevent exceeding [-1.0, 1.0] due to minute numerical calculation errors
    return np.clip(R_partial, -1.0, 1.0)

def run_structural_stiffness_analysis(
        t_idx: int, 
        T_slice: np.ndarray, 
        q_history: List[np.ndarray]
) -> Tuple[List[list], np.ndarray]:
    """!
    @brief [Pure Orchestration Function] Run structural stiffness resolution.
    @details Isolates elasticity constraints coupling the domain.

    @param t_idx Current evaluation time step.
    @param T_slice Current transition tensor.
    @param q_history Array of pure flux vectors temporal domain.

    @return Tuple (Flattened records, current pure flux).

    @pre
        - Historical domains align structurally matching `N` scales.
    @post
        - Automatically returns zero bounds avoiding matrix inversion crashes.
    @invariant
        - Represents exact constrained geometry interactions safely isolated.
    """    
    N = T_slice.shape[0]
    records = []

    q_current = cto.compute_net_flux(T_slice)
    
    temp_history = q_history + [q_current]
    q_hist_arr = np.array(temp_history)

    if len(q_hist_arr) > 2:
        dq_history = np.diff(q_hist_arr, axis=0)
        covariance = csl.compute_covariance_matrix(dq_history)
        K_safe = csl.compute_safe_pinv(covariance, rcond=1e-15, lambda_reg=1e-4)
        # * Added: Conversion to Partial Correlation matrix (normalization for human interpretation)
        R_partial = compute_partial_correlation(K_safe)
    else:
        K_safe = np.zeros((N, N))
        R_partial = np.zeros((N, N))

    for i in range(N):
        for j in range(N):
            records.append([
                t_idx, i, j, 
                f"{K_safe[i, j]:.12f}",
                f"{R_partial[i, j]:.4f}" # * Added: Partial correlation coefficient (-1.0 to 1.0)
            ])
            
    return records, q_current

def main():
    parser = get_base_parser("TLU Structural Stiffness Matrix Filter")
    parser.add_argument("--history_window", type=int, default=12, help="Length of history used for covariance calculation")
    
    # * Fix: Added partial_corr to the header
    output_header = ["t_idx", "src_idx", "tgt_idx", "stiffness_k", "partial_corr"]
    args, N, reader, writer = setup_pipeline(parser, output_header)
    
    q_history_window = []

    for t_idx, T_slice in yield_time_slices(reader, N):
        records, q_current = run_structural_stiffness_analysis(
            t_idx=t_idx, 
            T_slice=T_slice, 
            q_history=q_history_window
        )
        
        q_history_window.append(q_current)
        if len(q_history_window) > args.history_window:
            q_history_window.pop(0)
            
        for rec in records:
            writer.writerow(rec)

if __name__ == "__main__":
    main()
