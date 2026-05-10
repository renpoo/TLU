#!/usr/bin/env python3
"""
@file 06_4_coo_to_time_node_stream.py
@brief WMU Time-Node Stream Translator
@details
Converts the universal COO stream [t_idx, src_idx, tgt_idx, value] into a Time-Node signal stream [t_idx, node_idx, value] for Wave Mechanics Unit (WMU).
For accounting nodes: Calculates net flux (sum(inflows) - sum(outflows)).
For market nodes (source = THE_WORLD): Directly inherits the absolute state/volume.
"""

import sys
import pandas as pd

def main():
    try:
        df = pd.read_csv(sys.stdin)
    except Exception as e:
        sys.stderr.write(f"[ERROR] Failed to read input: {e}\n")
        sys.exit(1)
        
    if df.empty:
        sys.exit(0)
        
    # TLU COO Contract:
    # tgt_idx receives the value (+), src_idx loses the value (-)
    
    # Inflows
    tgt_df = df[['t_idx', 'tgt_idx', 'value']].copy()
    tgt_df.rename(columns={'tgt_idx': 'node_idx'}, inplace=True)
    
    # Outflows
    src_df = df[['t_idx', 'src_idx', 'value']].copy()
    src_df.rename(columns={'src_idx': 'node_idx'}, inplace=True)
    src_df['value'] = -src_df['value']
    
    # Combine all transactions
    combined = pd.concat([tgt_df, src_df], ignore_index=True)
    
    # Remove dummy external reservoir
    combined = combined[combined['node_idx'] != 'THE_WORLD']
    
    # Aggregate to find net signal amplitude X(t) for each node at time t
    # For market data, since THE_WORLD is the only source, the net sum is exactly the injected value (Price/Volume).
    final_df = combined.groupby(['t_idx', 'node_idx'], as_index=False)['value'].sum()
    
    # Ensure chronological sort
    final_df = final_df.sort_values(by=['t_idx', 'node_idx'])
    
    final_df.to_csv(sys.stdout, index=False)

if __name__ == "__main__":
    main()
