# 🔬 異常検知・財務健全性判定レポート (Sample 0)

## 1. 検査結論 (Executive Summary)

* **総合判定:** **正常・健全 (Healthy / Normal)**
* **重症度:** 🟢 **NORMAL (異常なし)**
* **概要:**
    本システムは、資産残高の推移（B/S）および取引流量（P/L）のいずれにおいても、不整合のない健全な状態を維持しています。循環取引（架空還流）、資金流出（簿外取引）、記帳ミスの兆候は検出されませんでした。

    時系列の推定過程において、4月、6月、7月、12月に流動性の Z-Score が一時的にしきい値 `3.0` を超え、**7月に最大 `4.90`** に達していますが、これは初期データの不足に伴う統計共分散の不安定性（コールドスタート問題）や、期末・決算期などの商取引の季節的集中に起因する**「統計的偽陽性 (False Positive)」**と判断されます。

    物理保存則に基づく **「システム保存残差（キルヒホッフ残差）`System Conservation Residual`」は全期間を通じて `0.00`** を維持しており、簿外への資金流出が発生していないことが数学的に証明されています。

---

## 2. 伝統的会計分析の限界 (Limitations of Traditional Audits)

売上高や自己資本の右肩上がりの推移のみを監視する従来の会計監査では、潜在的な資金滞留や簿外口座へのわずかな資金リークを検出することは困難です。本システムの伝統的なB/SおよびP/L推移は以下の通りです。

* **B/S 資産・資本推移 & ブロック図:**
    ![B/S Trend](../../../../samples/Sample_0_Healthy/readme_plots/000_0_1__BS_Trend.png)
    ![B/S Block Total](../../../../samples/Sample_0_Healthy/readme_plots/000_0_1__BS_Block_Total.png)
* **P/L 売上・費用推移 & ウォーターフォール図:**
    ![P/L Trend](../../../../samples/Sample_0_Healthy/readme_plots/000_0_1__PL_Trend.png)
    ![P/L Waterfall Total](../../../../samples/Sample_0_Healthy/readme_plots/000_0_1__PL_Waterfall_Total.png)

これらは一見すると現預金が増加し、販管費も売上に比例して拡大しているため健全に見えますが、真の安全性を確認するには、取引ネットワークのトポロジーや熱力学的パラメータを用いた多角的な検証が必要です。

---

## 3. 根本的な異常の特定 (Fundamental Pathophysiology)

本サンプルにおいて、**検出された異常（病理）はありません。**

管理部門、販売部門、製造部門等の間で行われるすべての取引フローは保存則を満たしており、不要な還流閉路や特定の取引関係への異常な集中は見られず、正常な取引活動に基づいています。

---

## 4. 数理解析エンジンによる定量データ

解析エンジンにより得られた主要な指標と可視化データは以下の通りです。

### 4.1. 質量保存則の検証 (Kirchhoff Residual)

システム全体の資金流入と流出の差分を示す `System Conservation Residual` は全期間を通じて **`0.00` (誤差なし)** であり、不正な簿外資金移動がないことを証明しています。

* **マクロフォレンジックダッシュボード:**
    ![Macro Forensics](../../../../samples/Sample_0_Healthy/readme_plots/002_2_1__macro_forensics_dashboard.png)

### 4.2. 結合剛性と主成分分析 (Stiffness & PCA)

剛性行列（Stiffness Matrix）の解析では、取引開始後、各勘定科目の間に偏りのないしなやかな接続が構築されています。特定の勘定科目間での資金滞留（剛性ロック）は発生していません。また、主成分分析（PCA）における主成分比率（Eigenvalue Ratio）もなだらかに分布しており、特定ペアへの極端な取引同期はありません。

* **構造剛性行列 (t=6):**
    ![Stiffness Month 7](../../../../samples/Sample_0_Healthy/readme_plots/000_2_1__structural_stiffness.t.00006.png)
* **PCA 主要軸比率:**
    ![PCA Ratio](../../../../samples/Sample_0_Healthy/readme_plots/000_2_2__principal_axes_ratio.png)

### 4.3. トポロジー解析と循環取引の排除 (Spectral Radius)

隣接結合行列の最大固有値である「スペクトル半径（Spectral Radius）」は、全期間にわたって **`0.00`** を維持しています。これは、架空売上などの資金還流ループが一切存在しないことを証明しています。

* **システム安定性指標 (Spectral Radius):**
    ![System Stability](../../../../samples/Sample_0_Healthy/readme_plots/004_1_2__system_stability.png)

