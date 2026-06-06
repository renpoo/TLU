# 002_1. 情報幾何学とトポロジー (Information Geometry & Topology)

本ガイドは、Tensor-Link Utility (TLU) における情報幾何学分析モジュール（`002_1`）について、グラフの種類ごとに各検証サンプルの出力と数値に基づく臨床解説を縦列に整理したものです。

---

## 🔬 情報幾何学とトポロジーの物理数学理論

システムの状態確率分布の変位（構造変化の勢い）を、情報多様体上の距離尺度である**「KLダイバージェンス（KL Divergence Drift）」**として測定します。これにより、従来の統計Zスコア（Z-Score）が「茹でガエル現象（モデルの病的ベースライン学習）」によって沈黙する局面でも、構造の断裂（相転移）を鋭く検知します。

---

## 🧭 目次

- [ネットワーク・トポロジー時系列](#1-ネットワークトポロジー時系列-002_1_2__network_topologytpng)

---

## 📊 情報幾何学・トポロジーグラフと個別サンプルの所見

### 1. ネットワークトポロジー時系列 (`002_1_2__network_topology.t*.png`)

システム内のノード間における取引量や物理的流量を太いエッジで表現し、トポロジーの時系列進化を示した有向グラフです。

#### 🟢 Sample 0 (正常代謝)

**臨床解説:**
取引流量（エッジ）は各期を通して均等に分散・循環しており、特定の閉路が不自然に太く固定化されるようなトポロジーの偏りはありません。
![Sample 0 Topology t0](../../samples/Sample_0_Healthy/readme_plots/002_1_2__network_topology.t.00000.png)
![Sample 0 Topology t3](../../samples/Sample_0_Healthy/readme_plots/002_1_2__network_topology.t.00003.png)

#### 🟡 Sample 1 (循環取引)

**臨床解説:**
アノマリー開始の $t=0$ および $t=4$ において、`ACC_Cash` (現預金) と `ACC_Accounts_Receivable` (売掛金) の間に、極太の双方向還流エッジが直結して現れています。
![Sample 1 Topology t0](../../samples/Sample_1_Wash_Trade/readme_plots/002_1_2__network_topology.t.00000.png)
![Sample 1 Topology t3](../../samples/Sample_1_Wash_Trade/readme_plots/002_1_2__network_topology.t.00003.png)
![Sample 1 Topology t4](../../samples/Sample_1_Wash_Trade/readme_plots/002_1_2__network_topology.t.00004.png)
![Sample 1 Topology t5](../../samples/Sample_1_Wash_Trade/readme_plots/002_1_2__network_topology.t.00005.png)
![Sample 1 Topology t11](../../samples/Sample_1_Wash_Trade/readme_plots/002_1_2__network_topology.t.00011.png)

#### 🔴 Sample 2 (資金横領)

**臨床解説:**
アノマリーの進行に伴い、`Accounts_Receivable` から `UNKNOWN_LEAK` という簿外の吸い出し先ノードへ向かって資金がバイパス流出する、太い一方向のエッジが常態化しています。
![Sample 2 Topology t0](../../samples/Sample_2_Embezzlement_Leak/readme_plots/002_1_2__network_topology.t.00000.png)
![Sample 2 Topology t1](../../samples/Sample_2_Embezzlement_Leak/readme_plots/002_1_2__network_topology.t.00001.png)
![Sample 2 Topology t2](../../samples/Sample_2_Embezzlement_Leak/readme_plots/002_1_2__network_topology.t.00002.png)
![Sample 2 Topology t3](../../samples/Sample_2_Embezzlement_Leak/readme_plots/002_1_2__network_topology.t.00003.png)
![Sample 2 Topology t4](../../samples/Sample_2_Embezzlement_Leak/readme_plots/002_1_2__network_topology.t.00004.png)
![Sample 2 Topology t11](../../samples/Sample_2_Embezzlement_Leak/readme_plots/002_1_2__network_topology.t.00011.png)

#### 🟡 Sample 3 (入力ミス)

**臨床解説:**
$t=1$（2020-02）の片面入力エラーが生じた際、売掛金ノードの引き当て側のみが太く接続されますが、翌期にミスが修正されると、トポロジーは通常時の分散した接続状態に戻ります。
![Sample 3 Topology t0](../../samples/Sample_3_Unbalanced_Mistake/readme_plots/002_1_2__network_topology.t.00000.png)
![Sample 3 Topology t3](../../samples/Sample_3_Unbalanced_Mistake/readme_plots/002_1_2__network_topology.t.00003.png)
![Sample 3 Topology t4](../../samples/Sample_3_Unbalanced_Mistake/readme_plots/002_1_2__network_topology.t.00004.png)

#### 🔴 Sample 4 (複合アノマリー)

**臨床解説:**
循環取引の「双方向の架空還流エッジ」と、資金横領による「`UNKNOWN_LEAK` へのバイパス流出エッジ」がトポロジー上に同時に直結しており、極めて不自然な二極化を示しています。
![Sample 4 Topology t0](../../samples/Sample_4_Composite_Chaos/readme_plots/002_1_2__network_topology.t.00000.png)
![Sample 4 Topology t3](../../samples/Sample_4_Composite_Chaos/readme_plots/002_1_2__network_topology.t.00003.png)
![Sample 4 Topology t4](../../samples/Sample_4_Composite_Chaos/readme_plots/002_1_2__network_topology.t.00004.png)
![Sample 4 Topology t5](../../samples/Sample_4_Composite_Chaos/readme_plots/002_1_2__network_topology.t.00005.png)
![Sample 4 Topology t8](../../samples/Sample_4_Composite_Chaos/readme_plots/002_1_2__network_topology.t.00008.png)
![Sample 4 Topology t11](../../samples/Sample_4_Composite_Chaos/readme_plots/002_1_2__network_topology.t.00011.png)

#### 🔴 Sample 5 (京都交差点網)

**臨床解説:**
渋滞デッドロック（$t=51$）の発生後、ボトルネックである `23_四条烏丸` や `21_四条室町` の周辺エッジが極端に太く凝固（車両の滞留固着）し、周辺道路のエッジは白く消滅しています。
![Sample 5 Topology t0](../../samples/Sample_5_Kyoto_Traffic/readme_plots/002_1_2__network_topology.t.00000.png)
![Sample 5 Topology t6](../../samples/Sample_5_Kyoto_Traffic/readme_plots/002_1_2__network_topology.t.00006.png)
![Sample 5 Topology t12](../../samples/Sample_5_Kyoto_Traffic/readme_plots/002_1_2__network_topology.t.00012.png)
![Sample 5 Topology t18](../../samples/Sample_5_Kyoto_Traffic/readme_plots/002_1_2__network_topology.t.00018.png)
![Sample 5 Topology t24](../../samples/Sample_5_Kyoto_Traffic/readme_plots/002_1_2__network_topology.t.00024.png)
![Sample 5 Topology t50](../../samples/Sample_5_Kyoto_Traffic/readme_plots/002_1_2__network_topology.t.00050.png)
![Sample 5 Topology t51](../../samples/Sample_5_Kyoto_Traffic/readme_plots/002_1_2__network_topology.t.00051.png)
![Sample 5 Topology t52](../../samples/Sample_5_Kyoto_Traffic/readme_plots/002_1_2__network_topology.t.00052.png)
![Sample 5 Topology t53](../../samples/Sample_5_Kyoto_Traffic/readme_plots/002_1_2__network_topology.t.00053.png)

#### 🟡 Sample 6 (市場二部グラフ)

**臨床解説:**
市場二部グラフにおいて、共謀するボットアカウントと標的の銘柄ノードを結ぶ有向エッジが異常膨張し、市場全体の自律的な注文エッジを物理的に覆い隠しています。
![Sample 6 Topology t0](../../samples/Sample_6_Market_Stock_Flow/readme_plots/002_1_2__network_topology.t.00000.png)
![Sample 6 Topology t6](../../samples/Sample_6_Market_Stock_Flow/readme_plots/002_1_2__network_topology.t.00006.png)
![Sample 6 Topology t38](../../samples/Sample_6_Market_Stock_Flow/readme_plots/002_1_2__network_topology.t.00038.png)
![Sample 6 Topology t39](../../samples/Sample_6_Market_Stock_Flow/readme_plots/002_1_2__network_topology.t.00039.png)
![Sample 6 Topology t40](../../samples/Sample_6_Market_Stock_Flow/readme_plots/002_1_2__network_topology.t.00040.png)
![Sample 6 Topology t51](../../samples/Sample_6_Market_Stock_Flow/readme_plots/002_1_2__network_topology.t.00051.png)

#### 🟡 Sample 7 (市場資金移動)

**臨床解説:**
W41の共謀開始の瞬間、`USR_003` と `USR_004` の間に資金がキャッチボールされる極太の往復エッジが突然直結し、長期間にわたってこの間だけで流動性が拘束されている様子を示します。
![Sample 7 Topology t0](../../samples/Sample_7_Market_Cash_Flow/readme_plots/002_1_2__network_topology.t.00000.png)
![Sample 7 Topology t6](../../samples/Sample_7_Market_Cash_Flow/readme_plots/002_1_2__network_topology.t.00006.png)
![Sample 7 Topology t38](../../samples/Sample_7_Market_Cash_Flow/readme_plots/002_1_2__network_topology.t.00038.png)
![Sample 7 Topology t39](../../samples/Sample_7_Market_Cash_Flow/readme_plots/002_1_2__network_topology.t.00039.png)
![Sample 7 Topology t40](../../samples/Sample_7_Market_Cash_Flow/readme_plots/002_1_2__network_topology.t.00040.png)
![Sample 7 Topology t51](../../samples/Sample_7_Market_Cash_Flow/readme_plots/002_1_2__network_topology.t.00051.png)

#### 🔴 Sample 8 (fMRI 脳梗塞)

**臨床解説:**
梗塞（$t=30$）が起きた瞬間から、梗塞野（運動野）へ流入・流出するすべての機能的結合エッジがブラックアウト（消失）し、梗塞によるトポロジー断裂が視覚化されています。
![Sample 8 Topology t0](../../samples/Sample_8_fMRI_Stroke/readme_plots/002_1_2__network_topology.t.00000.png)
![Sample 8 Topology t29](../../samples/Sample_8_fMRI_Stroke/readme_plots/002_1_2__network_topology.t.00029.png)
![Sample 8 Topology t30](../../samples/Sample_8_fMRI_Stroke/readme_plots/002_1_2__network_topology.t.00030.png)
![Sample 8 Topology t31](../../samples/Sample_8_fMRI_Stroke/readme_plots/002_1_2__network_topology.t.00031.png)
![Sample 8 Topology t59](../../samples/Sample_8_fMRI_Stroke/readme_plots/002_1_2__network_topology.t.00059.png)

#### 🔴 Sample 9 (fMRI てんかん発作)

**臨床解説:**
てんかん同調バーストの発生に伴い、脳領野全体のBOLD活動エッジが極太の「過同期パターン」へと変質し、全脳が同一 of 振動キャッチボールにハックされています。
![Sample 9 Topology t0](../../samples/Sample_9_fMRI_Seizure/readme_plots/002_1_2__network_topology.t.00000.png)
![Sample 9 Topology t29](../../samples/Sample_9_fMRI_Seizure/readme_plots/002_1_2__network_topology.t.00029.png)
![Sample 9 Topology t30](../../samples/Sample_9_fMRI_Seizure/readme_plots/002_1_2__network_topology.t.00030.png)
![Sample 9 Topology t31](../../samples/Sample_9_fMRI_Seizure/readme_plots/002_1_2__network_topology.t.00031.png)
![Sample 9 Topology t59](../../samples/Sample_9_fMRI_Seizure/readme_plots/002_1_2__network_topology.t.00059.png)
