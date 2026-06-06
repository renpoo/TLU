# 002_2. 会計・物流フォレンジック監視 (Forensic Auditing)

本ガイドは、Tensor-Link Utility (TLU) における会計・物流フォレンジック監視モジュール（`002_2`）を説明します。各検証サンプルの出力と数値に基づく解説を記載します。

---

## 🔬 情報幾何学と質量保存則の理論

閉鎖型の実体ネットワークにおいては、キルヒホッフの第一法則（電流則＝質量保存則）が成立します。ノードに入力される総流量と流出する総流量 of 差分を「保存残差 (Conservation Residual)」または「相対漏洩率 (Relative Leak Ratio)」と定義します。

$$Residual_i = \sum Flux_{in} - \sum Flux_{out}$$

正常な会計記帳や物理的流通では、ダブルエントリー（借貸平均）の制約があります。この残差値は常に `0.00` となります。この値が正の値として長期にわたって検知された場合、質量（資金・車両）がシステム外へバイパス流出（簿外横領など）していることを証明します。

システムの状態確率分布の変位（構造変化の勢い）を、情報多様体上の距離尺度である「KLダイバージェンス（KL Divergence Drift）」として測定します。これにより、従来の統計Zスコア（Z-Score）が検知できない構造の断裂（相転移）を検知します。

---

## 📊 会計・物流フォレンジック監視グラフと個別サンプルの所見

### 2. マクロフォレンジック監視ダッシュボード (`002_2_1__macro_forensics_dashboard.png`)

キルヒホッフの第一法則に基づく「保存残差」の時系列変化を示す監査・フォレンジックダッシュボードです。

#### 🟢 Sample 0 (正常代謝)

**臨床解説:**
保存残差は全期を通じて `0.00` を維持します。システム外への漏洩はありません。構造ドリフト（KL）は初期 $t=2$ に `1.61` となります。それ以外は低水準に落ち着きます。最終期 $t=11$ には `0.07` となります。統計 Z-Score は、取引集中期にあたる $t=6$ にしきい値を超えます。このとき状態 $Z_X$ が `4.14`、速度 $Z_v$ が `4.90` となります。しかし、残差やドリフトは上昇していません。そのため、これは異常構造への相転移ではありません。正常な季節的ボラティリティの上昇を示します。

- ![Sample 0 Forensics Dashboard](Sample_0_Healthy/readme_plots/002_2_1__macro_forensics_dashboard.png)

#### 🟡 Sample 1 (循環取引)

**臨床解説:**
還流取引（Wash Trade）が発生します。そのため借方と貸方は一致します。システム外への資金漏洩を示す保存残差は、全期を通じて `0.00` となります。統計 Z-Score はしきい値付近を推移します。状態 $Z_X$ は最大 `1.97`、速度 $Z_v$ は最大 `3.87` となります。これは顕著なアノマリーとしては検知されません。情報幾何指標の構造ドリフト（KL）は、還流経路が形成された初期段階（$t=2$）に `1.22` のピークを記録します。その後も取引パターンの歪みを捉え続けます。構造ドリフトは、残差やZ-Scoreでは見逃される還流取引を検知します。

- ![Sample 1 Forensics Dashboard](Sample_1_Wash_Trade/readme_plots/002_2_1__macro_forensics_dashboard.png)

#### 🔴 Sample 2 (資金横領)

**臨床解説:**
$t=1, 2$ に `UNKNOWN_LEAK` への流出が始まります。このとき `307.30` から `359.73` の残差が検出されます。さらに $t=7, 8, 10$ にかけて最大 `364.53` に達する保存残差が記録されます。構造ドリフト（KL）は、流出開始初期の $t=2$ に `1.18` まで上昇します。その後は流出パターンの固定化に伴い減衰します。統計 Z-Score は初期 $t=6$ で最大値となります（$Z_X$=`3.82`, $Z_v$=`3.71`）。しかし、流出の当事期である $t=7$ や $t=8$ 以降は、異常状態がベースラインとして学習されます。そのため、Z-Score は `0.65` から `1.00` 付近まで低下します。本サンプルでは、保存残差の追跡と初期の KL ドリフトが横領を検知します。

- ![Sample 2 Forensics Dashboard](Sample_2_Embezzlement_Leak/readme_plots/002_2_1__macro_forensics_dashboard.png)

