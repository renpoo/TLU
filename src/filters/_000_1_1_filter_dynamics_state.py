#!/usr/bin/env python3
# ==========================================
# _000_1_1_filter_dynamics_state.py
# TLU System: Dynamics State Pipeline Filter
# ==========================================
import sys
import csv
import argparse
import numpy as np
from typing import List, Tuple

from src.filters.cli_parser import get_base_parser
from src.filters.stream_processor import setup_pipeline, yield_time_slices
from src.core.core_tensor_ops import compute_net_flux
from src.core.core_kinematics import compute_derivatives
from src.core.core_dynamics import estimate_virtual_mass_and_viscosity, compute_external_force_residual

def run_dynamics_state_analysis(
        t_idx: int, 
        T_slice: np.ndarray, 
        q_history: List[np.ndarray], 
        v_history: List[np.ndarray]
) -> Tuple[List[list], np.ndarray, np.ndarray]:
    """ [Pure Orchestration Function] """
    N = T_slice.shape[0]
    
    # 1. Current pure flux (this becomes q in phase space)
    q_current = compute_net_flux(T_slice)
    
    temp_q_hist = np.array(q_history + [q_current])
    
    # 2. Velocity v and Acceleration a
    v_current, a_current = compute_derivatives(temp_q_hist)
    temp_v_hist = np.array(v_history + [v_current])
    
    # 3. Virtual mass M and Viscosity C
    M, C = estimate_virtual_mass_and_viscosity(temp_q_hist, temp_v_hist, base_epsilon=1e-10, velocity_scale_ratio=0.1)

    # 4. External input (F_ext)
    K = np.zeros(N, dtype=float)
    dq = np.zeros(N, dtype=float)
    F_ext = compute_external_force_residual(M, C, K, a_current, v_current, dq)

    # 5. Record format (added net_flux_q)
    records = []
    for i in range(N):
        records.append([
            t_idx, i, 
            f"{q_current[i]:.4f}",  # <--- Added: Absolute coordinates (position) in phase space
            f"{v_current[i]:.4f}", 
            f"{a_current[i]:.4f}", 
            f"{M[i]:.4f}", 
            f"{C[i]:.4f}", 
            f"{F_ext[i]:.4f}"
        ])
    
    return records, q_current, v_current

def main():
    parser = get_base_parser("TLU Dynamics State Filter")
    parser.add_argument("--history_window", type=int, default=100)
    
    # Added to header as well
    output_header = ["t_idx", "node_idx", "net_flux_q", "velocity_v", "acceleration_a", "inertia_M", "viscosity_C", "external_force_F"]
    args, N, reader, writer = setup_pipeline(parser, output_header)

    q_history_window = []
    v_history_window = []

    for t_idx, T_slice in yield_time_slices(reader, N):
        records, q_current, v_current = run_dynamics_state_analysis(
            t_idx, T_slice, q_history_window, v_history_window
        )
        
        q_history_window.append(q_current)
        v_history_window.append(v_current)
        if len(q_history_window) > args.history_window:
            q_history_window.pop(0)
            v_history_window.pop(0)
            
        for rec in records:
            writer.writerow(rec)

if __name__ == "__main__":
    main()
