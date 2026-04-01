import pandas as pd

# 1. データの読み込み
df = pd.read_csv("workspace/input_stream/Dummy_Kyoto_Traffic_Journal_Amount.csv")

# 2. Trans_Date列を日付（datetime）型に変換
df['Trans_Date'] = pd.to_datetime(df['Trans_Date'])

# 3. 日付から「年月（YYYY-MM）」形式の新しい列を作成
df['YearMonth'] = df['Trans_Date'].dt.strftime('%Y-%m')

# 4. 年月, Src, Tgt でグループ化し、Amountを合計（sum）
df_monthly = df.groupby(['YearMonth', 'Src', 'Tgt'], as_index=False)['Amount'].sum()

# 5. 結果を新しいCSVファイルとして保存
df_monthly.to_csv("workspace/input_stream/Dummy_Kyoto_Traffic_Journal_Monthly.csv", index=False, encoding="utf-8-sig")

# 確認用出力
print(f"集約完了: {len(df_monthly)} 行の月次データを作成しました。")
print(df_monthly.head())
