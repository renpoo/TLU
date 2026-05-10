import subprocess
import pandas as pd
import io
import os

def test_parse_journal():
    script_path = os.path.join(os.path.dirname(__file__), '../../src/filters/00_1_parse_journal.py')
    input_csv = """Trans_Date,Entry_ID,Debit,Credit,Account_Name,Dept_Name
2026-01-01,1,100,0,ACC_Cash,DPT_A
2026-01-01,1,0,100,ACC_Sales,DPT_B
"""
    result = subprocess.run(['python3', script_path], input=input_csv.encode('utf-8'), capture_output=True)
    assert result.returncode == 0, f"Script failed: {result.stderr.decode('utf-8')}"
    
    out_df = pd.read_csv(io.BytesIO(result.stdout))
    assert len(out_df) == 1
    assert out_df.iloc[0]['src_idx'] == 'ACC_Sales'
    assert out_df.iloc[0]['tgt_idx'] == 'ACC_Cash'
    assert out_df.iloc[0]['value'] == 100.0

def test_parse_journal_leak():
    script_path = os.path.join(os.path.dirname(__file__), '../../src/filters/00_1_parse_journal.py')
    # Unbalanced entry
    input_csv = """Trans_Date,Entry_ID,Debit,Credit,Account_Name,Dept_Name
2026-01-01,1,150,0,ACC_Cash,DPT_A
2026-01-01,1,0,100,ACC_Sales,DPT_B
"""
    result = subprocess.run(['python3', script_path], input=input_csv.encode('utf-8'), capture_output=True)
    assert result.returncode == 0
    
    out_df = pd.read_csv(io.BytesIO(result.stdout))
    assert len(out_df) == 2
    # The base amount is 100
    base = out_df[out_df['tgt_idx'] == 'ACC_Cash']
    leak = out_df[out_df['src_idx'] == 'UNKNOWN_LEAK']
    
    assert base[base['src_idx'] == 'ACC_Sales']['value'].values[0] == 100.0
    assert leak['value'].values[0] == 50.0
