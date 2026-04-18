#!/usr/bin/env python3
# ==========================================
# _0_1_preprocess_monthly_summary_for_traffic.py
# TLU System: Pre-filtering Layer
# Action: Monthly Aggregation of Traffic Data
# ==========================================

import pandas as pd

# 1. Read data
df = pd.read_csv("workspace/input_stream/Dummy_Kyoto_Traffic_Journal_Amount.csv")

# 2. Convert Trans_Date column to datetime type
df['Trans_Date'] = pd.to_datetime(df['Trans_Date'])

# 3. Create a new "YearMonth (YYYY-MM)" column from date
df['YearMonth'] = df['Trans_Date'].dt.strftime('%Y-%m')

# 4. Group by YearMonth, Src, Tgt and sum the Amount
df_monthly = df.groupby(['YearMonth', 'Src', 'Tgt'], as_index=False)['Amount'].sum()

# 5. Save the result as a new CSV file
df_monthly.to_csv("workspace/input_stream/Dummy_Kyoto_Traffic_Journal_Aggregated.csv", index=False, encoding="utf-8")

# Output for confirmation
print(f"Aggregation complete: Created {len(df_monthly)} rows of monthly data.")
print(df_monthly.head())
