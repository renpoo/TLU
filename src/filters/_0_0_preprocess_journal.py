#!/usr/bin/env python3
# _0_0_preprocess_journal.py
import pandas as pd
import sys

def main():
    # コマンドライン引数から入力ファイルと出力ファイルを受け取る（デフォルトも設定）
    input_file = sys.argv[1] if len(sys.argv) > 1 else 'workspace/input_stream/Dummy_Journal_Stream.csv'
    output_file = sys.argv[2] if len(sys.argv) > 2 else 'workspace/input_stream/Dummy_Journal_Stream_Amount.csv'

    # CSVを読み込む
    df = pd.read_csv(input_file)

    # 日付でソート
    df = df.sort_values(by='Trans_Date')

    # 勘定科目には "ACC_" の prefix を付ける
    df['Account_Name'] = df['Account_Name'].apply(lambda x: f"ACC_{x}")

    # 部門には "DPT_" の prefix を付ける
    df['Dept_Name'] = df['Dept_Name'].apply(lambda x: f"DPT_{x}")
    
    # Debit と Credit を足して、新しい 'Amount' 列を作成する
    df['Amount'] = df['Debit'] + df['Credit']


    # 各フィールドでソート
    df = df.sort_values(by='Dept_Name')
    df = df.sort_values(by='Account_Name')
    df = df.sort_values(by='Trans_Date')
    df = df.sort_values(by='Entry_ID')

    # 新しいCSVとして保存する (インデックス番号は出力しない)
    df.to_csv(output_file, index=False)
    print(f"✅ 'Amount'列を追加し、{output_file} に保存しました。")

if __name__ == '__main__':
    main()
