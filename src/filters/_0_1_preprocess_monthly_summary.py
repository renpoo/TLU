#!/usr/bin/env python3
# ==========================================
# _0_1_preprocess_monthly_summary.py
# TLU System: Pre-filtering Layer
# Action: Monthly Aggregation of Journal Entries (Account:Dept Level)
# ==========================================
import sys
import pandas as pd

def main():
    try:
        # 1. 標準入力からストリームを読み込む
        df = pd.read_csv(sys.stdin)
    except Exception as e:
        print(f"Error reading input: {e}", file=sys.stderr)
        sys.exit(1)

    if df.empty:
        sys.exit(0)

    # 2. Trans_Date から「YYYY-MM」形式の月次ラベルを作成
    df['Month'] = pd.to_datetime(df['Trans_Date']).dt.strftime('%Y-%m')

    # 3. 貸借（Debit / Credit）のフラックスを単一の「ノード間の移動（From -> To）」に再構成する
    debits = df[df['Debit'] > 0][['Entry_ID', 'Month', 'Account_Name', 'Dept_Name', 'Debit']].rename(
        columns={'Account_Name': 'Tgt_Account', 'Dept_Name': 'Tgt_Dept', 'Debit': 'Amount'}
    )
    
    credits = df[df['Credit'] > 0][['Entry_ID', 'Account_Name', 'Dept_Name']].rename(
        columns={'Account_Name': 'Src_Account', 'Dept_Name': 'Src_Dept'}
    )
    
    # Entry_ID で結合し、1行で Source -> Target を表現
    edges = pd.merge(debits, credits, on='Entry_ID', how='inner')

    # 4. 勘定科目と部門を ':' で連結し、一意のノード名を作成
    edges['Trans_Date'] = edges['Month']
    edges['Src'] = edges['Src_Account'].astype(str)
    edges['Tgt'] = edges['Tgt_Account'].astype(str)
    # edges['Src'] = edges['Src_Dept'].astype(str)
    # edges['Tgt'] = edges['Tgt_Dept'].astype(str)
    # edges['Src'] = edges['Src_Account'].astype(str) + ':' + edges['Src_Dept'].astype(str)
    # edges['Tgt'] = edges['Tgt_Account'].astype(str) + ':' + edges['Tgt_Dept'].astype(str)

    # 5. 月、Sourceノード、Targetノード の組み合わせで金額（Amount）を合計（集約）
    monthly_summary = edges.groupby(['Trans_Date', 'Src', 'Tgt'])['Amount'].sum().reset_index()

    # 6. TLU Projector が読めるフラットな COO 形式に再フォーマット
    monthly_summary.to_csv(sys.stdout, index=False)

if __name__ == "__main__":
    main()
