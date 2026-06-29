import unittest
import subprocess
import pandas as pd
import io
import os

class TestSkipInitialStream(unittest.TestCase):
    def setUp(self):
        self.script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src/filters/_0_2_skip_initial_stream.py'))

    def run_filter(self, input_csv, skip_seconds, col_time="Trans_Date"):
        cmd = ['python3', self.script_path, '--col_time', col_time, '--skip_seconds', str(skip_seconds)]
        res = subprocess.run(cmd, input=input_csv.encode('utf-8'), capture_output=True)
        return res

    def test_skip_behavior(self):
        csv_data = (
            "Trans_Date,Src,Tgt,Amount\n"
            "2024-01-01 10:00:00,A,B,10\n"
            "2024-01-01 10:00:05,A,B,20\n"
            "2024-01-01 10:00:15,A,B,30\n"
            "2024-01-01 10:00:20,A,B,40\n"
            "2024-01-01 10:00:25,A,B,50\n"
        )
        
        # Skip: 20 seconds.
        # Start is 10:00:00. Cutoff is 10:00:20.
        # Should keep 10:00:20 and 10:00:25, drop 00, 05, 15.
        res = self.run_filter(csv_data, 20)
        self.assertEqual(res.returncode, 0, res.stderr.decode('utf-8'))
        df = pd.read_csv(io.BytesIO(res.stdout))
        self.assertEqual(len(df), 2)
        self.assertEqual(df.iloc[0]['Trans_Date'], '2024-01-01 10:00:20')
        self.assertEqual(df.iloc[1]['Trans_Date'], '2024-01-01 10:00:25')

    def test_zero_skip(self):
        csv_data = (
            "Trans_Date,Src,Tgt,Amount\n"
            "2024-01-01 10:00:00,A,B,10\n"
        )
        res = self.run_filter(csv_data, 0)
        self.assertEqual(res.returncode, 0)
        df = pd.read_csv(io.BytesIO(res.stdout))
        self.assertEqual(len(df), 1)

if __name__ == '__main__':
    unittest.main()
