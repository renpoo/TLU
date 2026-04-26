#!/usr/bin/env python3
# ==========================================
# _004_1_2_filter_system_stability.py
# TLU System: System Stability (Poles) Filter
# Version: 8.0.0 (Linear Algebra Extension)
# ==========================================
import sys
import argparse
import numpy as np
import pandas as pd

from src.filters.cli_parser import get_base_parser
from src.filters.stream_processor import setup_pipeline, yield_time_slices

from src.core.core_tensor_ops import compute_transition_matrix

def run_system_stability_analysis(
        t_idx: int, 
        T_slice: np.ndarray
) -> list:
    """!
    @brief [Pure Orchestration Function] Run System Stability (Spectral Radius) resolution.
    @details Extracts the spectral radius (max absolute eigenvalue) of the transition matrix A to determine system stability.

    @param t_idx Current evaluation time step.
    @param T_slice Current transition tensor (N x N).

    @return Flattened records.
    """    
    N = T_slice.shape[0]
    records = []

    # Calculate Transition Matrix A
    A_matrix = compute_transition_matrix(T_slice)
    
    # Calculate eigenvalues
    # eigvals handles general (asymmetric) matrices
    eigenvalues = np.linalg.eigvals(A_matrix)
    
    # Calculate magnitudes (absolute values of complex eigenvalues)
    magnitudes = np.abs(eigenvalues)
    
    # Spectral radius is the maximum magnitude
    spectral_radius = np.max(magnitudes) if len(magnitudes) > 0 else 0.0
    
    # Check stability (if radius > 1.0, system is unstable/diverging)
    is_stable = 1 if spectral_radius <= 1.0 else 0

    records.append([
        t_idx, 
        f"{spectral_radius:.6f}",
        is_stable
    ])

    return records

def main():
    parser = get_base_parser("TLU System Stability Filter")
    
    output_header = ["t_idx", "spectral_radius", "is_stable"]
    args, N, reader, writer = setup_pipeline(parser, output_header)
    
    for t_idx, T_slice in yield_time_slices(reader, N):
        records = run_system_stability_analysis(
            t_idx=t_idx, 
            T_slice=T_slice
        )
        
        for rec in records:
            writer.writerow(rec)

if __name__ == "__main__":
    main()
