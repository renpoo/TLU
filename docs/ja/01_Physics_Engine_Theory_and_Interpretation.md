# 01. 物理・数学フィルター理論とデータ解読ガイド (Physics-Mathematics Engine Theory & Interpretation)

Tensor-Link Utility (TLU) は、抽象的なネットワークデータに「質量」「力」「エネルギー」「粘性」といった物理的実在性を与え、その変形やエネルギー収支からシステミックな異常を判定する、8つの主要分析モジュール（物理数学フィルター）を搭載しています。

本書は、各フィルターの**数理物理的理論基盤（Physics Theory）**と、出力される可視化グラフの**フォレンジック的解読ガイド（Data Interpretation）**を統合した、TLUシステムのコア解説書です。検証サンプル（正常、交通デッドロック、資金横領、相場操縦等）の実際のグラフを対比・引用しながら解説します。

---

## 🧭 目次 (Table of Contents)

0. [財務基礎状態と基本統計量 (Basic Statistics & Foundation - Prefix: `000_0`)](#0-財務基礎状態と基本統計量-basic-statistics--foundation---prefix-000_0)
1. [構造剛性と主成分分析 (Stiffness & PCA / Classical Mechanics - Prefix: `000_2`)](#1-構造剛性と主成分分析-stiffness--pca--classical-mechanics---prefix-000_2)
2. [運動学と動的状態空間 (Kinematics & State-Space - Prefix: `000_1`)](#2-運動学と動的状態空間-kinematics--state-space---prefix-000_1)
3. [熱力学とエントロピー (Thermodynamics & Entropy - Prefix: `001_1`, `001_2`)](#3-熱力学とエントロピー-thermodynamics--entropy---prefix-001_1-001_2)
4. [情報幾何学と相対保存則 (Information Geometry & Forensics - Prefix: `002_1`, `002_2`)](#4-情報幾何学と相対保存則-information-geometry--forensics---prefix-002_1-002_2)
5. [逆運動学と目標到達性 (Kinematics & Reachability - Prefix: `003_1`)](#5-逆運動学と目標到達性-kinematics--reachability---prefix-003_1)
6. [システム安定性とフィードバック制御 (Control Theory & LQR - Prefix: `004_1`, `004_2`)](#6-システム安定性とフィードバック制御-control-theory--lqr---prefix-004_1-004_2)
7. [信号処理と波動力学 (Wave Mechanics & Coherence - Prefix: `005_1`, `005_2`)](#7-信号処理と波動力学-wave-mechanics--coherence---prefix-005_1-005_2)

---

## 0. 財務基礎状態と基本統計量 (Basic Statistics & Foundation - Prefix: `000_0`)

### 🔬 物理・数理理論 (Physics Theory)

システム全体の活動量（売上、資産、総車両数など）を「基礎体力・体格」として把握した上で、状態変数の時間変化に対して伝統的な統計分析（確率密度関数 KDE, ローリング分位数, 歪度 Skewness, 尖度 Kurtosis）を適用します。

特に、システムのボラティリティに対するZ-Score（標準化得点）は以下の数式で定義されます。

$$Z = \frac{x_t - \mu_{window}}{\sigma_{window}}$$

ここで、 $\mu_{window}$ と $\sigma_{window}$ は過去窓（例：12週間）のローリング平均および標準偏差です。Z-Scoreが極端に高い（ $Z > 3.0$ ）、あるいは尖度が異常に高い（ファットテール）場合、システムが通常許容できない「突発的な発作」に対する脆弱性（ブラックスワン体質）を示します。

### 📊 グラフの解読とサンプル比較 (Data Interpretation)

* **財務・基礎状態グラフ:** `000_0_1__BS_Block_Total.png`, `000_0_1__PL_Waterfall_Total.png`, `000_0_1__PL_Trend_Revenue_vs_Expenses.png`
* **統計分布グラフ:** `000_0_2_3__histogram_kde.png`, `000_0_2_4__rolling_quantiles.png`, `000_0_2_5__kurtosis_vs_phase.png`

#### 🟢 正常な季節変動 (Sample 0) vs 🔴 カモフラージュされた循環取引 (Sample 1)

* **Sample 0:** [Sample 0 P/L Waterfall](../../samples/Sample_0_Healthy/readme_plots/000_0_1__PL_Waterfall_Total.png) - 季節性の決済集中により、流動性のZ-Scoreが一時的に最大 `4.90` (7月) まで跳ね上がりますが、キルヒホッフ残差が `0.00` であるため「統計的偽陽性」と判定されます。
* **Sample 1:** [Sample 1 P/L Trend](../../samples/Sample_1_Wash_Trade/readme_plots/000_0_1__PL_Trend.png) - 循環取引により売上高が見かけ上右肩上がりに成長していますが、それを支えるためのSG&A経費が「横ばい（平坦）」であり、物理的な活動の拡大と矛盾する架空仕訳であることが露呈します。

#### ⚕️ 検査基準と一次所見

1. **歪度と尖度の異常:** KDE分布やRolling Quantilesにおいて、極端に尾が長い（Fat-tail / 高Kurtosis）場合、「普段は平穏だが、突然致命的なショックが訪れる脆弱な体質」と判断します。
2. **茹でガエル（基底順順応）:** ほかの指標で慢性的な病的活動（高い粘性や質量漏洩）が存在するにもかかわらず、Z-Scoreが常に平坦な場合、「統計モデルが異常を正常ベースラインとして学習してしまっている」と判定します。

---

## 1. 構造剛性と主成分分析 (Stiffness & PCA / Classical Mechanics - Prefix: `000_2`)

### 🔬 物理・数理理論 (Physics Theory)

ネットワークを構成する各ノード間の取引関係（エッジ）を、フックの法則に基づく**「弾性バネ (Elastic Springs)」**としてモデル化します。
ノード間の偏相関関係や流量のボラティリティから、システムの「剛性行列（Stiffness Matrix）」 $K$ を計算します。

$$F_{external} = K \cdot \Delta X$$

ここで、 $\Delta X$ は各ノードの状態変位（資金残高のボラティリティ、交差点の混雑度など）、 $F_{external}$ は外部力です。
システムが健全な状態であれば、バネは柔軟に伸び縮みして外部ショックを吸収します（弾性状態）。しかし、特定の循環ループやボトルネックが発生すると、一部のバネが極限まで収縮して凝固する**「剛性ロック (Stiffness Lock)」**が発生します。

剛性行列 $K$ に対して主成分分析（PCA）を適用し、支配的固有空間の固有値比率（Explained Variance Ratio）の時系列推移を追跡することで、システム全体の「結合剛性の偏在」を数理的に証明します。

### 📊 グラフの解読とサンプル比較 (Data Interpretation)

* **剛性行列・主成分グラフ:** `000_2_1__structural_stiffness.t.*.png`, `000_2_2__principal_axes_ratio.png`, `000_2_3__eigenvector_evolution.png`

#### 🟢 正常な挙動 (Sample 0)

正常代謝（Sample 0）では、勘定科目（ノード）間の剛性行列は偏りのないなだらかな分布を描き、PCAの支配比率も特定の主成分に100%近くハックされることはありません。

* **剛性行列 (Stiffness Matrix):** [Sample 0 Stiffness (t=6)](../../samples/Sample_0_Healthy/readme_plots/000_2_1__structural_stiffness.t.00006.png)
* **PCA 主要軸比率 (PCA Ratio):** [Sample 0 PCA Ratio](../../samples/Sample_0_Healthy/readme_plots/000_2_2__principal_axes_ratio.png)
  * *解読点:* 特定ペアへの極端な取引同期がなく、固有値比率が滑らかに減衰している「しなやかな」トポロジー構造を示しています。

#### 🔴 異常な挙動：交通デッドロック (Sample 5)

都市交通のグリッドロック（Sample 5）では、ボトルネックが発生する前後で剛性行列の構造が劇的に変化（相転移）します。

* **Onset (t=51 / W52):** [Sample 5 Stiffness t51](../../samples/Sample_5_Kyoto_Traffic/readme_plots/000_2_1__structural_stiffness.t.00051.png) - ボトルネック `23_四条烏丸` の流入容量が 5% に絞られ、`13_二条烏丸` 周辺に剛性の負荷が集中し始めます。
* **Paralysis (t=52 / W53):** [Sample 5 Stiffness t52](../../samples/Sample_5_Kyoto_Traffic/readme_plots/000_2_1__structural_stiffness.t.00052.png) - 交通麻痺が起き、PC1寄与率が **`71.77%`**（固有値 `56931.13`）をマークして周辺を強力にロック（血栓状態）。
* **Chronic (t=53 / W54):** [Sample 5 Stiffness t53](../../samples/Sample_5_Kyoto_Traffic/readme_plots/000_2_1__structural_stiffness.t.00053.png) - 剛性ロックが抜け道の `22_四条新町` や `17_五条新町` へと波及し、ネットワーク全域が「慢性的な関節硬直」に陥っています。

#### 🟡 異常な挙動：相場操縦の共謀ロック (Sample 7)

ユーザー間の資金移動ネットワーク（Sample 7）において、共謀するボット口座（`USR_003` と `USR_004`）が対当取引を始めると、PC1寄与率が瞬時に **`99.67%`** へと急上昇します。

* **固有ベクトル進化図 (Eigenvector Evolution):** [Sample 7 Eigenvector Evolution](../../samples/Sample_7_Market_Users_Weekly/readme_plots/000_2_3__eigenvector_evolution.png)
  * *解読点:* W41 (`t=40`) の瞬間、PC1のローディング（ベクトルの向き）が `USR_004` (`0.7287`) と `USR_003` (`-0.6820`) に異常集中し、2者間だけで力学的剛性がほぼ100%ロック（対当取引による支配）された様子が鮮烈に告発されています。

#### ⚕️ 検査基準と一次所見

1. **剛性の異常:** 剛性が極端に高い場合、「システムが硬直化（Rigidity）しており、外部ショックに脆い」という所見を下します。
2. **主軸の崩壊 (Eigenvector Shift):** PCAの第一主成分と第二主成分が急激に入れ替わった場合、「組織の主要なエネルギー・ルート（経絡のメインパイプ）が物理的に組み替わった（構造的転換）」という所見を下します。

---

## 2. 運動学と動的状態空間 (Kinematics & State-Space - Prefix: `000_1`)

### 🔬 物理・数理理論 (Physics Theory)

システムの動的プロセスを状態空間軌道（Phase Portrait）として可視化し、ノード間の流量抵抗や質量移送の遅れを「粘性 $C$」、および規模や慣性的な重さを「慣性 $J$」として運動方程式に基づき定義します。

$$F_{external} = J \cdot \ddot{X} + C \cdot \dot{X} + K \cdot X$$

* **粘性（Viscosity）:** 手作業の転記、売掛金回収のタイムラグ、道路の車線減少などによる「流動抵抗」。
* **慣性（Inertia）:** 巨額の資本、過剰な在庫、重厚なインフラなど「システム全体の重さ・方向転換の鈍さ」。

システムの挙動は状態（位置 $X$、速度 $v = \dot{X}$、加速度 $a = \ddot{X}$）から構築される3次元の位相空間軌道（Phase Portrait Ribbon Plot）に射影されます。

### 📊 グラフの解読とサンプル比較 (Data Interpretation)

* **動的状態空間グラフ:** `000_1_8__phase_portrait_3d.png`, `000_1_4__3d_dynamics_inertia.png`, `000_1_5__3d_dynamics_viscosity.png`, `000_1_6__3d_dynamics_external_force.png`

#### 🟢 正常収束 (Sample 0) vs 🔴 壊滅的発散 (Sample 4) vs 🔴 破壊的共振 (Sample 2)

* **Sample 0:** [Sample 0 3D Phase Portrait](../../samples/Sample_0_Healthy/readme_plots/000_1_8__phase_portrait_3d.png) - 軌道リボンは非常に滑らかな閉ループ（リミットサイクル）へ安定的に収束し、不規則なバーストや軌道のゆがみは見られません。
* **Sample 4:** [Sample 4 3D Dynamics External Force](../../samples/Sample_4_Composite_Chaos/readme_plots/000_1_6__3d_dynamics_external_force.png) - 循環取引（過還流）と資金流出が同時に進行した結果、安定アトラクターから逸脱し、軌道が宇宙空間へ無限に発散する「システミック・メルトダウン」を示します。
* **Sample 2:** [Sample 2 3D Dynamics External Force](../../samples/Sample_2_Embezzlement_Leak/readme_plots/000_1_6__3d_dynamics_external_force.png) - 質量（資金）流出による弾性バネの損失に伴い、外部加振に対して **10億（1e9）スケールに達する壊滅的な異常共振（ノッキング）** が発生します。

#### ⚕️ 検査基準と一次所見

1. **粘性の高低:** 粘性（Viscosity）が高い場合、「システムはアナログな手作業や摩擦（肩こり）に依存しており、それがコスト増やミスの温床となっている」という所見を下します。
2. **慣性の偏り:** 慣性（Inertia）が特定のノードに異常に集中している場合、「システムの一部がメタボリックに肥大化し、全体の機動性を奪っている」という所見を下します。
3. **軌道（Phase Portrait）の異常:** 位相空間における軌道が予測不能なカオスに陥っている場合、「組織の自律的なブレーキが失われている」と判定します。

---

## 3. 熱力学とエントロピー (Thermodynamics & Entropy - Prefix: `001_1`, `001_2`)

### 🔬 物理・数理理論 (Physics Theory)

システム全体の活動量を「内部エネルギー $U$」、ノード間の遷移確率の分散度（無秩序さ）を「エントロピー $S$」、システムの時間変化率（流量ボラティリティ）を「温度 $T$」と定義します。
これらを用いて、システムが構造を維持し活動するために残されているポテンシャルである**「自由エネルギー $F$」**を定義します。

$$F = U - T \cdot S$$

熱力学第二法則（エントロピー増大の法則）により、不可逆なシステムでは活動に伴って摩擦（ $T \times S$ ）が発生し、自由エネルギーが健全に散逸します。
しかし、病的還流ループが存在すると、内部エネルギー $U$ は高水準に維持される（お金や車が不毛に激しく動く）にもかかわらず、それが外部への有意義な価値移送や代謝に結びつかず、すべて無駄な「摩擦熱（エントロピー損失 $T \times S$ ）」として消費され、自由エネルギー $F$ が急激に目減りします。

さらに、各ノード間の「反応速度の遅れ」を「Lag行列」として計算し、経絡の詰まり（滞留セクター）を特定します。

### 📊 グラフの解読とサンプル比較 (Data Interpretation)

* **熱力学・Lag行列グラフ:** `001_1_1__thermodynamics_dashboard.png`, `001_1_2__thermodynamics_energy_stack.png`, `001_1_3__thermodynamics_ts_diagram.png`, `001_2_1__local_thermo_scatter.png`, `001_2_2__lag_matrix_correlation.png`

#### 🟢 正常な成長 (Sample 0)

健全な事業体（Sample 0）では、無駄な往復取引（摩擦）が発生しないため、自由エネルギー $F$ が内部エネルギー $U$ に追従して健全に右肩上がりに成長します。

* **熱力学エネルギースタック:** [Sample 0 Energy Stack](../../samples/Sample_0_Healthy/readme_plots/001_1_2__thermodynamics_energy_stack.png)
  * *解読点:* 白い実線（自由エネルギー $F$）がエンジ色の領域（摩擦損失 $TS$）に押し潰されることなく、Uの上昇に伴って力強く上昇している健全な代謝を示しています。

#### 🔴 交通デッドロックによる「凍結」 (Sample 5)

交差点容量制限（Sample 5）では、システム全体のエントロピー $S$ が `40.50` から `38.70` へと微減したものの、局所的な激しい摩擦（速度のばらつき）によってマクロ温度 $T$ が `457.24` から **`547.06`** へと急上昇。
その結果、散逸損失（$TS$）が増加し、自由エネルギー $F$ は `2,481,482` から **`2,478,826`** へと減少しました。

* **熱力学エネルギースタック:** [Sample 5 Energy Stack](../../samples/Sample_5_Kyoto_Traffic/readme_plots/001_1_2__thermodynamics_energy_stack.png)
* **T-S ダイアグラム:** [Sample 5 T-S Diagram](../../samples/Sample_5_Kyoto_Traffic/readme_plots/001_1_3__thermodynamics_ts_diagram.png)
  * *解読点:* T-Sダイアグラムにおいて、アノマリー発動後に右上方向の層（2020年度）から左下方向の層（事故後の2021年度）へと収縮する「閉じた異常ループ」が描かれており、系全体がしなやかな流動能力を失った「熱的死」を示しています。
* **3D局所温度・エントロピープロット:**
  * [Sample 5 3D Local Temperature](../../samples/Sample_5_Kyoto_Traffic/readme_plots/001_1_2_2__3d_local_temperature.png) - 事故交差点である `23_四条烏丸` の局所温度 $T_i$ が `32.58` から **`1.87`** へと急降下し、冷え切った「コールドアイランド（凍結状態）」を形成。
  * [Sample 5 3D Local Entropy](../../samples/Sample_5_Kyoto_Traffic/readme_plots/001_1_2_1__3d_local_entropy.png) - 流入元の `21_四条室町` の局所エントロピー $s_i$ が `1.993` から **`1.674`** へと低下（進行の選択肢を奪われたトポロジーの拘束状態）。

#### ⚕️ 検査基準と一次所見

1. **エントロピーの負の歪度 (Negative Skewness):** エントロピーが極端な負の歪度を持つ場合、「強権的な市場介入」や「人工的な相場操縦」によって、システムの自然なゆらぎが強制的に殺されているという所見を下します。
2. **自由エネルギーの枯渇:** Fが低下し、Sが増大している場合、組織が「非効率なカオス（無駄な経費や摩擦）」に飲み込まれている所見を下します。
3. **Lag（遅延）の集中:** Lag行列（`001_2_2__lag_matrix_correlation.png`）において、特定ノード間でLagが異常に高い場合、「そこで情報の伝達や資金の精算が滞留している（経絡の詰まり）」と判断します。

---

## 4. 情報幾何学と相対保存則 (Information Geometry & Forensics - Prefix: `002_1`, `002_2`)

### 🔬 物理・数理理論 (Physics Theory)

閉鎖ネットワークにおいては、キルヒホッフの第一法則（電流則＝質量保存則）が厳密に成立します。
任意のノードに入力される総流量と、流出する総流量の差分を**「保存残差 (Conservation Residual)」**または**「相対漏洩率 (Relative Leak Ratio)」**と呼びます。

$$Residual_i = \sum Flux_{in} - \sum Flux_{out}$$

正常な会計や物理流通では、この値は常に `0.00` （誤差なし）となります。もし正の値が発生した場合、説明のつかない質量（資金・血液）がシステム外へバイパス流出（大出血・横領）していることを物理的に証明します。

さらに、システムの状態確率分布の変位（構造変化の勢い）を、情報多様体上の距離尺度である**「KLダイバージェンス（KL Divergence Drift）」**として測定します。これにより、従来の統計Zスコア（Z-Score）が茹でガエル現象（モデル汚染）によって沈黙する局面でも、構造の断裂を鋭く検知します。

### 📊 グラフの解読とサンプル比較 (Data Interpretation)

* **トポロジー＆フォレンジックグラフ:** `002_1_2__info_stress_scatter.png`, `002_1_2__network_topology.t.*.png`, `002_1_3__manifold_dimensionality.png`, `002_2_1__macro_forensics_dashboard.png`, `002_2_2__micro_forensics_scatter.png`, `002_2_2_1__3d_micro_kl_drift.png`, `002_2_2_2__3d_micro_z_score_X.png`

#### 🔴 資金横領による「質量欠損」 (Sample 2)

資金横領（Sample 2）では、回収した資金が正常な預金口座に格納されず、簿外へ siphoning （流出）されます。

* **マクロフォレンジック監視ダッシュボード:**
  * [Sample 0 Healthy Dashboard](../../samples/Sample_0_Healthy/readme_plots/002_2_1__macro_forensics_dashboard.png) - 残差は `0.00` の一本線を維持。
  * [Sample 2 Embezzlement Dashboard](../../samples/Sample_2_Embezzlement_Leak/readme_plots/002_2_1__macro_forensics_dashboard.png) - 資金流出が発生したステップで残差が最大 **`364.53`** 急増し、累計で **`$1,353.48`** の「質量欠損」が発生している様子が数学的に露出しています。

#### 🟡 入力ミスによる「一時的歪み」 (Sample 3)

仕訳の片面入力ミス（Sample 3）では、一時的に残差が最大 **`906.29`** 発生し、KL Drift が **`20.68`** まで跳ね上がりますが、翌月に修正されると直ちにゼロへと自己治癒（復元）します。

* **3D Micro KL Drift (Transient Spike):** [Sample 3 3D Micro KL Drift](../../samples/Sample_3_Unbalanced_Mistake/readme_plots/002_2_2_1__3d_micro_kl_drift.png)
  * *解読点:* アノマリーが発生した `2020-02` にのみ、針状の非常に鋭い単一スパイク（城壁）がそびえ立っていますが、翌ステップには平坦な原っぱに戻っており、システムの弾力性が維持されている「一時的ノイズ」であることが一目で判別できます。

#### 🟡 共謀取引による情報幾何学的スパイク (Sample 7)

相場操縦（Sample 7）では、共謀グループの高速マッチドオーダーにより、情報幾何学遷移確率が激変します。

* **3D Micro KL Drift (Clique Wall):** [Sample 7 3D Micro KL Drift](../../samples/Sample_7_Market_Users_Weekly/readme_plots/002_2_2_1__3d_micro_kl_drift.png)
  * *解読点:* パニック売りに陥った一般小売投資家（`USR_010` 等）の座標軸に沿って、通常取引の背景ノイズを遥かに逆比例で凌駕する**「幾何学的な城壁」**が屹立し、市場の流動性が特定の共謀関係（PC1）にハックされた余波を証明しています。

#### ⚕️ 検査基準と一次所見

1. **経絡の断裂 (Edge Stress):** 取引（エッジ）の応力が `0.00` になることは、ノード間の実体的な取引や車流がしっかりと停止し、パイプが麻痺（血栓化）したことを意味します。
2. **大出血 (Mass Leakage):** 質量保存残差が `0.00` より大きければ、即座に「簿外への物理的質量消失」という、最も深刻なフォレンジック・アラートの所見を導出します。
3. **発生源の特定:** 3D Micro KL Drift / Z-Scoreプロットから、時間および空間の鋭い尖塔を特定し、「この瞬間のこのノード間取引が病因（震源地）である」と判定します。

---

## 5. 逆運動学と目標到達性 (Kinematics & Reachability - Prefix: `003_1`)

### 🔬 物理・数理理論 (Physics Theory)

経営目標（KPI）やネットワークの制御ターゲットを、多関節ロボットアームの**「エンド・エフェクター（手先位置）」**としてマッピングし、各セクターや取引口座の稼働ポテンシャルを**「アームの関節角度（ジョイント）」**としてモデル化します。

順運動学（Forward Kinematics: FK）によって現在の構造から到達可能なパフォーマンス空間を計算し、逆に設定された野心的な目標（KPI）に対して**「逆運動学 (Inverse Kinematics: IK)」**を解くことで、必要な関節ベクトル（各部門の負荷配分）を逆算します。

$$Target\_KPI = FK(Joint\_Angles)$$
$$Joint\_Angles_{required} = IK(Target\_KPI)$$

もし、アームの幾何学的限界（特異点や可動域限界）によりIKが解けない、または到達誤差（Reachability Error）が異常高値を示す場合、現在の組織・交通インフラの構造を変更しない限り、その目標は「物理的に到達不可能」であることを客観的に証明します。

### 📊 グラフの解読とサンプル (Data Interpretation)

* **IK最適化シミュレーションプロット:** `003_1_2__3d_kinematics_ik.png`

#### 🔴 目標到達限界の可視化 (Sample 5)

ボトルネックが注入された都市交通（Sample 5）では、いくら車両のルートを変更しようとしても、ボトルネック周辺の流体力学的な飽和制限によって目標通過台数を達成することは困難になります。

* **3D Kinematics IK Space Ribbon:** [Sample 5 3D Kinematics IK](../../samples/Sample_5_Kyoto_Traffic/readme_plots/003_1_2__3d_kinematics_ik.png)
  * *解読点:* アームの軌道リボンが特定の平面に折りたたまれ、特異点（デッドロックによる自由度喪失）に吸い込まれていく「可動域の破綻」を示しています。

---

## 6. システム安定性とフィードバック制御 (Control Theory & LQR - Prefix: `004_1`, `004_2`)

### 🔬 物理・数理理論 (Physics Theory)

ネットワークの状態遷移を離散状態方程式として記述します。

$$X(t+1) = A \cdot X(t) + B \cdot u(t)$$

ここで、 $A$ はネットワークの隣接接続確率行列、 $u(t)$ は制御入力、 $B$ は入力パスです。
接続行列 $A$ の最大固有値である**「スペクトル半径（Spectral Radius $\rho$）」**を監視します。

$$\rho = \max_{i} |\lambda_i|$$

$\rho < 1.0$ であれば、システムは自己減衰能力（安定性）を持ちます。しかし、架空の資金還流ループ（循環取引）や交差点グリッドロックが形成されると、スペクトル半径が境界値の **`1.0`** に飽和（または接近）し、システム全体のエネルギーが閉回路に拘束されて制御不能となります。

TLUは、最適線形レギュレータ（LQR）制御理論を用いて、システムを健康な定常状態へ引き戻すためのフィードバックゲイン $K_{lqr}$ を算出し、その感度（Sensitivity Matrix）からシステム内の**「最も介入効果の高いノード（ツボ＝経穴：Acupressure Score最大ノード）」**を特定します。

$$u(t) = -K_{lqr} \cdot X(t)$$

### 📊 グラフの解読とサンプル比較 (Data Interpretation)

* **安定性・LQR制御グラフ:** `004_1_2__system_stability_dashboard.png`, `004_1_3__control_lqr_performance_space.png`, `004_2_1__sensitivity_matrix.png`

#### 🔴 システム安定性の境界飽和 (Sample 5, 7)

* **交通グリッドロック安定性:** [Sample 5 Stability Graph](../../samples/Sample_5_Kyoto_Traffic/readme_plots/004_1_2__system_stability.png)
* **共謀資金移動安定性:** [Sample 7 Stability Graph](../../samples/Sample_7_Market_Users_Weekly/readme_plots/004_1_2__system_stability.png)
  * *解読点:* スペクトル半径が `1.00` の水平な直線を描いて張り付いており、システムが自律的な減衰能力を失い、病的還流によって閉じた永久アトラクター（デッドロック）を形成している証拠です。

#### ⚕️ LQR感度によるツボの特定

* **Sample 5 LQR 制御感度スペース:** [Sample 5 LQR Space](../../samples/Sample_5_Kyoto_Traffic/readme_plots/004_1_3__control_lqr_performance_space.png)
* **Sample 7 LQR 制御感度スペース:** [Sample 7 LQR Space](../../samples/Sample_7_Market_Users_Weekly/readme_plots/004_1_3__control_lqr_performance_space.png)
  * *解読点:* グラフ上の「黄色い鋭いピーク」は、最も介入感度が高いノードを示しています。Sample 5 では `23_四条烏丸` や `13_二条烏丸`（感度 `41.52`）が、Sample 7 では還流ハブの `USR_003`/`USR_004` がそれに相当し、ここへ動的制限をかけることで還流ループを最小限の介入コストで破壊できることを示しています。

---

## 7. 信号処理と波動力学 (Wave Mechanics & Coherence - Prefix: `005_1`, `005_2`)

### 🔬 物理・数理理論 (Physics Theory)

健全なシステム（自然な商取引、日常の交通、安静時の脳神経）には、無数の独立した意思決定ノードが関与しているため、その合成周波数スペクトルは**「1/f ゆらぎ (Fractal Noise)」**を描きます。

これに対し、悪意ある注文ボットの共謀や、てんかん発作などの病的状態では、特定のノード同士がミリ秒単位でタイミングを合わせるため、波動力学的な**「位相同調 (Phase Coherence)」**が発生し、1/f ゆらぎのフラクタル傾きが急降下して「同期の死」を引き起こします。

TLUは、ノード間の位相差の時系列変化を測定する**「位相ドリフト（Phase Drift）」**およびコヒーレンス行列を計算し、統計モデルでは検知できない「隠された強制同期」を暴きます。

### 📊 グラフの解読とサンプル (Data Interpretation)

* **波動・ノイズスペクトルグラフ:** `005_1_1__resonant_frequency.png`, `005_1_2__phase_drift_heatmap.png`, `005_2_1__fractal_noise_spectrum.png`

#### 🟡 ボット同期取引の暴き出し (Sample 7)

株式市場における超高速 matched orders（Sample 7）では、共謀する2者間の位相差がゼロ近くに固定されます。

* **位相ドリフトヒートマップ (Phase Drift Heatmap):** [Sample 7 Phase Drift Heatmap](../../samples/Sample_7_Market_Users_Weekly/readme_plots/005_1_2__phase_drift_heatmap.png)
  * *解読点:* 特定のユーザーペア（`USR_003` と `USR_004`）の間だけ、位相差のばらつきが消失してヒートマップ上で真っ黒（位相差 `0.00`）に染まる定常バンドが出現します。これは、二人が独立してランダムに発注しているのではなく、ミリ秒単位で「同期してキャッチボールを繰り返している」という相場操縦の波動力学的実証です。

#### ⚕️ 検査基準と一次所見

1. **1/fノイズの傾き異常:** 周波数スペクトルを観察し、健康なピンクノイズから逸脱してフラット（白色）またはブラウン運動（茶色）化している場合、「多様性が失われ、一部のアルゴリズムや強権的プレイヤーにシステムが同期・支配されている」と判定します。
2. **同期の検出:** 位相ヒートマップにおいて、特定のノード群の波形が同期（位相差 `0.00`）している場合、「自然界ではあり得ない異常位相同調であり、人工的に仕組まれた還流不正（Wash Trade）である」と検査します。
