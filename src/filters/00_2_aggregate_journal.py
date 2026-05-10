#!/usr/bin/env python3
"""
@file 00_2_aggregate_journal.py
@brief TLU/WMU Pre-processing Phase 0: Temporal aggregation for accounting flux data.
@details
Aggregates the daily sparse COO transaction stream into specified intervals.
Since accounting transactions represent 'Flux' (velocity), the aggregation strategy is mathematically fixed to 'SUM'.
Missing edges in specific time bins are inherently treated as 0.0 in the sparse COO structure.

@param --interval Temporal resolution: 'day', 'week', 'month', 'quarter', 'year'.
@note If interval is 'day', this filter acts nearly as a pass-through, but it still executes spatial aggregation (summing multiple transactions occurring on the same day between identical nodes) to compress the graph.
@pre Input must be CSV via stdin with columns: ['t_idx', 'src_idx', 'tgt_idx', 'value']
@post Output is CSV via stdout with identical columns, temporally and spatially aggregated.
"""

import sys
import pandas as pd
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Temporal aggregator for Journal COO.")
    parser.add_argument("--interval", choices=['day', 'week', 'month', 'quarter', 'year'], required=True, help="Aggregation interval")
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

    # Validate contract
    required = ['t_idx', 'src_idx', 'tgt_idx', 'value']
    for req in required:
        if req not in df.columns:
            sys.stderr.write(f"[ERROR] Missing required column: {req}\n")
            sys.exit(1)

    # Parse dates
    df['t_idx'] = pd.to_datetime(df['t_idx'], format='mixed', errors='coerce')
    df = df.dropna(subset=['t_idx'])

    # Apply temporal grouping mapping
    if args.interval == "day":
        # Pass-through temporal wise, but spatial aggregation will still occur
        df['_Agg_Time'] = df['t_idx'].dt.strftime('%Y-%m-%d')
    elif args.interval == "week":
        # ISO week format
        df['_Agg_Time'] = df['t_idx'].dt.isocalendar().year.astype(str) + "-W" + df['t_idx'].dt.isocalendar().week.astype(str).str.zfill(2)
    elif args.interval == "month":
        df['_Agg_Time'] = df['t_idx'].dt.strftime('%Y-%m')
    elif args.interval == "quarter":
        df['_Agg_Time'] = df['t_idx'].dt.year.astype(str) + "-Q" + df['t_idx'].dt.quarter.astype(str)
    elif args.interval == "year":
        df['_Agg_Time'] = df['t_idx'].dt.year.astype(str)

    # Execute spatial and temporal aggregation (SUM for Flux)
    summary = df.groupby(['_Agg_Time', 'src_idx', 'tgt_idx'])['value'].sum().reset_index()
    summary = summary.rename(columns={'_Agg_Time': 't_idx'})

    # Output back to stdout
    summary.to_csv(sys.stdout, index=False)

if __name__ == "__main__":
    main()
