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

    src_cols = [c.strip() for c in args.col_src.split(',')]
    tgt_cols = [c.strip() for c in args.col_tgt.split(',')]

    # Validate columns
    for c in [args.col_time, args.col_val] + src_cols + tgt_cols:
        if c not in df.columns:
            print(f"CRITICAL: Column '{c}' not found in the input stream. Available columns: {list(df.columns)}", file=sys.stderr)
            sys.exit(1)

    # Convert time
    df['parsed_time'] = pd.to_datetime(df[args.col_time], errors='coerce')
    df = df.dropna(subset=['parsed_time'])
    df = df.sort_values('parsed_time')
    
    df[args.col_time] = df['parsed_time'].apply(lambda x: get_period_str(x, args.interval))

    is_multi = len(src_cols) > 1 or len(tgt_cols) > 1

    if is_multi:
        expanded_dfs = []
        for s_col in src_cols:
            for t_col in tgt_cols:
                sub_df = df[[args.col_time, s_col, t_col, args.col_val]].copy()
                sub_df = sub_df.rename(columns={s_col: 'Src', t_col: 'Tgt'})
                expanded_dfs.append(sub_df)
        expanded_df = pd.concat(expanded_dfs, ignore_index=True)
        
        # Aggregate expanded stream
        grouped = expanded_df.groupby([args.col_time, 'Src', 'Tgt'], sort=False)
        summary = grouped[args.col_val].sum().reset_index()
    else:
        # Backward compatibility for single-column
        grouped = df.groupby([args.col_time, args.col_src, args.col_tgt], sort=False)
        summary = grouped[args.col_val].sum().reset_index()

    summary.to_csv(sys.stdout, index=False)

if __name__ == "__main__":
    main()
