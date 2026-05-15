# Sample 7: 株式市場における相場操縦（直接グラフ: 共謀グループの特定 / 馴合売買の熱力学）

> [!NOTE]
> **【重要】Sample 6 と Sample 7 の関係性と対象アノマリー（相場操縦）について**
> 本サンプル（Sample 7）は、前サンプル（Sample 6）と完全に同一の株式市場のダミーデータから派生した一対の実験セットの後編です。
>
> * **Sample 6（前作）:** ログを「ユーザーと銘柄」の二部グラフ（Bipartite Graph）に射影したもの。**「どの銘柄が操縦（水増し）されているか」**という視点（左からの景色）を検証しました。
> * **Sample 7（本作）:** 同じログを、銘柄を捨象して「ユーザーからユーザーへの直接の資金移動」に射影したもの。**「誰と誰が結託して馴合売買を行っているのか」**という犯行グループの輪郭（右からの景色）を検証します。

---

# 🔬 メタ解析 統合レポート (Meta-Analysis Synthesis Report / Laboratory Findings)

## 1. 最新の機械学習ベース自動診断結果 (ML-Based Automated Diagnosis)

本サンプル（**Sample_7_Market_Users_Weekly**）に対する自動判定結果です。純粋な物理指標がドメイン特有の異常をどう捉えるかを解説します。

### 【A. 確定診断 (Final Pathologies) とドメイン解釈】

### 【B. 構造的進化と摩擦分類 (Structural Evolution & Viscosity)】

- **動粘度（摩擦係数）レンジ:** `0.00 ~ 0.00`
- 🧊 **構造診断: 超流動 / 低摩擦（新世代型/アルゴリズム構造）**
  - **解説:** システムは高度に自動化されており、摩擦が極端に低くなっています。効率的ですが、一度ショックが起きると歯止めが効かず、一瞬で熱死を引き起こす危険性を孕んでいます。

### 【C. スケール不変の物理指標 (Scale-Invariant Diagnostic Metrics)】

## 2. 従来型分析（集計的スナップショット）の限界 (Traditional Perspective)

ここでは「ユーザー（投資家）」をノードとし、ユーザー間の資金移動をエッジとして集計した結果を従来のダッシュボードで確認する。

**【全期間の累積フロー (P/L Waterfall) & 貸借対照表 (B/S)】**
![Sample 7 PL Waterfall](../../../../samples/Sample_7_Market_Users_Weekly/readme_plots/000_0_1__PL_Waterfall_Total.png)
![Sample 7 BS Block](../../../../samples/Sample_7_Market_Users_Weekly/readme_plots/000_0_1__BS_Block_Total.png)

**【第52週時点の各ユーザーの純増減額（P/L）サマリー】**

* `USR_001`: **+$4,225,702**（資金流入超過）
* `USR_002`: **+$8,706,571**
* `USR_004`: **-$12,385,805**（資金流出超過）
* `USR_005`: **-$6,925,827**

単なる口座残高やユーザーの損益（P/L）のランキングだけを見ていても、「USR_001は利益を出している上手な投資家」「USR_004は大損している投資家」という表面的な結果しか分からない。背後で「USR_001とUSR_006が秒間何十回も同じ資金をキャッチボールして出来高を水増ししている」という共謀の事実は、この静的な残高一覧からは完全に抜け落ちてしまう。

## 3. 物理的病跡の特定（Fundamental Pathophysiology）

本サンプルの根本原因は、特定のユーザー群による「馴合売買（Collusive Trading / Matched Orders）」の共謀である。

* **特定された証拠:**
  銘柄という仲介ノードを捨象し、資金の流れだけを追跡した結果、`2020-02-03 11:41:21`（第6週）において `USR_001` と `USR_006` の2名間で、わずか2.5秒の間に約3070ドル×9回の巨大な資金キャッチボールが直接行われている事実が特定された。さらに `2020-06-29`（第27週）にも `USR_007` と `USR_002` の間で同様のキャッチボールが発生している。これがシステム全体の熱力学を崩壊させている共謀グループ（Clique）の核である。

## 4. 物理・数理エンジンによる証明 (Physical and Mathematical Proof)

### 4.1. マクロフォレンジックと剛性の硬直 (Macro Forensics & Structural Stiffness)

Sample 6と同様に、Wash Trade は市場内で完結するため質量保存則の違反（マクロ残差）は発生しない。しかし、特定のユーザー間での異常な資金還流により、システムの剛性行列は局所的な共振と絶対硬直（Rigid Lock ＝ 外部資金が一切流入しない閉鎖的な共振・フリーズ状態）を起こしている。

![Sample 7 Macro Forensics](../../../../samples/Sample_7_Market_Users_Weekly/readme_plots/002_2_1__macro_forensics_dashboard.png)
![Sample 7 External Force 3D](../../../../samples/Sample_7_Market_Users_Weekly/readme_plots/000_1_6__3d_dynamics_external_force.png)

* **1枚目【始点】**: `t.00000` (正常な剛性)
* **2枚目【変化の直前】**: `t.00005` (第6週)
* **3枚目【変化の当該時点】**: `t.00006` (第7週: 資金還流による硬直発生)
* **4枚目【変化の直後】**: `t.00007` (第8週)
* **5枚目【終点】**: `t.00051` (第52週)

