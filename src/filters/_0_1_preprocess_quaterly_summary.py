#!/usr/bin/env python3
# _00x_preprocess_quaterly_summary.py
import sys, pandas as pd

df = pd.read_csv(sys.stdin)

df["Month"] = df["TxnDate"].str.split("-").str[1].astype(int)
df["Quarter"] = "Q" + ((df["Month"] - 1) // 3 + 1).astype(str)

df = df.sort_values(["Quarter", "Month"])

df.to_csv(sys.stdout, index=False)
