#!/usr/bin/env python3
"""
@file 06_1_a_fetch_market.py
@brief TLU/WMU External Data Harvester: Fetches market data (Daily) from Yahoo! Finance.
@details
Thin Adapter pattern. Fetches raw data and immediately outputs to standard output as a wide CSV.
No aggregation or transformation is performed here.

@pre Requires yfinance.
@post Outputs wide CSV with columns like: Date, AAPL_Close, AAPL_Volume, etc.
"""

import yfinance as yf
import pandas as pd
import argparse
import sys

def parse_args():
    parser = argparse.ArgumentParser(description="Fetch Market Data from yfinance")
    parser.add_argument("--tickers", required=True, help="Comma separated tickers (e.g. ^GSPC,^VIX,AAPL)")
    parser.add_argument("--start", default="2020-01-01", help="Start date YYYY-MM-DD")
    parser.add_argument("--end", default="2024-01-01", help="End date YYYY-MM-DD")
    parser.add_argument("--only_close", action="store_true", help="Only output Close prices (drops Open, High, Low, Volume)")
    return parser.parse_args()

def main():
    args = parse_args()
    tickers = [t.strip() for t in args.tickers.split(",")]
    
    # Note: auto_adjust=True keeps adjusted prices.
    try:
        data = yf.download(tickers, start=args.start, end=args.end, progress=False, auto_adjust=True)
    except Exception as e:
        sys.stderr.write(f"[ERROR] Failed to fetch data: {e}\n")
        sys.exit(1)
        
    if data.empty:
        sys.stderr.write("[ERROR] No data fetched from yfinance.\n")
        sys.exit(1)
        
    # If multiple tickers, columns are MultiIndex (Price, Ticker) -> Flatten to Ticker_Price
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = [f"{col[1]}_{col[0]}" for col in data.columns]
    else:
        # Single ticker case
        ticker = tickers[0]
        data.columns = [f"{ticker}_{col}" for col in data.columns]
        
    # Reset index to get Date as a column
    data = data.reset_index()
    # Normalize Date format
    data['Date'] = pd.to_datetime(data['Date']).dt.strftime('%Y-%m-%d')
    
    if args.only_close:
        keep_cols = ['Date'] + [col for col in data.columns if col.endswith('_Close')]
        data = data[keep_cols]
    
    data.to_csv(sys.stdout, index=False)

if __name__ == '__main__':
    main()
