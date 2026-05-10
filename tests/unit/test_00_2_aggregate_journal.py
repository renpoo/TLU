import subprocess
import pandas as pd
import io
import os

def test_aggregate_journal_week():
    script_path = os.path.join(os.path.dirname(__file__), '../../src/filters/00_2_aggregate_journal.py')
    input_csv = """t_idx,src_idx,tgt_idx,value
2026-01-01,ACC_Sales,ACC_Cash,100
2026-01-02,ACC_Sales,ACC_Cash,200
2026-02-01,ACC_Sales,ACC_Cash,50
"""
    result = subprocess.run(['python3', script_path, '--interval', 'week'], input=input_csv.encode('utf-8'), capture_output=True)
    assert result.returncode == 0, f"Script failed: {result.stderr.decode('utf-8')}"
    
    out_df = pd.read_csv(io.BytesIO(result.stdout))
    assert len(out_df) == 2
    assert out_df.iloc[0]['t_idx'] == '2026-W01'
    assert out_df.iloc[0]['value'] == 300.0
    # 2026-02-01 is week 4 or 5
    assert out_df.iloc[1]['t_idx'] == '2026-W04'
    assert out_df.iloc[1]['value'] == 50.0

def test_aggregate_journal_day():
    script_path = os.path.join(os.path.dirname(__file__), '../../src/filters/00_2_aggregate_journal.py')
    input_csv = """t_idx,src_idx,tgt_idx,value
2026-01-01,ACC_Sales,ACC_Cash,100
2026-01-01,ACC_Sales,ACC_Cash,200
"""
    result = subprocess.run(['python3', script_path, '--interval', 'day'], input=input_csv.encode('utf-8'), capture_output=True)
    assert result.returncode == 0
    
    out_df = pd.read_csv(io.BytesIO(result.stdout))
    assert len(out_df) == 1
    assert out_df.iloc[0]['t_idx'] == '2026-01-01'
    assert out_df.iloc[0]['value'] == 300.0
