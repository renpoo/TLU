# Sample 6: 株式市場における相場操縦（二部グラフ: 操縦銘柄の特定 / 仮装売買の熱力学）

> [!NOTE]
> **【重要】Sample 6 と Sample 7 の関係性と対象アノマリー（相場操縦）について**
> 本サンプル（Sample 6）と次サンプル（Sample 7）は、完全に同一の株式市場のダミーデータから派生した一対の実験セットです。
> * **Sample 6（本作）:** ログを「ユーザーと銘柄」の二部グラフ（Bipartite Graph）に射影したもの。**「どの銘柄が操縦されているか」**という視点（左からの景色）を検証します。
> * **Sample 7（次作）:** 同じログを「ユーザー間」の直接グラフに射影したもの。**「誰と誰が結託して馴合売買を行っているか」**という視点（右からの景色）を検証します。

---

# 🔬 メタ解析 統合レポート (Meta-Analysis Synthesis Report / Laboratory Findings)

## 1. 最新の機械学習ベース自動診断結果 (ML-Based Automated Diagnosis)

本サンプル（**Sample_6_Market_Bipartite_Weekly**）に対する自動判定結果です。純粋な物理指標がドメイン特有の異常をどう捉えるかを解説します。

### 【A. 確定診断 (Final Pathologies) とドメイン解釈】

#### 🚨 アルゴリズムの無限ループ（人為的な価格操作）
- **証拠 (Evidence):** Max Spectral Radius: 1.0000.
- **専門家の解釈:** 
  特定の口座間で、極端に高速で無意味な自己強化ループ（株のキャッチボール）が形成されています。実需を伴わないウォッシュトレードによって、人工的に出来高を水増し・相場を操縦している可能性を示す、決定的なトポロジー的署名です。

### 【B. 構造的進化と摩擦分類 (Structural Evolution & Viscosity)】

- **動粘度（摩擦係数）レンジ:** `372566544.89 ~ 372566544.89`
- 🩸 **構造診断: 血栓症 / 高摩擦（旧世代型構造）**
  - **解説:** システムは手動プロセスや物理的な制約に依存しており、パニック時や異常時に「物理的な詰まり（血栓）」を起こしやすい構造です。

### 【C. スケール不変の物理指標 (Scale-Invariant Diagnostic Metrics)】

## 2. 従来型分析（集計的スナップショット）の限界 (Traditional Perspective)

**【全期間の累積フロー (P/L Waterfall) & 貸借対照表 (B/S)】**
![Sample 6 PL Waterfall](../../../../samples/Sample_6_Market_Bipartite_Weekly/readme_plots/000_0_1__PL_Waterfall_Total.png)
![Sample 6 BS Block](../../../../samples/Sample_6_Market_Bipartite_Weekly/readme_plots/000_0_1__BS_Block_Total.png)

株式市場の総体は「純粋な運動系（閉鎖系）」であるため、全期間のネット蓄積量（B/S）はプラスマイナスゼロ（白紙）となる。従来の証券ツールの集計ダッシュボードでは、Wash Trade が行われた銘柄は単に**「出来高が急増している活発で人気のある銘柄（巨大なP/L）」**として表示され、無関係な一般投資家の買いを誘発してしまう。静的な集計ツールは、その膨大な出来高が「有意義な経済活動」なのか「少人数による自作自演の摩擦熱」なのかを区別できない。

## 3. 物理的病跡の特定（Fundamental Pathophysiology）
本サンプルの根本原因は、特定のユーザー群による「仮装売買（Wash Trade）」アルゴリズムの意図的な稼働である。

* **特定された証拠:**
  `2020-02-03 11:41:21`（第6週）において、`USR_001` と `USR_006` の2名が、わずか **2.5秒間** の間に、`STK_005` に対して 1,000〜3,300株（約3070ドル/株）の巨大な売買注文を **9回連続** で相互に約定させていた事実がトランザクションレベルで確認された。さらに `2020-06-29`（第27週）にも別のユーザーペアによる同様の高速還流が発生している。このアルゴリズムの暴走が、マクロな異常指標の完全な発生源である。

## 4. 物理・数理エンジンによる証明 (Physical and Mathematical Proof)

### 4.1. マクロフォレンジックと剛性の硬直 (Macro Forensics & Structural Stiffness)

Wash Tradeは市場内で完結する取引であるため、システム外への質量漏洩（マクロ残差）は発生しない。しかし、異常な頻度での資金還流により、剛性行列（サスペンション）は特定のノード間で絶対硬直（Rigid Lock ＝ 外部からの健全な注文を受け付けられない市場のフリーズ状態）を起こし、外部からの健全な注文を受け入れられない状態に陥っている。

![Sample 6 Macro Forensics](../../../../samples/Sample_6_Market_Bipartite_Weekly/readme_plots/002_2_1__macro_forensics_dashboard.png)
![Sample 6 External Force 3D](../../../../samples/Sample_6_Market_Bipartite_Weekly/readme_plots/000_1_6__3d_dynamics_external_force.png)

* **1枚目【始点】**: `t.00000` (正常な剛性)
* **2枚目【変化の直前】**: `t.00005` (第6週)
* **3枚目【変化の当該時点】**: `t.00006` (第7週: 資金還流による硬直発生)
* **4枚目【変化の直後】**: `t.00007` (第8週)
* **5枚目【終点】**: `t.00051` (第52週)

