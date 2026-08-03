#!/usr/bin/env python3
# ==========================================
# _002_1_1_filter_info_curvature.py
# TLU System: Information Curvature Pipeline Filter
# Version: 8.0.0 (Refactored with BaseFilter Architecture)
# ==========================================
import sys
import argparse
import numpy as np
from typing import List, Tuple, Dict, Any

from src.filters.base_filter import BaseFilter, HistoryBuffer
from src.core.core_tensor_ops import compute_net_flux
from src.core.core_information_geometry import (
    compute_information_curvature, 
    compute_information_density
)

def run_info_curvature_analysis(
        t_idx: int, 
        T_slice: np.ndarray, 
        q_history_window: List[np.ndarray]
) -> Tuple[List[list], np.ndarray]:
    """!
    @brief [Pure Orchestration Function] Extract local information curvature dynamics.
    @details Legacy interface retained for backward compatibility with integration tests.
    """
    N = T_slice.shape[0]
    q_current = compute_net_flux(T_slice)
    temp_hist = np.array(q_history_window + [q_current])
    
    curvature_vec = compute_information_curvature(temp_hist)
    density_vec = compute_information_density(T_slice)
    
    records = []
    for i in range(N):
        records.append([
            t_idx, i, 
            f"{curvature_vec[i]:.6f}", 
            f"{density_vec[i]:.4f}"
        ])
        
    return records, q_current


class InformationCurvatureFilter(BaseFilter):
    cli_description = "TLU Information Curvature Filter"
    output_header = ["t_idx", "node_idx", "curvature", "density"]
    history_config = {"q": 3}

    def add_arguments(self, parser: argparse.ArgumentParser):
        parser.add_argument("--window", type=int, default=3, help="Time window width for curvature calculation")

    def process_slice(
        self, 
        t_idx: int, 
        T_slice: np.ndarray, 
        history: HistoryBuffer,
        X_initial: np.ndarray,
        args: argparse.Namespace
    ) -> Tuple[List[List[Any]], Dict[str, np.ndarray]]:
        
        q_hist = history.get("q")
        records, q_current = run_info_curvature_analysis(t_idx, T_slice, q_hist)

        return records, {"q": q_current}

def main():
    filter_app = InformationCurvatureFilter()
    filter_app.run()

if __name__ == "__main__":
    main()
