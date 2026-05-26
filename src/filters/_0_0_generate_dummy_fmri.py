# ==========================================
# _0_0_generate_dummy_fmri.py
# TLU System: Utility & Simulation Layer
# Category: Dummy Data Generation (Biological Network Model)
#
# THEORY & DOMAIN MAPPING:
# This script simulates an fMRI scan for a single patient (Patient Zero).
# - Measurement: The BOLD (Blood Oxygenation Level Dependent) signal.
# - Nodes: Standard macroscopic cortical regions (e.g., Prefrontal Cortex, Motor Cortex).
# - Flux (Src -> Tgt): Represents "Effective Connectivity" (因果的有効接続性). 
#   It models the directed causal influence, measuring how much the neural activity 
#   in one region drives the blood flow / metabolic activity in another region.
# ==========================================

import sys
import csv
import argparse
import random
import datetime
import math

def setup_argparser():
    parser = argparse.ArgumentParser(description="TLU fMRI Connectivity Generator")
    parser.add_argument("--pathology", type=str, default="healthy", choices=["healthy", "stroke", "seizure"], help="Type of pathology to inject")
    parser.add_argument("--seed", type=int, default=42, help="Random seed")
    parser.add_argument("--out-initial-state", type=str, default="", help="Path to write the initial state (Day 0) CSV")
    return parser

def generate_stream(args):
    start_date = datetime.datetime(2024, 1, 1, 10, 0, 0)
    total_trs = 300 # 300 TRs (approx 10 minutes at TR=2.0s).
    
    writer = csv.writer(sys.stdout)
    writer.writerow(["Trans_Date", "Src", "Tgt", "Amount"])
    
    nodes = ["Prefrontal_Cortex", "Motor_Cortex", "Visual_Cortex", "Parietal_Lobe", "Temporal_Lobe"]

    balances = {node: 100000.00 for node in nodes}
    if args.out_initial_state:
        with open(args.out_initial_state, "w", encoding="utf-8") as f:
            state_writer = csv.writer(f, lineterminator='\n')
            state_writer.writerow(["node_label", "initial_X"])
            for node in nodes:
                # baseline initial values (Must be large enough to sustain closed-loop flux without going negative)
                state_writer.writerow([node, f"{balances[node]:.2f}"])
    
    for tr in range(total_trs):
        current_date = start_date + datetime.timedelta(seconds=tr * 2)
        date_str = current_date.isoformat()
        
        t = tr * 0.1
        
        # To avoid directional bias, shuffle the source order each TR
        src_nodes = list(nodes)
        random.shuffle(src_nodes)
        
        for src in src_nodes:
            tgt_nodes = list(nodes)
            random.shuffle(tgt_nodes)
            for tgt in tgt_nodes:
                if src == tgt:
                    continue
                
                # Base organic flow (1/f pink noise approximation via overlapping sine waves)
                base_flux = 100 + 30 * math.sin(t * 0.5) + 20 * math.sin(t * 1.2) + random.uniform(-10, 10)
                
                # Apply pathology
                if args.pathology == "stroke" and tr >= 150:
                    if tgt == "Motor_Cortex":
                        base_flux = base_flux * 0.05 # 95% blockage
                
                elif args.pathology == "seizure" and tr >= 150:
                    if src == "Temporal_Lobe" or tgt == "Temporal_Lobe":
                        base_flux = 500 + 200 * math.sin(tr * 1.5)
                
                amount = round(base_flux, 2)
                
                # Enforce physical mass conservation
                if balances[src] < amount:
                    amount = balances[src]
                
                if amount >= 1.0:
                    balances[src] -= amount
                    balances[tgt] += amount
                    writer.writerow([date_str, src, tgt, f"{amount:.2f}"])

def main():
    parser = setup_argparser()
    args = parser.parse_args()
    random.seed(args.seed)
    generate_stream(args)

if __name__ == "__main__":
    main()
