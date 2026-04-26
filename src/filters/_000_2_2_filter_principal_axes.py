#!/usr/bin/env python3
# ==========================================
# _000_2_2_filter_principal_axes.py
# TLU System: Principal Axes (PCA) Filter
# Version: 8.0.0 (Linear Algebra Extension)
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

def run_principal_axes_analysis(
        t_idx: int, 
        T_slice: np.ndarray, 
        q_history: List[np.ndarray],
        top_k: int
) -> Tuple[List[list], np.ndarray]:
    """!
    @brief [Pure Orchestration Function] Run Principal Axes (PCA) resolution.
    @details Extracts the dominant modes of variance (eigenvalues/eigenvectors) from the covariance matrix.

    @param t_idx Current evaluation time step.
    @param T_slice Current transition tensor.
    @param q_history Array of pure flux vectors temporal domain.
    @param top_k Number of top principal components to output.

    @return Tuple (Flattened records, current pure flux).
    """    
    N = T_slice.shape[0]
    records = []

    q_current = cto.compute_net_flux(T_slice)
    
    temp_history = q_history + [q_current]
    q_hist_arr = np.array(temp_history)

    if len(q_hist_arr) > 2:
        dq_history = np.diff(q_hist_arr, axis=0)
        covariance = csl.compute_covariance_matrix(dq_history)
        
        # Calculate eigenvalues and eigenvectors
        # eigh is used for symmetric matrices (like covariance)
        eigenvalues, eigenvectors = np.linalg.eigh(covariance)
        
        # Sort in descending order
        idx_sorted = np.argsort(eigenvalues)[::-1]
        eigenvalues = eigenvalues[idx_sorted]
        eigenvectors = eigenvectors[:, idx_sorted]
        
        # Calculate explained variance ratio
        total_variance = np.sum(np.maximum(eigenvalues, 0)) # prevent negative tiny noise
        
        # Limit to top_k components or N
        k_limit = min(top_k, N)
        
        for k in range(k_limit):
            eig_val = eigenvalues[k]
            # Safety for ratio if total_variance is 0
            ratio = eig_val / total_variance if total_variance > 1e-15 else 0.0
            
            for i in range(N):
                vec_val = eigenvectors[i, k]
                records.append([
                    t_idx, 
                    k,                  # component_idx (0 is 1st PC)
                    i,                  # node_idx
                    f"{eig_val:.6f}",
                    f"{ratio:.6f}",
                    f"{vec_val:.6f}"
                ])
    else:
        # Not enough history
        k_limit = min(top_k, N)
        for k in range(k_limit):
            for i in range(N):
                records.append([t_idx, k, i, "0.000000", "0.000000", "0.000000"])

    return records, q_current

def main():
    parser = get_base_parser("TLU Principal Axes Filter")
    parser.add_argument("--history_window", type=int, default=12, help="Length of history used for covariance calculation")
    parser.add_argument("--top_k", type=int, default=3, help="Number of top principal components to extract")
    
    output_header = ["t_idx", "component_idx", "node_idx", "eigenvalue", "explained_variance_ratio", "vector_value"]
    args, N, reader, writer = setup_pipeline(parser, output_header)
    
    q_history_window = []

    for t_idx, T_slice in yield_time_slices(reader, N):
        records, q_current = run_principal_axes_analysis(
            t_idx=t_idx, 
            T_slice=T_slice, 
            q_history=q_history_window,
            top_k=args.top_k
        )
        
        q_history_window.append(q_current)
        if len(q_history_window) > args.history_window:
            q_history_window.pop(0)
            
        for rec in records:
            writer.writerow(rec)

if __name__ == "__main__":
    main()
