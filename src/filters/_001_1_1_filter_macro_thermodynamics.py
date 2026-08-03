#!/usr/bin/env python3
# ==========================================
# _001_1_1_filter_macro_thermodynamics.py
# TLU System: Macro Thermodynamics Filter
# Version: 8.0.0 (Refactored with BaseFilter Architecture)
# ==========================================
import sys
import argparse
import numpy as np
import pandas as pd
from typing import List, Tuple, Dict, Any

from src.filters.base_filter import BaseFilter, HistoryBuffer
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
        v_history_window: List[np.ndarray], 
        X_history_window: List[np.ndarray],
        X_initial: np.ndarray,
        work_indices: List[int], 
        heat_indices: List[int]
) -> Tuple[List[list], np.ndarray, np.ndarray]:
    """!
    @brief [Pure Orchestration Function] Execute macro thermodynamic bounds.
    @details Legacy interface retained for backward compatibility with integration tests.
    """
    v_current = compute_net_flux(T_slice)
    
    if len(X_history_window) == 0:
        X_current = X_initial + v_current
    else:
        X_current = X_history_window[-1] + v_current

    U = compute_internal_energy(X_current)
    temp_X_hist = np.array(X_history_window + [X_current])

    W = compute_work(v_current, work_indices)
    Q_heat = compute_heat(v_current, heat_indices)

    P = compute_transition_matrix(T_slice)
    S = compute_macro_entropy(P)

    if len(temp_X_hist) > 1:
        T = compute_macro_temperature(temp_X_hist)
    else:
        T = 0.0

    gradT = 0.0
    F = compute_helmholtz_free_energy(U, T, S)

    record = [
        t_idx, 
        f"{U:.4f}", f"{S:.4f}", f"{T:.4f}", 
        f"{W:.4f}", f"{Q_heat:.4f}", f"{gradT:.4f}", f"{F:.4f}"
    ]
    
    return [record], v_current, X_current


class MacroThermodynamicsFilter(BaseFilter):
    cli_description = "TLU Macro Thermodynamics Filter"
    output_header = ["t_idx", "gross_activity_U", "entropy_S", "temperature_T", "work_W", "heat_Q", "grad_T", "free_energy_F"]
    history_config = {"X": 3, "v": 3}

    def add_arguments(self, parser: argparse.ArgumentParser):
        parser.add_argument("--temp_window", type=int, default=3, help="Time window width for temperature calculation")
        parser.add_argument("--work_labels", type=str, default="", help="Node labels considered as effective work (W)")
        parser.add_argument("--heat_labels", type=str, default="", help="Node labels considered as dissipated heat (Q)")

    def process_slice(
        self, 
        t_idx: int, 
        T_slice: np.ndarray, 
        history: HistoryBuffer,
        X_initial: np.ndarray,
        args: argparse.Namespace
    ) -> Tuple[List[List[Any]], Dict[str, np.ndarray]]:
        
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

        v_hist = history.get("v")
        X_hist = history.get("X")

        records, v_current, X_current = run_thermodynamics_analysis(
            t_idx, T_slice, v_hist, X_hist, X_initial, work_indices, heat_indices
        )

        state_updates = {
            "v": v_current,
            "X": X_current
        }

        return records, state_updates

def main():
    filter_app = MacroThermodynamicsFilter()
    filter_app.run()

if __name__ == "__main__":
    main()