#### 🟡 Sample 3 (入力ミス)

**臨床解説:**
片面入力エラーが発生します。該当ステップは $t=1, 2$（最大残差 `340.01`）および $t=10$（最大残差 `906.29`）です。これらの時期に、保存残差がスパイクを形成します。その後、エラーが手動修正されます。翌ステップ（$t=3, 11$）には `0.00` に復帰します。構造ドリフト（KL）は初期エラー発生期（$t=2$）に `1.87` のスパイクを示します。統計 Z-Score も最大 `5.29` に上昇します。しかし、これは一過性で解消します。すべての指標が、異常発生の瞬間のみ同期スパイクを見せます。次のステップで定常値に戻ります。この過渡的ダイナミクスは、一過性の局所入力エラーとその後の自己修正を示します。

- ![Sample 3 Forensics Dashboard](Sample_3_Unbalanced_Mistake/readme_plots/002_2_1__macro_forensics_dashboard.png)

#### 🔴 Sample 4 (複合アノマリー)

**臨床解説:**
架空取引による同期駆動と、簿外横領による資産消失が同時に進行します。横領の激化に伴い、$t=5$ から保存残差が発生します。$t=8$ には最大 `4,773.57` に達する残差スパイクが発生します。これは資金が外部へ流出している事実を示します。構造ドリフト（KL）は初期（$t=2$）に `1.59` となります。還流と漏洩による構造断裂を反映します。中盤以降も高水準で推移します。Z-Score は中盤 $t=6$ で速度 $Z_v$ が `3.42` となります。以降はモデル学習の汚染が進みます。そのため、最盛期の $t=8$ 以降も Z-Score は `1.52` 以下に沈黙します。保存残差と KL ドリフトの双方が機能します。この複合破綻の全容を示します。

- ![Sample 4 Forensics Dashboard](Sample_4_Composite_Chaos/readme_plots/002_2_1__macro_forensics_dashboard.png)

#### 🔴 Sample 5 (京都交差点網)

**臨床解説:**
車両が交差点内に滞留・固着しています。そのため、保存残差は全期を通じて `0.00` となります。渋滞の相転移点は $t=12$ です。この時期に、構造ドリフト（KL）が `1.76`、統計 Z-Score が状態 $Z_X$=`7.25`、速度 $Z_v$=`9.86` を記録します。フリーズ状態に移行した $t=23$ には、車両の動きが消失します。そのためボラティリティがゼロになります。統計 Z-Score は状態 $Z_X$=`0.62`、速度 $Z_v$=`0.43` へと低下します。この状態において、構造ドリフト（KL）のみがトポロジーのフリーズ状態を検出します。これは主要交差点へのエッジの凝固と、周辺の干上がりによるものです。

- ![Sample 5 Forensics Dashboard](Sample_5_Kyoto_Traffic/readme_plots/002_2_1__macro_forensics_dashboard.png)

#### 🔴 Sample 8 (fMRI 脳梗塞)

**臨床解説:**
虚血により、運動野への流入・流出血液量が断裂されます。血液が脳外へ消失したわけではありません。そのため、保存残差は `0.00` となります。梗塞が発生する $t=30$ に、血液量の変化から速度 Z-Score ($Z_v$) が `51.44` のスパイクを示します。状態 Z-Score ($Z_X$) は最大でも `0.06` となり沈黙します。$t=30$ 以降、機能が停止した運動野は変動を失います。速度 $Z_v$ も平坦化して正常しきい値内に戻ります。構造ドリフト（KL）は、梗塞発生の $t=30$ に `1.29` へ上昇します。機能的結合の切断を反映します。最終期 $t=59$ に至るまで `0.54` 以上の高水準を維持します。構造ドリフトが脳組織の壊死と機能的切断の固定化を特定します。

- ![Sample 8 Forensics Dashboard](Sample_8_fMRI_Stroke/readme_plots/002_2_1__macro_forensics_dashboard.png)

#### 🔴 Sample 9 (fMRI てんかん発作)

