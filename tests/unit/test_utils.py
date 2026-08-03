#!/usr/bin/env python3
# ==========================================
# tests/unit/test_utils.py
# Unit tests for src/utils/ modules
# ==========================================
import unittest
import tempfile
import os
import json
import pandas as pd

from src.utils._99_export_json_summary import export_summary_json

class TestUtils(unittest.TestCase):
    def test_export_summary_json_empty_dir(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            summary = export_summary_json(tmp_dir)
            self.assertIn("metadata", summary)
            self.assertIn("thermodynamics", summary)

    def test_export_summary_json_with_mock_csv(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            csv_path = os.path.join(tmp_dir, "result.000_1_1_filter_dynamics.analysis.csv")
            df = pd.DataFrame([{"t_idx": 0, "net_flux": 100.0}])
            df.to_csv(csv_path, index=False)
            
            summary = export_summary_json(tmp_dir)
            self.assertIn("dynamics", summary["thermodynamics"])
            self.assertEqual(len(summary["thermodynamics"]["dynamics"]), 1)
            self.assertEqual(summary["thermodynamics"]["dynamics"][0]["net_flux"], 100.0)

if __name__ == '__main__':
    unittest.main()
