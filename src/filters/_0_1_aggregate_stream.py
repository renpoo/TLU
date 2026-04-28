#!/usr/bin/env python3
# ==========================================
# _0_1_aggregate_stream.py
# TLU System: Pre-filtering Layer
# Action: Universal Time-Series Aggregation (Graph Downsampler)
# ==========================================

import sys
import pandas as pd
from src.filters.cli_parser import parse_projector_args

def main():
    mapping_config = parse_projector_args(sys.argv[1:])
    col_time = mapping_config.get("col_time", "Timestamp")
    col_src = mapping_config.get("col_src", "Src")
    col_tgt = mapping_config.get("col_tgt", "Tgt")
    col_val = mapping_config.get("col_val", "Amount")
    col_multiplier = mapping_config.get("col_multiplier", "")
    interval = mapping_config.get("interval", "day")

    try:
        df = pd.read_csv(sys.stdin)
    except Exception as e:
        print(f"Error reading input: {e}", file=sys.stderr)
        sys.exit(1)

    if df.empty:
        sys.exit(0)

    # 1. Resolve Value (Amount vs Volume * Price)
    if col_multiplier and col_multiplier in df.columns:
        df['_Agg_Value'] = df[col_val] * df[col_multiplier]
    else:
        df['_Agg_Value'] = df[col_val]

    # 2. Time formatting based on interval
    dt_col = pd.to_datetime(df[col_time], format='mixed')
    
    if interval == "day":
        df['_Agg_Time'] = dt_col.dt.strftime('%Y-%m-%d')
    elif interval == "week":
        # ISO week: YYYY-Www
        df['_Agg_Time'] = dt_col.dt.isocalendar().year.astype(str) + "-W" + dt_col.dt.isocalendar().week.astype(str).str.zfill(2)
    elif interval == "month":
        df['_Agg_Time'] = dt_col.dt.strftime('%Y-%m')
    elif interval == "quarter":
        df['_Agg_Time'] = dt_col.dt.year.astype(str) + "-Q" + dt_col.dt.quarter.astype(str)
    elif interval == "year":
        df['_Agg_Time'] = dt_col.dt.year.astype(str)
    else: # "none"
        df['_Agg_Time'] = df[col_time]

    # 3. Handle missing source/target cleanly
    df[col_src] = df[col_src].fillna("UNKNOWN_SRC")
    df[col_tgt] = df[col_tgt].fillna("UNKNOWN_TGT")

    # 4. Aggregate
    summary = df.groupby(['_Agg_Time', col_src, col_tgt])['_Agg_Value'].sum().reset_index()

    # 5. Rename columns back to generic or parsed names for downstream
    summary = summary.rename(columns={
        '_Agg_Time': col_time,
        '_Agg_Value': col_val
    })

    # 6. Reformat into a flat COO format and output to stdout
    summary.to_csv(sys.stdout, index=False)

if __name__ == "__main__":
    main()
