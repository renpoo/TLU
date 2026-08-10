import unittest
import subprocess
import pandas as pd
import io
import os

class TestAggregateStream(unittest.TestCase):
    def setUp(self):
        self.script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src/filters/_0_1_aggregate_stream.py'))

    def run_agg(self, input_csv, interval, cols=None):
        if cols is None:
            cols = ["--col_time", "time", "--col_src", "src", "--col_tgt", "tgt", "--col_val", "val"]
        cmd = ['python3', self.script_path, '--interval', interval] + cols
        res = subprocess.run(cmd, input=input_csv.encode('utf-8'), capture_output=True)
        return res

    def test_macro_intervals(self):
        csv_data = "time,src,tgt,val\n2026-01-01 12:00:00,A,B,10\n2026-01-01 13:00:00,A,B,20\n2026-01-02 00:00:00,A,B,30\n"
        
        # Interval: day
        res = self.run_agg(csv_data, "day")
        self.assertEqual(res.returncode, 0, res.stderr.decode('utf-8'))
        df = pd.read_csv(io.BytesIO(res.stdout))
        self.assertEqual(len(df), 2)
        self.assertEqual(df.iloc[0]['time'], '2026-01-01')
        self.assertEqual(df.iloc[0]['val'], 30)

        # Interval: week
        res = self.run_agg(csv_data, "week")
        self.assertEqual(res.returncode, 0, res.stderr.decode('utf-8'))
        df = pd.read_csv(io.BytesIO(res.stdout))
        self.assertEqual(df.iloc[0]['time'], '2026-W01')

    def test_macro_intervals_with_coefficients(self):
        csv_data = (
            "time,src,tgt,val\n"
            "2026-01-01 12:00:00,A,B,10\n"
            "2026-02-15 12:00:00,A,B,20\n"
            "2026-03-20 12:00:00,A,B,30\n"
            "2027-01-01 12:00:00,A,B,40\n"
        )
        
        # Test: day 3
        # Groups: 1/1, 2/15, 3/20, 1/1(2027) will all be distinct since they are far apart.
        # But we'll test the day 3 grouping logic on consecutive days.
        consec_csv = (
            "time,src,tgt,val\n"
            "2026-01-01 12:00:00,A,B,10\n"
            "2026-01-02 12:00:00,A,B,20\n"
            "2026-01-03 12:00:00,A,B,30\n"
            "2026-01-04 12:00:00,A,B,40\n"
        )
        res = self.run_agg(consec_csv, "day 3")
        self.assertEqual(res.returncode, 0, res.stderr.decode('utf-8'))
        df = pd.read_csv(io.BytesIO(res.stdout))
        self.assertEqual(len(df), 2)
        self.assertEqual(df.iloc[0]['time'], '2026-01-01')
        self.assertEqual(df.iloc[0]['val'], 60)
        self.assertEqual(df.iloc[1]['time'], '2026-01-04')
        self.assertEqual(df.iloc[1]['val'], 40)

        # Test: month 2
        # Jan and Feb -> 2026-01 (Bin 1: 30)
        # Mar -> 2026-03 (Bin 2: 30)
        # Jan 2027 -> 2027-01 (Bin 3: 40)
        res = self.run_agg(csv_data, "month 2")
        self.assertEqual(res.returncode, 0, res.stderr.decode('utf-8'))
        df = pd.read_csv(io.BytesIO(res.stdout))
        self.assertEqual(len(df), 3)
        self.assertEqual(df.iloc[0]['time'], '2026-01')
        self.assertEqual(df.iloc[0]['val'], 30)
        self.assertEqual(df.iloc[1]['time'], '2026-03')
        self.assertEqual(df.iloc[1]['val'], 30)
        self.assertEqual(df.iloc[2]['time'], '2027-01')
        self.assertEqual(df.iloc[2]['val'], 40)

        # Test: quarter 4 (Q1, Q2, Q3, Q4 all group together to Q1)
        # All 2026 rows (Jan, Feb, Mar) -> 2026-Q1 (Bin 1: 60)
        # 2027 row -> 2027-Q1 (Bin 2: 40)
        res = self.run_agg(csv_data, "quarter 4")
        self.assertEqual(res.returncode, 0, res.stderr.decode('utf-8'))
        df = pd.read_csv(io.BytesIO(res.stdout))
        self.assertEqual(len(df), 2)
        self.assertEqual(df.iloc[0]['time'], '2026-Q1')
        self.assertEqual(df.iloc[0]['val'], 60)
        self.assertEqual(df.iloc[1]['time'], '2027-Q1')
        self.assertEqual(df.iloc[1]['val'], 40)

        # Test: year 2 (even year grouping, 2026 and 2027 group to 2026)
        # All rows -> 2026 (Total sum = 100)
        res = self.run_agg(csv_data, "year 2")
        self.assertEqual(res.returncode, 0, res.stderr.decode('utf-8'))
        df = pd.read_csv(io.BytesIO(res.stdout))
        self.assertEqual(len(df), 1)
        self.assertEqual(str(df.iloc[0]['time']), '2026')
        self.assertEqual(df.iloc[0]['val'], 100)

    def test_custom_intervals_english(self):
        csv_data = (
            "time,src,tgt,val\n"
            "2026-01-01 12:00:01,A,B,10\n"
            "2026-01-01 12:00:02,A,B,20\n"
            "2026-01-01 12:00:04,A,B,30\n"
        )
        # Interval: 3s
        res = self.run_agg(csv_data, "3s")
        self.assertEqual(res.returncode, 0, res.stderr.decode('utf-8'))
        df = pd.read_csv(io.BytesIO(res.stdout))
        self.assertEqual(len(df), 2)
        self.assertEqual(df.iloc[0]['time'], '2026-01-01 12:00:00')
        self.assertEqual(df.iloc[0]['val'], 30)
        self.assertEqual(df.iloc[1]['time'], '2026-01-01 12:00:03')
        self.assertEqual(df.iloc[1]['val'], 30)

        # Interval: second 3 (reverse order)
        res = self.run_agg(csv_data, "second 3")
        self.assertEqual(res.returncode, 0, res.stderr.decode('utf-8'))
        df2 = pd.read_csv(io.BytesIO(res.stdout))
        self.assertTrue(df.equals(df2))

        # Interval: 2 hour (baseline conversion)
        res = self.run_agg(csv_data, "2 hour")
        self.assertEqual(res.returncode, 0, res.stderr.decode('utf-8'))
        df = pd.read_csv(io.BytesIO(res.stdout))
        self.assertEqual(len(df), 1)
        self.assertEqual(df.iloc[0]['time'], '2026-01-01 12:00:00')

    def test_invalid_and_fallback(self):
        csv_data = "time,src,tgt,val\n2026-01-01 12:00:01,A,B,10\n"
        res = self.run_agg(csv_data, "invalid_interval")
        self.assertEqual(res.returncode, 0)
        df = pd.read_csv(io.BytesIO(res.stdout))
        self.assertEqual(df.iloc[0]['time'], '2026-01-01')

if __name__ == '__main__':
    unittest.main()