**臨床解説:**
全脳が過同期放電で自励振動します。総信号質量は脳内に留まります。そのため、保存残差は全期を通じて `0.00` のままです。発作が開始する $t=30$ に、構造ドリフト（KL）は `1.33` へ上昇します。過同期のピークである $t=38$ に最大値 `1.77` に達します。脳全域のトポロジー変化を検知します。対照的に、状態 Z-Score ($Z_X$) は最大 `0.0001` となり反応しません。速度 Z-Score ($Z_v$) も発作期（$t \ge 30$）には `1.3` 前後に留まります。てんかん時のBOLD信号は、規則的なサイン波に固着します。ボラティリティが一定になるため、統計モデルは定常状態と判定します。本サンプルは、統計モデルが検出できない過同期バーストを構造ドリフト（KL）が検知することを示します。

- ![Sample 9 Forensics Dashboard](Sample_9_fMRI_Seizure/readme_plots/002_2_1__macro_forensics_dashboard.png)

---

### 3. 3次元局所KL Drift (`002_2_2_1__3d_micro_kl_drift.png`)

情報多様体上における状態確率分布の変位（KLダイバージェンス）の時間・空間推移を示す3次元グラフです。構造変化の勢いを示します。

#### 🟢 Sample 0 (正常代謝)

**臨床解説:**
KL Drift の時空間分布はスパイクを見せることなく、全期を通じて低水準で推移しています。

- ![Sample 0 KL Drift](Sample_0_Healthy/readme_plots/002_2_2_1__3d_micro_kl_drift.png)

#### 🟡 Sample 1 (循環取引)

**臨床解説:**
循環取引が発生するタイムステップ（1月、2月、5月）において、対象の還流ノードに変位が立ち上がります。

- ![Sample 1 KL Drift](Sample_1_Wash_Trade/readme_plots/002_2_2_1__3d_micro_kl_drift.png)

#### 🔴 Sample 2 (資金横領)

**臨床解説:**
横領の開始以降、`UNKNOWN_LEAK` と関連預金口座の周辺において、時間軸に沿って情報空間の変位が形成されます。

- ![Sample 2 KL Drift](Sample_2_Embezzlement_Leak/readme_plots/002_2_2_1__3d_micro_kl_drift.png)

#### 🟡 Sample 3 (入力ミス)

**臨床解説:**
片面入力エラーが発生した $t=1$（2020-02）の瞬間、`Accounts_Receivable` に `20.68`、`Cash` に `5.01` のスパイクが発生します。

- ![Sample 3 KL Drift](Sample_3_Unbalanced_Mistake/readme_plots/002_2_2_1__3d_micro_kl_drift.png)

#### 🔴 Sample 4 (複合アノマリー)

**臨床解説:**
架空取引による同期駆動と横領による漏洩流路の双方から、時空間の変位が形成されます。

- ![Sample 4 KL Drift](Sample_4_Composite_Chaos/readme_plots/002_2_2_1__3d_micro_kl_drift.png)

#### 🔴 Sample 5 (京都交差点網)

**臨床解説:**
渋滞デッドロックが発生します。ボトルネックである四条烏丸の座標に、時間軸に沿って KL Drift のスパイクが形成されます。

- ![Sample 5 KL Drift](Sample_5_Kyoto_Traffic/readme_plots/002_2_2_1__3d_micro_kl_drift.png)

#### 🟢 Sample 6 (株券流体)

**臨床解説:**
KL Drift の時空間分布はスパイクを見せることなく、全期を通じて低水準で推移しています。

- ![Sample 6 KL Drift](Sample_6_Market_Stock_Flow/readme_plots/002_2_2_1__3d_micro_kl_drift.png)

#### 🟢 Sample 7 (現金流体)

**臨床解説:**
KL Drift プロットには時間軸に沿って屹立するような変位はなく、安定した状態を維持しています。

- ![Sample 7 KL Drift](Sample_7_Market_Cash_Flow/readme_plots/002_2_2_1__3d_micro_kl_drift.png)

#### 🔴 Sample 8 (fMRI 脳梗塞)

**臨床解説:**
脳梗塞が $t=30$ に発生します。運動野（`Motor_Cortex`）の座標を中心に、情報多様体上に KL Drift の変位が発生します。壊死領域を特定します。

- ![Sample 8 KL Drift](Sample_8_fMRI_Stroke/readme_plots/002_2_2_1__3d_micro_kl_drift.png)

#### 🔴 Sample 9 (fMRI てんかん発作)

**臨床解説:**
てんかんバーストが発生します。側頭葉から脳全域へ向かって過同期の変位が波及します。全脳がハックされた状態を捉えています。

