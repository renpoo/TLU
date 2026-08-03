#!/usr/bin/env python3
# ==========================================
# _000_1_1_filter_dynamics_state.py
# TLU System: Dynamics State Pipeline Filter
# Version: 8.0.0 (Refactored with BaseFilter Architecture)
# ==========================================
import sys
import argparse
import numpy as np
from typing import List, Tuple, Dict, Any

from src.filters.base_filter import BaseFilter, HistoryBuffer
from src.core.core_tensor_ops import compute_net_flux
from src.core.core_kinematics import compute_derivatives, compute_higher_order_derivatives
from src.core.core_dynamics import estimate_virtual_mass_and_viscosity, compute_external_force_residual

def run_dynamics_state_analysis(
        t_idx: int, 
        T_slice: np.ndarray, 
        X_history: List[np.ndarray], 
        v_history: List[np.ndarray],
        X_initial: np.ndarray
) -> Tuple[List[list], np.ndarray, np.ndarray]:
    """!
    @brief [Pure Orchestration Function] Run dynamics state analysis.
    @details Legacy interface retained for backward compatibility with integration tests.
    """
    N = T_slice.shape[0]
    
    # 1. Current pure flux (velocity v)
    v_current = compute_net_flux(T_slice)
    temp_v_hist = np.array(v_history + [v_current])
    
    # Calculate Absolute Balance X
    if len(X_history) == 0:
        X_current = X_initial + v_current
    else:
        X_current = X_history[-1] + v_current
        
    temp_X_hist = np.array(X_history + [X_current])
    
    # 2. Acceleration a, Jerk j, Snap s
    v_latest, a_current = compute_derivatives(temp_v_hist)
    jerk_current, snap_current = compute_higher_order_derivatives(temp_v_hist)
    
    # 3. Virtual mass M and Viscosity C
    M, C = estimate_virtual_mass_and_viscosity(temp_X_hist, damping_ratio=0.1)

    # 4. External input (F_ext)
    K = np.zeros(N, dtype=float)
    dq = np.zeros(N, dtype=float)
    F_ext = compute_external_force_residual(M, C, K, a_current, v_current, dq)

    # 5. Record format
    records = []
    for i in range(N):
        records.append([
            t_idx, i, 
            f"{X_current[i]:.4f}", 
            f"{v_current[i]:.4f}", 
            f"{a_current[i]:.4f}", 
            f"{jerk_current[i]:.4f}",
            f"{snap_current[i]:.4f}",
            f"{M[i]:.4f}", 
            f"{C[i]:.4f}", 
            f"{F_ext[i]:.4f}"
        ])
    
    return records, X_current, v_current


class DynamicsStateFilter(BaseFilter):
    cli_description = "TLU Dynamics State Filter"
    output_header = ["t_idx", "node_idx", "state_X", "velocity_v", "acceleration_a", "jerk_j", "snap_s", "inertia_M", "viscosity_C", "external_force_F"]
    history_config = {"X": 100, "v": 100}

    def add_arguments(self, parser: argparse.ArgumentParser):
        parser.add_argument("--history_window", type=int, default=100, help="History sliding window size")

    def process_slice(
        self, 
        t_idx: int, 
        T_slice: np.ndarray, 
        history: HistoryBuffer,
        X_initial: np.ndarray,
        args: argparse.Namespace
    ) -> Tuple[List[List[Any]], Dict[str, np.ndarray]]:
        
        X_hist = history.get("X")
        v_hist = history.get("v")

        records, X_current, v_current = run_dynamics_state_analysis(
            t_idx, T_slice, X_hist, v_hist, X_initial
        )

        state_updates = {
            "X": X_current,
            "v": v_current
        }

        return records, state_updates

def main():
    filter_app = DynamicsStateFilter()
    filter_app.run()

if __name__ == "__main__":
    main()
