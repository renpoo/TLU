import unittest
import subprocess
import pandas as pd
import io
import os

class TestTimeseriesToCoo(unittest.TestCase):
    def test_timeseries_to_coo(self):
        script_path = os.path.join(os.path.dirname(__file__), '../../src/filters/06_2_timeseries_to_coo.py')
        input_csv = """Date,^GSPC_Close,^VIX_Close
2020-01-01,3225.52,18.84
2020-01-02,3257.85,18.22
"""
        result = subprocess.run(['python3', script_path, '--dummy_src', 'Market_Offset'], input=input_csv.encode('utf-8'), capture_output=True)
        self.assertEqual(result.returncode, 0, f"Script failed: {result.stderr.decode('utf-8')}")
        
        out_df = pd.read_csv(io.BytesIO(result.stdout))
        
        # Expected rows = 2 days * 2 tickers = 4
        self.assertEqual(len(out_df), 4)
        
        # Check standard COO structure
        self.assertListEqual(list(out_df.columns), ['t_idx', 'src_idx', 'tgt_idx', 'value'])
        
        # Check first row
        self.assertEqual(out_df.iloc[0]['t_idx'], '2020-01-01')
        self.assertEqual(out_df.iloc[0]['src_idx'], 'Market_Offset')
        self.assertEqual(out_df.iloc[0]['tgt_idx'], '^GSPC_Close')
        self.assertEqual(out_df.iloc[0]['value'], 3225.52)

if __name__ == '__main__':
    unittest.main()
