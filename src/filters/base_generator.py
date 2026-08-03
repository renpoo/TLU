#!/usr/bin/env python3
# ==========================================
# src/filters/base_generator.py
# TLU Base Generator Framework
# ==========================================
"""!
@file base_generator.py
@brief Standard Base Framework for TLU Dummy Data Generators.
@details Handles seed initialization, common CLI parameters (--seed, --months, --out-initial-state),
         and Day 0 initial state CSV export.
"""

import sys
import csv
import argparse
import random
import numpy as np
from typing import Dict, Any, Optional

class BaseGenerator:
    """!
    @brief Abstract Base Class for TLU Synthetic Data Generators.
    """
    cli_description: str = "TLU Dummy Data Generator"

    def __init__(self):
        self.parser = argparse.ArgumentParser(description=self.cli_description)
        self.add_common_arguments()
        self.add_arguments(self.parser)

    def add_common_arguments(self):
        self.parser.add_argument("--months", type=int, default=12, help="Period to generate (in months)")
        self.parser.add_argument("--seed", type=int, default=42, help="Random seed for reproducibility")
        self.parser.add_argument("--out-initial-state", type=str, default="", help="Path to write the initial state (Day 0) CSV")

    def add_arguments(self, parser: argparse.ArgumentParser):
        """Override in subclass to add generator-specific CLI arguments."""
        pass

    def setup_seed(self, seed: int):
        """Set random seeds for both Python random and NumPy."""
        random.seed(seed)
        np.random.seed(seed)

    def export_initial_state(self, filepath: str, balances: Dict[str, float], prefix: str = "ACC_"):
        """!
        @brief Export opening accounting/physical balances to Day 0 CSV.
        """
        if not filepath:
            return
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                writer = csv.writer(f, lineterminator='\n')
                writer.writerow(["node_label", "initial_X"])
                for label, val in balances.items():
                    if val > 0:
                        node_name = f"{prefix}{label}" if not label.startswith(prefix) else label
                        writer.writerow([node_name, f"{val:.2f}"])
        except Exception as e:
            print(f"[WARN] Failed to write initial state to {filepath}: {e}", file=sys.stderr)

    def generate(self, args: argparse.Namespace):
        """!
        @brief Main generation logic. Must be implemented by subclass.
        """
        raise NotImplementedError("Subclasses must implement generate()")

    def run(self):
        args = self.parser.parse_args()
        self.setup_seed(args.seed)
        self.generate(args)
