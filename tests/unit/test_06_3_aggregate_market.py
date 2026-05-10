import unittest
import subprocess
import pandas as pd
import io
import os

class TestAggregateMarket(unittest.TestCase):
    def test_aggregate_market_position_vs_flux(self):
        script_path = os.path.join(os.path.dirname(__file__), '../../src/filters/06_3_aggregate_market.py')
        # Input COO data containing both a Position variable (^GSPC_Close) and a Flux variable (^GSPC_Volume)
        # 3 days of data, mapping to the same 'week' interval (e.g. 2020-W01)
        # And another week for the .diff() to show its effect
        input_csv = """t_idx,src_idx,tgt_idx,value
2020-01-01,Market_Offset,^GSPC_Close,100.0
2020-01-02,Market_Offset,^GSPC_Close,110.0
2020-01-03,Market_Offset,^GSPC_Close,120.0
2020-01-01,Market_Offset,^GSPC_Volume,10.0
2020-01-02,Market_Offset,^GSPC_Volume,20.0
2020-01-03,Market_Offset,^GSPC_Volume,30.0
2020-01-08,Market_Offset,^GSPC_Close,125.0
2020-01-09,Market_Offset,^GSPC_Close,130.0
2020-01-08,Market_Offset,^GSPC_Volume,15.0
2020-01-09,Market_Offset,^GSPC_Volume,25.0
"""
        # Execute script with interval=week
        result = subprocess.run(['python3', script_path, '--interval', 'week'], input=input_csv.encode('utf-8'), capture_output=True)
        self.assertEqual(result.returncode, 0, f"Script failed: {result.stderr.decode('utf-8')}")
        
        out_df = pd.read_csv(io.BytesIO(result.stdout))
        
        # We expect 2 weeks * 2 indicators = 4 rows
        self.assertEqual(len(out_df), 4)
        
        # Sort values to safely extract
        out_df = out_df.sort_values(['tgt_idx', 't_idx']).reset_index(drop=True)
        
        # Verify Position (State) Data (^GSPC_Close)
        # First week: The last observed absolute position was 120.0.
        # Since it is the first record, .diff().fillna(val) should retain 120.0.
        self.assertEqual(out_df.loc[0, 'tgt_idx'], '^GSPC_Close')
        self.assertEqual(out_df.loc[0, 'value'], 120.0)
        
        # Second week: The last observed absolute position was 130.0.
        # The .diff() between week 2 (130.0) and week 1 (120.0) is 10.0!
        self.assertEqual(out_df.loc[1, 'tgt_idx'], '^GSPC_Close')
        self.assertEqual(out_df.loc[1, 'value'], 10.0)
        
        # Verify Flux Data (^GSPC_Volume)
        # First week: The sum of flux is 10.0 + 20.0 + 30.0 = 60.0.
        # Volume should NOT be diffed.
        self.assertEqual(out_df.loc[2, 'tgt_idx'], '^GSPC_Volume')
        self.assertEqual(out_df.loc[2, 'value'], 60.0)
        
        # Second week: The sum of flux is 15.0 + 25.0 = 40.0.
        self.assertEqual(out_df.loc[3, 'tgt_idx'], '^GSPC_Volume')
        self.assertEqual(out_df.loc[3, 'value'], 40.0)

if __name__ == '__main__':
    unittest.main()
