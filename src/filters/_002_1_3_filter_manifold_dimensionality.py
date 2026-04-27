#!/usr/bin/env python3
# ==========================================
# _002_1_3_filter_manifold_dimensionality.py
# TLU System: Manifold Dimensionality (SVD) Filter
# Version: 8.0.0 (Linear Algebra Extension)
# ==========================================
import sys
import argparse
import numpy as np
import pandas as pd

from src.filters.cli_parser import get_base_parser
from src.filters.stream_processor import setup_pipeline, yield_time_slices

def run_manifold_dimensionality_analysis(
        t_idx: int, 
        T_slice: np.ndarray,
        top_k: int,
        threshold: float
) -> list:
    """!
    @brief [Pure Orchestration Function] Run Manifold Dimensionality (SVD) resolution.
    @details Extracts the effective dimensionality (rank) of the transition manifold using SVD.

    @param t_idx Current evaluation time step.
    @param T_slice Current transition tensor (N x N).
    @param top_k Number of top singular values to output.

    @return Flattened records.
    """    
    N = T_slice.shape[0]
    records = []

    # Calculate Singular Value Decomposition
    # SVD works on any N x N matrix (symmetric or not)
    U, S, Vh = np.linalg.svd(T_slice, compute_uv=True)
    
    # S contains singular values in descending order
    # Calculate effective rank (number of singular values > threshold)
    effective_rank = np.sum(S > threshold)
    
    total_s = np.sum(S)
    
    k_limit = min(top_k, N)
    
    for k in range(k_limit):
        s_val = S[k]
        ratio = s_val / total_s if total_s > threshold else 0.0
        
        # We output left and right singular vectors' dominant nodes
        # To keep CSV flat and concise, we just output the singular value and ratio
        # If needed, full U and Vh could be output similar to PCA
        records.append([
            t_idx, 
            k,
            f"{s_val:.6f}",
            f"{ratio:.6f}",
            effective_rank
        ])

    return records

def main():
    parser = get_base_parser("TLU Manifold Dimensionality Filter")
    parser.add_argument("--top_k", type=int, default=5, help="Number of top singular values to extract")
    
    output_header = ["t_idx", "component_idx", "singular_value", "explained_ratio", "effective_rank"]
    args, N, reader, writer = setup_pipeline(parser, output_header)
    
    for t_idx, T_slice in yield_time_slices(reader, N):
        records = run_manifold_dimensionality_analysis(
            t_idx=t_idx, 
            T_slice=T_slice,
            top_k=args.top_k,
            threshold=args.thresh_manifold_svd
        )
        
        for rec in records:
            writer.writerow(rec)

if __name__ == "__main__":
    main()
