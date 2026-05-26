#!/usr/bin/env python3
import sys
import pandas as pd
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--col_time", required=True)
    parser.add_argument("--col_src", required=True)
    parser.add_argument("--col_tgt", required=True)
    parser.add_argument("--col_val", required=True)
    parser.add_argument("--interval", default='week')
    return parser.parse_args()

def get_period_str(dt, interval):
    if interval == 'day':
        return dt.strftime('%Y-%m-%d')
    elif interval == 'week':
        return dt.strftime('%G-W%V')
    elif interval == 'month':
        return dt.strftime('%Y-%m')
    elif interval == 'quarter':
        quarter = (dt.month - 1) // 3 + 1
        return f"{dt.year}-Q{quarter}"
    elif interval == 'year':
        return dt.strftime('%Y')
    else:
        # Fallback to pandas floor for strings like '10s', '1min', '1H'
        try:
            return pd.Timestamp(dt).floor(interval).strftime('%Y-%m-%d %H:%M:%S')
        except Exception:
            return dt.strftime('%Y-%m-%d')

def main():
    args = parse_args()
    try:
        df = pd.read_csv(sys.stdin)
    except Exception:
        sys.exit(1)
        
    if df.empty:
        sys.exit(0)

    # Convert time
    df['parsed_time'] = pd.to_datetime(df[args.col_time], errors='coerce')
    df = df.dropna(subset=['parsed_time'])
    df = df.sort_values('parsed_time')
    
    df[args.col_time] = df['parsed_time'].apply(lambda x: get_period_str(x, args.interval))

    # We will just sum the col_val.
    grouped = df.groupby([args.col_time, args.col_src, args.col_tgt], sort=False)
    summary = grouped[args.col_val].sum().reset_index()

    summary.to_csv(sys.stdout, index=False)

if __name__ == "__main__":
    main()
