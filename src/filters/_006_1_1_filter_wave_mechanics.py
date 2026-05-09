#!/usr/bin/env python3
# ==========================================
# _006_1_1_filter_wave_mechanics.py
# TLU System: Mathematical Filter (006_1_1)
# Category: Quantum/Wave Mechanics (Phase Space)
# Description: Converts Position Space (A) to Phase Space (Z) via Fourier duality.
# ==========================================
import sys
import argparse
import pandas as pd
import numpy as np
import os
from src.core.wmu_engine import WMUEngine

def main():
    parser = argparse.ArgumentParser(description="006_1_1: Wave Mechanics & Phase Space Filter")
    parser.add_argument('--out_plot', type=str, default="wmu_phase_matrix", help="Filename for the output plot")
    args = parser.parse_args()

    # Read hydrated dynamics state from stdin
    try:
        df = pd.read_csv(sys.stdin)
    except Exception as e:
        sys.stderr.write(f"[ERROR] Failed to read CSV from stdin: {e}\n")
        sys.exit(1)

    if df.empty:
        sys.stderr.write("[WARN] Input stream is empty. Exiting.\n")
        print("node_label,phase_score,wave_role")
        return

    required_cols = ['time_label', 'node_label', 'state_X']
    for col in required_cols:
        if col not in df.columns:
            sys.stderr.write(f"[ERROR] Missing required column: {col}\n")
            sys.exit(1)

    # Convert Position Space (state_X) into a phase-space matrix
    df_A = df.pivot(index='time_label', columns='node_label', values='state_X').fillna(0)
    
    # Calculate Velocity (V) as Absolute Flux (Proxy for transaction volume)
    # This prevents the discriminant (D) from being zero.
    df_V = df_A.diff().abs().fillna(0) * 2.0

    tickers_dict = {col: col for col in df_A.columns}
    
    wmu = WMUEngine(tickers_dict)
    
    # Override out_dir to TLU_PLOT_DIR if it exists
    plot_dir = os.environ.get('TLU_PLOT_DIR', './output_plots')
    os.makedirs(plot_dir, exist_ok=True)
    wmu.out_dir = plot_dir
    
    wmu.load_local_data(df_A, df_V)
    
    try:
        wmu.calculate_phase_space()
        start_date = df_A.index[0]
        end_date = df_A.index[-1]
        imag_corr = wmu.analyze_era(start_date, end_date)
        
        # Plot matrix
        wmu.plot_matrix(imag_corr, "WMU Unified Phase Space", args.out_plot)
        
        # Calculate scores for CSV output
        scores = imag_corr.sum().sort_values(ascending=False)
        
        # Print header
        print("node_label,phase_score,wave_role")
        for node, score in scores.items():
            role = "Leader (Source)" if score > 0 else "Laggard (Sink)"
            print(f"{node},{score:.4f},{role}")
            
    except Exception as e:
        sys.stderr.write(f"[ERROR] WMU Engine failed: {e}\n")
        sys.exit(1)

if __name__ == '__main__':
    main()
