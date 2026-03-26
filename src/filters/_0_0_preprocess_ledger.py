#!/usr/bin/env python3
# _00x_preprocess_ledger.py
import pandas as pd
import sys

def main():
    # コマンドライン引数から入力ファイルと出力ファイルを受け取る（デフォルトも設定）
    input_file = sys.argv[1] if len(sys.argv) > 1 else 'General-Ledger.csv'
    output_file = sys.argv[2] if len(sys.argv) > 2 else 'General-Ledger-Amount.csv'

    # CSVを読み込む
    df = pd.read_csv(input_file)

    # 日付でソート
    df = df.sort_values(by='TxnDate')

    # 勘定科目には "ACC_" の prefix を付ける
    df['AccountName'] = df['AccountName'].apply(lambda x: f"ACC_{x}")

    # 部門には "DPT_" の prefix を付ける
    df['Dept'] = df['Dept'].apply(lambda x: f"DPT_{x}")
    
    # Debit と Credit を足して、新しい 'Amount' 列を作成する
    df['Amount'] = df['Debit'] + df['Credit']


    # 各フィールドでソート
    df = df.sort_values(by='Dept')
    df = df.sort_values(by='AccountName')
    df = df.sort_values(by='TxnDate')


    # 新しいCSVとして保存する (インデックス番号は出力しない)
    df.to_csv(output_file, index=False)
    print(f"✅ 'Amount'列を追加し、{output_file} に保存しました。")

if __name__ == '__main__':
    main()
