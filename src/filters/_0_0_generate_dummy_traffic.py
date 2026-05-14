import random
import datetime
import csv
import sys
import argparse
import math

def setup_argparser():
    parser = argparse.ArgumentParser(description="TLU Traffic Generator")
    parser.add_argument("--out-initial-state", type=str, default="", help="Path to write the initial state (Day 0) CSV")
    parser.add_argument("--seed", type=int, default=42, help="Random seed")
    return parser

rows = ["一条", "二条", "三条", "四条", "五条"]
cols = ["堀川", "新町", "室町", "烏丸", "車屋町"]

nodes = []
for r in rows:
    for c in cols:
        nodes.append(f"{r}{c}")

def generate_stream(args):
    random.seed(args.seed)
    start_date = datetime.date(2020, 1, 1)
    total_days = 720 # 2 years

    writer = csv.writer(sys.stdout, lineterminator='\n')
    writer.writerow(["Trans_Date", "Src", "Tgt", "Amount"])

    balances = {node: 100000.00 for node in nodes}

    if args.out_initial_state:
        with open(args.out_initial_state, "w", encoding="utf-8") as f:
            state_writer = csv.writer(f, lineterminator='\n')
            state_writer.writerow(["node_label", "initial_X"])
            for node in nodes:
                # Baseline traffic capacity at each intersection (must be large enough)
                state_writer.writerow([node, f"{balances[node]:.2f}"])

    for day in range(total_days):
        current_date = start_date + datetime.timedelta(days=day)
        date_str = current_date.strftime("%Y-%m-%d")

        # Seasonal/Weekly variation (e.g. more traffic on weekends)
        weekend_multiplier = 1.5 if current_date.weekday() >= 5 else 1.0

        for r_idx in range(len(rows)):
            for c_idx in range(len(cols)):
                current_node = f"{rows[r_idx]}{cols[c_idx]}"
                
                neighbors = []
                if r_idx + 1 < len(rows): # Downward
                    neighbors.append(f"{rows[r_idx+1]}{cols[c_idx]}")
                if c_idx + 1 < len(cols): # Rightward
                    neighbors.append(f"{rows[r_idx]}{cols[c_idx+1]}")
                    
                for neighbor in neighbors:
                    # Traffic is heavier towards the center (Shijo Karasuma is r=3, c=3)
                    dist_from_center = abs(r_idx - 3) + abs(c_idx - 3)
                    base_volume = max(20, 150 - dist_from_center * 20) * weekend_multiplier
                    
                    # Add pink noise (organic fluctuation)
                    noise = 30 * math.sin(day * 0.1) + random.randint(-10, 20)
                    volume_A2B = max(1, int(base_volume + noise))
                    volume_B2A = max(1, int(base_volume + noise + random.randint(-10, 10)))
                    
                    # ⚠️ ANOMALY INJECTION: Traffic Gridlock / Blockade
                    # At day >= 360, a major construction/accident blocks Shijo Karasuma ("四条烏丸")
                    if day >= 360:
                        if current_node == "四条烏丸" or neighbor == "四条烏丸":
                            # Traffic flow drops to 5% of normal capacity (Severe bottleneck / Thrombus)
                            volume_A2B = max(1, int(volume_A2B * 0.05))
                            volume_B2A = max(1, int(volume_B2A * 0.05))

                    # Enforce strict mass conservation (A -> B)
                    if balances[current_node] < volume_A2B:
                        volume_A2B = int(balances[current_node])
                    if volume_A2B > 0:
                        balances[current_node] -= volume_A2B
                        balances[neighbor] += volume_A2B
                        writer.writerow([date_str, current_node, neighbor, volume_A2B])

                    # Enforce strict mass conservation (B -> A)
                    if balances[neighbor] < volume_B2A:
                        volume_B2A = int(balances[neighbor])
                    if volume_B2A > 0:
                        balances[neighbor] -= volume_B2A
                        balances[current_node] += volume_B2A
                        writer.writerow([date_str, neighbor, current_node, volume_B2A])

if __name__ == "__main__":
    parser = setup_argparser()
    args = parser.parse_args()
    generate_stream(args)
