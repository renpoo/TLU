#!/usr/bin/env python3
# ==========================================
# _004_2_1_filter_sensitivity.py
# TLU System: Meta-Analysis Layer (Sensitivity & Trade-off Matrix)
# Version: 8.0.0 (Refactored with BaseFilter Architecture)
# ==========================================
import sys
import argparse
import numpy as np
from typing import List, Tuple, Dict, Any

from src.filters.base_filter import BaseFilter, HistoryBuffer
import src.core.core_kinematics as ck
import src.core.core_tensor_ops as cto
import src.core.core_safe_linalg as csl

def run_sensitivity_analysis(
        t_idx: int, 
        T_slice: np.ndarray, 
        q_history: List[np.ndarray],
        delta: float,
        gamma: float, 
        max_k: int
) -> Tuple[List[list], np.ndarray]:
    """!
    @brief [Pure Orchestration Function] Exert sensitivity test mapping across exhaustive network domains.
    @details Legacy interface retained for backward compatibility with integration tests.
    """    
    N = T_slice.shape[0]
    records = []

    q_current = cto.compute_net_flux(T_slice)
    P_current = cto.compute_transition_matrix(T_slice)
    M_echo = ck.build_echo_matrix(P_current, gamma, max_k)
    
    temp_history = q_history + [q_current]
    q_hist_arr = np.array(temp_history)
    if len(q_hist_arr) > 2:
        dq_history = np.diff(q_hist_arr, axis=0)
        covariance = csl.compute_covariance_matrix(dq_history)
        K_safe = csl.compute_safe_pinv(covariance, rcond=csl.DEFAULT_RCOND, lambda_reg=csl.DEFAULT_LAMBDA_REG)
    else:
        K_safe = np.eye(N)

    for i in range(N):
        static_dq = np.zeros(N)
        static_dq[i] = delta
        echo_impact = ck.run_forward_simulation(P_current, static_dq, gamma, max_k)
        
        fk_total_ripple = np.sum(np.abs(echo_impact))
        fk_impact_others = np.copy(echo_impact)
        fk_impact_others[i] = 0.0
        fk_max_node = int(np.argmax(np.abs(fk_impact_others)))
        fk_max_impact = fk_impact_others[fk_max_node]

        J = M_echo[:, [i]].T 
        dq_opt = ck.solve_ik_with_safe_stiffness(J, K_safe, [delta], lambda_ratio=1e-4)
        
        strain_energy = 0.5 * np.dot(dq_opt.T, np.dot(K_safe, dq_opt))
        ik_adjust_others = np.copy(dq_opt)
        ik_adjust_others[i] = 0.0
        ik_max_node = int(np.argmax(np.abs(ik_adjust_others)))
        ik_max_adjust = ik_adjust_others[ik_max_node]

        records.append([
            t_idx, i, 
            f"{fk_total_ripple:.4f}", f"{fk_max_impact:.4f}", fk_max_node,
            f"{strain_energy:.4f}", f"{ik_max_adjust:.4f}", ik_max_node
        ])
        
    return records, q_current


class SensitivityFilter(BaseFilter):
    cli_description = "TLU Sensitivity & Trade-off Meta-Filter"
    output_header = [
        "t_idx", "node_idx", 
        "fk_total_ripple", "fk_max_impact", "fk_max_impact_node",
        "ik_strain_energy", "ik_max_adjust", "ik_max_adjust_node"
    ]
    history_config = {"q": 100}

    def add_arguments(self, parser: argparse.ArgumentParser):
        parser.add_argument("--delta", type=float, default=10.0, help="Virtual investment amount")
        parser.add_argument("--gamma", type=float, default=0.85)
        parser.add_argument("--max_k", type=int, default=5)
        parser.add_argument("--history_window", type=int, default=100)

    def process_slice(
        self, 
        t_idx: int, 
        T_slice: np.ndarray, 
        history: HistoryBuffer,
        X_initial: np.ndarray,
        args: argparse.Namespace
    ) -> Tuple[List[List[Any]], Dict[str, np.ndarray]]:
        
        q_hist = history.get("q")
        records, q_current = run_sensitivity_analysis(
            t_idx=t_idx, T_slice=T_slice, q_history=q_hist,
            delta=args.delta, gamma=args.gamma, max_k=args.max_k
        )

        return records, {"q": q_current}

def main():
    filter_app = SensitivityFilter()
    filter_app.run()

if __name__ == "__main__":
    main()
