#!/usr/bin/env python3
# ==========================================
# _005_1_1_filter_resonant_frequency.py
# TLU System: Resonant Frequency Pipeline Filter
# Version: 8.0.0 (Refactored with BaseFilter Architecture)
# ==========================================
import sys
import argparse
import numpy as np
import pandas as pd
from typing import List, Tuple, Dict, Any

from src.filters.base_filter import BaseFilter, HistoryBuffer, assert_valid_matrix
from src.filters.stream_processor import setup_pipeline, yield_time_slices
from src.core.core_signal_processing import compute_resonant_frequency

class ResonantFrequencyFilter(BaseFilter):
    cli_description = "TLU Resonant Frequency Filter"
    output_header = ["node_idx", "dominant_frequency", "spectral_power"]

    def add_arguments(self, parser: argparse.ArgumentParser):
        parser.add_argument('--max_tau', type=int, default=12, help="Maximum lag (tau) for correlation / window size")

    def run(self):
        args = self.parser.parse_args()
        args_res, N, reader, writer = setup_pipeline(self.parser, self.output_header)
        
        flux_history = []
        for t_idx, T_slice in yield_time_slices(reader, N):
            assert_valid_matrix(T_slice, N)
            outflow = np.sum(T_slice, axis=1)
            inflow = np.sum(T_slice, axis=0)
            flux_history.append(outflow + inflow)

        if not flux_history:
            return

        flux_mat = np.array(flux_history)  # Time x Nodes
        records = []
        for node in range(N):
            flux_series = flux_mat[:, node]
            if len(flux_series) < 2 or np.sum(flux_series) == 0:
                records.append([node, 0.0, 0.0])
                continue
                
            freq, power = compute_resonant_frequency(flux_series, max_tau=args.max_tau)
            records.append([node, freq, power])

        # Sort by power descending
        records.sort(key=lambda r: r[2], reverse=True)

        formatted = self.format_records(records)
        for rec in formatted:
            writer.writerow(rec)

        sys.stdout.flush()

def main():
    filter_app = ResonantFrequencyFilter()
    filter_app.run()

if __name__ == "__main__":
    main()
