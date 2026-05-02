import pandas as pd
import random
import datetime
import csv
import sys
import argparse

def setup_argparser():
    parser = argparse.ArgumentParser(description="TLU Traffic Generator")
    parser.add_argument("--out-initial-state", type=str, default="", help="Path to write the initial state (Day 0) CSV")
    return parser

# 1. Configuration: 9x9 grid (inspired by Kyoto street names)
# rows = ["Ichijo", "Nijo", "Sanjo", "Shijo", "Gojo", "Rokujo", "Shichijo", "Hachijo", "Kujo"]
# cols = ["Horikawa", "Shinmachi", "Muromachi", "Karasuma", "Kurumaya", "Higashinotoin", "Ainomachi", "Sakaimachi", "Yanaginobanba"]
rows = ["一条", "二条", "三条", "四条", "五条"]
cols = ["堀川", "新町", "室町", "烏丸", "車屋町"]


nodes = []
for r in rows:
    for c in cols:
        nodes.append(f"{r}{c}")

# 2. Create adjacency list (connect only up, down, left, right)
transactions = []

def generate_stream(args):
    start_date = datetime.date(2020, 1, 1)
    total_days = 12 * 2 * 30 

    writer = csv.writer(sys.stdout)
    writer.writerow(["Trans_Date", "Src", "Tgt", "Amount"])

    if args.out_initial_state:
        with open(args.out_initial_state, "w", encoding="utf-8") as f:
            state_writer = csv.writer(f, lineterminator='\n')
            state_writer.writerow(["node_label", "initial_X"])
            for node in nodes:
                # Give a baseline static population/traffic at each node
                state_writer.writerow([node, f"{random.uniform(100, 500):.2f}"])

    for day in range(total_days):
        current_date = start_date + datetime.timedelta(days=day)
        date_str = current_date.strftime("%Y-%m-%d")
        daily_entries = []

        for r_idx in range(len(rows)):
            for c_idx in range(len(cols)):
                current_node = f"{rows[r_idx]}{cols[c_idx]}"
                
                # Identify adjacent intersections (checking only right and down covers all edges)
                neighbors = []
                if r_idx + 1 < len(rows): # Downward
                    neighbors.append(f"{rows[r_idx+1]}{cols[c_idx]}")
                if c_idx + 1 < len(cols): # Rightward
                    neighbors.append(f"{rows[r_idx]}{cols[c_idx+1]}")
                    
                for neighbor in neighbors:
                    # Generate round-trip traffic (journal entry format)
                    # Traffic is weighted to be heavier towards the center (near Shijo Karasuma)
                    dist_from_center = abs(r_idx - 3) + abs(c_idx - 3)
                    base_volume = max(10, 100 - dist_from_center * 5)
                    
                    # A -> B
                    transactions.append({
                        "Trans_Date": date_str,
                        "Src": current_node, # Credit (Sender)
                        "Tgt": neighbor,     # Debit (Receiver)
                        "Amount": base_volume + random.randint(0, 30)
                    })
                    # B -> A
                    transactions.append({
                        "Trans_Date": date_str,
                        "Src": neighbor,
                        "Tgt": current_node,
                        "Amount": base_volume + random.randint(0, 30)
                    })

    # 3. Save as CSV
    import os
    env_dir = os.environ.get("TARGET_ENV", "workspace")
    df = pd.DataFrame(transactions)
    df.to_csv(f"{env_dir}/input_stream/Dummy_Kyoto_Traffic_Journal_Amount.csv", index=False, encoding="utf-8")

    # print(f"Generation complete: Created {len(df)} rows of traffic data.", file=sys.stderr)

if __name__ == "__main__":
    parser = setup_argparser()
    args = parser.parse_args()
    generate_stream(args)
