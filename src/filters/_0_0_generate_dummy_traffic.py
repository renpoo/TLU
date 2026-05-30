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
    parser.add_argument("--anomaly-node", type=str, default="ShijoKarasuma", help="Target intersection for the anomaly")
    parser.add_argument("--anomaly-start", type=int, default=360, help="Day when the anomaly starts")
    parser.add_argument("--anomaly-ratio", type=float, default=0.05, help="Outflow/inflow ratio at anomaly node during blockade")
    parser.add_argument("--detour-rate", type=float, default=0.80, help="Ratio of traffic redirected away from anomaly node")
    return parser

# rows = ["一条", "二条", "三条", "四条", "五条"]
# cols = ["堀川", "新町", "室町", "烏丸", "車屋町"]
rows = ["Ichijo", "Nijo", "Sanjo", "Shijo", "Gojo"]
cols = ["Horikawa", "Shinmachi", "Muromachi", "Karasuma", "Kurumayacho"]

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

    balances = {node: 10000.00 for node in nodes}

    # Pre-build neighbors topology map (Up, Down, Left, Right)
    neighbors_map = {}
    for r in range(len(rows)):
        for c in range(len(cols)):
            node = f"{rows[r]}{cols[c]}"
            nb = []
            if r - 1 >= 0: nb.append(f"{rows[r-1]}{cols[c]}")
            if r + 1 < len(rows): nb.append(f"{rows[r+1]}{cols[c]}")
            if c - 1 >= 0: nb.append(f"{rows[r]}{cols[c-1]}")
            if c + 1 < len(cols): nb.append(f"{rows[r]}{cols[c+1]}")
            neighbors_map[node] = nb

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

        # Pass 1: Calculate base traffic flow V_base for all existing grid links
        # Note: To match base volume calculations with original center distances
        V_base = {node: {} for node in nodes}
        for r_idx in range(len(rows)):
            for c_idx in range(len(cols)):
                current_node = f"{rows[r_idx]}{cols[c_idx]}"
                
                # Downward & Rightward edges only, to define double-directed base flow
                edges = []
                if r_idx + 1 < len(rows):
                    edges.append(f"{rows[r_idx+1]}{cols[c_idx]}")
                if c_idx + 1 < len(cols):
                    edges.append(f"{rows[r_idx]}{cols[c_idx+1]}")
                    
                for neighbor in edges:
                    dist_from_center = abs(r_idx - 3) + abs(c_idx - 3)
                    base_volume = max(20, 150 - dist_from_center * 20) * weekend_multiplier
                    
                    noise = 30 * math.sin(day * 0.1) + random.randint(-10, 20)
                    volume_A2B = max(1, int(base_volume + noise))
                    volume_B2A = max(1, int(base_volume + noise + random.randint(-10, 10)))
                    
                    V_base[current_node][neighbor] = volume_A2B
                    V_base[neighbor][current_node] = volume_B2A

        # Pass 2: Apply Anomaly Bottleneck and Bypass Detour dynamics
        V_final = {node: {} for node in nodes}
        for node in nodes:
            for nb in neighbors_map[node]:
                V_final[node][nb] = V_base[node][nb]

        anomaly_node = args.anomaly_node
        is_anomaly_active = (day >= args.anomaly_start)

        if is_anomaly_active and anomaly_node in nodes:
            for node in nodes:
                nbs = neighbors_map[node]
                
                # Case A: Restrict outflow from the anomaly node itself
                if node == anomaly_node:
                    for nb in nbs:
                        V_final[node][nb] = max(1, int(V_base[node][nb] * args.anomaly_ratio))
                    continue

                # Case B: Avoid going to the anomaly node (Bypass detour)
                if anomaly_node in nbs:
                    orig_to_anomaly = V_base[node][anomaly_node]
                    actual_to_anomaly = max(1, int(orig_to_anomaly * args.anomaly_ratio))
                    V_final[node][anomaly_node] = actual_to_anomaly

                    blocked_volume = orig_to_anomaly - actual_to_anomaly
                    detour_volume = int(blocked_volume * args.detour_rate)

                    healthy_nbs = [nb for nb in nbs if nb != anomaly_node]
                    if healthy_nbs and detour_volume > 0:
                        # Redistribute detour traffic evenly to other healthy neighbors
                        detour_per_node = detour_volume // len(healthy_nbs)
                        for h_nb in healthy_nbs:
                            V_final[node][h_nb] += detour_per_node

        # Pass 3: Enforce strict local mass conservation and log transactions
        for node in nodes:
            nbs = neighbors_map[node]
            total_out = sum(V_final[node][nb] for nb in nbs)
            
            if total_out > balances[node]:
                scale = balances[node] / total_out
                for nb in nbs:
                    V_final[node][nb] = int(V_final[node][nb] * scale)

            for nb in nbs:
                vol = V_final[node][nb]
                if vol > 0:
                    balances[node] -= vol
                    balances[nb] += vol
                    writer.writerow([date_str, node, nb, vol])

if __name__ == "__main__":
    parser = setup_argparser()
    args = parser.parse_args()
    generate_stream(args)
