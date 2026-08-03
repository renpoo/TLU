#!/usr/bin/env python3
# ==========================================
# _0_1_aggregate_stream.py
# TLU System: Pre-processing Layer
# Category: Stream Spatial & Temporal Aggregator
# Version: 6.0.0 (Refactored with BaseAggregator Architecture)
# ==========================================
import os
import sys

# Ensure repository root is on sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.filters.base_aggregator import BaseAggregator

class StreamAggregator(BaseAggregator):
    cli_description = "TLU General Multi-Column Stream Aggregator"
    default_interval = "week"

def main():
    agg = StreamAggregator()
    agg.run()

if __name__ == "__main__":
    main()
