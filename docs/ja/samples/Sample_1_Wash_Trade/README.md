# 🔬 メタ解析臨床診断報告書（Sample 1: Wash Trade）

## 1. エグゼクティブ・サマリー

*   **総合診断:** **循環取引トポロジー（架空還流・売上水増し）による構造的「浮腫」**
*   **概況:** 本システム（財務ドメイン）は、売上高および利益の水増しを目的とした、Accounts Receivable（売掛金）と Cash（現金）の間での意図的な資金還流（キャッチボール）に起因する**自己強化的な循環フィードバックループ（Wash Trade）**を形成しており、極めて危険な状態（HIGH）にあります。総売上高 $1,067,391.62 のうち、病的循環によって生成された架空売上が混入しています。貸借バランスや入力の整合性は保たれているため（質量保存則は維持）、従来の静的監査では発見が困難ですが、トポロジーおよび熱力学の物理エンジンにより病的循環構造が数学的に証明されました。

---

## 2. 従来型監査・静的分析の限界

伝統的な会計監査（集計レポート）や静的分析では、借方と貸方の金額が完全に一致し、かつ帳簿上の営業利益が大幅な黒字（営業利益 $156,838.99）を計上しているため、この架空取引を即座に検知することは困難です。

*   **B/S 資産・資本の推移およびブロック構成:**
    ![Sample 1 BS Trend](../../../../samples/Sample_1_Wash_Trade/readme_plots/000_0_1__BS_Trend.png)
    ![Sample 1 BS Block](../../../../samples/Sample_1_Wash_Trade/readme_plots/000_0_1__BS_Block_Total.png)
*   **P/L 収益・費用の推移およびウォーターフォール構成:**
    ![Sample 1 PL Trend](../../../../samples/Sample_1_Wash_Trade/readme_plots/000_0_1__PL_Trend.png)
    ![Sample 1 PL Waterfall](../../../../samples/Sample_1_Wash_Trade/readme_plots/000_0_1__PL_Waterfall_Total.png)

このように、表面的な集計結果からは、売上と現金が綺麗に成長している「超優良企業」に見えます。しかし、その現金の「流れ方」が不自然に高速で閉じた循環を描いているというダイナミクスは、静的な貸借対照表のブロック図からは一切把握できません。

---

## 3. 根本病理の特定（根本的な病態生理）

本サンプルの病因は、ダミーデータ生成ロジック（`_0_0_generate_dummy_journal.py`）に埋め込まれた以下の**「粉飾取引スクリプト」**にあります。

*   **第4週〜第5週にかけての架空還流:**
    *   手元資金（Cash）を外部（ダミー会社等）に流出させる。
    *   同額の「架空の売上（Sales）」を計上し、売掛金（Accounts Receivable）を増大させる。
    *   流出させた現金を、売掛金の「回収」という名目で再び Cash 口座に還流させる。

「実態価値の創造を伴わず、帳簿上の数字のみを高速で循環させる行為」は、物理的にはシステム内の特定ルートにおける「超伝導的（摩擦ゼロの）自己循環電流」として検出されます。

---

## 4. 物理・数学エンジンによる数理証明（臨床検査証拠）

### 4.1. 質量保存の検証（キルヒホッフ残差と出血の有無）
物理的な保存則残差指標である **`System Conservation Residual`** は `0.000000`（完全なゼロ）に張り付いています。これは、還流スキームを設計した主体が、貸借一致の原則（複式簿記の質量保存）を厳密に守って仕訳を行っているためであり、単純な「計算ミスによる出血」などの形では異常が顕在化しないことを示しています。

*   **マクロ監視ダッシュボード（上: 本サンプル、下: 正常系）:**
    ![Sample 1 Macro Forensics](../../../../samples/Sample_1_Wash_Trade/readme_plots/002_2_1__macro_forensics_dashboard.png)
    ![Sample 0 Macro Forensics](../../../../samples/Sample_0_Healthy/readme_plots/002_2_1__macro_forensics_dashboard.png)

