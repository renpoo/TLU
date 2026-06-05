# 001_3. 局所温度分析 (Local Temperature)

本ガイドは、Tensor-Link Utility (TLU) における「3次元局所温度（`001_1_2_2__3d_local_temperature.png`）」について、各検証サンプルの出力と数値に基づく臨床解説を整理したものです。

---

## 🔬 物理数学理論：局所温度 $T_i$
TLUは、各ノード $i$ における流量のボラティリティ（時間的変動の標準偏差）を「局所温度 $T_i$」と定義します。これは、ノードの活動量および残高の瞬間的な変動の激しさを表します。

$$T_i \propto \text{StdDev}(X_i(t))$$

活動が過熱すると局所温度は急上昇し、逆に活動がフリーズ（膠着または壊死）すると温度は絶対零度に向けて降下します。

---

## 📊 3次元局所温度と個別サンプルの所見

各ノードごとの時間的残高ボラティリティ（標準偏差）の時空間変化を示す3次元グラフです。

#### 🟢 Sample 0 (正常代謝)
**臨床解説:**
局所的な温度の過度な偏在（局所スパイク）はなく、システム全体がなだらかで均一な流動代謝状態（適正温度）に保たれています。
- ![Sample 0 Local Temp](Sample_0_Healthy/readme_plots/001_1_2_2__3d_local_temperature.png)

#### 🟡 Sample 1 (循環取引)
**臨床解説:**
循環取引発生と同期して、還流の軸である `ACC_Cash`、`ACC_Accounts_Receivable`、`ACC_Sales_Revenue` の3ノードが同時に巨大な山のように過熱（時間的ボラティリティの急上昇）しています。
- ![Sample 1 Local Temp](Sample_1_Wash_Trade/readme_plots/001_1_2_2__3d_local_temperature.png)

#### 🔴 Sample 2 (資金横領)
**臨床解説:**
漏洩（横領）が発生している期間、現金預金口座の活動ボラティリティ（温度）が継続的に過熱しており、簿外へのバイパス移動に伴う残高の激しい動的スパイクを捉えています。
- ![Sample 2 Local Temp](Sample_2_Embezzlement_Leak/readme_plots/001_1_2_2__3d_local_temperature.png)

#### 🟡 Sample 3 (入力ミス)
**臨床解説:**
片面入力エラーが生じた $t=1$ に、該当勘定ノードのローリング標準偏差が一時的に爆発して鋭い温度の塔を形成しますが、修正とともに翌ステップには瞬時に平穏化します。
- ![Sample 3 Local Temp](Sample_3_Unbalanced_Mistake/readme_plots/001_1_2_2__3d_local_temperature.png)

#### 🔴 Sample 4 (複合アノマリー)
**臨床解説:**
還流による往復取引の過熱と、横領による漏洩流出の過熱が重なり、複数の箇所でボラティリティ温度が巨大な火柱のように立ち上がっています。
- ![Sample 4 Local Temp](Sample_4_Composite_Chaos/readme_plots/001_1_2_2__3d_local_temperature.png)

#### 🔴 Sample 5 (京都交差点網)
**臨床解説:**
交差点網の局所温度です。ボトルネック交差点の `23_四条烏丸` 付近が、デッドロックによる完全フリーズによって青色（局所温度急降下 $T_i=1.87$）を示す「コールドアイランド現象」が発生しています。
- ![Sample 5 Local Temp](Sample_5_Kyoto_Traffic/readme_plots/001_1_2_2__3d_local_temperature.png)

#### 🟢 Sample 6 (株券流体)
**臨床解説:**
ボット間取引は高速ですが、保存則に基づき全体の保有バランスは厳しく制御されています。そのため、異常なボラティリティの偏り（局所過熱）はなく、空間的な局所温度は完全に平穏な範囲に収まっています。
- ![Sample 6 Local Temp](Sample_6_Market_Stock_Flow/readme_plots/001_1_2_2__3d_local_temperature.png)

#### 🟢 Sample 7 (現金流体)
**臨床解説:**
ユーザー間の分散送金決済フロー。一部の取引口座で送金量が活発になっても、システム全体として残高の急激な偏りや断絶は発生しないため、全期間・全ノードにおいて局所温度は適正な平衡状態を保っています。
- ![Sample 7 Local Temp](Sample_7_Market_Cash_Flow/readme_plots/001_1_2_2__3d_local_temperature.png)

#### 🔴 Sample 8 (fMRI 脳梗塞)
**臨床解説:**
梗塞が発生した $t=30$ 以降、運動野（額葉）周辺のBOLD信号の標準偏差（ボラティリティ）が不可逆に消失します。この領域の局所温度は絶対零度付近まで急激に冷え込み、トポロジー上に青く沈んだ広大な「コールドアイランド（熱的虚脱）」が形成されます。
- ![Sample 8 Local Temp](Sample_8_fMRI_Stroke/readme_plots/001_1_2_2__3d_local_temperature.png)

#### 🔴 Sample 9 (fMRI てんかん発作)
**臨床解説:**
てんかんの異常高周波振動により、脳全体のBOLD信号が激しくボラティリティを変動させます。これにより、脳のほぼ全領域が限界値まで過熱し、空間全体が一斉に真っ赤に染まる「全脳熱的過熱（ハイパーサーミア）」状態を引き起こします。
- ![Sample 9 Local Temp](Sample_9_fMRI_Seizure/readme_plots/001_1_2_2__3d_local_temperature.png)
