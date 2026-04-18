#!/usr/bin/env python3
# ==========================================
# _001_2_filter_lag_matrix.py
# TLU System: Time-Lag (Cross-Correlation) Matrix Filter
# ==========================================
import sys
import argparse
import numpy as np
from typing import List

from src.filters.cli_parser import get_base_parser
from src.filters.stream_processor import setup_pipeline, yield_time_slices
from src.core.core_tensor_ops import compute_net_flux
from src.core.core_dynamics import compute_optimal_time_lag

def run_lag_matrix_analysis(q_history_list: List[np.ndarray], max_lag: int) -> List[list]:
    """!
    @brief [Pure Orchestration Function] Run correlation bounding arrays.
    @details Exposes lag constraints across independent dimensional combinations.

    @param q_history_list Complete history of sequentially bounded structural flux limits.
    @param max_lag Theoretical bound representing causality offset limit.

    @return Returns flattened array elements (src_idx, tgt_idx, optimal_lag, max_correlation).

    @pre
        - Elements correctly bounded geometrically matching constant target step bounds.
    @post
        - Strictly asserts causality variables within maximum index constraints.
    @invariant
        - Automatically asserts cross-covariance structures geometrically aligned in discrete time.
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
            
            # How much sig_B is delayed (lag) compared to sig_A, and the correlation coefficient at that time
            best_lag, max_corr = compute_optimal_time_lag(sig_A, sig_B, max_lag)
            
            # Exclude labels and return only pure indices and numerical values
            records.append([
                i, j, best_lag, f"{max_corr:.4f}"
            ])
            
    return records

def main():
    parser = get_base_parser("TLU Full Matrix Time-Lag Filter")
    parser.add_argument("--max_lag", type=int, default=6, help="Maximum time lag to search (number of steps)")
    
    output_header = ["src_idx", "tgt_idx", "optimal_lag", "max_correlation"]
    args, N, reader, writer = setup_pipeline(parser, output_header)

    q_history_list = []
    
    # 1. Accumulate pure flux for the entire period from the stream
    for _, T_slice in yield_time_slices(reader, N):
        q_current = compute_net_flux(T_slice)
        q_history_list.append(q_current)

    # 2. After all data is collected, calculate the N x N correlation matrix in one go
    records = run_lag_matrix_analysis(q_history_list, args.max_lag)

    # 3. Output the result
    for rec in records:
        writer.writerow(rec)

if __name__ == "__main__":
    main()
