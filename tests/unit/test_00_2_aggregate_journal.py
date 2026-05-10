import unittest
import subprocess
import pandas as pd
import io
import os

class TestAggregateJournal(unittest.TestCase):
    def test_aggregate_journal_week(self):
        script_path = os.path.join(os.path.dirname(__file__), '../../src/filters/00_2_aggregate_journal.py')
        input_csv = """t_idx,src_idx,tgt_idx,value
2026-01-01,ACC_Sales,ACC_Cash,100
2026-01-02,ACC_Sales,ACC_Cash,200
2026-02-01,ACC_Sales,ACC_Cash,50
"""
        result = subprocess.run(['python3', script_path, '--interval', 'week'], input=input_csv.encode('utf-8'), capture_output=True)
        self.assertEqual(result.returncode, 0, f"Script failed: {result.stderr.decode('utf-8')}")
        
        out_df = pd.read_csv(io.BytesIO(result.stdout))
        self.assertEqual(len(out_df), 2)
        self.assertEqual(out_df.iloc[0]['t_idx'], '2026-W01')
        self.assertEqual(out_df.iloc[0]['value'], 300.0)
        self.assertEqual(out_df.iloc[1]['t_idx'], '2026-W05')
        self.assertEqual(out_df.iloc[1]['value'], 50.0)

    def test_aggregate_journal_day(self):
        script_path = os.path.join(os.path.dirname(__file__), '../../src/filters/00_2_aggregate_journal.py')
        input_csv = """t_idx,src_idx,tgt_idx,value
2026-01-01,ACC_Sales,ACC_Cash,100
2026-01-01,ACC_Sales,ACC_Cash,200
"""
        result = subprocess.run(['python3', script_path, '--interval', 'day'], input=input_csv.encode('utf-8'), capture_output=True)
        self.assertEqual(result.returncode, 0)
        
        out_df = pd.read_csv(io.BytesIO(result.stdout))
        self.assertEqual(len(out_df), 1)
        self.assertEqual(out_df.iloc[0]['t_idx'], '2026-01-01')
        self.assertEqual(out_df.iloc[0]['value'], 300.0)

if __name__ == '__main__':
    unittest.main()
