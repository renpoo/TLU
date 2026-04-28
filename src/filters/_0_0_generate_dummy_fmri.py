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
    return parser

def generate_stream(args):
    start_date = datetime.datetime(2024, 1, 1, 10, 0, 0)
    total_trs = 300 # 300 TRs (approx 10 minutes at TR=2.0s).
    
    writer = csv.writer(sys.stdout)
    writer.writerow(["Trans_Date", "Src", "Tgt", "Amount"])
    
    nodes = ["Prefrontal_Cortex", "Motor_Cortex", "Visual_Cortex", "Parietal_Lobe", "Temporal_Lobe"]
    
    for tr in range(total_trs):
        current_date = start_date + datetime.timedelta(seconds=tr * 2)
        date_str = current_date.isoformat()
        
        t = tr * 0.1
        
        for src in nodes:
            for tgt in nodes:
                if src == tgt:
                    continue
                
                # Base organic flow (1/f pink noise approximation via overlapping sine waves)
                # Adds deterministic oscillation + random noise
                base_flux = 100 + 30 * math.sin(t * 0.5) + 20 * math.sin(t * 1.2) + random.uniform(-10, 10)
                
                # Apply pathology
                if args.pathology == "stroke" and tr >= 150:
                    # Arterial blockage to Motor cortex
                    if tgt == "Motor_Cortex":
                        base_flux = base_flux * 0.05 # 95% blockage
                
                elif args.pathology == "seizure" and tr >= 150:
                    # Epileptic Hypersynchrony: Temporal lobe broadcasts massive deterministic wave
                    # To create a perfect Topological Feedback Loop (Spectral Radius = 1.0),
                    # we make the Temporal node both send and receive perfectly symmetric synchronized flux.
                    if src == "Temporal_Lobe" or tgt == "Temporal_Lobe":
                        base_flux = 500 + 200 * math.sin(tr * 1.5)
                
                # Ensure positive flow
                amount = max(1.0, round(base_flux, 2))
                
                writer.writerow([date_str, src, tgt, amount])

def main():
    parser = setup_argparser()
    args = parser.parse_args()
    random.seed(args.seed)
    generate_stream(args)

if __name__ == "__main__":
    main()
