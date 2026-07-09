#!/usr/bin/env python3
# ==========================================
# _000_2_4_filter_stiffness_difference.py
# TLU System: Extract temporal differences of structural stiffness matrix elements
# ==========================================

import sys
import pandas as pd

def main():
    try:
        df = pd.read_csv(sys.stdin)
    except Exception as e:
        print(f"Error reading input: {e}", file=sys.stderr)
        sys.exit(1)
        
    if df.empty:
        print("t_idx,src_idx,tgt_idx,stiffness_diff")
        sys.exit(0)
        
    required_cols = ['t_idx', 'src_idx', 'tgt_idx', 'stiffness_k']
    for col in required_cols:
        if col not in df.columns:
            print(f"Error: missing required column {col}", file=sys.stderr)
            sys.exit(1)

    max_t = int(df['t_idx'].max()) + 1
    
    # Pivot matrix to align time steps for subtraction
    pivot_df = df.pivot(index=['src_idx', 'tgt_idx'], columns='t_idx', values='stiffness_k').fillna(0.0)
    
    # Ensure all time columns are present
    for t in range(max_t):
        if t not in pivot_df.columns:
            pivot_df[t] = 0.0
            
    diff_cols = []
    # t=0 difference is defined as 0.0 (no previous step exists)
    diff_cols.append(pd.Series(0.0, index=pivot_df.index, name=0))
    
    # Calculate difference for t >= 1
    for t in range(1, max_t):
        diff = pivot_df[t] - pivot_df[t - 1]
        diff_cols.append(pd.Series(diff, name=t))
        
    diff_df = pd.concat(diff_cols, axis=1).stack().reset_index()
    diff_df.columns = ['src_idx', 'tgt_idx', 't_idx', 'stiffness_diff']
    
    # Reorder to match normal TLU format
    diff_df = diff_df[['t_idx', 'src_idx', 'tgt_idx', 'stiffness_diff']]
    diff_df = diff_df.sort_values(['t_idx', 'src_idx', 'tgt_idx'])
    
    diff_df.to_csv(sys.stdout, index=False)

if __name__ == '__main__':
    main()
