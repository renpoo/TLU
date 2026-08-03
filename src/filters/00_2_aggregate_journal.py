#!/usr/bin/env python3
# ==========================================
# 00_2_aggregate_journal.py
# TLU System: Pre-processing Phase 0
# Category: Temporal & Spatial Journal Aggregator
# Version: 6.0.0 (Refactored with BaseAggregator Architecture)
# ==========================================
import os
import sys

# Ensure repository root is on sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.filters.base_aggregator import BaseAggregator

class JournalAggregator(BaseAggregator):
    cli_description = "Temporal aggregator for Journal COO."
    default_interval = "week"

def main():
    agg = JournalAggregator()
    agg.run()

if __name__ == "__main__":
    main()