- ![Sample 9 KL Drift](Sample_9_fMRI_Seizure/readme_plots/002_2_2_1__3d_micro_kl_drift.png)

---

### 4. 3次元局所Z-Score (`002_2_2_2__3d_micro_z_score_X.png`)

統計モデルに基づく、各ノードごとの Z-Score の時間・空間推移を示す3次元グラフです。KL Drift との対比に使用します。

#### 🟢 Sample 0 (正常代謝)

**臨床解説:**
季節変動の取引集中期（7月）に、一時的な Z-Score の上昇（最大 `4.14`）が発生します。残差や剛性の異常はなく正常です。

- ![Sample 0 Z-Score](Sample_0_Healthy/readme_plots/002_2_2_2__3d_micro_z_score_X.png)

#### 🟡 Sample 1 (循環取引)

**臨床解説:**
循環取引により、Z-Score がアノマリー期に最大 `3.87` まで上昇します。後半は還流がベースラインとして学習されます。そのため、Z-Score が低下する現象が観察されます。

- ![Sample 1 Z-Score](Sample_1_Wash_Trade/readme_plots/002_2_2_2__3d_micro_z_score_X.png)

#### 🔴 Sample 2 (資金横領)

**臨床解説:**
流出の開始初期に一時的な Z-Score の上昇（`3.82`）が発生します。漏洩が常態化すると、Z-Score は低下し沈黙します。情報幾何指標との併用が必要です。

- ![Sample 2 Z-Score](Sample_2_Embezzlement_Leak/readme_plots/002_2_2_2__3d_micro_z_score_X.png)

#### 🟡 Sample 3 (入力ミス)

**臨床解説:**
入力ミスが発生した瞬間に、該当勘定の Z-Score が `5.29` まで上昇します。翌期には消滅します。

- ![Sample 3 Z-Score](Sample_3_Unbalanced_Mistake/readme_plots/002_2_2_2__3d_micro_z_score_X.png)

#### 🔴 Sample 4 (複合アノマリー)

**臨床解説:**
循環取引の同期月には、最大 `3.42` の Z-Score 上昇を検知します。しかし、これは横領による資金枯渇と混ざり合います。ベースライン学習が進むため、警告が沈黙しやすくなります。

- ![Sample 4 Z-Score](Sample_4_Composite_Chaos/readme_plots/002_2_2_2__3d_micro_z_score_X.png)

#### 🔴 Sample 5 (京都交差点網)

**臨床解説:**
完全なデッドロック状態に移行します。その後は車両が完全に停止して動きません。時間的な変動（ボラティリティ）がなくなります。Z-Score は `0.00` へと完全に平坦化（沈黙）します。

- ![Sample 5 Z-Score](Sample_5_Kyoto_Traffic/readme_plots/002_2_2_2__3d_micro_z_score_X.png)

#### 🟢 Sample 6 (株券流体)

**臨床解説:**
期間を通じて Z-Score の過度な上昇はありません。モデル汚染による低下現象も確認されません。定常状態を維持しています。

- ![Sample 6 Z-Score](Sample_6_Market_Stock_Flow/readme_plots/002_2_2_2__3d_micro_z_score_X.png)

#### 🟢 Sample 7 (現金流体)

**臨床解説:**
Z-Score のスパイクや低下による沈黙アノマリーは検出されません。統計的にも平穏に推移しています。

- ![Sample 7 Z-Score](Sample_7_Market_Cash_Flow/readme_plots/002_2_2_2__3d_micro_z_score_X.png)

#### 🔴 Sample 8 (fMRI 脳梗塞)

**臨床解説:**
脳梗塞が $t=30$ に発生します。血液減少時の変動を検知し、Z-Score が `0.07` に上昇します。その後は活動停止状態（無変動）となります。そのため、Z-Score は沈黙します。

- ![Sample 8 Z-Score](Sample_8_fMRI_Stroke/readme_plots/002_2_2_2__3d_micro_z_score_X.png)

#### 🔴 Sample 9 (fMRI てんかん発作)

**臨床解説:**
てんかん発作発生時に Z-Score は沈黙します。変動が規則的なサイン波に固着するためです。ボラティリティが一定になります。統計モデルの死角を示しています。

- ![Sample 9 Z-Score](Sample_9_fMRI_Seizure/readme_plots/002_2_2_2__3d_micro_z_score_X.png)
