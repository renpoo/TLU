#!/usr/bin/env python3
# ==========================================
# _000_2_1_filter_structural_stiffness.py
# TLU System: Structural Stiffness Matrix Filter
# Version: 8.0.0 (Refactored with BaseFilter Architecture)
# ==========================================
import sys
import argparse
import numpy as np
import pandas as pd
from typing import List, Tuple, Dict, Any

from src.filters.base_filter import BaseFilter, HistoryBuffer
import src.core.core_tensor_ops as cto
import src.core.core_safe_linalg as csl

def compute_partial_correlation(K_precision: np.ndarray) -> np.ndarray:
    """!
    @brief [Pure Math] Calculate Partial Correlation matrix from Precision matrix.
    """
    N = K_precision.shape[0]
    R_partial = np.zeros((N, N), dtype=float)
    
    diag_K = np.diag(K_precision)
    safe_diag = np.where(diag_K > 0, diag_K, 1e-15)
    
    for i in range(N):
        for j in range(N):
            if i == j:
                R_partial[i, j] = 1.0
            else:
                val = -K_precision[i, j] / np.sqrt(safe_diag[i] * safe_diag[j])
                R_partial[i, j] = val
                
    return np.clip(R_partial, -1.0, 1.0)

def run_structural_stiffness_analysis(
        t_idx: int, 
        T_slice: np.ndarray, 
        q_history: List[np.ndarray]
) -> Tuple[List[list], np.ndarray]:
    """!
    @brief [Pure Orchestration Function] Run structural stiffness resolution.
    @details Legacy interface retained for backward compatibility with integration tests.
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
        R_partial = compute_partial_correlation(K_safe)
    else:
        K_safe = np.zeros((N, N))
        R_partial = np.zeros((N, N))

    for i in range(N):
        for j in range(N):
            records.append([
                t_idx, i, j, 
                f"{K_safe[i, j]:.12f}",
                f"{R_partial[i, j]:.4f}"
            ])
            
    return records, q_current


class StructuralStiffnessFilter(BaseFilter):
    cli_description = "TLU Structural Stiffness Matrix Filter"
    output_header = ["t_idx", "src_idx", "tgt_idx", "stiffness_k", "partial_corr"]
    history_config = {"q": 12}

    def add_arguments(self, parser: argparse.ArgumentParser):
        parser.add_argument("--history_window", type=int, default=12, help="Length of history used for covariance calculation")

    def process_slice(
        self, 
        t_idx: int, 
        T_slice: np.ndarray, 
        history: HistoryBuffer,
        X_initial: np.ndarray,
        args: argparse.Namespace
    ) -> Tuple[List[List[Any]], Dict[str, np.ndarray]]:
        
        q_hist = history.get("q")
        records, q_current = run_structural_stiffness_analysis(
            t_idx=t_idx,
            T_slice=T_slice,
            q_history=q_hist
        )

        return records, {"q": q_current}

def main():
    filter_app = StructuralStiffnessFilter()
    filter_app.run()

if __name__ == "__main__":
    main()
