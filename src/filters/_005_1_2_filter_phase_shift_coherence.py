#!/usr/bin/env python3
# ==========================================
# _005_1_2_filter_phase_shift_coherence.py
# TLU System: Mathematical Filter (005_1_2)
# Category: Signal Processing & Wave Mechanics
# Description: Calculates phase shift and coherence between node pairs at a target frequency.
# ==========================================
import sys
import argparse
import pandas as pd
import numpy as np
from src.core.core_signal_processing import compute_traversing_phase_shift

def main():
    parser = argparse.ArgumentParser(description="005_1_2: Phase Shift & Coherence Filter (Traversing)")
    parser.add_argument('--target_freq', type=float, required=True, help="Target frequency to evaluate (e.g., 0.25 for 4-week period)")
    parser.add_argument('--window_size', type=int, default=24, help="Size of the sliding window")
    parser.add_argument('--step_size', type=int, default=4, help="Step size for sliding window")
    args = parser.parse_args()

    try:
        df = pd.read_csv(sys.stdin)
    except Exception as e:
        sys.stderr.write(f"[ERROR] Failed to read CSV from stdin: {e}\n")
        sys.exit(1)

    if df.empty:
        sys.stderr.write("[WARN] Input stream is empty. Exiting.\n")
        print("t_idx,src_idx,tgt_idx,coherence,phase_shift")
        return

    # To be fully decoupled, we check what columns exist.
    # Normal COO has 'src_idx', 'tgt_idx', 'value'.
    # PCA COO has 'component' instead of src/tgt. We can abstract this if we just know it has t_idx, node_idx, value.
    # But for now, we assume it has t_idx, and some identifier.
    # Actually, the batch pipeline uses projector, so it always maps to t_idx, src_idx, tgt_idx, value.
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
    
    for src in nodes:
        x = activity_pivot[src].values
        
        if len(x) < args.window_size or np.sum(x) == 0:
            continue
            
        for tgt in nodes:
            y = activity_pivot[tgt].values
            
            if np.sum(y) == 0:
                continue
                
            t_indices, coherences, phase_shifts = compute_traversing_phase_shift(
                x, y, args.window_size, args.step_size, args.target_freq
            )
            
            for t_idx, c, p in zip(t_indices, coherences, phase_shifts):
                results.append({
                    't_idx': t_idx + t_min,  # Map back to absolute time
                    'src_idx': src,
                    'tgt_idx': tgt,
                    'coherence': c,
                    'phase_shift': p
                })

    res_df = pd.DataFrame(results)
    
    if res_df.empty:
        print("t_idx,src_idx,tgt_idx,coherence,phase_shift")
    else:
        res_df.to_csv(sys.stdout, index=False, float_format="%.4f")

if __name__ == '__main__':
    main()
