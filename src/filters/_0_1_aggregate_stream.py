#!/usr/bin/env python3
import sys
import re
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

def parse_interval(interval_str: str):
    clean = interval_str.strip().lower()
    
    # 1. Unit then number (e.g. "day 3", "week 2")
    match_unit_num = re.match(r'^([a-zA-Z]+)\s*(\d+)$', clean)
    if match_unit_num:
        unit, num_str = match_unit_num.groups()
        return unit, int(num_str)
        
    # 2. Number then unit (e.g. "3 day", "3s")
    match_num_unit = re.match(r'^(\d+)\s*([a-zA-Z]+)$', clean)
    if match_num_unit:
        num_str, unit = match_num_unit.groups()
        return unit, int(num_str)
        
    # 3. Unit only (default coefficient to 1)
    return clean, 1

def get_period_series(series: pd.Series, interval: str) -> pd.Series:
    unit, num = parse_interval(interval)
    
    # Day
    if unit in ['day', 'd', 'days']:
        if num == 1:
            return series.dt.strftime('%Y-%m-%d')
        else:
            return series.dt.floor(f"{num}d").dt.strftime('%Y-%m-%d')
            
    # Week
    elif unit in ['week', 'w', 'weeks']:
        if num == 1:
            return series.dt.strftime('%G-W%V')
        else:
            return series.dt.floor(f"{num}W").dt.strftime('%Y-%m-%d')
            
    # Month
    elif unit in ['month', 'm', 'months']:
        if num == 1:
            return series.dt.strftime('%Y-%m')
        else:
            rounded_month = ((series.dt.month - 1) // num) * num + 1
            return series.dt.year.astype(str) + '-' + rounded_month.astype(str).str.zfill(2)
            
    # Quarter
    elif unit in ['quarter', 'q', 'quarters']:
        q = (series.dt.month - 1) // 3 + 1
        if num == 1:
            return series.dt.year.astype(str) + '-Q' + q.astype(str)
        else:
            rounded_q = ((q - 1) // num) * num + 1
            return series.dt.year.astype(str) + '-Q' + rounded_q.astype(str)
            
    # Year
    elif unit in ['year', 'y', 'years']:
        if num == 1:
            return series.dt.strftime('%Y')
        else:
            rounded_year = (series.dt.year // num) * num
            return rounded_year.astype(str)
            
    # Custom sub-day units
    pd_unit = None
    if unit in ['s', 'sec', 'second', 'seconds']:
        pd_unit = 's'
    elif unit in ['min', 'minute', 'minutes']:
        pd_unit = 'min'
    elif unit in ['h', 'hr', 'hour', 'hours']:
        pd_unit = 'h'
        
    if pd_unit:
        freq = f"{num}{pd_unit}"
        try:
            return series.dt.floor(freq).dt.strftime('%Y-%m-%d %H:%M:%S')
        except Exception:
            pass
            
    # Fallback to pandas floor directly with num+unit
    try:
        freq = f"{num}{unit}" if num > 1 else unit
        return series.dt.floor(freq).dt.strftime('%Y-%m-%d %H:%M:%S')
    except Exception:
        return series.dt.strftime('%Y-%m-%d')

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
    
    df[args.col_time] = get_period_series(df['parsed_time'], args.interval)

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
