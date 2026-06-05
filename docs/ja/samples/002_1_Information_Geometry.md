# 002. 情報幾何学と相対保存則 (Information Geometry & Forensics)

本ガイドは、Tensor-Link Utility (TLU) における情報幾何学分析モジュール（`002_1`）を説明します。グラフの種類ごとに、各サンプルの出力と数値に基づく解説を記載します。

---

## 🔬 情報幾何学と質量保存則の理論

閉鎖型の実体ネットワークにおいては、キルヒホッフの第一法則（電流則＝質量保存則）が成立します。ノードへの総入力流量と総出力流量の差分を「保存残差 (Conservation Residual)」または「相対漏洩率 (Relative Leak Ratio)」と定義します。

$$Residual_i = \sum Flux_{in} - \sum Flux_{out}$$

正常な会計記帳や物理的流通では、ダブルエントリー（借貸平均）の制約があります。この残差値は常に `0.00` となります。この値が正の値として長期にわたって検知された場合、質量（資金・車両）がシステム外へバイパス流出（簿外横領など）していることを証明します。

システムの状態確率分布の変位（構造変化の勢い）を、情報多様体上の距離尺度である「KLダイバージェンス（KL Divergence Drift）」として測定します。これにより、従来の統計Zスコア（Z-Score）が検知できない構造の断裂（相転移）を検知します。

---

## 📊 情報幾何学・トポロジーグラフと個別サンプルの所見

### 1. ネットワークトポロジー時系列 (`002_1_2__network_topology.t*.png`)

システム内のノード間における取引量や物理的流量をエッジの太さで表現します。トポロジーの時系列変化を示す有向グラフです。

#### 🟢 Sample 0 (正常代謝)

**臨床解説:**
取引流量（エッジ）は各期を通して分散・循環しています。特定の閉路が太く固定化されるようなトポロジーの偏りはありません。
![Sample 0 Topology t0](Sample_0_Healthy/readme_plots/002_1_2__network_topology.t.00000.png)
![Sample 0 Topology t3](Sample_0_Healthy/readme_plots/002_1_2__network_topology.t.00003.png)

#### 🟡 Sample 1 (循環取引)

**臨床解説:**
アノマリー開始の $t=0$ および $t=4$ において、`ACC_Cash` と `ACC_Accounts_Receivable` の間に双方向還流エッジが接続されます。
![Sample 1 Topology t0](Sample_1_Wash_Trade/readme_plots/002_1_2__network_topology.t.00000.png)
![Sample 1 Topology t3](Sample_1_Wash_Trade/readme_plots/002_1_2__network_topology.t.00003.png)
![Sample 1 Topology t4](Sample_1_Wash_Trade/readme_plots/002_1_2__network_topology.t.00004.png)
![Sample 1 Topology t5](Sample_1_Wash_Trade/readme_plots/002_1_2__network_topology.t.00005.png)
![Sample 1 Topology t11](Sample_1_Wash_Trade/readme_plots/002_1_2__network_topology.t.00011.png)

#### 🔴 Sample 2 (資金横領)

**臨床解説:**
アノマリーが進行します。`Accounts_Receivable` から `UNKNOWN_LEAK` というノードへ資金がバイパス流出します。一方向のエッジが常態化します。
![Sample 2 Topology t0](Sample_2_Embezzlement_Leak/readme_plots/002_1_2__network_topology.t.00000.png)
![Sample 2 Topology t1](Sample_2_Embezzlement_Leak/readme_plots/002_1_2__network_topology.t.00001.png)
![Sample 2 Topology t2](Sample_2_Embezzlement_Leak/readme_plots/002_1_2__network_topology.t.00002.png)
![Sample 2 Topology t3](Sample_2_Embezzlement_Leak/readme_plots/002_1_2__network_topology.t.00003.png)

#### 🟡 Sample 3 (入力ミス)

**臨床解説:**
$t=1$（2020-02）に片面入力エラーが発生します。売掛金ノードの片側のみが接続されて貸借不一致を示します。翌期（$t=2$ 以降）にミスが修正されます。トポロジーは通常時の分散した接続状態に戻ります。

- ![Sample 3 Topology t0 (通常)](Sample_3_Unbalanced_Mistake/readme_plots/002_1_2__network_topology.t.00000.png)
- ![Sample 3 Topology t1 (エラー発生)](Sample_3_Unbalanced_Mistake/readme_plots/002_1_2__network_topology.t.00001.png)
- ![Sample 3 Topology t2 (エラー発生直後)](Sample_3_Unbalanced_Mistake/readme_plots/002_1_2__network_topology.t.00002.png)
- ![Sample 3 Topology t3 (エラー解消通常)](Sample_3_Unbalanced_Mistake/readme_plots/002_1_2__network_topology.t.00003.png)
- ![Sample 3 Topology t4 (エラー解消後)](Sample_3_Unbalanced_Mistake/readme_plots/002_1_2__network_topology.t.00004.png)

