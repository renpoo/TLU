# 🔬 メタ検査臨床検査レポート：循環取引（架空売上の自己還流ループ） (Sample 1)

## 1. 検査結論 (Executive Summary)

* **総合検査:** **位相幾何学的循環不全（Wash Trade / 自己還流ループ）**
* **重症度:** 🟠 **HIGH (重篤な資金還流障害)**
* **アノマリー発生時期と金額（仕訳原本検証済み）:**
  * **2020-01-03 (t=0)**: 金額 **`$40,433.60`** (仕訳 ID: `E_000020`〜`E_000022`)
  * **2020-02-01 (t=1)**: 金額 **`$53,282.77`** (仕訳 ID: `E_000257`〜`E_000259`)
  * **2020-05-22 (t=4)**: 金額 **`$44,939.48`** (仕訳 ID: `E_001327`〜`E_001329`)
* **臨床概要:**
  本システムは、現預金と売掛金のキャッチボールによる循環取引（売上水増し）が発生しています。
  ダブルエントリーによる貸借平均の原則（保存則）は維持されています。そのため、従来の監査手法（静的試算表の検証など）では検出不可能です。
  物理解析エンジンは、隣接結合行列の最大固有値である最大スペクトル半径 $\rho$ = 0.7488$ の上昇と、内部エネルギーを自己還流させる閉路の形成を特定しました。
  この往復取引は、キャッシュ残高の変動（ボラティリティ上昇）をもたらします。システム温度 $T$ およびエントロピー損失 $TS$ を増大させます。その結果、システム全体の自由エネルギー $F = U - TS$ が減少しています。資金繰りの破綻（黒字倒産）を招く状態です。

---

## 2. 伝統的表層分析の限界：累積 vs 期間別（単月）の可視化

伝統的な会計監査や累積スナップショット（B/S, P/L）の監視では、この還流を見抜くことはできません。貸借を一致させて記帳しているためです。B/S はバランスします。P/L 上では売上高が拡大します。営業黒字（累積売上 `$1,094,143.89` に対して純利益 `$201,321.16`）が達成されているように見えます。

累積（Cumulative）と期間別（Periodic / 単月）の財務諸表プロットを並べて比較します。異常値のスパイクが特定月（1月, 2月, 5月）に集中して発生しています。

### B/S 資産・資本推移の比較（累積 vs 期間別）

* **累積 B/S Trend:**
  ![B/S Trend](readme_plots/000_0_1__BS_Trend.png)
* **期間別（単月） B/S Trend (Periodic):**
  ![B/S Trend Periodic](readme_plots/000_0_1__BS_Trend_Periodic.png)

### B/S ブロック合計の比較（累積 vs 期間別）

* **累積 B/S Block Total:**
  ![B/S Block Total](readme_plots/000_0_1__BS_Block_Total.png)
* **期間別（単月） B/S Block Total (Periodic):**
  ![B/S Block Total Periodic](readme_plots/000_0_1__BS_Block_Total_Periodic.png)

### P/L 売上・費用推移の比較（累積 vs 期間別）

* **累積 P/L Trend:**
  ![P/L Trend](readme_plots/000_0_1__PL_Trend.png)
* **期間別（単月） P/L Trend (Periodic):**
  ![P/L Trend Periodic](readme_plots/000_0_1__PL_Trend_Periodic.png)

### P/L ウォーターフォール図の比較（累積 vs 期間別）

* **累積 P/L Waterfall:**
  ![P/L Waterfall Total](readme_plots/000_0_1__PL_Waterfall_Total.png)
* **期間別（単月） P/L Waterfall (Periodic):**
  ![P/L Waterfall Total Periodic](readme_plots/000_0_1__PL_Waterfall_Total_Periodic.png)

**【対比分析】**
累積グラフでは緩やかに上昇しているように見えます。期間別（Periodic）グラフでは、1月 (t=0)、2月 (t=1)、5月 (t=4) において現預金（Cash）と売掛金（AR）の取引がスパイクを発生させていることがわかります。

---

## 3. 固有トポロジーと剛性の硬直化

循環取引の発生は、ネットワークトポロジーの構造的な歪みと、特定の勘定科目間における「剛性（Stiffness）のロック」として現れます。

