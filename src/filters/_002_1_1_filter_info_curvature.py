#!/usr/bin/env python3
# ==========================================
# _002_1_1_filter_info_curvature.py
# TLU System: Information Curvature Pipeline Filter
# ==========================================
import sys
import argparse
import numpy as np
from typing import List, Tuple

from src.filters.cli_parser import get_base_parser
from src.filters.stream_processor import setup_pipeline, yield_time_slices

from src.core.core_tensor_ops import compute_net_flux
from src.core.core_information_geometry import (
    compute_information_curvature, 
    compute_information_density
)

def run_info_curvature_analysis(
        t_idx: int, 
        T_slice: np.ndarray, 
        q_history_window: List[np.ndarray]
) -> Tuple[List[list], np.ndarray]:
    """!
    @brief [Pure Orchestration Function] Extract local information curvature dynamics.
    @details Evaluates spatial bounds analyzing pure state density shifts per structure.

    @param t_idx Coordinate sequence index.
    @param T_slice Current transition tensor boundary slice.
    @param q_history_window Chronological arrays tracking pure unrolled dynamics.

    @return Tuple (Flattened record tuples, Generic physical net flux array).

    @pre
        - Structural parameters safely ordered minimizing memory state mutation.
    @post
        - Enforces strict geometry isolating explicit metrics without context coupling.
    @invariant
        - Preserves strict independence calculating local acceleration boundaries correctly.
    """
    N = T_slice.shape[0]
    
    # 1. Calculate the latest pure flux
    q_current = compute_net_flux(T_slice)
    
    # Create a temporary history including the current state for curvature calculation
    temp_hist = np.array(q_history_window + [q_current])
    
    # 2. Calculate Curvature and Density
    curvature_vec = compute_information_curvature(temp_hist)
    density_vec = compute_information_density(T_slice)
    
    # 3. Record format (exclude labels and make it pure tensor data)
    records = []
    for i in range(N):
        records.append([
            t_idx, i, 
            f"{curvature_vec[i]:.6f}", 
            f"{density_vec[i]:.4f}"
        ])
        
    return records, q_current

def main():
    parser = get_base_parser("TLU Information Curvature Filter")
    parser.add_argument("--window", type=int, default=3, help="Time window width for curvature calculation (minimum 3)")
    
    output_header = ["t_idx", "node_idx", "curvature", "density"]
    args, N, reader, writer = setup_pipeline(parser, output_header)

    q_history_window = []

    for t_idx, T_slice in yield_time_slices(reader, N):
        records, q_current = run_info_curvature_analysis(
            t_idx, T_slice, q_history_window
        )
        
        # Safe update of history
        q_history_window.append(q_current)
        # Retain window size - 1, since the caller will append q_current to temp_hist
        if len(q_history_window) > max(args.window, 3) - 1:
            q_history_window.pop(0)
            
        for rec in records:
            writer.writerow(rec)

if __name__ == "__main__":
    main()
