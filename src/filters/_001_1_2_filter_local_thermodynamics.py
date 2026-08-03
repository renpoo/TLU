#!/usr/bin/env python3
# ==========================================
# _001_1_2_filter_local_thermodynamics.py
# TLU System: Local Thermodynamics Pipeline Filter
# Version: 8.0.0 (Refactored with BaseFilter Architecture)
# ==========================================
import sys
import argparse
import numpy as np
from typing import List, Tuple, Dict, Any

from src.filters.base_filter import BaseFilter, HistoryBuffer
from src.core.core_tensor_ops import compute_net_flux, compute_transition_matrix
from src.core.core_information_geometry import compute_shannon_entropy
from src.core.core_thermodynamics import (
    compute_local_internal_energy,
    compute_local_temperature,
    compute_local_temperature_gradient
)

def run_local_thermo_analysis(
        t_idx: int, 
        T_slice: np.ndarray, 
        v_history_window: List[np.ndarray],
        X_history_window: List[np.ndarray],
        X_initial: np.ndarray
) -> Tuple[List[list], np.ndarray, np.ndarray]:
    """!
    @brief [Pure Orchestration Function] Run local thermodynamic bounds.
    @details Legacy interface retained for backward compatibility with integration tests.
    """
    N = T_slice.shape[0]

    P_mat = compute_transition_matrix(T_slice)
    s_local = compute_shannon_entropy(P_mat)
    
    v_current = compute_net_flux(T_slice)
    
    if len(X_history_window) == 0:
        X_current = X_initial + v_current
    else:
        X_current = X_history_window[-1] + v_current

    u_local = compute_local_internal_energy(X_current)
    temp_X_hist = np.array(X_history_window + [X_current])
    
    if len(temp_X_hist) > 1:
        t_local = compute_local_temperature(temp_X_hist)
    else:
        t_local = np.zeros(N)

    grad_t_local = compute_local_temperature_gradient(t_local, T_slice)

    records = []
    for i in range(N):
        records.append([
            t_idx, i, 
            f"{u_local[i]:.4f}", f"{s_local[i]:.4f}", f"{t_local[i]:.4f}", f"{grad_t_local[i]:.4f}"
        ])

    return records, v_current, X_current


class LocalThermodynamicsFilter(BaseFilter):
    cli_description = "TLU Local Thermodynamics Filter"
    output_header = ["t_idx", "node_idx", "local_internal_energy_u", "local_entropy_s", "local_temperature_t", "local_grad_t"]
    history_config = {"v": 3, "X": 3}

    def add_arguments(self, parser: argparse.ArgumentParser):
        parser.add_argument("--temp_window", type=int, default=3, help="Time window width for local temperature calculation")

    def process_slice(
        self, 
        t_idx: int, 
        T_slice: np.ndarray, 
        history: HistoryBuffer,
        X_initial: np.ndarray,
        args: argparse.Namespace
    ) -> Tuple[List[List[Any]], Dict[str, np.ndarray]]:
        
        v_hist = history.get("v")
        X_hist = history.get("X")

        records, v_current, X_current = run_local_thermo_analysis(
            t_idx, T_slice, v_hist, X_hist, X_initial
        )

        return records, {"v": v_current, "X": X_current}

def main():
    filter_app = LocalThermodynamicsFilter()
    filter_app.run()

if __name__ == "__main__":
    main()