#### 🔴 Sample 4 (複合アノマリー)

**臨床解説:**
循環取引による双方向の還流エッジと、資金横領による `UNKNOWN_LEAK` へのバイパス流出エッジが同時に現れます。トポロジーの二極化を示します。
![Sample 4 Topology t0](Sample_4_Composite_Chaos/readme_plots/002_1_2__network_topology.t.00000.png)
![Sample 4 Topology t3](Sample_4_Composite_Chaos/readme_plots/002_1_2__network_topology.t.00003.png)
![Sample 4 Topology t4](Sample_4_Composite_Chaos/readme_plots/002_1_2__network_topology.t.00004.png)
![Sample 4 Topology t5](Sample_4_Composite_Chaos/readme_plots/002_1_2__network_topology.t.00005.png)
![Sample 4 Topology t8](Sample_4_Composite_Chaos/readme_plots/002_1_2__network_topology.t.00008.png)
![Sample 4 Topology t11](Sample_4_Composite_Chaos/readme_plots/002_1_2__network_topology.t.00011.png)

#### 🔴 Sample 5 (京都交差点網)

**臨床解説:**
渋滞デッドロックが $t=18$ に発生します。ボトルネックである `23_四条烏丸` や `21_四条室町` の周辺エッジが太くなります。車両が滞留固着します。周辺道路のエッジは消滅します。

- ![Sample 5 Topology t0](Sample_5_Kyoto_Traffic/readme_plots/002_1_2__network_topology.t.00000.png)
- ![Sample 5 Topology t10](Sample_5_Kyoto_Traffic/readme_plots/002_1_2__network_topology.t.00010.png)
- ![Sample 5 Topology t11](Sample_5_Kyoto_Traffic/readme_plots/002_1_2__network_topology.t.00011.png)
- ![Sample 5 Topology t12](Sample_5_Kyoto_Traffic/readme_plots/002_1_2__network_topology.t.00012.png)
- ![Sample 5 Topology t14](Sample_5_Kyoto_Traffic/readme_plots/002_1_2__network_topology.t.00014.png)
- ![Sample 5 Topology t23](Sample_5_Kyoto_Traffic/readme_plots/002_1_2__network_topology.t.00023.png)

#### 🟢 Sample 6 (株券流体)

**臨床解説:**
市場二部グラフを分析します。共謀するUSRアカウントと標的の銘柄ノードを結ぶ有向エッジが増加します。市場全体の自律的な注文エッジを覆い隠します。

- ![Sample 6 Topology t0](Sample_6_Market_Stock_Flow/readme_plots/002_1_2__network_topology.t.00000.png)
- ![Sample 6 Topology t6](Sample_6_Market_Stock_Flow/readme_plots/002_1_2__network_topology.t.00006.png)
- ![Sample 6 Topology t12](Sample_6_Market_Stock_Flow/readme_plots/002_1_2__network_topology.t.00012.png)
- ![Sample 6 Topology t18](Sample_6_Market_Stock_Flow/readme_plots/002_1_2__network_topology.t.00018.png)

#### 🟢 Sample 7 (現金流体)

**臨床解説:**
決済流動性の対流が発生します。`USR_003` と `USR_004` の間に往復エッジが直結します。長期間にわたってこの間だけで流動性が拘束されます。

- ![Sample 7 Topology t0](Sample_7_Market_Cash_Flow/readme_plots/002_1_2__network_topology.t.00000.png)
- ![Sample 7 Topology t6](Sample_7_Market_Cash_Flow/readme_plots/002_1_2__network_topology.t.00006.png)
- ![Sample 7 Topology t12](Sample_7_Market_Cash_Flow/readme_plots/002_1_2__network_topology.t.00012.png)
- ![Sample 7 Topology t18](Sample_7_Market_Cash_Flow/readme_plots/002_1_2__network_topology.t.00018.png)

#### 🔴 Sample 8 (fMRI 脳梗塞)

**臨床解説:**
脳梗塞が $t=30$ に発生します。梗塞野（運動野）へ流入・流出する機能的結合エッジが消失します。梗塞によるトポロジー断裂が視覚化されます。
![Sample 8 Topology t0](Sample_8_fMRI_Stroke/readme_plots/002_1_2__network_topology.t.00000.png)
![Sample 8 Topology t29](Sample_8_fMRI_Stroke/readme_plots/002_1_2__network_topology.t.00029.png)
![Sample 8 Topology t30](Sample_8_fMRI_Stroke/readme_plots/002_1_2__network_topology.t.00030.png)
![Sample 8 Topology t31](Sample_8_fMRI_Stroke/readme_plots/002_1_2__network_topology.t.00031.png)
![Sample 8 Topology t59](Sample_8_fMRI_Stroke/readme_plots/002_1_2__network_topology.t.00059.png)

