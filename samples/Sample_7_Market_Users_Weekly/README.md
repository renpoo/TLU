# 🔬 TLU Medical & Consulting Report (Laboratory Findings)

**Target Sample:** `Sample_7_Market_Users_Weekly` (ユーザー間取引市場・エコシステム)
**Time Granularity:** Weekly

---

## 1. Executive Summary (診断の要約)

**結論: 🔴 Critical Condition - Systemic Fragility & Flash Crash (脆弱な体質と突発的な発作)**

本サンプル（ユーザー間取引市場）は、普段は活発に取引が行われているように見えますが、内部に極めて危険な「脆弱性（フラッシュクラッシュの種）」を抱えています。
自由エネルギーの分布が「極端な負の歪み（Negative Skewness: -2.64）」を示しており、これは「システムが突然ショックを吸収しきれなくなり、周期的に心不全（流動性の枯渇）を起こす」という非常に危険な体質であることを物理的に証明しています。

---

## 2. Foundation & Constitution (基礎体力と体質)

![B/S Total](output_plots/000_0_1__BS_Block_Total.png)
![P/L Waterfall](output_plots/000_0_1__PL_Waterfall_Total.png)
![P/L Trend](output_plots/000_0_1__PL_Trend_Revenue_vs_Expenses.png)

市場全体のボリューム（体格）は維持されており、表面上は「流動性の高い健康な市場」に見えます。しかし、比較衡量の原則に従えば、この高いボラティリティこそが「発作の予兆」です。

---

## 3. Statistical Baseline (基本統計量)

![Histogram](output_plots/support/000_0_2_3__histogram_kde.png)
![Rolling Quantiles](output_plots/000_0_2_4__rolling_quantiles.png)

- **分析 (Z-Scoreの超過):** Z-Scoreが `3.0` を超える明らかな異常値（発作）が2回記録されています。統計的な確率分布（KDE）には「左に長く引いた尾（ファットテール）」が存在しており、これはシステムが「ゆっくりと成長し、ある日突然暴落する」という非対称な病態（Fragility）に陥っていることを示します。

---

## 4. Macro Thermodynamics (マクロ熱力学と気の滞り)

![Thermodynamics Dashboard](output_plots/001_1_1__thermodynamics_dashboard.png)
![Thermodynamics Stack](output_plots/001_1_2__thermodynamics_energy_stack.png)
![T-S Diagram](output_plots/001_1_3__thermodynamics_ts_diagram.png)

- **分析 (負の歪み):** 自由エネルギー（F）の歪度（Skewness）が `-2.64` です。システム内のエネルギーが一部の巨大ユーザー（クジラ）に吸い寄せられ、末端のユーザーにはエネルギーが行き渡らない「極端な貧富の差（偏り）」が起きています。

---

## 5. Structural Pathology (経絡の断裂と変異)

![Macro Forensics](output_plots/002_2_1__macro_forensics_dashboard.png)

- **分析:** Leak Ratio は `0.0` です。市場外への資金流出（ハッキング等）は起きていません。問題は内部の構造的偏りにあります。

---

## 6. System Stability (動的安定性と脈)

![System Stability](output_plots/004_1_2__system_stability_dashboard.png)

- **分析 (脈の暴走と共振):** 最大スペクトル半径が `1.0` に達しています。市場参加者が皆同じ方向（群集心理）に動くことで、価格が異常なフィードバックループ（共振）を起こしています。この人工的な「同期」がフラッシュクラッシュ（発作）の引き金です。

---

## 7. Deep Dive Analytics & Treatment Plan (詳細病因特定と治療方針)

### 7.1 Micro Pathology (病因の特定)
![3D Z-Score X](output_plots/support/002_2_2_2__3d_micro_z_score_X.png)
![3D KL Drift](output_plots/support/002_2_2_1__3d_micro_kl_drift.png)

- **病因の特定:** 特定のアルゴリズムトレーダー、または少数の巨大ノードが、相場を牽引する形で異常なZ-Scoreを記録しています。彼らの動きがシステム全体の位相を狂わせています。

### 7.2 Kinematic State Space (体格と肩こり)
![Phase Portrait 3D](output_plots/support/000_1_8__phase_portrait_3d.png)
![3D Inertia](output_plots/support/000_1_4__3d_dynamics_inertia.png)
![3D Viscosity](output_plots/support/000_1_5__3d_dynamics_viscosity.png)

- **体格と肩こりの診断:** 粘性が非常に高い状態です。市場の摩擦（スリッページや流動性コスト）が高いため、ショックが発生した際に価格が滑り落ちるのを誰も止められません。

### 7.3 Information Geometry & Stress (トポロジーの変遷)
![Topology t=0](output_plots/support/002_1_2__network_topology.t.00000.png)
![Topology t=3](output_plots/support/002_1_2__network_topology.t.00003.png)
![Topology t=5](output_plots/support/002_1_2__network_topology.t.00005.png)
![Topology t=8](output_plots/support/002_1_2__network_topology.t.00008.png)
![Topology t=11](output_plots/support/002_1_2__network_topology.t.00011.png)

### 7.4 Wave Mechanics & Fractal Noise (波動と人工的同期)
![Fractal Noise](output_plots/support/005_2_1_fractal_noise_spectrum.png)
- **分析:** 市場全体が一つの巨大な波に同期してしまっており、多様性（ピンクノイズ）が失われています。

### 7.5 LQR Control & Dynamic Treatment (経絡秘孔の特定と自律的治療提案)
![LQR Space](output_plots/support/004_1_3__control_lqr_performance_space.png)
![Sensitivity Matrix](output_plots/support/004_2_1__sensitivity_matrix.png)

- **診断と治療方針 (Oriental Medicine Consulting):** 
  この市場の脆弱性を治療するための特効薬（ツボ）は以下の通りです。
  1. **位相のズレ（Phase Shift）の分散:** 現在、全ユーザーが同じタイミングで売買する「位相の同期（群集心理）」が起きています。取引手数料の動的変動（ダイナミックプライシング）や、指値注文に対するインセンティブ設計を導入し、参加者の「取引タイミング（位相）」を意図的に分散させ、共振ループを破壊してください。
  2. **慣性（Inertia）の再配分:** 巨大な慣性を持つ一極集中のノード（クジラ）がシステムを支配しています。市場の多様性を回復するため、小口ユーザーへの流動性還元（ダイエットと代謝の促進）が必要です。

---

## 8. 🚨 Forensic Alert & Falsifiability (異常・不正の別途指摘と反証可能性)

* **🚨 Forensic Alert:** 
  漏洩（Leakage）はなく、意図的な横領行為はありません。しかし、スペクトル半径1.0と負の歪度は「特定のアルゴリズムによる市場操縦（Market Manipulation / Wash Trade）」の可能性を示唆しています。
* **Verification Requirements (反証可能性の確認):**
  1. フラッシュクラッシュ（Z-Score超過）が発生した週の直前に、特定のノード群間で自己売買（Wash Trade）のループが形成されていないか、取引ログを個別に追跡すること。
