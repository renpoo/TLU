#!/usr/bin/env python3
# ==========================================
# _005_1_1_filter_resonant_frequency.py
# TLU System: Mathematical Filter (005_1_1)
# Category: Signal Processing & Wave Mechanics
# Description: Calculates the dominant resonant frequency of node fluxes.
# ==========================================
import sys
import argparse
import pandas as pd
import numpy as np
from src.core.core_signal_processing import compute_resonant_frequency

def main():
    parser = argparse.ArgumentParser(description="005_1_1: Autocorrelation & Resonant Frequency Filter")
    parser.add_argument('--max_tau', type=int, required=True, help="Maximum lag (tau) for correlation / window size")
    args = parser.parse_args()

    # 1. Read COO Stream
    try:
        df = pd.read_csv(sys.stdin)
    except Exception as e:
        sys.stderr.write(f"[ERROR] Failed to read CSV from stdin: {e}\n")
        sys.exit(1)

    if df.empty:
        sys.stderr.write("[WARN] Input stream is empty. Exiting.\n")
        # Output empty schema
        print("node_idx,dominant_frequency,spectral_power")
        return

    required_cols = ['t_idx', 'src_idx', 'tgt_idx', 'value']
    for col in required_cols:
        if col not in df.columns:
            sys.stderr.write(f"[ERROR] Missing required column: {col}\n")
            sys.exit(1)

    # 2. Extract macro fluxes per node
    # Here we treat both inflows and outflows as activity. Let's compute net absolute flux per node.
    # Alternatively, we could do total outflow or total inflow.
    # For a simple activity measure, we sum amount per t_idx per src_idx (outflow).
    
    outflows = df.groupby(['t_idx', 'src_idx'])['value'].sum().reset_index()
    outflows.rename(columns={'src_idx': 'node_idx'}, inplace=True)
    
    inflows = df.groupby(['t_idx', 'tgt_idx'])['value'].sum().reset_index()
    inflows.rename(columns={'tgt_idx': 'node_idx'}, inplace=True)
    
    # Total activity (in + out)
    activity = pd.concat([outflows, inflows]).groupby(['t_idx', 'node_idx'])['value'].sum().reset_index()

    # Get continuous time index
    t_min = df['t_idx'].min()
    t_max = df['t_idx'].max()
    full_t = pd.DataFrame({'t_idx': np.arange(t_min, t_max + 1)})
    
    nodes = activity['node_idx'].unique()
    
    results = []
    
    # 3. Compute resonant frequency for each node
    for node in nodes:
        node_data = activity[activity['node_idx'] == node]
        
        # Merge with full time index to ensure no missing time steps (fill with 0)
        ts_df = pd.merge(full_t, node_data, on='t_idx', how='left').fillna(0)
        flux_series = ts_df['value'].values
        
        if len(flux_series) < 2 or np.sum(flux_series) == 0:
            results.append({
                'node_idx': node,
                'dominant_frequency': 0.0,
                'spectral_power': 0.0
            })
            continue
            
        freq, power = compute_resonant_frequency(flux_series, max_tau=args.max_tau)
        
        results.append({
            'node_idx': node,
            'dominant_frequency': freq,
            'spectral_power': power
        })

    # 4. Output results
    res_df = pd.DataFrame(results)
    
    # Sort by power descending to show the most resonant nodes first
    res_df = res_df.sort_values('spectral_power', ascending=False)
    
    # Print to stdout
    res_df.to_csv(sys.stdout, index=False, float_format="%.4f")

if __name__ == '__main__':
    main()
