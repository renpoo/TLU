import pandas as pd
import random
import datetime
import csv
import sys

# 1. 設定：9x9の格子（京都の通り名をイメージ）
# rows = ["一条", "二条", "三条", "四条", "五条", "六条", "七条", "八条", "九条"]
# cols = ["堀川", "新町", "室町", "烏丸", "車屋", "東洞", "間之町", "堺町", "柳馬"]
rows = ["一条", "二条", "三条", "四条", "五条"]
cols = ["堀川", "新町", "室町", "烏丸", "車屋"]
# rows = ["Ichijo", "Nijo", "Sanjo", "Shijo", "Gojo", "Rokujo", "Shichijo", "Hachijo", "Kujo"]
# cols = ["Horikawa", "Shinmachi", "Muromachi", "Karasuma", "Kurumaya", "Higashinotoin", "Ainomachi", "Sakaimachi", "Yanaginobanba"]
# rows = ["Ichijo", "Nijo", "Sanjo", "Shijo", "Gojo"]
# cols = ["Horikawa", "Shinmachi", "Muromachi", "Karasuma", "Kurumaya"]


nodes = []
for r in rows:
    for c in cols:
        nodes.append(f"{r}{c}")

# 2. 隣接リストの作成（上下左右のみ結合）
transactions = []

start_date = datetime.date(2020, 1, 1)
total_days = 12 * 2 * 30 

writer = csv.writer(sys.stdout)
writer.writerow(["Trans_Date", "Src", "Tgt", "Amount"])

for day in range(total_days):
    current_date = start_date + datetime.timedelta(days=day)
    date_str = current_date.strftime("%Y-%m-%d")
    daily_entries = []

    for r_idx in range(len(rows)):
        for c_idx in range(len(cols)):
            current_node = f"{rows[r_idx]}{cols[c_idx]}"
            
            # 隣接する交差点を特定（右と下だけチェックすれば全エッジを網羅できる）
            neighbors = []
            if r_idx + 1 < len(rows): # 下方向
                neighbors.append(f"{rows[r_idx+1]}{cols[c_idx]}")
            if c_idx + 1 < len(cols): # 右方向
                neighbors.append(f"{rows[r_idx]}{cols[c_idx+1]}")
                
            for neighbor in neighbors:
                # 往復のトラフィックを生成（仕訳日記帳形式）
                # 交通量は中心部（四条烏丸付近）ほど多くなるよう重み付け
                dist_from_center = abs(r_idx - 3) + abs(c_idx - 3)
                base_volume = max(10, 100 - dist_from_center * 5)
                
                # A -> B
                transactions.append({
                    "Trans_Date": date_str,
                    "Src": current_node, # 貸方（出し手）
                    "Tgt": neighbor,      # 借方（受け手）
                    "Amount": base_volume + random.randint(0, 30)
                })
                # B -> A
                transactions.append({
                    "Trans_Date": date_str,
                    "Src": neighbor,
                    "Tgt": current_node,
                    "Amount": base_volume + random.randint(0, 30)
                })

# 3. CSVとして保存
df = pd.DataFrame(transactions)
df.to_csv("workspace/input_stream/Dummy_Kyoto_Traffic_Journal_Amount.csv", index=False, encoding="utf-8")

print(f"生成完了: {len(df)} 行のトラフィックデータを作成しました。")
print(df.head())