### 剛性行列（Stiffness Matrix）の時系列シーケンス

循環取引が発生した月には、現預金（`ACC_Cash`）と売掛金（`ACC_Accounts_Receivable`）の間の結合が硬直化します。

* **① 2020-01 (t=0: 還流開始時):**
  ![Stiffness t0](readme_plots/000_2_1__structural_stiffness.t.00000.png)
* **② 2020-04 (t=3: 一時沈静期):**
  ![Stiffness t3](readme_plots/000_2_1__structural_stiffness.t.00003.png)
* **③ 2020-05 (t=4: 還流再発時):**
  ![Stiffness t4](readme_plots/000_2_1__structural_stiffness.t.00004.png)
* **④ 2020-06 (t=5: 還流終了直後):**
  ![Stiffness t5](readme_plots/000_2_1__structural_stiffness.t.00005.png)
* **⑤ 2020-12 (t=11: 最終観測期):**
  ![Stiffness t11](readme_plots/000_2_1__structural_stiffness.t.00011.png)

### 主成分分析（PCA）と固有ベクトル推移

主成分分析におけるエネルギー寄与率は、アノマリーの発生期（t=4）に第1主成分（PC1）が **`95.28%`** に達します。流動性が支配されていることを示します。

* **PCA 主要軸比率 (PCA Principal Axes Ratio):**
  ![PCA Ratio](readme_plots/000_2_2__principal_axes_ratio.png)

PC1, PC2, PC3 の固有ベクトルを分析します。異常取引を主導した勘定科目の影響度がわかります。

* **PC1 固有ベクトル推移:**
  ![PC1 Eigenvector](readme_plots/000_2_3__eigenvector_evolution.png)
  第1主成分では `01_ACC_Accounts_Receivable` (`-0.7162`) と `03_ACC_Cash` (`0.3524`)、`07_ACC_Sales_Revenue` (`0.5183`) に成分が集中します。特定の還流ペアが全社の流動性を支配していることを示します。
* **PC2 固有ベクトル推移:**
  ![PC2 Eigenvector](readme_plots/000_2_3__eigenvector_evolution_pc2.png)
* **PC3 固有ベクトル推移:**
  ![PC3 Eigenvector](readme_plots/000_2_3__eigenvector_evolution_pc3.png)

### 最大スペクトル半径 $\rho$ （システム安定性）

最大スペクトル半径は、還流の発生月（1月, 2月, 5月）に上昇します。トポロジー的に資金還流閉路が構築されていた証拠を示します。

* **システム安定性指標 (Spectral Radius):**
  ![System Stability](readme_plots/004_1_2__system_stability.png)

### ネットワーク・トポロジー時系列シーケンス

* **① 2020-01 (t=0: 現預金 ⇄ 売掛金の双方向エッジが形成):**
  ![Topology t0](readme_plots/002_1_2__network_topology.t.00000.png)
* **② 2020-04 (t=3: 通常の流路へ分散):**
  ![Topology t3](readme_plots/002_1_2__network_topology.t.00003.png)
* **③ 2020-05 (t=4: 自己還流ループが再接続):**
  ![Topology t4](readme_plots/002_1_2__network_topology.t.00004.png)
* **④ 2020-06 (t=5: 還流チャネルが細り、通常化へ移行):**
  ![Topology t5](readme_plots/002_1_2__network_topology.t.00005.png)
* **⑤ 2020-12 (t=11: 正常な業務フローへ復帰):**
  ![Topology t11](readme_plots/002_1_2__network_topology.t.00011.png)

---

## 4. 永久空転熱力学サイクルとモデル汚染

本サンプルの熱力学的挙動は、エネルギー浪費（摩擦熱）の存在と、AI統計モデルの死角を示します。

### 熱力学エネルギー構造の可視化

* **熱力学エネルギースタック:**
  ![Thermodynamics Energy Stack](readme_plots/001_1_2__thermodynamics_energy_stack.png)
* **T-S ダイアグラム (T-S Diagram):**
  ![T-S Diagram](readme_plots/001_1_3__thermodynamics_ts_diagram.png)

