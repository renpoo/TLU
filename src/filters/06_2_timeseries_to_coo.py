#!/usr/bin/env python3
"""
@file 06_2_timeseries_to_coo.py
@brief TLU/WMU External Data Pipeline: Translates wide time-series to standard COO stream.
@details
Converts [Date, Ticker1_Price, Ticker2_Price] into [t_idx, src_idx, tgt_idx, value] 
by mapping a dummy origin (THE_WORLD) to each indicator.

@pre Input CSV via stdin must have a time column.
@post Output CSV via stdout is a COO transaction stream.
"""

import sys
import pandas as pd
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Convert Wide Time-Series to COO Stream")
    parser.add_argument("--col_time", default="Date", help="Name of the time column in input")
    parser.add_argument("--dummy_src", default="THE_WORLD", help="Source node for external environment")
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
        
    if args.col_time not in df.columns:
        sys.stderr.write(f"[ERROR] Time column '{args.col_time}' not found in input.\n")
        sys.exit(1)
        
    # Melt wide to long
    melted = df.melt(id_vars=[args.col_time], var_name='tgt_idx', value_name='value')
    
    # Drop NaNs: The Zero-Energy Concept.
    # If data doesn't exist for a day, no energy is injected.
    melted = melted.dropna(subset=['value'])
    
    # Sector Mapping for Bipartite/Hierarchical Topology
    SECTOR_MAP = {
        'AAPL': 'Sector_IT', 'MSFT': 'Sector_IT', 'NVDA': 'Sector_IT', 'AVGO': 'Sector_IT', 'HPQ': 'Sector_IT', 'STX': 'Sector_IT',
        'JNJ': 'Sector_Health', 'BIIB': 'Sector_Health', 'PRGO': 'Sector_Health',
        'JPM': 'Sector_Fin', 'SYF': 'Sector_Fin', 'NAVI': 'Sector_Fin',
        'AMZN': 'Sector_Disc', 'TSLA': 'Sector_Disc', 'HD': 'Sector_Disc', 'M': 'Sector_Disc', 'KSS': 'Sector_Disc',
        'GOOG': 'Sector_Comm', 'META': 'Sector_Comm', 'DIS': 'Sector_Comm', 'LYV': 'Sector_Comm', 'NWSA': 'Sector_Comm',
        'CAT': 'Sector_Ind', 'DOV': 'Sector_Ind', 'PNR': 'Sector_Ind',
        'PG': 'Sector_Staples', 'CAG': 'Sector_Staples', 'CPB': 'Sector_Staples',
        'XOM': 'Sector_Energy', 'HAL': 'Sector_Energy', 'APA': 'Sector_Energy',
        'NEE': 'Sector_Util', 'NI': 'Sector_Util', 'PNW': 'Sector_Util',
        'PLD': 'Sector_RE', 'BXP': 'Sector_RE', 'VNO': 'Sector_RE',
        'LIN': 'Sector_Mat', 'SEE': 'Sector_Mat', 'OI': 'Sector_Mat'
    }
    
    def map_sector(tgt):
        ticker = tgt.split('_')[0]
        return SECTOR_MAP.get(ticker, args.dummy_src)
        
    melted['src_idx'] = melted['tgt_idx'].apply(map_sector)
    
    # Rename time column to match TLU standard
    melted = melted.rename(columns={args.col_time: 't_idx'})
    
    # Reorder columns
    final_df = melted[['t_idx', 'src_idx', 'tgt_idx', 'value']]
    
    final_df.to_csv(sys.stdout, index=False)

if __name__ == "__main__":
    main()
