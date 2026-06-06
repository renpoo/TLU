# 000. 財務基礎状態、構造剛性、および運動学 (Basic Statistics, Stiffness & Kinematics)

本ガイドは、Tensor-Link Utility (TLU) における統計分析、運動学、および構造剛性・PCAについて解説します。

---

## 000_0: 財務基礎状態と基本統計量

### 1. 財務状態の基本構造（貸借対照表 B/S & 損益計算書 P/L）

「B/Sブロック総計（`000_0_1__BS_Block_Total.png`）」は、B/Sをブロックのバランスとして可視化します。「P/Lウォーターフォール（`000_0_1__PL_Waterfall_Total.png`）」は、P/Lの利益構造を可視化します。これらを並べて、システムのマクロ構造を評価します。

#### 🟢 Sample 0 (正常代謝)

**臨床解説:**
資産と負債・自己資本が対称にバランスよく並びます。売上から費用が差し引かれます。純利益が残ります。健全な基礎構造です。

- ![Sample 0 BS Block Total](Sample_0_Healthy/readme_plots/000_0_1__BS_Block_Total.png)
- ![Sample 0 PL Waterfall](Sample_0_Healthy/readme_plots/000_0_1__PL_Waterfall_Total.png)

#### 🟡 Sample 1 (循環取引)

**臨床解説:**
売掛金が肥大化しています。P/Lでは売上高が大きいです。一方、費用は極小です。循環取引による架空の利益創出を示します。

- ![Sample 1 BS Block Total](Sample_1_Wash_Trade/readme_plots/000_0_1__BS_Block_Total.png)
- ![Sample 1 PL Waterfall](Sample_1_Wash_Trade/readme_plots/000_0_1__PL_Waterfall_Total.png)

#### 🔴 Sample 2 (資金横領)

**臨床解説:**
売上金は計上されています。回収された資金が簿外に漏洩しています。そのため、手元現預金が圧縮されます。ダミーの `UNKNOWN_LEAK` ノードが資産を構成しています。

- ![Sample 2 BS Block Total](Sample_2_Embezzlement_Leak/readme_plots/000_0_1__BS_Block_Total.png)
- ![Sample 2 PL Waterfall](Sample_2_Embezzlement_Leak/readme_plots/000_0_1__PL_Waterfall_Total.png)

#### 🟡 Sample 3 (入力ミス)

**臨床解説:**
仕訳の貸借一方のみを入力した一時的エラーです。B/Sの左右バランスが崩れます。残差が生じています。P/Lの営業収支は比較的正常に保たれています。

- ![Sample 3 BS Block Total](Sample_3_Unbalanced_Mistake/readme_plots/000_0_1__BS_Block_Total.png)
- ![Sample 3 PL Waterfall](Sample_3_Unbalanced_Mistake/readme_plots/000_0_1__PL_Waterfall_Total.png)

#### 🔴 Sample 4 (複合アノマリー)

**臨床解説:**
架空売上の水増しによる売掛金膨張が発生しています。また、横領による資金流出が同居しています。粉飾による肥大化と出血が同時に発生しています。

- ![Sample 4 BS Block Total](Sample_4_Composite_Chaos/readme_plots/000_0_1__BS_Block_Total.png)
- ![Sample 4 PL Waterfall](Sample_4_Composite_Chaos/readme_plots/000_0_1__PL_Waterfall_Total.png)

#### 🔴 Sample 5 (京都交差点網)

**臨床解説:**
交差点別の滞留車両数と流入流出です。主要交差点に滞留車両が偏っています。流動制限により流出ポテンシャルが崩壊しています。

- ![Sample 5 BS Block Total](Sample_5_Kyoto_Traffic/readme_plots/000_0_1__BS_Block_Total.png)
- ![Sample 5 PL Waterfall](Sample_5_Kyoto_Traffic/readme_plots/000_0_1__PL_Waterfall_Total.png)

#### 🟢 Sample 6 (株券流体)

**臨床解説:**
株券保有バランスと出来高です。出来高は大きいです。しかし、実需を伴う株式のやり取りはゼロに近いです。USR間での安定的な対流を示します。

- ![Sample 6 BS Block Total](Sample_6_Market_Stock_Flow/readme_plots/000_0_1__BS_Block_Total.png)
- ![Sample 6 PL Waterfall](Sample_6_Market_Stock_Flow/readme_plots/000_0_1__PL_Waterfall_Total.png)

#### 🟢 Sample 7 (現金流体)

**臨床解説:**
現金保有バランスと直接送金の出来高です。口座間での安定した取引媒介が行われています。不整合残差はありません。

- ![Sample 7 BS Block Total](Sample_7_Market_Cash_Flow/readme_plots/000_0_1__BS_Block_Total.png)
- ![Sample 7 PL Waterfall](Sample_7_Market_Cash_Flow/readme_plots/000_0_1__PL_Waterfall_Total.png)

