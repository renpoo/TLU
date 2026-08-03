#!/usr/bin/env python3
# ==========================================
# _000_2_2_filter_principal_axes.py
# TLU System: Principal Axes (PCA) Filter
# Version: 8.0.0 (Refactored with BaseFilter Architecture)
# ==========================================
import sys
import argparse
import numpy as np
from typing import List, Tuple, Dict, Any

from src.filters.base_filter import BaseFilter, HistoryBuffer
import src.core.core_tensor_ops as cto
import src.core.core_safe_linalg as csl

def run_principal_axes_analysis(
        t_idx: int, 
        T_slice: np.ndarray, 
        q_history: List[np.ndarray],
        top_k: int
) -> Tuple[List[list], np.ndarray]:
    """!
    @brief [Pure Orchestration Function] Run Principal Axes (PCA) resolution.
    @details Legacy interface retained for backward compatibility with unit tests.
    """    
    N = T_slice.shape[0]
    records = []

    q_current = cto.compute_net_flux(T_slice)
    
    temp_history = q_history + [q_current]
    q_hist_arr = np.array(temp_history)

    if len(q_hist_arr) > 2:
        dq_history = np.diff(q_hist_arr, axis=0)
        covariance = csl.compute_covariance_matrix(dq_history)
        
        eigenvalues, eigenvectors = np.linalg.eigh(covariance)
        
        idx_sorted = np.argsort(eigenvalues)[::-1]
        eigenvalues = eigenvalues[idx_sorted]
        eigenvectors = eigenvectors[:, idx_sorted]
        
        total_variance = np.sum(np.maximum(eigenvalues, 0))
        k_limit = min(top_k, N)
        
        for k in range(k_limit):
            eig_val = eigenvalues[k]
            ratio = eig_val / total_variance if total_variance > 1e-15 else 0.0
            
            for i in range(N):
                vec_val = eigenvectors[i, k]
                records.append([
                    t_idx, 
                    k,
                    i,
                    f"{eig_val:.6f}",
                    f"{ratio:.6f}",
                    f"{vec_val:.6f}"
                ])
    else:
        k_limit = min(top_k, N)
        for k in range(k_limit):
            for i in range(N):
                records.append([t_idx, k, i, "0.000000", "0.000000", "0.000000"])

    return records, q_current


class PrincipalAxesFilter(BaseFilter):
    cli_description = "TLU Principal Axes Filter"
    output_header = ["t_idx", "component_idx", "node_idx", "eigenvalue", "explained_variance_ratio", "vector_value"]
    history_config = {"q": 12}

    def add_arguments(self, parser: argparse.ArgumentParser):
        parser.add_argument("--history_window", type=int, default=12, help="Length of history used for covariance calculation")
        parser.add_argument("--top_k", type=int, default=3, help="Number of top principal components to extract")

    def process_slice(
        self, 
        t_idx: int, 
        T_slice: np.ndarray, 
        history: HistoryBuffer,
        X_initial: np.ndarray,
        args: argparse.Namespace
    ) -> Tuple[List[List[Any]], Dict[str, np.ndarray]]:
        
        q_hist = history.get("q")
        records, q_current = run_principal_axes_analysis(
            t_idx=t_idx, 
            T_slice=T_slice, 
            q_history=q_hist,
            top_k=args.top_k
        )

        return records, {"q": q_current}

def main():
    filter_app = PrincipalAxesFilter()
    filter_app.run()

if __name__ == "__main__":
    main()
