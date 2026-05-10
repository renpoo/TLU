import sys
import pandas as pd
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Aggregate market COO stream by time.")
    parser.add_argument("--interval", choices=['day', 'week', 'month', 'quarter', 'year'], default='week')
    return parser.parse_args()

def get_period_str(dt, interval):
    if interval == 'day':
        return dt.strftime('%Y-%m-%d')
    elif interval == 'week':
        # ISO week: YYYY-Www
        # Using %G for ISO year and %V for ISO week
        return dt.strftime('%G-W%V')
    elif interval == 'month':
        return dt.strftime('%Y-%m')
    elif interval == 'quarter':
        quarter = (dt.month - 1) // 3 + 1
        return f"{dt.year}-Q{quarter}"
    elif interval == 'year':
        return dt.strftime('%Y')
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
    df['parsed_time'] = pd.to_datetime(df['t_idx'], errors='coerce')
    df = df.dropna(subset=['parsed_time'])
    
    # We must preserve chronological order to use .iloc[-1] (.last()) correctly.
    df = df.sort_values('parsed_time')
    
    df['t_idx'] = df['parsed_time'].apply(lambda x: get_period_str(x, args.interval))

    # Apply domain-specific market aggregation rules:
    # Volume -> SUM (Flux physics)
    # Price/Rate -> LAST (Position physics)
    aggregated = []
    
    grouped = df.groupby(['t_idx', 'src_idx', 'tgt_idx'], sort=False)
    for name, group in grouped:
        t_val, src_val, tgt_val = name
        
        if 'Volume' in str(tgt_val):
            val = group['value'].sum()
        else:
            # Default to Last Observed Value for Prices, Index Levels, Rates
            val = group['value'].iloc[-1]
            
        aggregated.append({
            't_idx': t_val,
            'src_idx': src_val,
            'tgt_idx': tgt_val,
            'value': val
        })
        
    if not aggregated:
        sys.exit(0)
        
    final_df = pd.DataFrame(aggregated)
    final_df.to_csv(sys.stdout, index=False)

if __name__ == "__main__":
    main()