#### 🔴 Sample 8 (fMRI 脳梗塞)

**臨床解説:**
脳葉別の酸素BOLD信号量と機能活動の収支バランスです。運動野の信号が激減しています。機能損失エリアがあります。これにより、脳全体の活動収支をマイナスに引き下げています。

- ![Sample 8 BS Block Total](Sample_8_fMRI_Stroke/readme_plots/000_0_1__BS_Block_Total.png)
- ![Sample 8 PL Waterfall](Sample_8_fMRI_Stroke/readme_plots/000_0_1__PL_Waterfall_Total.png)

#### 🔴 Sample 9 (fMRI てんかん発作)

**臨床解説:**
脳活動強度と活動収支です。側頭葉の活動が全体の酸素資源を独占しています。異常同調が発生しています。これにより、全体の認知機能ポテンシャルが損失しています。

- ![Sample 9 BS Block Total](Sample_9_fMRI_Seizure/readme_plots/000_0_1__BS_Block_Total.png)
- ![Sample 9 PL Waterfall](Sample_9_fMRI_Seizure/readme_plots/000_0_1__PL_Waterfall_Total.png)

---

### 2. 時系列トレンド・ダイナミクス（B/S & P/L トレンド）

累積的な変動推移（`BS_Trend` / `PL_Trend`）と、各期間ごとの単期変動（`BS_Trend_Periodic` / `PL_Trend_Periodic`）を対比させて分析します。

#### 🟢 Sample 0 (正常代謝)

**臨床解説:**
売上と費用が安定的に連動します。期末純利益が一定幅で成長を続ける理想的なパターンです。

- ![Sample 0 BS Trend](Sample_0_Healthy/readme_plots/000_0_1__BS_Trend.png)
- ![Sample 0 PL Trend](Sample_0_Healthy/readme_plots/000_0_1__PL_Trend.png)
- ![Sample 0 BS Trend Periodic](Sample_0_Healthy/readme_plots/000_0_1__BS_Trend_Periodic.png)
- ![Sample 0 PL Trend Periodic](Sample_0_Healthy/readme_plots/000_0_1__PL_Trend_Periodic.png)

#### 🟡 Sample 1 (循環取引)

**臨床解説:**
売上・売掛金が右肩上がりに膨張します。一方、営業費用は単期的にも完全に平坦です。商取引の自然なボラティリティや季節変動が観測されません。

- ![Sample 1 BS Trend](Sample_1_Wash_Trade/readme_plots/000_0_1__BS_Trend.png)
- ![Sample 1 PL Trend](Sample_1_Wash_Trade/readme_plots/000_0_1__PL_Trend.png)
- ![Sample 1 BS Trend Periodic](Sample_1_Wash_Trade/readme_plots/000_0_1__BS_Trend_Periodic.png)
- ![Sample 1 PL Trend Periodic](Sample_1_Wash_Trade/readme_plots/000_0_1__PL_Trend_Periodic.png)

#### 🔴 Sample 2 (資金横領)

**臨床解説:**
現預金が持続的に流出（減少）しています。P/L上は黒字として累積されています。売掛金の回収タイミングにもかかわらず、現預金の増分が極端に少ない状態です。資産の簿外流出が繰り返されています。

- ![Sample 2 BS Trend](Sample_2_Embezzlement_Leak/readme_plots/000_0_1__BS_Trend.png)
- ![Sample 2 PL Trend](Sample_2_Embezzlement_Leak/readme_plots/000_0_1__PL_Trend.png)
- ![Sample 2 BS Trend Periodic](Sample_2_Embezzlement_Leak/readme_plots/000_0_1__BS_Trend_Periodic.png)
- ![Sample 2 PL Trend Periodic](Sample_2_Embezzlement_Leak/readme_plots/000_0_1__PL_Trend_Periodic.png)

#### 🟡 Sample 3 (入力ミス)

**臨床解説:**
$t=1$ (2020-02) において、貸借が不一致の一時的仕訳ミスが発生しました。単期のトレンドにおいてB/SおよびP/Lに急激なノイズが発生しています。次期には修正されます。累積的にも一過性の変動として吸収されています。

- ![Sample 3 BS Trend](Sample_3_Unbalanced_Mistake/readme_plots/000_0_1__BS_Trend.png)
- ![Sample 3 PL Trend](Sample_3_Unbalanced_Mistake/readme_plots/000_0_1__PL_Trend.png)
- ![Sample 3 BS Trend Periodic](Sample_3_Unbalanced_Mistake/readme_plots/000_0_1__BS_Trend_Periodic.png)
- ![Sample 3 PL Trend Periodic](Sample_3_Unbalanced_Mistake/readme_plots/000_0_1__PL_Trend_Periodic.png)

#### 🔴 Sample 4 (複合アノマリー)

**臨床解説:**
架空売上による売掛金累積と利益累積が増加します。その裏で、期間ごとには多額の資金流出（横領）が記録されています。粉飾と実際の資金流出が対比されます。

