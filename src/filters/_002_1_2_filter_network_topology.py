#!/usr/bin/env python3
# ==========================================
# _002_1_2_filter_network_topology.py
# TLU System: Network Topology & Edge Stress Filter
# ==========================================
import sys
import argparse
import numpy as np
from typing import List, Tuple

from src.filters.cli_parser import get_base_parser
from src.filters.stream_processor import setup_pipeline, yield_time_slices
from src.core.core_topology import compute_edge_stress

def run_network_topology_analysis(
        t_idx: int, 
        T_slice: np.ndarray, 
        T_history_window: List[np.ndarray]
) -> List[list]:
    """!
    @brief [Pure Orchestration Function] Run network topology analysis.
    @details Determines sparse edge configurations tracking spatial stress limits.

    @param t_idx Sequence temporal index.
    @param T_slice Transaction layout matrix bounds.
    @param T_history_window Array list of tensors framing memory offsets.

    @return Aggregated edge list formatted for I/O routing.

    @pre
        - T_history_window holds correctly sized matrix structures.
    @post
        - Unconditionally filters entirely zero-weighted interactions conserving memory bounds securely.
    @invariant
        - Calculates uncoupled pure bounds preserving structural density.
    """
    N = T_slice.shape[0]
    
    # Calculate edge stress (Z-score)
    stress_matrix = compute_edge_stress(T_slice, T_history_window)
    
    records = []
    # Extract only edges with transaction (weight) greater than zero for all node pairs
    for i in range(N):
        for j in range(N):
            weight = T_slice[i, j]
            if weight > 0:
                stress = stress_matrix[i, j]
                # Output format: [t_idx, src_idx, tgt_idx, weight, stress]
                records.append([
                    t_idx, i, j, 
                    f"{weight:.4f}", f"{stress:.4f}"
                ])
                
    return records

def main():
    parser = get_base_parser("TLU Network Topology & Edge Stress Filter")
    parser.add_argument("--baseline_window", type=int, default=12, help="Baseline period for stress calculation")
    
    output_header = ["t_idx", "src_idx", "tgt_idx", "weight", "stress"]
    args, N, reader, writer = setup_pipeline(parser, output_header)

    T_history_window = []

    for t_idx, T_slice in yield_time_slices(reader, N):
        records = run_network_topology_analysis(t_idx, T_slice, T_history_window)
        
        # Safe update of history
        T_history_window.append(T_slice.copy())
        if len(T_history_window) > args.baseline_window:
            T_history_window.pop(0)
            
        for rec in records:
            writer.writerow(rec)

if __name__ == "__main__":
    main()
