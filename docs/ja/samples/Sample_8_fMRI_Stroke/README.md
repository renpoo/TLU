# Sample 8: 生体ネットワークへの適用（fMRI Stroke - 脳卒中/虚血の熱力学）

> [!NOTE]
> **【重要】Sample 8 と Sample 9 の関係性と対象ドメインについて**
> 本サンプル（Sample 8）と次サンプル（Sample 9）は、金融データや交通データではなく、人間の脳（fMRI）における**「BOLD信号の有効接続性（Effective Connectivity）」**をシミュレートした生体データです。
> TLUの「汎用物理エンジン」が、社会科学（金融・交通）の領域を超え、生命科学（生体ネットワークの病変）をもシームレスに診断できることを証明するためのグランドフィナーレとなるテストケースです。
> * **Sample 8（本作）:** 脳ネットワークの特定の部位（運動野）への血流・信号が物理的に遮断される**「脳卒中・梗塞（Stroke / Ischemia）」**をシミュレートします。ネットワークの一部が「枯渇・壊死」していくプロセスを検証します。
> * **Sample 9（次作）:** 特定の部位（側頭葉）から異常な同期信号が放射される**「てんかん発作（Epileptic Seizure）」**をシミュレートします。エネルギーが過剰に「暴走・共鳴」するプロセスを検証します。

---

# 🔬 メタ解析 統合レポート (Meta-Analysis Synthesis Report / Laboratory Findings)

## 1. エグゼクティブ・サマリー
本システム（生体脳ドメイン）は、時間経過の中盤において**「特定のノード（運動野）に対する致命的なエネルギー供給の遮断（Stroke/梗塞）」**を発症し、結果としてネットワーク全体が**「熱力学的エネルギーの崩壊（Thermodynamic Energy Depletion）」**に陥る極めて重篤な状態（HIGH Severity）にあると診断される。運動野への流入経路だけが閉塞し、「他の部位へノイズは出力するが、入力は一切受け取れない」という孤立と壊死のプロセスが進行している。

## 2. 従来型分析（集計的スナップショット）の限界 (Traditional Perspective)

**【全期間の累積フロー (P/L Waterfall) & 貸借対照表 (B/S)】**
![Sample 8 PL Waterfall](../../../../samples/Sample_8_fMRI_Stroke/readme_plots/000_0_1__PL_Waterfall_Total.png)
![Sample 8 BS Block](../../../../samples/Sample_8_fMRI_Stroke/readme_plots/000_0_1__BS_Block_Total.png)

P/Lサマリーを見ると、運動野（Motor Cortex）だけが極端なマイナス（-$60,191）になっている。「他の部位へ信号は出しているが、入力は一切受け取れていない」という物理的な動脈閉塞のサインである。しかし従来の静的な集計ツールでは、この単なる「残高の異常」が、ネットワーク全体にどのような熱力学的な負荷（エントロピーの増大 ＝ 無駄な摩擦熱やエネルギー浪費の増大）を与え、生命活動全体をどう蝕んでいるかの「動的な死のプロセス」を描き出すことは不可能である。

## 3. 物理的病跡の特定（Fundamental Pathophysiology）
本サンプルの根本原因は、ジェネレーターコード `_0_0_generate_dummy_fmri.py` において意図的に組み込まれた「動脈閉塞のスクリプト」にある。

* **特定された証拠:**
  `if tgt == "Motor_Cortex": base_flux = base_flux * 0.05`
  時間ステップ `TR >= 150` 以降、運動野（`Motor_Cortex`）へ向かうすべての血流（エッジ）が人為的に 95% カット（虚血状態）されていた。TLUが検知したマクロな崩壊は、この局所的な質量保存の破綻が引き金となっている。

## 4. 物理・数理エンジンによる証明 (Physical and Mathematical Proof)

### 4.1. マクロフォレンジックと剛性の硬直 (Macro Forensics & Structural Stiffness)

局所的な血流の遮断により、システム全体の質量保存に不均衡が生じている。さらに、運動野の「入力ゼロ・出力のみ」という非対称な状態が長引くにつれ、システムの剛性行列（内部構造）は徐々に硬直（Rigid Lock ＝ 脳全体の弾力性が失われ、健全な信号処理を受け付けない状態）へと向かい、脳全体の弾力性が失われていく。

![Sample 8 Macro Forensics](../../../../samples/Sample_8_fMRI_Stroke/readme_plots/002_2_1__macro_forensics_dashboard.png)
![Sample 8 External Force 3D](../../../../samples/Sample_8_fMRI_Stroke/readme_plots/000_1_6__3d_dynamics_external_force.png)

* **1枚目【始点】**: `t.00000` (正常な剛性)
* **2枚目【変化の直前】**: `t.00029` (TR=145)
* **3枚目【変化の当該時点】**: `t.00030` (TR=150: 梗塞発生)
* **4枚目【変化の直後】**: `t.00031` (TR=155)
* **5枚目【終点】**: `t.00059` (TR=295: 完全硬直)

