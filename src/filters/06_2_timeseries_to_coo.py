#!/usr/bin/env python3
"""
@file 06_2_timeseries_to_coo.py
@brief TLU/WMU External Data Pipeline: Translates wide time-series to standard COO stream.
@details
Converts [Date, Ticker1_Price, Ticker2_Price] into [t_idx, src_idx, tgt_idx, value] 
by mapping a dummy origin (THE_WORLD) to each indicator.

@pre Input CSV via stdin must have a time column.
@post Output CSV via stdout is a COO transaction stream.
"""

import sys
import pandas as pd
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Convert Wide Time-Series to COO Stream")
    parser.add_argument("--col_time", default="Date", help="Name of the time column in input")
    parser.add_argument("--dummy_src", default="THE_WORLD", help="Source node for external environment")
    return parser.parse_args()

def main():
    args = parse_args()
    
    try:
        df = pd.read_csv(sys.stdin)
    except Exception as e:
        sys.stderr.write(f"[ERROR] Failed to read input: {e}\n")
        sys.exit(1)
        
    if df.empty:
        sys.exit(0)
        
    if args.col_time not in df.columns:
        sys.stderr.write(f"[ERROR] Time column '{args.col_time}' not found in input.\n")
        sys.exit(1)
        
    # Melt wide to long
    melted = df.melt(id_vars=[args.col_time], var_name='tgt_idx', value_name='value')
    
    # Drop NaNs: The Zero-Energy Concept.
    # If data doesn't exist for a day, no energy is injected.
    melted = melted.dropna(subset=['value'])
    
    # Add dummy source
    melted['src_idx'] = args.dummy_src
    
    # Rename time column to match TLU standard
    melted = melted.rename(columns={args.col_time: 't_idx'})
    
    # Reorder columns
    final_df = melted[['t_idx', 'src_idx', 'tgt_idx', 'value']]
    
    final_df.to_csv(sys.stdout, index=False)

if __name__ == "__main__":
    main()
