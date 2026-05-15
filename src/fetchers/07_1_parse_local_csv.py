#!/usr/bin/env python3
"""
@file 07_1_parse_local_csv.py
@brief TLU/WMU External Data Pipeline: Reads local timeseries CSV, filters columns, and calculates flux (.diff)
"""
import sys
import pandas as pd
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Read local CSV and calculate diff")
    parser.add_argument("--input_csv", required=True, help="Path to input CSV")
    parser.add_argument("--columns", required=True, help="Comma separated list of columns to keep")
    parser.add_argument("--col_time", default="Date", help="Name of the time column if not index")
    return parser.parse_args()

def main():
    args = parse_args()
    
    try:
        data = pd.read_csv(args.input_csv, index_col=0, parse_dates=True)
    except Exception as e:
        sys.stderr.write(f"[ERROR] Failed to read {args.input_csv}: {e}\n")
        sys.exit(1)
        
    cols = [c.strip() for c in args.columns.split(",")]
    
    # Filter columns that actually exist
    valid_cols = [c for c in cols if c in data.columns]
    if not valid_cols:
        sys.stderr.write(f"[ERROR] None of the specified columns found in CSV.\n")
        sys.exit(1)
        
    data = data[valid_cols]
    
    # Calculate Flux (Discrete Derivative)
    delta_data = data.diff().dropna()
    
    # Reset index to make the Date a column again
    delta_data = delta_data.reset_index()
    
    # Ensure the time column has the expected name
    if delta_data.columns[0] != args.col_time:
        delta_data = delta_data.rename(columns={delta_data.columns[0]: args.col_time})
        
    # Output to stdout
    delta_data.to_csv(sys.stdout, index=False)

if __name__ == "__main__":
    main()
