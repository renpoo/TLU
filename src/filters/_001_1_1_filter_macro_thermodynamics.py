#!/usr/bin/env python3
# ==========================================
# _001_1_1_filter_macro_thermodynamics.py
# TLU System: Macro Thermodynamics Filter
# ==========================================
import sys
import csv
import argparse
import numpy as np
import pandas as pd
from typing import List, Tuple

from src.filters.cli_parser import get_base_parser
from src.filters.stream_processor import setup_pipeline, yield_time_slices

from src.core.core_thermodynamics import (
    compute_internal_energy,
    compute_work,
    compute_heat,
    compute_macro_entropy,
    compute_macro_temperature,
    compute_helmholtz_free_energy,
)
from src.core.core_tensor_ops import compute_net_flux, compute_transition_matrix

def run_thermodynamics_analysis(
        t_idx: int, 
        T_slice: np.ndarray, 
        q_history_window: List[np.ndarray], 
        work_indices: List[int], 
        heat_indices: List[int]
) -> Tuple[List[list], np.ndarray]:
    """ [Pure Orchestration Function] """
    # 1. Internal energy U (Total activity)
    U = compute_internal_energy(T_slice)
    
    # 2. Pure flux
    q_current = compute_net_flux(T_slice)
    
    # Temporarily combine the current state for temperature calculation (assumes it will be popped by the caller)
    temp_q_hist = np.array(q_history_window + [q_current])

    # 3. Effective work (W) and Dissipated heat (Q)
    W = compute_work(q_current, work_indices)
    Q_heat = compute_heat(q_current, heat_indices)

    # 4. Macro entropy S
    P = compute_transition_matrix(T_slice)
    S = compute_macro_entropy(P)

    # 5. Macro temperature T (Volatility)
    if len(temp_q_hist) > 1:
        T = compute_macro_temperature(temp_q_hist)
    else:
        T = 0.0

    # 6. Free energy F = U - TS
    gradT = 0.0 # Gradient is conceptually zero for macro indicators
    F = compute_helmholtz_free_energy(U, T, S)

    # Since it is an indicator for the entire network, output is only 1 row per time slice
    record = [
        t_idx, 
        f"{U:.4f}", f"{S:.4f}", f"{T:.4f}", 
        f"{W:.4f}", f"{Q_heat:.4f}", f"{gradT:.4f}", f"{F:.4f}"
    ]
    
    return [record], q_current

def main():
    parser = get_base_parser("TLU Macro Thermodynamics Filter")
    parser.add_argument("--temp_window", type=int, default=3, help="Time window width for temperature calculation")
    parser.add_argument("--work_labels", type=str, default="", help="Node labels considered as effective work (W) (e.g., 'ACC_Sales,ACC_Profit')")
    parser.add_argument("--heat_labels", type=str, default="", help="Node labels considered as dissipated heat (Q) (e.g., 'ACC_Waste,ACC_Loss')")
    
    output_header = ["t_idx", "gross_activity_U", "entropy_S", "temperature_T", "work_W", "heat_Q", "grad_T", "free_energy_F"]
    args, N, reader, writer = setup_pipeline(parser, output_header)

    # [Domain resolution at I/O layer] Extract index from string using the latest _node_map.csv
    work_indices = []
    heat_indices = []
    if args.work_labels or args.heat_labels:
        try:
            df_map = pd.read_csv(args.node_map)
            label_to_idx = dict(zip(df_map['node_label'], df_map['node_idx']))
            
            if args.work_labels:
                for lbl in args.work_labels.split(','):
                    lbl = lbl.strip()
                    if lbl in label_to_idx:
                        work_indices.append(int(label_to_idx[lbl]))
            
            if args.heat_labels:
                for lbl in args.heat_labels.split(','):
                    lbl = lbl.strip()
                    if lbl in label_to_idx:
                        heat_indices.append(int(label_to_idx[lbl]))
        except Exception as e:
            print(f"[WARN] Failed to parse labels: {e}", file=sys.stderr)

    q_history_window = []

    for t_idx, T_slice in yield_time_slices(reader, N):
        records, q_current = run_thermodynamics_analysis(
            t_idx, T_slice, q_history_window, work_indices, heat_indices
        )
        
        # Safe update of history (Sliding window)
        q_history_window.append(q_current)
        if len(q_history_window) > args.temp_window:
            q_history_window.pop(0)
            
        for rec in records:
            writer.writerow(rec)

if __name__ == "__main__":
    main()
