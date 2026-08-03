#!/usr/bin/env python3
# ==========================================
# _002_1_3_filter_manifold_dimensionality.py
# TLU System: Manifold Dimensionality (SVD) Filter
# Version: 8.0.0 (Refactored with BaseFilter Architecture)
# ==========================================
import sys
import argparse
import numpy as np
from typing import List, Tuple, Dict, Any

from src.filters.base_filter import BaseFilter, HistoryBuffer

def run_manifold_dimensionality_analysis(
        t_idx: int, 
        T_slice: np.ndarray,
        top_k: int,
        threshold: float
) -> list:
    """!
    @brief [Pure Orchestration Function] Run Manifold Dimensionality (SVD) resolution.
    @details Legacy interface retained for backward compatibility with unit tests.
    """    
    N = T_slice.shape[0]
    records = []

    U, S, Vh = np.linalg.svd(T_slice, compute_uv=True)
    effective_rank = np.sum(S > threshold)
    total_s = np.sum(S)
    k_limit = min(top_k, N)
    
    for k in range(k_limit):
        s_val = S[k]
        ratio = s_val / total_s if total_s > threshold else 0.0
        records.append([
            t_idx, 
            k,
            f"{s_val:.6f}",
            f"{ratio:.6f}",
            effective_rank
        ])

    return records


class ManifoldDimensionalityFilter(BaseFilter):
    cli_description = "TLU Manifold Dimensionality Filter"
    output_header = ["t_idx", "component_idx", "singular_value", "explained_ratio", "effective_rank"]

    def add_arguments(self, parser: argparse.ArgumentParser):
        parser.add_argument("--top_k", type=int, default=5, help="Number of top singular values to extract")

    def process_slice(
        self, 
        t_idx: int, 
        T_slice: np.ndarray, 
        history: HistoryBuffer,
        X_initial: np.ndarray,
        args: argparse.Namespace
    ) -> Tuple[List[List[Any]], Dict[str, np.ndarray]]:
        
        records = run_manifold_dimensionality_analysis(
            t_idx=t_idx, 
            T_slice=T_slice,
            top_k=args.top_k,
            threshold=args.thresh_manifold_svd
        )

        return records, {}

def main():
    filter_app = ManifoldDimensionalityFilter()
    filter_app.run()

if __name__ == "__main__":
    main()
