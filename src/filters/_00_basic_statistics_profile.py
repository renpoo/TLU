#!/usr/bin/env python3
# ==========================================
# _00_basic_statistics_profile.py
# TLU System: SDL_007 Classical Statistical Baseline
# Category: Pre-analysis / Baseline Validation
# ==========================================

import sys
import pandas as pd
import numpy as np
import argparse
from scipy.stats import skew, kurtosis

def parse_args():
    parser = argparse.ArgumentParser(description="Calculate classical statistical baseline.")
    parser.add_argument("--start_time", type=str, default=None, help="Start time (inclusive)")
    parser.add_argument("--end_time", type=str, default=None, help="End time (inclusive)")
    parser.add_argument("--output_md", type=str, default=None, help="Markdown output file")
    return parser.parse_args()

def calculate_stats(series, name):
    if len(series) == 0:
        return {"Name": name, "Mean": 0, "StdDev": 0, "Min": 0, "Max": 0, "Skew": 0, "Kurtosis": 0}
    
    return {
        "Name": name,
        "Mean": series.mean(),
        "StdDev": series.std() if len(series) > 1 else 0,
        "Min": series.min(),
        "Max": series.max(),
        "Skew": skew(series, nan_policy='omit') if len(series) > 2 else 0,
        "Kurtosis": kurtosis(series, nan_policy='omit') if len(series) > 3 else 0
    }

def main():
    args = parse_args()
    
    try:
        df = pd.read_csv(sys.stdin)
    except Exception as e:
        sys.stderr.write(f"[ERROR] Failed to read input stream: {e}\n")
        sys.exit(1)
        
    if df.empty:
        sys.stderr.write("[WARN] Empty input stream.\n")
        sys.exit(0)

    # Detect time column
    time_col = 'time_label' if 'time_label' in df.columns else 't_idx'
    if time_col not in df.columns:
        sys.stderr.write("[ERROR] Time column not found.\n")
        sys.exit(1)

    # Apply time window filtering
    if args.start_time:
        df = df[df[time_col] >= args.start_time]
    if args.end_time:
        df = df[df[time_col] <= args.end_time]

    if df.empty:
        sys.stderr.write("[WARN] Empty stream after time filtering.\n")
        sys.exit(0)

    # Ensure required columns exist
    if 'node_label' not in df.columns or 'velocity_v' not in df.columns or 'state_X' not in df.columns:
        sys.stderr.write("[ERROR] Required columns (node_label, velocity_v, state_X) not found.\n")
        sys.exit(1)

    stats_list = []

    # 1. Macro-Level Statistics (System Total Flux)
    # Group by time to get the absolute magnitude of flux across the whole system
    macro_df = df.groupby(time_col).agg({
        'velocity_v': lambda x: x.abs().sum() / 2.0  # Total systemic trading volume (divided by 2 since it's zero-sum)
    }).reset_index()
    
    macro_stats = calculate_stats(macro_df['velocity_v'], "MACRO_SYSTEM_VOLUME")
    stats_list.append(macro_stats)

    # Macro-Level Net Flux (Should be close to 0 if perfectly closed, or non-zero if open system)
    macro_net_df = df.groupby(time_col)['velocity_v'].sum().reset_index()
    macro_net_stats = calculate_stats(macro_net_df['velocity_v'], "MACRO_NET_FLUX")
    stats_list.append(macro_net_stats)

    # 2. Micro-Level Statistics (Per Node)
    for node, group in df.groupby('node_label'):
        node_stats = calculate_stats(group['velocity_v'], f"MICRO_{node}")
        stats_list.append(node_stats)

    # Create summary DataFrame
    stats_df = pd.DataFrame(stats_list)

    # Format Output
    if args.output_md:
        try:
            with open(args.output_md, 'w') as f:
                f.write("# Classical Statistical Baseline (SDL_007)\n\n")
                
                f.write(f"**Time Window:** `{args.start_time or 'START'} -> {args.end_time or 'END'}`\n")
                f.write(f"**Total Time Steps:** `{len(df[time_col].unique())}`\n\n")
                
                f.write("## 1. Macro-Level Statistics (System-Wide)\n")
                macro_subset = stats_df[stats_df['Name'].str.startswith('MACRO_')].copy()
                f.write("| Name | Mean | StdDev | Min | Max | Skew | Kurtosis |\n")
                f.write("|---|---|---|---|---|---|---|\n")
                for _, row in macro_subset.iterrows():
                    f.write(f"| {row['Name']} | {row['Mean']:.4f} | {row['StdDev']:.4f} | {row['Min']:.4f} | {row['Max']:.4f} | {row['Skew']:.4f} | {row['Kurtosis']:.4f} |\n")
                f.write("\n\n")
                
                f.write("## 2. Micro-Level Statistics (Node Velocity/Flux)\n")
                micro_subset = stats_df[stats_df['Name'].str.startswith('MICRO_')].copy()
                f.write("| Node | Mean | StdDev | Min | Max | Skew | Kurtosis |\n")
                f.write("|---|---|---|---|---|---|---|\n")
                for _, row in micro_subset.iterrows():
                    name = row['Name'].replace('MICRO_', '')
                    f.write(f"| {name} | {row['Mean']:.4f} | {row['StdDev']:.4f} | {row['Min']:.4f} | {row['Max']:.4f} | {row['Skew']:.4f} | {row['Kurtosis']:.4f} |\n")
                f.write("\n")
                
            sys.stderr.write(f"[INFO] Statistical baseline saved to {args.output_md}\n")
        except Exception as e:
            sys.stderr.write(f"[ERROR] Failed to write markdown: {e}\n")
            sys.exit(1)
    else:
        # Output as CSV if no MD file specified
        stats_df.to_csv(sys.stdout, index=False)

if __name__ == "__main__":
    main()
