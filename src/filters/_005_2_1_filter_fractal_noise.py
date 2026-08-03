#!/usr/bin/env python3
# ==========================================
# _005_2_1_filter_fractal_noise.py
# TLU System: Fractal Dimensionality & 1/f Noise Filter
# Version: 8.0.0 (Refactored with BaseFilter Architecture)
# ==========================================
import sys
import argparse
import numpy as np
import pandas as pd
from typing import List, Tuple, Dict, Any

from src.filters.base_filter import BaseFilter, HistoryBuffer, assert_valid_matrix
from src.filters.stream_processor import setup_pipeline, yield_time_slices
from src.core.core_signal_processing import compute_spectral_exponent_beta

class FractalNoiseFilter(BaseFilter):
    cli_description = "TLU Fractal Dimensionality & 1/f Noise Filter"
    output_header = ["node_idx", "spectral_exponent_beta", "noise_classification"]

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
            x = flux_mat[:, node]
            if np.sum(x) == 0:
                continue
                
            beta = compute_spectral_exponent_beta(x)
            
            if beta < args.thresh_fractal_lower:
                classification = "White Noise"
            elif beta <= args.thresh_fractal_upper:
                classification = "Pink Noise"
            else:
                classification = "Brown Noise"
                
            records.append([
                node, f"{beta:.4f}", classification
            ])

        formatted = self.format_records(records)
        for rec in formatted:
            writer.writerow(rec)

        sys.stdout.flush()

def main():
    filter_app = FractalNoiseFilter()
    filter_app.run()

if __name__ == "__main__":
    main()