### 4.2. 主成分分析による主要な要素の検証
主成分分析では、特定の固有ベクトル成分（`ACC_Cash` と `ACC_Accounts_Receivable` のペア）への固有値エネルギーの極端な集中が確認されます。これは、多面的なビジネス取引によって駆動される正常系とは異なり、システム全体のエネルギーの大部分が「特定の2口座間のピストン往復運動」のみに消費されている数学的証拠です。
（正常系の均等な分散状態については [正常系臨床リファレンス](../Sample_0_Healthy/README.md#42-主成分分析による主要な要素の検証) を参照）

*   **PCA主要軸比率:**
    ![Sample 1 PCA Ratio](../../../../samples/Sample_1_Wash_Trade/readme_plots/000_2_2__principal_axes_ratio.png)

### 4.3. 剛性行列力学ストレス
構造剛性行列の時系列遷移（以下5定点）において、第4週（t.00004）に取引が活性化した瞬間、特定の関節に極端な過負荷がかかり、関節可動域が固定される「剛性ロック（関節硬直）」が発生しています。
（正常系の安定した結合遷移については [正常系臨床リファレンス](../Sample_0_Healthy/README.md#43-剛性行列力学ストレス) を参照）

*   **1枚目 [Start]**: `t.00000` (接続未確立・白紙状態)
*   **2枚目 [Just Before Change]**: `t.00003` (正常結合)
*   **3枚目 [The Exact Point of Change]**: `t.00004` (還流取引の開始に伴う特定の関節への超負荷)
*   **4枚目 [Immediately After Change]**: `t.00005` (剛性ロック状態の固定化)
*   **5枚目 [End]**: `t.00011` (シミュレーション終了時の固定状態継続)

*   **構造剛性の推移シーケンス:**
    ![Sample 1 Stiffness t0](../../../../samples/Sample_1_Wash_Trade/readme_plots/000_2_1__structural_stiffness.t.00000.png)
    ![Sample 1 Stiffness t3](../../../../samples/Sample_1_Wash_Trade/readme_plots/000_2_1__structural_stiffness.t.00003.png)
    ![Sample 1 Stiffness t4](../../../../samples/Sample_1_Wash_Trade/readme_plots/000_2_1__structural_stiffness.t.00004.png)
    ![Sample 1 Stiffness t5](../../../../samples/Sample_1_Wash_Trade/readme_plots/000_2_1__structural_stiffness.t.00005.png)
    ![Sample 1 Stiffness t11](../../../../samples/Sample_1_Wash_Trade/readme_plots/000_2_1__structural_stiffness.t.00011.png)

### 4.4. ネットワーク・トポロジーの可視化
トポロジーの時系列遷移において、第4週（t.00004）以降、`ACC_Cash` と `ACC_Accounts_Receivable` の間に、通常ではあり得ない太さの「赤く燃え盛るショートカット閉回路（自己還流パイプライン）」が突如出現し、熱力学的なアイドリングを引き起こしている様子が視覚的に明らかになります。
（正常系のトポロジーについては [正常系臨床リファレンス](../Sample_0_Healthy/README.md#44-ネットワーク・トポロジーの可視化) を参照）

*   **1枚目 [Start]**: `t.00000` (初期分散状態)
*   **2枚目 [Just Before Change]**: `t.00003` (平穏な接続)
*   **3枚目 [The Exact Point of Change]**: `t.00004` (極太の異常ショートカット閉回路の形成)
*   **4枚目 [Immediately After Change]**: `t.00005` (還流の自己強化)
*   **5枚目 [End]**: `t.00011` (閉回路が支配する歪んだトポロジー)

*   **トポロジーの推移シーケンス:**
    ![Sample 1 Topology t0](../../../../samples/Sample_1_Wash_Trade/readme_plots/002_1_2__network_topology.t.00000.png)
    ![Sample 1 Topology t3](../../../../samples/Sample_1_Wash_Trade/readme_plots/002_1_2__network_topology.t.00003.png)
    ![Sample 1 Topology t4](../../../../samples/Sample_1_Wash_Trade/readme_plots/002_1_2__network_topology.t.00004.png)
    ![Sample 1 Topology t5](../../../../samples/Sample_1_Wash_Trade/readme_plots/002_1_2__network_topology.t.00005.png)
    ![Sample 1 Topology t11](../../../../samples/Sample_1_Wash_Trade/readme_plots/002_1_2__network_topology.t.00011.png)

### 4.5. スペクトル半径における異常の検証
最大スペクトル半径（赤線）は、第4週（t.00004）に還流が発生した瞬間、それまでの `0.5` 付近の平穏な状態から一気に危険水域である **`0.8353`** へと跳ね上がっています。これは、システムに注入された流動性が外部へ放出されず、内部に無限に「熱として閉じ込められる」フィードバック強度の数理的臨界を示しています。
（正常系の安定したスペクトル半径については [正常系臨床リファレンス](../Sample_0_Healthy/README.md#45-スペクトル半径における異常の検証) を参照）

*   **システム安定性指標（スペクトル半径）:**
    ![Sample 1 System Stability](../../../../samples/Sample_1_Wash_Trade/readme_plots/004_1_2__system_stability.png)

### 4.6. 熱力学的エネルギースタック
熱力学分析では、第4週以降、赤いレイヤー（エントロピー損失 $T\Delta S$）が不自然に急増し、白線で示される有効な自由エネルギー（Free Energy $F$）を著しく圧迫しています。実体的な付加価値（内部エネルギー）を生み出さない取引ピストン運動が、システム内部で無駄な摩擦熱（取引コストや金利などのアイドリングロス）をまき散らし、システム全体の効率を著しく低下させている物理的証拠です。
（正常系のエネルギースタックについては [正常系臨床リファレンス](../Sample_0_Healthy/README.md#46-熱力学的エネルギースタック) を参照）

*   **熱力学的エネルギースタック:**
    ![Sample 1 Thermodynamics Energy Stack](../../../../samples/Sample_1_Wash_Trade/readme_plots/001_1_2__thermodynamics_energy_stack.png)

### 4.7. T-S軌跡
T-Sダイアグラムにおいて、本システムは「異常な時計回りの閉じたカルノー・サイクル（時計回りのエンジンループ）」を描いています。これは、外部との熱交換ではなく、内部で意図的にエネルギーを循環させて仕事を擬似的に発生させている「永久機関の偽装」を示す決定的な熱力学的署名です。
（正常系の健康的な拡散経路については [正常系臨床リファレンス](../Sample_0_Healthy/README.md#47-T-S軌跡) を参照）

*   **T-S軌跡:**
    ![Sample 1 TS Diagram](../../../../samples/Sample_1_Wash_Trade/readme_plots/001_1_3__thermodynamics_ts_diagram.png)

---

## 5. 局所治療処方箋（Optimal Treatment / LQR制御）

*   **介入方針:** **自己還流パスの動的減衰（LQR介入によるインピーダンス増大）**
*   **LQR制御による介入検証（LQR パフォーマンススペース）:**
    ![Sample 1 LQR Performance Space](../../../../samples/Sample_1_Wash_Trade/readme_plots/004_1_3__control_lqr_performance_space.png)
    
    上図の LQR Performance Space では、還流取引の抑制にかかる「制御コスト（介入に伴う取引遅延や流動性低下の痛み）」と、「システム状態（還流の流速やスペクトル半径）の収束パフォーマンス」のトレードオフが可視化されています。制御感度の最適領域を選択し、`ACC_Cash` と `ACC_Accounts_Receivable` の間の取引伝導率に対して的確な負のフィードバック（遅延注入）をかけることで、プラットフォームに過剰な取引停止コストを強いることなく、安全かつ速やかに病的ループを収束させることができます。
*   **日常の運用アドバイス:**
    同一関係会社やダミー口座間での取引インターバル時間を義務化し、同額ピストン取引が発生した場合はシステム上で自動ロックをかけるゲートウェイ（バリデータ）を設置することが極めて有効です。

---

## 6. 🚨 警告アラート・反証可能性分析

### 6.1. 偽陽性（False Positive）判定
*   **事象:** トポロジーの赤色結合とスペクトル半径 `0.8` 超えのアラートが恒常的に発報。
*   **物理的接地:** 健全な商慣行として、一時的に短期借入と売掛金回収のタイミングが重なり、見かけ上の還流構造が短期間（1日以内）発生するケースがありますが、本サンプルのように数週間にわたって同一金額が継続的に高速回転し、かつ PC1 成分が極端に突出している場合は、通常の商慣行とは認められず、偽陽性の可能性は「0%」と臨床的に断定されます。

### 6.2. 反証可能性（Falsifiability）
本サンプルの「循環取引」という診断を覆すためには、以下の客観的証拠を提示する必要があります。
1.  **物理的実需の証明:** 還流取引の対象となった物品・役務の「物理的な納品実績書（受領印付き）」および「第三者運送業者の出荷ログ」。
2.  **第三者性の証明:** 資金還流の往復先口座が、本企業グループおよび経営陣と一切の資本関係・利害関係を持たない完全な独立第三者であるという法的証明。