### 4.4. 熱力学指標とエントロピー (Entropy & Free Energy)

内部エネルギー（Gross Activity $U$）は1月の `2,303,842.32` から12月の `4,132,519.04` へと増加し、それに並行して有効ポテンシャルを示す自由エネルギー（Free Energy $F$）も `2,303,842.32` から `3,869,999.47` へと着実に増加しています。
無駄な往復取引に起因する摩擦熱（エントロピー $T \times S$）の異常増加は見られず、商業的な支払サイクル（30〜90日程度）に整合する緩やかな散逸となっています。

* **熱力学エネルギースタック:**
    ![Thermodynamics Energy Stack](../../../../samples/Sample_0_Healthy/readme_plots/001_1_2__thermodynamics_energy_stack.png)
* **T-S ダイアグラム:**
    ![T-S Diagram](../../../../samples/Sample_0_Healthy/readme_plots/001_1_3__thermodynamics_ts_diagram.png)

### 4.5. 3D立体プロットによる多角解析

3Dプロットは、時間・空間の全方位においてシステムの平穏性を可視化しています。

* **① 3D運動位相空間軌跡:**
    ![3D Phase Portrait](../../../../samples/Sample_0_Healthy/readme_plots/000_1_8__phase_portrait_3d.png)
    軌道は安定アトラクターに滑らかに収束しており、還流による歪みやバーストは生じていません。
* **② 3D局所熱力学プロット:**
    ![3D Local Entropy](../../../../samples/Sample_0_Healthy/readme_plots/001_1_2_1__3d_local_entropy.png)
    ![3D Local Temperature](../../../../samples/Sample_0_Healthy/readme_plots/001_1_2_2__3d_local_temperature.png)
  * **局所エントロピー ($s_i$):** 単一の流出先しか持たない科目は数学的に `0.00` です。複数の流出先（経費支払や仕入れ）を持つ現預金ノード（`ACC_Cash`）のみが、正常範囲内（1.18〜1.86 bits、平均約 1.51 bits）の低エントロピーで推移しています。
  * **局所温度 ($T_i$):** 勘定残高の時系列ボラティリティを示します。急激な資金の往復や不整合が存在しないため、全期間において低く安定した平坦な温度分布を描いています。
* **③ 3Dミクロ情報幾何学プロット:**
    ![3D Micro KL Drift](../../../../samples/Sample_0_Healthy/readme_plots/002_2_2_1__3d_micro_kl_drift.png)
    全ノードにおいて KL Drift はゼロに近く、不正の開始を示すスパイクは一切検出されていません。

---

## 5. 制御介入と推奨アクション (LQR & Operations)

* **治療方針:** **対応不要 (No Treatment Required)**
* **LQR 介入:** システムは最適なバランス状態にあるため、フィードバック制御による介入は不要です。
    ![Sample 0 LQR Control](../../../../samples/Sample_0_Healthy/readme_plots/004_1_3__control_lqr_performance_space.png)
* **推奨アクション:**
    データ上の構造的健全性は証明されています。監査・管理チームは、データ整合性の調査ではなく、実地での銀行残高証明書の原本照合など、システム外の物理的実在性の検証にリソースを集中することを推奨します。

---

## 6. 🚨 アラートトリアージ & 反証可能性

### 6.1. 統計的偽陽性の判定 (False Positive Assessment)

* **アラート内容:** 4月 (`4.7943`), 6月 (`3.3940`), 7月 (`4.90`), 12月 (`3.8833`) において Z-Score が警告閾値 `3.0` を超過。
* **判定理由:**
    これは統計モデルの過渡的な偽陽性です。初期ステップにおける共分散推定の不さや、一時的な資金移動の集中（季節的要因）が強調されたものと判断されます。保存則残差が `0.00` を維持し、循環トポロジーも形成されていないため、これらのアラートは正常なゆらぎとして無視（Dismiss）して差し支えありません。

### 6.2. 本検査に対する反証条件 (Falsifiability)

本検査（健全）を覆すには、以下のいずれかの客観的証拠が必要です。

1. **銀行口座残高の不一致:** 帳簿上の現金残高と、金融機関から直接取得した「銀行預金通帳原本」等の残高の間に、1円でも調整不能なズレが存在すること。
2. **簿外口座の存在:** 把握している取引ネットワーク外に、システムから漏洩した資金を受け取るための未登録口座・別会社が存在すること。
