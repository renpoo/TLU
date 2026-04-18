#!/usr/bin/env python3
# ==========================================
# _0_1_preprocess_monthly_summary_for_traffic.py
# TLU System: Pre-filtering Layer
# Action: Monthly Aggregation of Traffic Data
# ==========================================

import sys
import pandas as pd
from src.filters.cli_parser import parse_projector_args

# Load configuration bounds cleanly mapping explicitly to sys parameters if no CLI arguments are supplied
mapping_config = parse_projector_args(sys.argv[1:])
col_time = mapping_config.get("col_time", "Trans_Date")
col_src = mapping_config.get("col_src", "Src")
col_tgt = mapping_config.get("col_tgt", "Tgt")
col_val = mapping_config.get("col_val", "Amount")

# 1. Read data
df = pd.read_csv("workspace/input_stream/Dummy_Kyoto_Traffic_Journal_Amount.csv")

# 2. Convert mapped time column to datetime type & Format directly bypassing manual YearMonth creation
df[col_time] = pd.to_datetime(df[col_time]).dt.strftime('%Y-%m')

# 4. Group strictly by mapped columns
df_monthly = df.groupby([col_time, col_src, col_tgt], as_index=False)[col_val].sum()

# 5. Save the result as a new CSV file
df_monthly.to_csv("workspace/input_stream/Dummy_Kyoto_Traffic_Journal_Aggregated.csv", index=False, encoding="utf-8")

# Output for confirmation
print(f"Aggregation complete: Created {len(df_monthly)} rows of monthly data.")
print(df_monthly.head())