1. **摩擦熱（エントロピー損失 $TS$）の膨張:**
   還流が発生する月（1月, 2月, 5月）に、残高の往復移動によってボラティリティ（システム温度 $T$）がスパイクします。エントロピー損失（赤色の $-TS$ 領域）が増大します。見かけの総活動量（内部エネルギー $U$）が増大します。しかし、自由エネルギー $F = U - TS$（白色の境界線）は減少しています。
2. **反時計回りのカルノーサイクル（T-S閉回路）:**
   T-Sダイアグラムは、閉じた卵型サイクルを描します。この閉路が囲む面積は、外部に仕事をせずシステム内部で放出された摩擦熱の総量です。還流による空転を示します。

### 3D 空間での局所熱力学的異常

* **3D 局所エントロピー ( $s_i$ ):**
  ![3D Local Entropy](readme_plots/001_1_2_1__3d_local_entropy.png)
  `ACC_Cash` が `ACC_Accounts_Receivable` への迂回流路（Wash Funding）を形成します。流出確率の偏りが生じます。還流月に局所エントロピーの上昇が検知されます。
* **3D 局所温度 ( $T_i$ ):**
  ![3D Local Temperature](readme_plots/001_1_2_2__3d_local_temperature.png)
  還流に関与する3ノード（現預金、売掛金、売上）において、残高ボラティリティの急増を示す局所温度のスパイクが発生しています。

### 3D ミクロ情報幾何学と「茹でガエル現象」（モデル汚染）

* **3D Micro KL Drift (情報幾何学的変化量):**
  ![3D Micro KL Drift](readme_plots/002_2_2_1__3d_micro_kl_drift.png)
* **3D Micro Z-Score (残高の位置偏差):**
  ![3D Micro Z-Score](readme_plots/002_2_2_2__3d_micro_z_score_X.png)

**【茹でガエル現象 (Model Pollution) の数学的証明】**
3D Micro KL Drift プロットでは、2020-01〜02の最初の還流において、`ACC_Cash` ノードに検出スパイクが立ち上がります。しかし、2020-05の還流では、同規模の循環取引であるにもかかわらず、検出される KL Drift スパイクが減少しています。
統計モデルが過去の異常取引を正常なベースラインの一部として学習するためです。統計的なしきい値監視だけに依存すると、リピートする異常を見落とす可能性があります。本システムでは、物理的な保存則と最大スペクトル半径というトポロジー指標を組み合わせます。これにより統計モデルの死角を回避します。

---

## 5. 局所治療処方箋 (LQR Control Treatment)

* **治療方針: 還流トポロジーの切断とピンポイント介入**
* **LQR 感度介入効果:**
  最適線形制御（LQR）による感度解析において、本ネットワークでは `ACC_Accounts_Receivable` (売掛金) ノードへの制御介入が最大の効果を発揮します。
  ![LQR Control](readme_plots/004_1_3__control_lqr_performance_space.png)

* **具体的な介入計画:**
  1. **トポロジー的インターロックの導入:**
     `ACC_Cash` ⇄ `ACC_Accounts_Receivable` 間の往復取引に対して、「1分以上のディレイ処理」または「二重決済の警告」システムを導入します。還流パスを物理的に切断します。
  2. **LQRピンポイント抑制:**
     LQR感度に基づき、還流のハブとなっている特定の取引先に紐づく売掛金残高に対してのみ取引上限枠を制限します。または個別承認プロセスを自動で実行します。健全な取引を阻害することなく、アノマリーの発生源となっている結合部を無力化します。

---

## 6. 🚨 反証可能性 (Falsification Analytics)

本レポートの判定が誤りであり、システムが健全な商取引を行っていると反証するには、以下の証拠を提示する必要があります。

1. **物流の原本証明:**
   対象ステップ（1月3日、2月1日、5月22日）における取引金額（計 `$138,655.85`）に対応する、物流業者が発行した「荷物追跡番号付き出荷伝票原本」および「納品確認書（受領印付き）」。実物の移動が存在したことの証明。
2. **法的主体の独立性証明:**
   送金元および送金先となっている法人が、同一支配下にないことを証明する「登記事項証明書原本」および「実質的支配者リスト（株主名簿原本）」。
