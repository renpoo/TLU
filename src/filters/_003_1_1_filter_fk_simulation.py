#!/usr/bin/env python3
# ==========================================
# _003_1_1_filter_fk_simulation.py
# TLU System: Forward Kinematics (FK) Simulation Filter
# ==========================================
import sys
import csv
import argparse
import numpy as np
import pandas as pd
from typing import List, Tuple

from src.filters.cli_parser import get_base_parser
from src.filters.stream_processor import setup_pipeline, yield_time_slices

import src.core.core_kinematics as ck
import src.core.core_tensor_ops as cto

def run_fk_analysis(
        t_idx: int, 
        T_slice: np.ndarray, 
        q_history: List[np.ndarray],
        fk_input_mode: str, 
        static_dq_input: np.ndarray,
        gamma: float, 
        max_k: int
) -> Tuple[List[list], np.ndarray]:
    """!
    @brief [Pure Orchestration Function] Apply wave propagation bounds using initial impulses.
    @details Aggregates unrolled finite echo dynamics modeling theoretical step constraints over pure flux.

    @param t_idx Execution bounded step index sequence.
    @param T_slice Extracted temporal baseline flux domain.
    @param q_history Absolute mapping historical tracker array slice.
    @param fk_input_mode Behavioral enum parameter explicit logic limit flag.
    @param static_dq_input Parameter explicit static base state injection bounds.
    @param gamma Extinction variable dampening numerical step bounds.
    @param max_k Numerical bounds limit representing discrete physical limits.

    @return Tuple (Structured node impact values layout array, Unbounded current raw mapping limits vector).

    @pre
        - Function parameter models strictly bound string choices against expected internal conditional structures logically correctly.
    @post
        - Unconditionally yields analytical approximations simulating structural wave bounds dynamically scaling inputs correctly.
    @invariant
        - Ensures spatial mappings analytically decay exponentially limiting structural variance perfectly safely within theoretical limitations.
    """    
    N = T_slice.shape[0]
    records = []

    q_current = cto.compute_net_flux(T_slice)
    P_current = cto.compute_transition_matrix(T_slice)
    
    if fk_input_mode == 'static':
        current_input_dq = static_dq_input
    elif fk_input_mode == 'actual':
        current_input_dq = q_current
    elif fk_input_mode == 'impulse':
        if len(q_history) > 0:
            q_baseline = np.mean(q_history, axis=0)
            current_input_dq = q_current - q_baseline
        else:
            current_input_dq = np.zeros(N)
    else:
        current_input_dq = np.zeros(N)

    echo_impact_dq = ck.run_forward_simulation(P_current, current_input_dq, gamma, max_k)

    for i in range(N):
        records.append([t_idx, i, f"{echo_impact_dq[i]:.4f}"])
        
    return records, q_current

def main():
    parser = get_base_parser("TLU Forward Kinematics (FK) Simulation Filter")
    parser.add_argument("--fk_input_mode", type=str, choices=['static', 'actual', 'impulse'], default="static")
    parser.add_argument("--static_dq_labels", type=str, default="", help="Format: 'Label:Value,Label:Value'")
    parser.add_argument("--gamma", type=float, default=0.85)
    parser.add_argument("--max_k", type=int, default=5)
    parser.add_argument("--history_window", type=int, default=100)
    
    output_header = ["t_idx", "node_idx", "fk_echo_impact"]
    args, N, reader, writer = setup_pipeline(parser, output_header)
    
    # [Domain resolution at I/O layer] Generate numerical array from string using the latest _node_map.csv
    static_dq_arr = np.zeros(N)
    if args.static_dq_labels:
        try:
            df_map = pd.read_csv(args.node_map)
            label_to_idx = dict(zip(df_map['node_label'], df_map['node_idx']))
            for pair in args.static_dq_labels.split(','):
                if ':' in pair:
                    lbl, val = pair.split(':', 1)
                    lbl = lbl.strip()
                    if lbl in label_to_idx:
                        idx = int(label_to_idx[lbl])
                        if idx < N:
                            static_dq_arr[idx] = float(val)
        except Exception as e:
            print(f"[WARN] Failed to parse labels: {e}", file=sys.stderr)

    q_history_window = []

    for t_idx, T_slice in yield_time_slices(reader, N):
        records, q_current = run_fk_analysis(
            t_idx=t_idx, T_slice=T_slice, q_history=q_history_window,
            fk_input_mode=args.fk_input_mode, static_dq_input=static_dq_arr,
            gamma=args.gamma, max_k=args.max_k
        )
        
        q_history_window.append(q_current)
        if len(q_history_window) > args.history_window:
            q_history_window.pop(0)
        
        for rec in records:
            writer.writerow(rec)

if __name__ == "__main__":
    main()
