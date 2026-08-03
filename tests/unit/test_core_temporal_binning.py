#!/usr/bin/env python3
# ==========================================
# tests/unit/test_core_temporal_binning.py
# Unit tests for core_temporal_binning.py
# ==========================================
import unittest
import pandas as pd

from src.core.core_temporal_binning import parse_interval_spec, apply_temporal_binning

class TestCoreTemporalBinning(unittest.TestCase):
    def test_parse_interval_spec(self):
        self.assertEqual(parse_interval_spec("week"), ("week", 1))
        self.assertEqual(parse_interval_spec("3d"), ("d", 3))
        self.assertEqual(parse_interval_spec("month 2"), ("month", 2))
        self.assertEqual(parse_interval_spec("12h"), ("h", 12))

    def test_apply_temporal_binning(self):
        dates = pd.to_datetime(["2020-01-01 10:00:00", "2020-01-02 15:30:00", "2020-01-15 00:00:00"])
        
        # Day
        binned_day = apply_temporal_binning(dates, "day")
        self.assertEqual(binned_day.iloc[0], "2020-01-01")
        self.assertEqual(binned_day.iloc[1], "2020-01-02")
        
        # Month
        binned_month = apply_temporal_binning(dates, "month")
        self.assertEqual(binned_month.iloc[0], "2020-01")
        self.assertEqual(binned_month.iloc[2], "2020-01")
        
        # Quarter
        binned_q = apply_temporal_binning(dates, "quarter")
        self.assertEqual(binned_q.iloc[0], "2020-Q1")

if __name__ == '__main__':
    unittest.main()
