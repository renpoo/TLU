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
    
    # ---------------------------------------------------------
    # Dimensional Unification (Position -> Flux)
    # ---------------------------------------------------------
    # TLU's COO stream natively expects Net Flux (v) because `000_1_1` integrates it.
    # Therefore, State/Position data (Prices, Rates) must be differentiated (.diff()).
    # Flux data (Volume) is already Flux and remains unchanged.
    flux_dfs = []
    for (src, tgt), group in final_df.groupby(['src_idx', 'tgt_idx'], sort=False):
        group = group.copy()
        if 'Volume' not in str(tgt):
            # By filling the first NaN with the original value, the integration (cumsum)
            # in 000_1_1 will perfectly reconstruct the absolute Position.
            group['value'] = group['value'].diff().fillna(group['value'])
        flux_dfs.append(group)
        
    if flux_dfs:
        final_df = pd.concat(flux_dfs, ignore_index=True)
        final_df = final_df.sort_values(['t_idx', 'src_idx', 'tgt_idx'])
        
    final_df.to_csv(sys.stdout, index=False)

if __name__ == "__main__":
    main()
