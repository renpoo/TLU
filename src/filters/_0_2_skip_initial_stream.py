#!/usr/bin/env python3
import sys
import pandas as pd
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Skip initial transient time period from stream data")
    parser.add_argument("--col_time", default="Trans_Date", help="Time column name")
    parser.add_argument("--skip_seconds", type=float, default=20.0, help="Duration to skip in seconds")
    return parser.parse_args()

def main():
    args = parse_args()
    try:
        df = pd.read_csv(sys.stdin)
    except Exception:
        sys.exit(1)
        
    if df.empty:
        sys.exit(0)

    if args.col_time not in df.columns:
        print(f"CRITICAL: Column '{args.col_time}' not found in the input stream. Available columns: {list(df.columns)}", file=sys.stderr)
        sys.exit(1)

    # Convert time to pandas datetime
    df['temp_parsed_time'] = pd.to_datetime(df[args.col_time], errors='coerce')
    df = df.dropna(subset=['temp_parsed_time'])
    
    if df.empty:
        df.drop(columns=['temp_parsed_time']).to_csv(sys.stdout, index=False)
        sys.exit(0)

    # Find the earliest time in the stream
    start_time = df['temp_parsed_time'].min()
    
    # Calculate cutoff time
    cutoff_time = start_time + pd.Timedelta(seconds=args.skip_seconds)
    
    # Filter rows
    df_filtered = df[df['temp_parsed_time'] >= cutoff_time].copy()
    
    # Drop temp column and output to stdout
    df_filtered = df_filtered.drop(columns=['temp_parsed_time'])
    df_filtered.to_csv(sys.stdout, index=False)

if __name__ == "__main__":
    main()
