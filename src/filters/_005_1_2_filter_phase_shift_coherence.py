#!/usr/bin/env python3
# ==========================================
# _005_1_2_filter_phase_shift_coherence.py
# TLU System: Phase Shift & Coherence Filter
# Version: 8.0.0 (Refactored with BaseFilter Architecture)
# ==========================================
import sys
import argparse
import numpy as np
import pandas as pd
from typing import List, Tuple, Dict, Any

from src.filters.base_filter import BaseFilter, HistoryBuffer, assert_valid_matrix
from src.filters.stream_processor import setup_pipeline, yield_time_slices
from src.core.core_signal_processing import compute_traversing_phase_shift

class PhaseShiftCoherenceFilter(BaseFilter):
    cli_description = "TLU Phase Shift & Coherence Filter"
    output_header = ["t_idx", "src_idx", "tgt_idx", "coherence", "phase_shift"]

    def add_arguments(self, parser: argparse.ArgumentParser):
        parser.add_argument('--target_freq', type=float, default=0.25, help="Target frequency to evaluate")
        parser.add_argument('--window_size', type=int, default=24, help="Size of the sliding window")
        parser.add_argument('--step_size', type=int, default=4, help="Step size for sliding window")

    def run(self):
        args = self.parser.parse_args()
        args_res, N, reader, writer = setup_pipeline(self.parser, self.output_header)
        
        flux_history = []
        t_indices = []
        for t_idx, T_slice in yield_time_slices(reader, N):
            assert_valid_matrix(T_slice, N)
            outflow = np.sum(T_slice, axis=1)
            inflow = np.sum(T_slice, axis=0)
            flux_history.append(outflow + inflow)
            t_indices.append(t_idx)

        if not flux_history:
            return

        flux_mat = np.array(flux_history)  # Time x Nodes
        t_min = t_indices[0] if t_indices else 0
        records = []

        for src in range(N):
            x = flux_mat[:, src]
            if len(x) < args.window_size or np.sum(x) == 0:
                continue
                
            for tgt in range(N):
                y = flux_mat[:, tgt]
                if np.sum(y) == 0:
                    continue
                    
                sub_t_indices, coherences, phase_shifts = compute_traversing_phase_shift(
                    x, y, args.window_size, args.step_size, args.target_freq
                )
                
                for step_t, c, p in zip(sub_t_indices, coherences, phase_shifts):
                    records.append([
                        step_t + t_min, src, tgt, c, p
                    ])

        formatted = self.format_records(records)
        for rec in formatted:
            writer.writerow(rec)

        sys.stdout.flush()

def main():
    filter_app = PhaseShiftCoherenceFilter()
    filter_app.run()

if __name__ == "__main__":
    main()
