#!/usr/bin/env python3
import sys
import pandas as pd

def main():
    try:
        df = pd.read_csv(sys.stdin)
    except Exception as e:
        print(f"Error reading input stream: {e}", file=sys.stderr)
        sys.exit(1)

    if df.empty:
        sys.exit(0)

    # df has columns: Timestamp, Stock_ID, Seller_ID, Buyer_ID, Price, Volume
    
    # Leg 1: Market clears to Buyer (Stock -> Buyer)
    leg1 = df[['Timestamp', 'Stock_ID', 'Buyer_ID', 'Price', 'Volume']].copy()
    leg1 = leg1.rename(columns={'Stock_ID': 'Src', 'Buyer_ID': 'Tgt'})

    # Leg 2: Seller clears to Market (Seller -> Stock)
    leg2 = df[['Timestamp', 'Seller_ID', 'Stock_ID', 'Price', 'Volume']].copy()
    leg2 = leg2.rename(columns={'Seller_ID': 'Src', 'Stock_ID': 'Tgt'})

    # Combine both legs
    bipartite_df = pd.concat([leg1, leg2], ignore_index=True)
    
    # Sort by Timestamp to maintain temporal order
    bipartite_df = bipartite_df.sort_values(by='Timestamp')

    # Output to stdout
    bipartite_df.to_csv(sys.stdout, index=False)

if __name__ == "__main__":
    main()
