# Sample 3: 単純な貸借不一致・転記ミス（Unbalanced Journal Mistake）

> [!NOTE]
> **概念実証実験にともなう免責事項**
> 本レポートで分析されるデータは実世界の企業のものではありません。検証を目的として、特定の病理学的状態を意図的に再現するために設計されたダミーデータです。本サンプル（Sample_3_Unbalanced_Mistake）は、意図的な不正ではなく、手作業の転記ミスやレガシーシステム連携時の「端数ズレ」などによる「貸借不一致（Debit != Credit）」が引き起こす物理的な質量欠損を証明するためのものです。

---

# 🔬 メタ解析 統合レポート (Meta-Analysis Synthesis Report / Laboratory Findings)

## 1. エグゼクティブ・サマリー
本システム（金融ドメイン）は、一部のトランザクションにおいて**質量保存則違反（Conservation Violation）** を発症しているものの、システム全体の剛性（サスペンション）は致命的な破壊を免れており、**警告状態（WARNING: Data Corruption）** と診断される。システム内から総額 `$4,440.45` の質量が未知のノードへと消失しているが、物理的傍証が示す通り、これは「悪意ある継続的な横領」ではなく、「単発的・偶発的なヒューマンエラー（仕訳ミス・データ腐敗）」であることが数学的に証明された。

## 2. 物理的病跡の特定（Fundamental Pathophysiology）
本サンプルの根本原因は、ダミーデータ生成ロジックにおいて意図的に仕込まれた「借方と貸方の金額の不一致（端数ズレ）」にある。
* **犯行（エラー）の手口:**
  * 取引先の経営悪化による一部未回収や決済手数料等に対し、適切な処理を怠った。
  * `E_002830` 等において、貸方(AR減少) `$1642.03` に対し、借方(現金増加) `$960.62` のように、システム間のデータ連携で不整合が発生した。
  * 結果として、差額がシステムから「消失」し、TLUのエンジンはそれを `UNKNOWN_LEAK` という特設ノードへの質量移動として処理した。

## 3. 物理・数理エンジンによる証明 (Physical and Mathematical Proof)

### 3.1. マクロフォレンジックと剛性の硬直 (Macro Forensics & Structural Stiffness)

![Sample 3 Macro Forensics](../../../../samples/Sample_3_Unbalanced_Mistake/readme_plots/002_2_1__macro_forensics_dashboard.png)

第42週を中心に、マクロ絶対残差の断続的なスパイク（最大値 `1038.49`）が観測される。しかし、Sample 2（横領）で発生した「絶対硬直（Rigid Lock）」は起きていない。

**【剛性行列と外力（サスペンションの回復）】**
![Sample 3 Structural Stiffness for Week 19](../../../../samples/Sample_3_Unbalanced_Mistake/readme_plots/000_2_1__structural_stiffness.t.00018.png)
![Sample 3 Structural Stiffness for Week 20](../../../../samples/Sample_3_Unbalanced_Mistake/readme_plots/000_2_1__structural_stiffness.t.00019.png)
![Sample 3 External Force](../../../../samples/Sample_3_Unbalanced_Mistake/readme_plots/000_1_6__3d_dynamics_external_force.png)

剛性行列は一時的に赤く波及するが、直後には元の健康なモザイク模様へと自己回復している。また、外力の異常共振も発生していない。これは、単発の入力ミスがシステム全体を破壊するほどのエネルギーを持たず、サスペンションが衝撃を吸収できている物理的証拠である。

### 3.2. ネットワークトポロジーの異常 (Topological Anomaly / Spectral Radius)

![Sample 3 System Stability](../../../../samples/Sample_3_Unbalanced_Mistake/readme_plots/004_1_2__system_stability.png)
![Sample_3_Unbalanced_Mistake Network Topology](../../../../samples/Sample_3_Unbalanced_Mistake/readme_plots/002_1_2__network_topology.t.00041.png)

Max Spectral Radius は `0.0000` のままであり、自己強化的な循環取引（Sample 1）のようなループは存在しない。システム全体のトポロジー構造は維持されている。

### 3.3. 熱力学的なエネルギー推移 (Thermodynamic Energy Stack)
システム全体の摩擦熱やエントロピー損失は限定的であり、致命的な熱的死には向かっていない。局所的な質量欠損はあるものの、総エネルギー量の推移はベースラインに近似している。

### 3.4. 局所的アノマリーと情報幾何学的変位 (3D Micro Z-Score & KL Drift)

![Sample 3 3D Z-Score](../../../../samples/Sample_3_Unbalanced_Mistake/readme_plots/002_2_2_2__3d_micro_z_score_X.png)
![Sample 3 3D KL Drift](../../../../samples/Sample_3_Unbalanced_Mistake/readme_plots/002_2_2_1__3d_micro_kl_drift.png)

Z-Scoreの3Dサーフェスにおいて、第20週に最初の「端数ズレ」が発生した瞬間、`UNKNOWN_LEAK` ノードへ鋭いスパイクが突き出ている。この「0から1への変異」は過去の標準偏差がゼロであるため従来の統計監視では透明化されやすいが、TLUのトポロジーと情報幾何学（KL Drift）は確率分布の破壊としてこれを逃さず捕捉している。

## 4. 従来型分析（集計的スナップショット）の限界 (Traditional Perspective)

**【第52週 損益計算書 (P/L) & 貸借対照表 (B/S)】**
![Sample 3 PL Waterfall](../../../../samples/Sample_3_Unbalanced_Mistake/readme_plots/000_0_1__PL_Waterfall_Total.png)
![Sample 3 BS Block](../../../../samples/Sample_3_Unbalanced_Mistake/readme_plots/000_0_1__BS_Block_Total.png)

従来の会計ソフトは、片端入力（Debit != Credit）があった場合、一時的な「仮払金」や「使途不明金」として強制的にバランスを合わせてしまう。結果として純利益は黒字（+$60,660.86）となり、静的なB/Sのバランスも一致するため、事業は正常に回っているように錯覚される。TLUの動的解析がなければ、このデータの腐敗は静かに進行し続ける。

## 5. ⚠️ 反証可能性と検証要件（Falsification Analytics）

* **偽陽性の可能性:** 今回のデータは「意図的な横領」というよりは、「取引先の不渡りや決済手数料による入金不足に対し、費用を計上せず売掛金を消し込んだ業務ミス」や「レガシーシステムから新システムへデータを移行する際の仕様バグ（端数処理の不一致）」である可能性が高い。
* **追加検証要件:**
  1. 第2章で特定された取引（`E_002786`, `E_002811`, `E_002830`）について、元の請求書控えと実際の銀行口座の着金履歴（Bank Statements）を突合し、実際の着金額が借方・貸方のどちらと一致しているかを確定させること。
  2. ERPシステムの入力フォームにおいて、「借方と貸方の金額が一致していない場合でも強制保存できてしまう」というシステム上の致命的なバリデーション欠陥がないか監査すること。
