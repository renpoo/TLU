#!/usr/bin/env python3
# ==========================================
# _004_1_2_filter_system_stability.py
# TLU System: System Stability (Poles) Filter
# Version: 8.0.0 (Refactored with BaseFilter Architecture)
# ==========================================
import sys
import argparse
import numpy as np
from typing import List, Tuple, Dict, Any

from src.filters.base_filter import BaseFilter, HistoryBuffer
from src.core.core_tensor_ops import compute_transition_matrix

def run_system_stability_analysis(
        t_idx: int, 
        T_slice: np.ndarray
) -> list:
    """!
    @brief [Pure Orchestration Function] Run System Stability (Spectral Radius) resolution.
    @details Legacy interface retained for backward compatibility with unit tests.
    """    
    N = T_slice.shape[0]
    records = []

    A_matrix = compute_transition_matrix(T_slice)
    eigenvalues = np.linalg.eigvals(A_matrix)
    magnitudes = np.abs(eigenvalues)
    spectral_radius = np.max(magnitudes) if len(magnitudes) > 0 else 0.0
    is_stable = 1 if spectral_radius <= 1.0 else 0

    records.append([
        t_idx, 
        f"{spectral_radius:.6f}",
        is_stable
    ])

    return records


class SystemStabilityFilter(BaseFilter):
    cli_description = "TLU System Stability Filter"
    output_header = ["t_idx", "spectral_radius", "is_stable"]

    def process_slice(
        self, 
        t_idx: int, 
        T_slice: np.ndarray, 
        history: HistoryBuffer,
        X_initial: np.ndarray,
        args: argparse.Namespace
    ) -> Tuple[List[List[Any]], Dict[str, np.ndarray]]:
        
        records = run_system_stability_analysis(
            t_idx=t_idx, 
            T_slice=T_slice
        )

        return records, {}

def main():
    filter_app = SystemStabilityFilter()
    filter_app.run()

if __name__ == "__main__":
    main()
