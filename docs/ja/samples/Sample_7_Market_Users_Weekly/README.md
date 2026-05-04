# Sample 7: 株式市場における相場操縦（直接グラフ: 共謀グループの特定 / 馴合売買の熱力学）

> [!NOTE]
> **【重要】Sample 6 と Sample 7 の関係性と対象アノマリー（相場操縦）について**
> 本サンプル（Sample 7）は、前サンプル（Sample 6）と完全に同一の株式市場のダミーデータから派生した一対の実験セットの後編です。
> * **Sample 6（前作）:** ログを「ユーザーと銘柄」の二部グラフ（Bipartite Graph）に射影したもの。**「どの銘柄が操縦（水増し）されているか」**という視点（左からの景色）を検証しました。
> * **Sample 7（本作）:** 同じログを、銘柄を捨象して「ユーザーからユーザーへの直接の資金移動」に射影したもの。**「誰と誰が結託して馴合売買を行っているのか」**という犯行グループの輪郭（右からの景色）を検証します。

---

# 🔬 メタ解析 統合レポート (Meta-Analysis Synthesis Report / Laboratory Findings)

## 1. エグゼクティブ・サマリー
本システムは、Sample 6 と同様に**「極限の位相幾何学的振動（Topological Feedback Loop）」**と**「熱力学的エネルギーの完全崩壊（Thermodynamic Energy Depletion）」**を発症している（HIGH Severity）。Sample 6 が「操縦されている銘柄」を暴き出したのに対し、この「ユーザー間直接グラフ」は、**「誰と誰が裏で結託して資金を還流させているか」**という犯行グループ（共謀シンジケート）の直接的な構造を、スペクトル半径 1.0 の極限振動として白日の下に晒している。

## 2. 物理的病跡の特定（Fundamental Pathophysiology）
本サンプルの根本原因は、特定のユーザー群による「馴合売買（Collusive Trading / Matched Orders）」の共謀である。

* **特定された証拠:**
  銘柄という仲介ノードを捨象し、資金の流れだけを追跡した結果、`USR_001` と `USR_006` の2名間で、わずか2.5秒の間に約3000ドル×9回の巨大な資金キャッチボールが直接行われている事実が特定された。これがシステム全体の熱力学を崩壊させている共謀グループ（Clique）の核である。

## 3. 物理・数理エンジンによる証明 (Physical and Mathematical Proof)

### 3.1. マクロフォレンジックと剛性の硬直 (Macro Forensics & Structural Stiffness)

Sample 6と同様に、Wash Trade は市場内で完結するため質量保存則の違反（マクロ残差）は発生しない。しかし、特定のユーザー間での異常な資金還流により、システムの剛性行列は局所的な共振と絶対硬直（Rigid Lock）を起こしている。

### 3.2. ネットワークトポロジーの異常 (Topological Anomaly / Spectral Radius)

![Sample_7_Market_Users_Weekly Network Topology](../../../../samples/Sample_7_Market_Users_Weekly/readme_plots/002_1_2__network_topology.t.00050.png)
![Sample 7 System Stability](../../../../samples/Sample_7_Market_Users_Weekly/readme_plots/004_1_2__system_stability.png)

赤色の線（Max Spectral Radius）が常に `1.0`（理論上の限界値）の天井に張り付いている。これは `User A -> User B -> User A` という直接的な資金のキャッチボール（還流ループ）が形成されていることを示す。特定のユーザー間で閉じた資金ループが形成され、それがシステム全体の共鳴を引き起こしているということは、完全に結託した相場操縦グループの存在を数学的に証明するものである。

### 3.3. 熱力学的なエネルギー推移 (Thermodynamic Energy Stack)

*(上: Sample 0 正常な経済成長 ／ 下: Sample 7 熱力学的な死)*
![Sample 0 Thermodynamics](../../../../samples/Sample_0_Healthy/readme_plots/001_1_2__thermodynamics_energy_stack.png)
![Sample 7 Thermodynamics](../../../../samples/Sample_7_Market_Users_Weekly/readme_plots/001_1_2__thermodynamics_energy_stack.png)

Sample 6 と同様の熱力学崩壊である。仮装売買（Wash Trade）は、ユーザーの「純残高（内部エネルギー）」をほとんど変化させずに「取引量（エントロピー/摩擦熱）」だけを無限大に発散させる。結果としてシステムの自由エネルギーが致命的なマイナス領域へ沈み込んでいる。

### 3.4. 局所的アノマリーと情報幾何学的変位 (3D Micro Z-Score & KL Drift)

![Sample 7 3D Z-Score](../../../../samples/Sample_7_Market_Users_Weekly/readme_plots/002_2_2_2__3d_micro_z_score_X.png)
![Sample 7 3D KL Drift](../../../../samples/Sample_7_Market_Users_Weekly/readme_plots/002_2_2_1__3d_micro_kl_drift.png)

Z-ScoreおよびKL Driftの3Dサーフェスにおいて、`USR_001` と `USR_006` と思われる特定ユーザー間で極端なスパイクが立ち並び、共謀グループの輪郭が明確に浮き彫りになっている。

## 4. 従来型分析（集計的スナップショット）の限界 (Traditional Perspective)

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

## 5. ⚠️ 反証可能性と検証要件（Falsification Analytics）

* **偽陽性の可能性:** HFT業者同士の偶発的なマッチングの可能性もゼロではないが、これほど閉じた資金還流ループが長期間維持されることは、意図的なアルゴリズムの結託（Wash Trade）以外には考えにくい。

### 💡 なぜ同じデータで異なるプロジェクション（Sample 6 と Sample 7）を作るのか？
TLUの強力な汎用性は、**「同じ生のトランザクションデータを、異なる空間（多様体）に射影（プロジェクション）することで、異なる視点の不正を立体的に暴き出せる」**点にある。
* **Sample 6（二部グラフ: User <-> Stock）:** 規制当局が「操縦されている銘柄」を検知するためのビューである。
* **Sample 7（直接グラフ: User <-> User）:** 捜査機関が「犯罪グループ（Clique）」の全体像と相関関係を直接的に洗い出すためのビューである。

TLUの汎用物理エンジンは、トポロジーの定義を少し変えるだけで、金融市場における「銘柄の異常」と「共謀グループの異常」という2つの異なる側面を、全く同じ熱力学方程式とトポロジー解析で同時に摘発できることが証明された。