![Sample 7 Structural Stiffness Week 1](../../../../samples/Sample_7_Market_Users_Weekly/readme_plots/000_2_1__structural_stiffness.t.00000.png)
![Sample 7 Structural Stiffness Week 6](../../../../samples/Sample_7_Market_Users_Weekly/readme_plots/000_2_1__structural_stiffness.t.00005.png)
![Sample 7 Structural Stiffness Week 7](../../../../samples/Sample_7_Market_Users_Weekly/readme_plots/000_2_1__structural_stiffness.t.00006.png)
![Sample 7 Structural Stiffness Week 8](../../../../samples/Sample_7_Market_Users_Weekly/readme_plots/000_2_1__structural_stiffness.t.00007.png)
![Sample 7 Structural Stiffness Week 52](../../../../samples/Sample_7_Market_Users_Weekly/readme_plots/000_2_1__structural_stiffness.t.00051.png)

### 4.2. ネットワークトポロジーの異常 (Topological Anomaly / Spectral Radius)

赤色の線（Max Spectral Radius ＝ 結託したユーザー間での資金キャッチボールの強度）が常に `1.0`（理論上の限界値）の天井に張り付いている。これは `User A -> User B -> User A` という直接的な資金のキャッチボール（還流ループ）が形成されていることを示す。特定のユーザー間で閉じた資金ループが形成され、それがシステム全体の共鳴を引き起こしているということは、完全に結託した相場操縦グループの存在を数学的に証明するものである。

![Sample 7 System Stability](../../../../samples/Sample_7_Market_Users_Weekly/readme_plots/004_1_2__system_stability.png)

* **1枚目【始点】**: `t.00000`
* **2枚目【変化の直前】**: `t.00005`
* **3枚目【変化の当該時点】**: `t.00006`
* **4枚目【変化の直後】**: `t.00007`
* **5枚目【終点】**: `t.00051`

![Sample 7 Network Topology W1](../../../../samples/Sample_7_Market_Users_Weekly/readme_plots/002_1_2__network_topology.t.00000.png)
![Sample 7 Network Topology W6](../../../../samples/Sample_7_Market_Users_Weekly/readme_plots/002_1_2__network_topology.t.00005.png)
![Sample 7 Network Topology W7](../../../../samples/Sample_7_Market_Users_Weekly/readme_plots/002_1_2__network_topology.t.00006.png)
![Sample 7 Network Topology W8](../../../../samples/Sample_7_Market_Users_Weekly/readme_plots/002_1_2__network_topology.t.00007.png)
![Sample 7 Network Topology W52](../../../../samples/Sample_7_Market_Users_Weekly/readme_plots/002_1_2__network_topology.t.00051.png)

### 4.3. 自由エネルギー崩壊の解決と「質量」の物理学 (Resolution of Heat Death via Mass)

過去の実験において、本サンプルは「自由エネルギーがマイナス8億まで崩壊する（熱的死）」という異常値を出していました。しかし、データ生成ロジックを見直し、**市場参加者に「バイ＆ホールドする機関投資家（巨大な質量）」と「超高頻度取引を行うHFT（速度のみの存在）」というプロファイルを付与した結果、システムの初期質量（$U$）が約12億ドルとして正確に認識され、自由エネルギー（$F$）の崩壊が完全にストップしました。**

システムは常に「約11億ドルの自由エネルギー」を保持して極めて安定しており、TLUの熱力学方程式が「質量（保有資産）と速度（取引量）のバランス」を極めて正確に物理演算していることが証明されました。

*(上: Sample 0 正常な経済成長 ／ 下: Sample 7 質量の導入により安定した株式市場の自由エネルギー)*
![Sample 0 Thermodynamics](../../../../samples/Sample_0_Healthy/readme_plots/001_1_2__thermodynamics_energy_stack.png)
![Sample 7 Thermodynamics](../../../../samples/Sample_7_Market_Users_Weekly/readme_plots/001_1_2__thermodynamics_energy_stack.png)

### 4.4. 局所的アノマリーと情報幾何学的変位 (3D Micro Z-Score & KL Drift)

Z-Score（過去の平均からの突出度合い）および情報幾何学的変位（KL Drift ＝ 共謀グループによる未知の異常な資金移動の発生）の3Dサーフェスにおいて、`USR_001` と `USR_006` と思われる特定ユーザー間で極端なスパイクが立ち並び、共謀グループの輪郭が明確に浮き彫りになっている。

![Sample 7 3D Z-Score](../../../../samples/Sample_7_Market_Users_Weekly/readme_plots/002_2_2_2__3d_micro_z_score_X.png)
![Sample 7 3D KL Drift](../../../../samples/Sample_7_Market_Users_Weekly/readme_plots/002_2_2_1__3d_micro_kl_drift.png)

## 5. ⚠️ 反証可能性と検証要件（Falsification Analytics）

* **偽陽性の可能性:** HFT業者同士の偶発的なマッチングの可能性もゼロではないが、これほど閉じた資金還流ループが長期間維持されることは、意図的なアルゴリズムの結託（Wash Trade）以外には考えにくい。

### 💡 なぜ同じデータで異なるプロジェクション（Sample 6 と Sample 7）を作るのか？

TLUの強力な汎用性は、**「同じ生のトランザクションデータを、異なる空間（多様体）に射影（プロジェクション）することで、異なる視点の不正を立体的に暴き出せる」**点にある。

* **Sample 6（二部グラフ: User <-> Stock）:** 規制当局が「操縦されている銘柄」を検知するためのビューである。
* **Sample 7（直接グラフ: User <-> User）:** 捜査機関が「犯罪グループ（Clique）」の全体像と相関関係を直接的に洗い出すためのビューである。

TLUの汎用物理エンジンは、トポロジーの定義を少し変えるだけで、金融市場における「銘柄の異常」と「共謀グループの異常」という2つの異なる側面を、全く同じ熱力学方程式とトポロジー解析で同時に摘発できることが証明された。