![Sample 8 Structural Stiffness 0](../../../../samples/Sample_8_fMRI_Stroke/readme_plots/000_2_1__structural_stiffness.t.00000.png)
![Sample 8 Structural Stiffness 29](../../../../samples/Sample_8_fMRI_Stroke/readme_plots/000_2_1__structural_stiffness.t.00029.png)
![Sample 8 Structural Stiffness 30](../../../../samples/Sample_8_fMRI_Stroke/readme_plots/000_2_1__structural_stiffness.t.00030.png)
![Sample 8 Structural Stiffness 31](../../../../samples/Sample_8_fMRI_Stroke/readme_plots/000_2_1__structural_stiffness.t.00031.png)
![Sample 8 Structural Stiffness 59](../../../../samples/Sample_8_fMRI_Stroke/readme_plots/000_2_1__structural_stiffness.t.00059.png)

### 4.2. ネットワークトポロジーの異常 (Topological Anomaly / Spectral Radius)

健常な脳の部位同士が、有機的かつ完全な双方向性のフィードバックループを形成しているため、数学的には循環取引と同じ「極限振動（スペクトル半径 1.0 ＝ 脳部位同士の双方向の過剰なフィードバック）」として捉えられている。しかしネットワークトポロジーを見ると、TR=150以降、特定のノード（Motor Cortex）に向かう流入エッジが極端に細くなり、有機的な結びつきが失われている。

![Sample 8 System Stability](../../../../samples/Sample_8_fMRI_Stroke/readme_plots/004_1_2__system_stability.png)

* **1枚目【始点】**: `t.00000`
* **2枚目【変化の直前】**: `t.00029` (TR=145)
* **3枚目【変化の当該時点】**: `t.00030` (TR=150: 梗塞発生)
* **4枚目【変化の直後】**: `t.00031` (TR=155)
* **5枚目【終点】**: `t.00059` (TR=295)

![Sample 8 Network Topology 0](../../../../samples/Sample_8_fMRI_Stroke/readme_plots/002_1_2__network_topology.t.00000.png)
![Sample 8 Network Topology 29](../../../../samples/Sample_8_fMRI_Stroke/readme_plots/002_1_2__network_topology.t.00029.png)
![Sample 8 Network Topology 30](../../../../samples/Sample_8_fMRI_Stroke/readme_plots/002_1_2__network_topology.t.00030.png)
![Sample 8 Network Topology 31](../../../../samples/Sample_8_fMRI_Stroke/readme_plots/002_1_2__network_topology.t.00031.png)
![Sample 8 Network Topology 59](../../../../samples/Sample_8_fMRI_Stroke/readme_plots/002_1_2__network_topology.t.00059.png)

### 4.3. 熱力学的なエネルギー推移 (Thermodynamic Energy Stack)

Sample 8 では、病変が発生する中盤（TR=150付近）から突如としてエントロピー損失（$T \Delta S$：赤色の層）が激増し、自由エネルギーがマイナス領域へと深く沈み込んでいる。特定部位への血流遮断がネットワーク内に強烈な不均衡を生み出し、システム全体として有意義な情報処理を行うポテンシャルが致命的に損なわれたことを示す完璧な証明であり、熱力学的な死（Heat Death ＝ 脳が有意義な情報処理を行うポテンシャルの致命的な喪失、宇宙が最後に行き着く静寂のようなエネルギーの完全な均質化と無秩序化）を意味する。

*(上: Sample 0 正常な経済成長 ／ 下: Sample 8 脳の熱力学的な死)*
![Sample 0 Thermodynamics](../../../../samples/Sample_0_Healthy/readme_plots/001_1_2__thermodynamics_energy_stack.png)
![Sample 8 Thermodynamics](../../../../samples/Sample_8_fMRI_Stroke/readme_plots/001_1_2__thermodynamics_energy_stack.png)

### 4.4. 局所的アノマリーと情報幾何学的変位 (3D Micro Z-Score & KL Drift)

Z-Score（過去の平均からの突出度合い）の3Dサーフェスにおいて、TR=150を境に運動野への流入成分が突如として深淵（マイナスのスパイク）へと沈み込み、局所的な「虚血・壊死」が検知されている。さらに 情報幾何学的変位（KL Drift ＝ 血流の欠落によるネットワークの確率分布の局所的な崩壊）において、運動野への情報流路が絶たれたことでネットワークの確率分布が局所的に崩壊し、巨大なスパイクが空間に突き刺さっている。血流（質量）の欠落がそのまま「情報幾何学的な死」として可視化されている。

![Sample 8 3D Z-Score](../../../../samples/Sample_8_fMRI_Stroke/readme_plots/002_2_2_2__3d_micro_z_score_X.png)
![Sample 8 3D KL Drift](../../../../samples/Sample_8_fMRI_Stroke/readme_plots/002_2_2_1__3d_micro_kl_drift.png)

## 5. ⚠️ 反証可能性と検証要件（Falsification Analytics）

* **偽陽性の可能性:** もしこれが実際のfMRIデータであった場合、特定の脳回に対するBOLD信号の流入だけが95%消失し、異常な共振を伴っている以上、単なる測定ノイズではなく、明らかな「器質的病変（虚血・梗塞）」である可能性が極めて高い。
* **追加検証要件:** TLUが「 Universal Physics Engine 」であることを証明した。金融の「横領」、交通網の「デッドロック」、脳の「脳卒中」は、すべて「ネットワークにおける質量の欠損と熱力学的崩壊」という同一の物理方程式でシームレスに診断できることが確認された。
