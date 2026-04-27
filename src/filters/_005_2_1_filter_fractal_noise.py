#!/usr/bin/env python3
# ==========================================
# _005_2_1_filter_fractal_noise.py
# TLU System: Mathematical Filter (005_2_1)
# Category: Signal Processing & Wave Mechanics
# Description: Calculates fractal dimensionality (1/f noise beta) for each node.
# ==========================================
import sys
import argparse
import pandas as pd
import numpy as np
from src.core.core_signal_processing import compute_spectral_exponent_beta
from src.filters.cli_parser import get_base_parser

def main():
    parser = get_base_parser("005_2_1: Fractal Dimensionality & 1/f Noise Filter")
    args = parser.parse_args()

    try:
        df = pd.read_csv(sys.stdin)
    except Exception as e:
        sys.stderr.write(f"[ERROR] Failed to read CSV from stdin: {e}\n")
        sys.exit(1)

    if df.empty:
        sys.stderr.write("[WARN] Input stream is empty. Exiting.\n")
        print("node_idx,spectral_exponent_beta,noise_classification")
        return

    required_cols = ['t_idx', 'src_idx', 'tgt_idx', 'value']
    for col in required_cols:
        if col not in df.columns:
            sys.stderr.write(f"[ERROR] Missing required column: {col}\n")
            sys.exit(1)

    t_min = df['t_idx'].min()
    t_max = df['t_idx'].max()
    full_t = pd.DataFrame({'t_idx': np.arange(t_min, t_max + 1)})
    
    outflows = df.groupby(['t_idx', 'src_idx'])['value'].sum().reset_index()
    outflows.rename(columns={'src_idx': 'node_idx'}, inplace=True)
    
    inflows = df.groupby(['t_idx', 'tgt_idx'])['value'].sum().reset_index()
    inflows.rename(columns={'tgt_idx': 'node_idx'}, inplace=True)
    
    activity = pd.concat([outflows, inflows]).groupby(['t_idx', 'node_idx'])['value'].sum().reset_index()

    activity_pivot = activity.pivot(index='t_idx', columns='node_idx', values='value').fillna(0)
    activity_pivot = activity_pivot.reindex(full_t['t_idx'], fill_value=0)
    
    nodes = activity_pivot.columns.tolist()
    
    results = []
    
    for node in nodes:
        x = activity_pivot[node].values
        
        if np.sum(x) == 0:
            continue
            
        beta = compute_spectral_exponent_beta(x)
        
        # Classification based on beta
        if beta < args.thresh_fractal_lower:
            classification = "White Noise"
        elif beta <= args.thresh_fractal_upper:
            classification = "Pink Noise"
        else:
            classification = "Brown Noise"
            
        results.append({
            'node_idx': node,
            'spectral_exponent_beta': beta,
            'noise_classification': classification
        })

    res_df = pd.DataFrame(results)
    
    if res_df.empty:
        print("node_idx,spectral_exponent_beta,noise_classification")
    else:
        res_df.to_csv(sys.stdout, index=False, float_format="%.4f")

if __name__ == '__main__':
    main()
