#!/usr/bin/env python3
# ==========================================
# _001_1_2_filter_local_thermodynamics.py
# TLU System: Local Thermodynamics Pipeline Filter
# ==========================================
import sys
import csv
import argparse
import numpy as np
from typing import List, Tuple

from src.filters.cli_parser import get_base_parser
from src.filters.stream_processor import setup_pipeline, yield_time_slices

from src.core.core_tensor_ops import compute_net_flux, compute_transition_matrix
from src.core.core_information_geometry import compute_shannon_entropy
from src.core.core_thermodynamics import (
    compute_local_internal_energy,
    compute_local_temperature
)

def run_local_thermo_analysis(
        t_idx: int, 
        T_slice: np.ndarray, 
        q_history_window: List[np.ndarray]
) -> Tuple[List[list], np.ndarray]:
    """!
    @brief [Pure Orchestration Function] Run local thermodynamic bounds.
    @details Tracks individual structural node energy balances isolating scalar interactions.

    @param t_idx Current temporal state map sequence.
    @param T_slice Total graph transition matrix.
    @param q_history_window Historical tensor tracking pure flux vector shifts.

    @return Tuple (Flattened record list, raw generic flux).

    @pre
        - Variables dynamically match topological constants N.
    @post
        - Synthesizes absolute energy bounds securely discarding context dependencies.
    @invariant
        - Temperature enforces statistical baseline variance metrics bounded physically per node.
    """
    N = T_slice.shape[0]

    # 1. Local internal energy u_i (Absolute activity)
    u_local = compute_local_internal_energy(T_slice)

    # 2. Local Shannon entropy s_i (Degree of dispersion)
    P_mat = compute_transition_matrix(T_slice)
    s_local = compute_shannon_entropy(P_mat)
    
    # 3. Local temperature t_i (Flux variance)
    q_current = compute_net_flux(T_slice)
    
    # Temporarily combine the current state for temperature calculation (assumes it will be popped by the caller)
    temp_q_hist = np.array(q_history_window + [q_current])
    
    if len(temp_q_hist) > 1:
        t_local = compute_local_temperature(temp_q_hist)
    else:
        t_local = np.zeros(N)

    # 4. Record format
    records = []
    for i in range(N):
        records.append([
            t_idx, i, 
            f"{u_local[i]:.4f}", f"{s_local[i]:.4f}", f"{t_local[i]:.4f}"
        ])

    return records, q_current

def main():
    parser = get_base_parser("TLU Local Thermodynamics Filter")
    parser.add_argument("--temp_window", type=int, default=3, help="Time window width for local temperature (volatility) calculation")
    
    output_header = ["t_idx", "node_idx", "local_internal_energy_u", "local_entropy_s", "local_temperature_t"]
    args, N, reader, writer = setup_pipeline(parser, output_header)

    q_history_window = []

    for t_idx, T_slice in yield_time_slices(reader, N):
        records, q_current = run_local_thermo_analysis(
            t_idx, T_slice, q_history_window
        )
        
        # Safe update of history (Sliding window)
        q_history_window.append(q_current)
        if len(q_history_window) > args.temp_window:
            q_history_window.pop(0)
            
        for rec in records:
            writer.writerow(rec)

if __name__ == "__main__":
    main()
