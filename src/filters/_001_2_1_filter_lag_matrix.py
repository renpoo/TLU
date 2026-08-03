#!/usr/bin/env python3
# ==========================================
# _001_2_1_filter_lag_matrix.py
# TLU System: Time-Lag (Cross-Correlation) Matrix Filter
# Version: 8.0.0 (Refactored with BaseFilter Architecture)
# ==========================================
import sys
import argparse
import numpy as np
from typing import List, Tuple, Dict, Any

from src.filters.base_filter import BaseFilter, HistoryBuffer, assert_valid_matrix
from src.filters.stream_processor import setup_pipeline, yield_time_slices
from src.core.core_tensor_ops import compute_net_flux
from src.core.core_dynamics import compute_optimal_time_lag

def run_lag_matrix_analysis(q_history_list: List[np.ndarray], max_lag: int) -> List[list]:
    """!
    @brief [Pure Orchestration Function] Run correlation bounding arrays.
    @details Legacy interface retained for backward compatibility with integration tests.
    """
    if not q_history_list:
        return []

    q_hist_arr = np.array(q_history_list)
    N = q_hist_arr.shape[1]
    
    records = []
    for i in range(N):
        for j in range(N):
            sig_A = q_hist_arr[:, i]
            sig_B = q_hist_arr[:, j]
            best_lag, max_corr = compute_optimal_time_lag(sig_A, sig_B, max_lag)
            records.append([
                i, j, best_lag, f"{max_corr:.4f}"
            ])
            
    return records


class LagMatrixFilter(BaseFilter):
    cli_description = "TLU Full Matrix Time-Lag Filter"
    output_header = ["src_idx", "tgt_idx", "optimal_lag", "max_correlation"]

    def add_arguments(self, parser: argparse.ArgumentParser):
        parser.add_argument("--max_lag", type=int, default=6, help="Maximum time lag to search")

    def run(self):
        args = self.parser.parse_args()
        args_res, N, reader, writer = setup_pipeline(self.parser, self.output_header)
        
        q_history_list = []
        for t_idx, T_slice in yield_time_slices(reader, N):
            assert_valid_matrix(T_slice, N)
            q_current = compute_net_flux(T_slice)
            q_history_list.append(q_current)

        records = run_lag_matrix_analysis(q_history_list, args.max_lag)
        formatted = self.format_records(records)
        for rec in formatted:
            writer.writerow(rec)

        sys.stdout.flush()

def main():
    filter_app = LagMatrixFilter()
    filter_app.run()

if __name__ == "__main__":
    main()