#### 🔴 Sample 9 (fMRI てんかん発作)

**臨床解説:**
てんかん同調バーストが発生します。脳領野全体のBOLD活動エッジが過同期パターンへと変質します。全脳が同一の振動パターンにハックされます。
![Sample 9 Topology t0](Sample_9_fMRI_Seizure/readme_plots/002_1_2__network_topology.t.00000.png)
![Sample 9 Topology t29](Sample_9_fMRI_Seizure/readme_plots/002_1_2__network_topology.t.00029.png)
![Sample 9 Topology t30](Sample_9_fMRI_Seizure/readme_plots/002_1_2__network_topology.t.00030.png)
![Sample 9 Topology t31](Sample_9_fMRI_Seizure/readme_plots/002_1_2__network_topology.t.00031.png)
![Sample 9 Topology t32](Sample_9_fMRI_Seizure/readme_plots/002_1_2__network_topology.t.00032.png)
![Sample 9 Topology t33](Sample_9_fMRI_Seizure/readme_plots/002_1_2__network_topology.t.00033.png)
![Sample 9 Topology t34](Sample_9_fMRI_Seizure/readme_plots/002_1_2__network_topology.t.00034.png)。

- ![Sample 6 Topology t0](Sample_6_Market_Stock_Flow/readme_plots/002_1_2__network_topology.t.00000.png)
- ![Sample 6 Topology t6](Sample_6_Market_Stock_Flow/readme_plots/002_1_2__network_topology.t.00006.png)
- ![Sample 6 Topology t12](Sample_6_Market_Stock_Flow/readme_plots/002_1_2__network_topology.t.00012.png)
- ![Sample 6 Topology t18](Sample_6_Market_Stock_Flow/readme_plots/002_1_2__network_topology.t.00018.png)

#### 🟢 Sample 7 (現金流体)

**臨床解説:**
決済流動性の対流中、`USR_003` と `USR_004` の間に資金がキャッチボールされる極太の往復エッジが突然直結し、長期間にわたってこの間だけで流動性が拘束されている様子を示します。

- ![Sample 7 Topology t0](Sample_7_Market_Cash_Flow/readme_plots/002_1_2__network_topology.t.00000.png)
- ![Sample 7 Topology t6](Sample_7_Market_Cash_Flow/readme_plots/002_1_2__network_topology.t.00006.png)
- ![Sample 7 Topology t12](Sample_7_Market_Cash_Flow/readme_plots/002_1_2__network_topology.t.00012.png)
- ![Sample 7 Topology t18](Sample_7_Market_Cash_Flow/readme_plots/002_1_2__network_topology.t.00018.png)

#### 🔴 Sample 8 (fMRI 脳梗塞)

**臨床解説:**
梗塞（$t=30$）が起きた瞬間から、梗塞野（運動野）へ流入・流出するすべての機能的結合エッジがブラックアウト（消失）し、梗塞によるトポロジー断裂が視覚化されています。
![Sample 8 Topology t0](Sample_8_fMRI_Stroke/readme_plots/002_1_2__network_topology.t.00000.png)
![Sample 8 Topology t29](Sample_8_fMRI_Stroke/readme_plots/002_1_2__network_topology.t.00029.png)
![Sample 8 Topology t30](Sample_8_fMRI_Stroke/readme_plots/002_1_2__network_topology.t.00030.png)
![Sample 8 Topology t31](Sample_8_fMRI_Stroke/readme_plots/002_1_2__network_topology.t.00031.png)
![Sample 8 Topology t59](Sample_8_fMRI_Stroke/readme_plots/002_1_2__network_topology.t.00059.png)

#### 🔴 Sample 9 (fMRI てんかん発作)

**臨床解説:**
てんかん同調バーストの発生に伴い、脳領野全体のBOLD活動エッジが極太の「過同期パターン」へと変質し、全脳が同一の振動キャッチボールにハックされています。
![Sample 9 Topology t0](Sample_9_fMRI_Seizure/readme_plots/002_1_2__network_topology.t.00000.png)
![Sample 9 Topology t29](Sample_9_fMRI_Seizure/readme_plots/002_1_2__network_topology.t.00029.png)
![Sample 9 Topology t30](Sample_9_fMRI_Seizure/readme_plots/002_1_2__network_topology.t.00030.png)
![Sample 9 Topology t31](Sample_9_fMRI_Seizure/readme_plots/002_1_2__network_topology.t.00031.png)
![Sample 9 Topology t32](Sample_9_fMRI_Seizure/readme_plots/002_1_2__network_topology.t.00032.png)
![Sample 9 Topology t33](Sample_9_fMRI_Seizure/readme_plots/002_1_2__network_topology.t.00033.png)
![Sample 9 Topology t34](Sample_9_fMRI_Seizure/readme_plots/002_1_2__network_topology.t.00034.png)