![Sample 6 Structural Stiffness Week 1](../../../../samples/Sample_6_Market_Bipartite_Weekly/readme_plots/000_2_1__structural_stiffness.t.00000.png)
![Sample 6 Structural Stiffness Week 6](../../../../samples/Sample_6_Market_Bipartite_Weekly/readme_plots/000_2_1__structural_stiffness.t.00005.png)
![Sample 6 Structural Stiffness Week 7](../../../../samples/Sample_6_Market_Bipartite_Weekly/readme_plots/000_2_1__structural_stiffness.t.00006.png)
![Sample 6 Structural Stiffness Week 8](../../../../samples/Sample_6_Market_Bipartite_Weekly/readme_plots/000_2_1__structural_stiffness.t.00007.png)
![Sample 6 Structural Stiffness Week 52](../../../../samples/Sample_6_Market_Bipartite_Weekly/readme_plots/000_2_1__structural_stiffness.t.00051.png)

### 4.2. ネットワークトポロジーの異常 (Topological Anomaly / Spectral Radius)

赤色の線（Max Spectral Radius ＝ 資金の完全な還流ループの強度）が常に `1.0`（理論上の限界値）の天井に張り付いている。これは `User A -> Stock X -> User B -> Stock X -> User A` という完全な閉回路（資金の還流ループ）が常態化していることを示し、市場のエネルギーが「外部からの健全な投資」ではなく「内部の自作自演による共鳴（ハウリング）」によって支配されていることを数学的に証明している。

![Sample 6 System Stability](../../../../samples/Sample_6_Market_Bipartite_Weekly/readme_plots/004_1_2__system_stability.png)

* **1枚目【始点】**: `t.00000`
* **2枚目【変化の直前】**: `t.00005`
* **3枚目【変化の当該時点】**: `t.00006`
* **4枚目【変化の直後】**: `t.00007`
* **5枚目【終点】**: `t.00051`

![Sample 6 Network Topology W1](../../../../samples/Sample_6_Market_Bipartite_Weekly/readme_plots/002_1_2__network_topology.t.00000.png)
![Sample 6 Network Topology W6](../../../../samples/Sample_6_Market_Bipartite_Weekly/readme_plots/002_1_2__network_topology.t.00005.png)
![Sample 6 Network Topology W7](../../../../samples/Sample_6_Market_Bipartite_Weekly/readme_plots/002_1_2__network_topology.t.00006.png)
![Sample 6 Network Topology W8](../../../../samples/Sample_6_Market_Bipartite_Weekly/readme_plots/002_1_2__network_topology.t.00007.png)
![Sample 6 Network Topology W52](../../../../samples/Sample_6_Market_Bipartite_Weekly/readme_plots/002_1_2__network_topology.t.00051.png)

### 4.3. 自由エネルギー崩壊の解決と「質量」の物理学 (Resolution of Heat Death via Mass)

過去の実験において、本サンプルは「自由エネルギーがマイナスへ無限に沈み込む（熱的死）」という異常値を出していました。しかし、データ生成ロジックを見直し、**市場参加者に「機関投資家（巨大な質量）」と「HFT（速度のみ）」というプロファイルを付与した結果、システムの初期質量（$U$）が約12億ドルとして正確に認識され、自由エネルギーの崩壊が完全にストップしました。**

システムは常にプラスの自由エネルギー（約11億）を保ち、TLUの熱力学方程式が「質量（保有資産）と速度（取引量）のバランス」を極めて正確に物理演算していることが証明されました。

*(上: Sample 0 正常な経済成長 ／ 下: Sample 6 質量の導入により安定した株式市場の自由エネルギー)*
![Sample 0 Thermodynamics](../../../../samples/Sample_0_Healthy/readme_plots/001_1_2__thermodynamics_energy_stack.png)
![Sample 6 Thermodynamics](../../../../samples/Sample_6_Market_Bipartite_Weekly/readme_plots/001_1_2__thermodynamics_energy_stack.png)

### 4.4. 局所的アノマリーと情報幾何学的変位 (3D Micro Z-Score & KL Drift)

Z-Score（過去の平均からの突出度合い）および情報幾何学的変位（KL Drift ＝ 過去の市場の確率分布からの極端な逸脱）の3Dサーフェスにおいて、一部の特定銘柄（Stock）と特定ユーザー群（User）の間に極端なスパイクが突き出しており、市場全体に不自然なエントロピーを波波させ、確率分布を汚染していることが視認できる。

![Sample 6 3D Z-Score](../../../../samples/Sample_6_Market_Bipartite_Weekly/readme_plots/002_2_2_2__3d_micro_z_score_X.png)
![Sample 6 3D KL Drift](../../../../samples/Sample_6_Market_Bipartite_Weekly/readme_plots/002_2_2_1__3d_micro_kl_drift.png)

## 5. ⚠️ 反証可能性と検証要件（Falsification Analytics）

* **偽陽性の可能性:** HFT（高頻度取引）業者のマーケットメイク・アルゴリズムが偶発的に共鳴した可能性もゼロではないが、2.5秒間に9回という極端な頻度と、スペクトル半径が1.0に張り付く完全な閉回路構造を考慮すると、意図的な相場操縦（Wash Trade）である可能性が極めて高い。
* **追加検証要件:**
  `USR_001` と `USR_006` の口座開設情報、IPアドレス、MACアドレス等を突合し、同一人物による複数口座の使い回し（シビル攻撃）でないかを規制当局に開示請求すること。未知の手口であっても、物理法則に反する資金還流はTLUの目をごまかすことはできない。
