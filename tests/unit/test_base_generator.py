#!/usr/bin/env python3
# ==========================================
# tests/unit/test_base_generator.py
# Unit tests for BaseGenerator framework
# ==========================================
import unittest
import tempfile
import os
import csv
import numpy as np

from src.filters.base_generator import BaseGenerator

class DummyGenerator(BaseGenerator):
    cli_description = "Dummy Test Generator"

class TestBaseGenerator(unittest.TestCase):
    def test_seed_setup(self):
        gen = DummyGenerator()
        gen.setup_seed(123)
        val1 = np.random.rand()
        
        gen.setup_seed(123)
        val2 = np.random.rand()
        self.assertEqual(val1, val2)

    def test_export_initial_state(self):
        gen = DummyGenerator()
        balances = {"Cash": 500.0, "Inventory": 300.0, "ZeroAcc": 0.0}
        
        with tempfile.NamedTemporaryFile(mode="w+", delete=False, suffix=".csv") as tmp:
            tmp_path = tmp.name

        try:
            gen.export_initial_state(tmp_path, balances)
            
            with open(tmp_path, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                rows = list(reader)
                
            self.assertEqual(rows[0], ["node_label", "initial_X"])
            self.assertEqual(rows[1], ["ACC_Cash", "500.00"])
            self.assertEqual(rows[2], ["ACC_Inventory", "300.00"])
            self.assertEqual(len(rows), 3) # ZeroAcc excluded
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)

if __name__ == '__main__':
    unittest.main()
