import unittest
import subprocess
import pandas as pd
import io
import os

class TestParseJournal(unittest.TestCase):
    def test_parse_journal(self):
        script_path = os.path.join(os.path.dirname(__file__), '../../src/filters/00_1_parse_journal.py')
        input_csv = """Trans_Date,Entry_ID,Debit,Credit,Account_Name,Dept_Name
2026-01-01,1,100,0,ACC_Cash,DPT_A
2026-01-01,1,0,100,ACC_Sales,DPT_B
"""
        result = subprocess.run(['python3', script_path], input=input_csv.encode('utf-8'), capture_output=True)
        self.assertEqual(result.returncode, 0, f"Script failed: {result.stderr.decode('utf-8')}")
        
        out_df = pd.read_csv(io.BytesIO(result.stdout))
        self.assertEqual(len(out_df), 1)
        self.assertEqual(out_df.iloc[0]['src_idx'], 'ACC_Sales')
        self.assertEqual(out_df.iloc[0]['tgt_idx'], 'ACC_Cash')
        self.assertEqual(out_df.iloc[0]['value'], 100.0)

    def test_parse_journal_leak(self):
        script_path = os.path.join(os.path.dirname(__file__), '../../src/filters/00_1_parse_journal.py')
        # Unbalanced entry
        input_csv = """Trans_Date,Entry_ID,Debit,Credit,Account_Name,Dept_Name
2026-01-01,1,150,0,ACC_Cash,DPT_A
2026-01-01,1,0,100,ACC_Sales,DPT_B
"""
        result = subprocess.run(['python3', script_path], input=input_csv.encode('utf-8'), capture_output=True)
        self.assertEqual(result.returncode, 0)
        
        out_df = pd.read_csv(io.BytesIO(result.stdout))
        self.assertEqual(len(out_df), 2)
        base = out_df[out_df['tgt_idx'] == 'ACC_Cash']
        leak = out_df[out_df['src_idx'] == 'UNKNOWN_LEAK']
        
        self.assertEqual(base[base['src_idx'] == 'ACC_Sales']['value'].values[0], 100.0)
        self.assertEqual(leak['value'].values[0], 50.0)

if __name__ == '__main__':
    unittest.main()
