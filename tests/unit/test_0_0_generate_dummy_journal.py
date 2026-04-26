import unittest
import io
import sys
from contextlib import redirect_stdout
import argparse
from src.filters._0_0_generate_dummy_journal import generate_stream

class TestGenerateDummyJournal(unittest.TestCase):
    def setUp(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("--months", type=int, default=1)
        self.parser.add_argument("--seed", type=int, default=42)
        self.parser.add_argument("--sales-leak-prob", type=float, default=0.0)
        self.parser.add_argument("--purchase-leak-prob", type=float, default=0.0)
        self.parser.add_argument("--wash-trade-prob", type=float, default=0.0)
        self.parser.add_argument("--unbalanced-mistake-prob", type=float, default=0.0)

    def test_balanced_entries(self):
        """Test that with 0.0 unbalanced probability, all entries strictly balance."""
        args = self.parser.parse_args(["--months", "1"])
        
        f = io.StringIO()
        with redirect_stdout(f):
            generate_stream(args)
            
        output = f.getvalue().strip().split('\n')
        header = output[0]
        data = output[1:]
        
        # Check balance per Entry_ID
        entries = {}
        for line in data:
            parts = line.split(',')
            entry_id = parts[0]
            debit = float(parts[4])
            credit = float(parts[5])
            
            if entry_id not in entries:
                entries[entry_id] = {'dr': 0.0, 'cr': 0.0}
            entries[entry_id]['dr'] += debit
            entries[entry_id]['cr'] += credit
            
        for entry_id, totals in entries.items():
            self.assertAlmostEqual(totals['dr'], totals['cr'], places=2, msg=f"Entry {entry_id} is unbalanced in normal mode.")

    def test_unbalanced_entries_injected(self):
        """Test that with 1.0 unbalanced probability, unbalanced entries are generated."""
        # 1.0 probability means every AR collection will be unbalanced.
        args = self.parser.parse_args(["--months", "2", "--unbalanced-mistake-prob", "1.0"])
        
        f = io.StringIO()
        with redirect_stdout(f):
            generate_stream(args)
            
        output = f.getvalue().strip().split('\n')
        data = output[1:]
        
        entries = {}
        for line in data:
            parts = line.split(',')
            entry_id = parts[0]
            debit = float(parts[4])
            credit = float(parts[5])
            
            if entry_id not in entries:
                entries[entry_id] = {'dr': 0.0, 'cr': 0.0}
            entries[entry_id]['dr'] += debit
            entries[entry_id]['cr'] += credit
            
        # We expect AT LEAST ONE entry to be unbalanced (specifically AR collections)
        unbalanced_count = sum(1 for totals in entries.values() if abs(totals['dr'] - totals['cr']) > 0.01)
        self.assertGreater(unbalanced_count, 0, "No unbalanced entries were generated despite prob=1.0")

if __name__ == '__main__':
    unittest.main()
