#!/usr/bin/env python3
# ==========================================
# tests/unit/test_base_aggregator.py
# Unit tests for BaseAggregator framework
# ==========================================
import unittest
import pandas as pd
import argparse

from src.filters.base_aggregator import BaseAggregator

class DummyAggregator(BaseAggregator):
    cli_description = "Dummy Test Aggregator"

class TestBaseAggregator(unittest.TestCase):
    def test_process_aggregation_daily(self):
        agg = DummyAggregator()
        df = pd.DataFrame([
            {"t_idx": "2020-01-01 10:00:00", "src_idx": "A", "tgt_idx": "B", "value": 10.0},
            {"t_idx": "2020-01-01 14:00:00", "src_idx": "A", "tgt_idx": "B", "value": 20.0},
            {"t_idx": "2020-01-02 09:00:00", "src_idx": "A", "tgt_idx": "B", "value": 5.0},
        ])
        
        args = argparse.Namespace(
            interval="day",
            col_time="t_idx",
            col_src="src_idx",
            col_tgt="tgt_idx",
            col_val="value"
        )
        
        summary = agg.process_aggregation(df, args)
        self.assertEqual(len(summary), 2)
        self.assertEqual(summary.iloc[0]["value"], 30.0)
        self.assertEqual(summary.iloc[1]["value"], 5.0)

if __name__ == '__main__':
    unittest.main()