- ![Sample 4 BS Trend](Sample_4_Composite_Chaos/readme_plots/000_0_1__BS_Trend.png)
- ![Sample 4 PL Trend](Sample_4_Composite_Chaos/readme_plots/000_0_1__PL_Trend.png)
- ![Sample 4 BS Trend Periodic](Sample_4_Composite_Chaos/readme_plots/000_0_1__BS_Trend_Periodic.png)
- ![Sample 4 PL Trend Periodic](Sample_4_Composite_Chaos/readme_plots/000_0_1__PL_Trend_Periodic.png)

#### 🔴 Sample 5 (京都交差点網)

**臨床解説:**
流入車両数と通過損失の推移です。アノマリーが発生した期において、車両数が急増（BS Trend）します。同時に、単期（Periodic）の滞留損失が拡大します。システム全体の流動ポテンシャルが一気に低下します。

- ![Sample 5 BS Trend](Sample_5_Kyoto_Traffic/readme_plots/000_0_1__BS_Trend.png)
- ![Sample 5 PL Trend](Sample_5_Kyoto_Traffic/readme_plots/000_0_1__PL_Trend.png)
- ![Sample 5 BS Trend Periodic](Sample_5_Kyoto_Traffic/readme_plots/000_0_1__BS_Trend_Periodic.png)
- ![Sample 5 PL Trend Periodic](Sample_5_Kyoto_Traffic/readme_plots/000_0_1__PL_Trend_Periodic.png)

#### 🟢 Sample 6 (株券流体)

**臨床解説:**
株式市場の出来高と保有推移です。累積取引量（P/L Trend）は上昇します。期間ごと（Periodic）には規則的対流が行われています。保有バランスも安定しています。

- ![Sample 6 BS Trend](Sample_6_Market_Stock_Flow/readme_plots/000_0_1__BS_Trend.png)
- ![Sample 6 PL Trend](Sample_6_Market_Stock_Flow/readme_plots/000_0_1__PL_Trend.png)
- ![Sample 6 BS Trend Periodic](Sample_6_Market_Stock_Flow/readme_plots/000_0_1__BS_Trend_Periodic.png)
- ![Sample 6 PL Trend Periodic](Sample_6_Market_Stock_Flow/readme_plots/000_0_1__PL_Trend_Periodic.png)

#### 🟢 Sample 7 (現金流体)

**臨床解説:**
口座間の現金保有バランスと直接送金の出来高です。取引量および残高の累積・単期推移の双方において、急激な偏りや断絶はありません。流動対流のもとでバランスを維持しています。

- ![Sample 7 BS Trend](Sample_7_Market_Cash_Flow/readme_plots/000_0_1__BS_Trend.png)
- ![Sample 7 PL Trend](Sample_7_Market_Cash_Flow/readme_plots/000_0_1__PL_Trend.png)
- ![Sample 7 BS Trend Periodic](Sample_7_Market_Cash_Flow/readme_plots/000_0_1__BS_Trend_Periodic.png)
- ![Sample 7 PL Trend Periodic](Sample_7_Market_Cash_Flow/readme_plots/000_0_1__PL_Trend_Periodic.png)

#### 🔴 Sample 8 (fMRI 脳梗塞)

**臨床解説:**
脳梗塞が発生します。TR=150 (t=30) の前後で、累積BOLD信号と機能収支がマイナスへ相転移します。単期の変動では、梗塞期に血流ポテンシャルが大暴落します。その後、低レベルで平坦に推移します。

- ![Sample 8 BS Trend](Sample_8_fMRI_Stroke/readme_plots/000_0_1__BS_Trend.png)
- ![Sample 8 PL Trend](Sample_8_fMRI_Stroke/readme_plots/000_0_1__PL_Trend.png)
- ![Sample 8 BS Trend Periodic](Sample_8_fMRI_Stroke/readme_plots/000_0_1__BS_Trend_Periodic.png)
- ![Sample 8 PL Trend Periodic](Sample_8_fMRI_Stroke/readme_plots/000_0_1__PL_Trend_Periodic.png)

#### 🔴 Sample 9 (fMRI てんかん発作)

**臨床解説:**
てんかん同調時のBOLD信号強度です。累積ではポテンシャルが減少します。単期の推移では、発作の周期に伴う活動強度の上下振動が同期して繰り返されます。

- ![Sample 9 BS Trend](Sample_9_fMRI_Seizure/readme_plots/000_0_1__BS_Trend.png)
- ![Sample 9 PL Trend](Sample_9_fMRI_Seizure/readme_plots/000_0_1__PL_Trend.png)
- ![Sample 9 BS Trend Periodic](Sample_9_fMRI_Seizure/readme_plots/000_0_1__BS_Trend_Periodic.png)
- ![Sample 9 PL Trend Periodic](Sample_9_fMRI_Seizure/readme_plots/000_0_1__PL_Trend_Periodic.png)
