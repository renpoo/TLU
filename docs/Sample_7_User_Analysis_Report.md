# 🩺 株式市場 ディープ・ダイブ解析レポート（ユーザー・ネットワーク視点）

**対象データ:** `Sample_7_Market_Users_Weekly`
**解析フレームワーク:** TLU メタ診断マニュアル + ユーザー観点（Traders as Nodes）

## 1. Executive Summary
市場全体のシステムは稼働していますが、特定のアクター（ユーザー）間に完全に閉じた「共謀ネットワーク（シンジケート）」が構築されています。彼らは互いの間でアルゴリズムによる超高速の資金ピンポンを行い、市場の流動性リソースを局所的に独占・浪費しています。

## 2. Core Pathology (Primary Finding)
* **Diagnosis:** HIGH: Topological Feedback Loop (Collusion / Syndicate Formation)
* **Severity:** CRITICAL
* **Physical Evidence:** Max Spectral Radius が `1.000` に到達。指定した特定ユーザー（USR_002, USR_003）を熱源とした場合、Relative Free Energy Ratio が `-13.70` までさらに劇的に悪化。
* **Financial Evidence:** ユーザー間（Seller → Buyer）のTrial Balanceにおいて、該当ユーザー間の直接的な資金のやり取り（Gross Flow）が数億ドル規模で発生している一方、彼らの最終的なNet資産の増減は無に等しい状態です。

![System Stability & Spectral Radius](./readme_plots/sample_7/system_stability.png)

![Thermodynamic Energy Depletion](./readme_plots/sample_7/thermodynamics.png)

## 3. Business Translation & Action Plan
特定ユーザーによる「馴れ合い売買（結託）」が数学的に証明されました。彼らは銘柄を隠れ蓑にしていましたが、ユーザー間の直接の資金フローを追跡したことで、彼らが互いに資金を還流させているだけの詐欺グループであることが特定されました。
**アクションプラン:** 取引所全体のシステムを止める必要はありません。ピンポイントで当該ユーザー（USR_002, USR_003）の証券口座を凍結し、コンプライアンス部門による資金洗浄（マネーロンダリング）または相場操縦の調査を開始してください。

## 4. 🔬 Multidimensional Deep-Dive Analysis
* **Kinematic State (運動学的状態):** 
  Z-Score 44.07の特異点を記録したユーザーは、非常に高い**加速度（Acceleration）**と低い粘性を持っています。これは、彼らがパンプ＆ダンプの「仕掛け人（Instigator）」として、突発的かつ暴力的な市場介入をプログラムで自動実行したことを示唆しています。
* **Structural Rigidity (構造的剛性):** 
  特定のユーザー群（サブグラフ）が、他から完全に孤立した強固なブロック構造（Rigid Block）を形成しています。これは、彼らが他の一般投資家（ノイズ）の介入を許さず、自分たちの中だけでクローズドな取引を回す「人工的な資本統制（Artificial Capital Control）」を行っている証拠です。

![Isolated Network Topology](./readme_plots/sample_7/network_topology.png)
* **Phase & Synchronization (位相と同期):** 
  独立しているはずの複数の口座間で、注文の位相ズレ（Phase Drift）が完全に `0.0` で同期しています。これは「中の人が同じ」であるか、「同一のアルゴリズム（Swarm Bot）によって全口座が中央集権的にコントロールされている」ことの物理的な証明です（Fabricated Synchronization）。
* **Systemic Vulnerability (システミックな脆弱性):** 
  感度行列（Sensitivity Matrix）は、この詐欺ネットワークの要石（Keystone）が**「中核となる特定ユーザーの口座」**であることを明確に示しています。市場の銘柄自体に介入するのではなく、このユーザー口座を「LQR制御による介入ターゲット」として凍結するだけで、一般市場に全く影響を与えずに（システミック・リスクゼロで）この不正ループのみを外科手術的に切除可能です。
