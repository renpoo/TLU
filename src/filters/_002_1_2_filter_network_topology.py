#!/usr/bin/env python3
# ==========================================
# _002_1_2_filter_network_topology.py
# TLU System: Network Topology & Edge Stress Filter
# Version: 8.0.0 (Refactored with BaseFilter Architecture)
# ==========================================
import sys
import argparse
import numpy as np
from typing import List, Tuple, Dict, Any

from src.filters.base_filter import BaseFilter, HistoryBuffer
from src.core.core_topology import compute_edge_stress

def run_network_topology_analysis(
        t_idx: int, 
        T_slice: np.ndarray, 
        T_history_window: List[np.ndarray]
) -> List[list]:
    """!
    @brief [Pure Orchestration Function] Run network topology analysis.
    @details Legacy interface retained for backward compatibility with integration tests.
    """
    N = T_slice.shape[0]
    stress_matrix = compute_edge_stress(T_slice, T_history_window)
    
    records = []
    for i in range(N):
        for j in range(N):
            weight = T_slice[i, j]
            if weight > 0:
                stress = stress_matrix[i, j]
                records.append([
                    t_idx, i, j, 
                    f"{weight:.4f}", f"{stress:.4f}"
                ])
                
    return records


class NetworkTopologyFilter(BaseFilter):
    cli_description = "TLU Network Topology & Edge Stress Filter"
    output_header = ["t_idx", "src_idx", "tgt_idx", "weight", "stress"]
    history_config = {"T": 12}

    def add_arguments(self, parser: argparse.ArgumentParser):
        parser.add_argument("--baseline_window", type=int, default=12, help="Baseline period for stress calculation")

    def process_slice(
        self, 
        t_idx: int, 
        T_slice: np.ndarray, 
        history: HistoryBuffer,
        X_initial: np.ndarray,
        args: argparse.Namespace
    ) -> Tuple[List[List[Any]], Dict[str, np.ndarray]]:
        
        T_hist = history.get("T")
        records = run_network_topology_analysis(t_idx, T_slice, T_hist)

        return records, {"T": T_slice.copy()}

def main():
    filter_app = NetworkTopologyFilter()
    filter_app.run()

if __name__ == "__main__":
    main()
