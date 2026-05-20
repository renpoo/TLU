# 🔬 メタ解析臨床診断報告書（Sample 2: Embezzlement Leak）

## 1. エグゼクティブ・サマリー

*   **総合診断:** **簿外資産流出（役員横領）による致命的な「大出血」および統計的盲点**
*   **概況:** 本システム（財務ドメイン）は、手元資金（Cash）から帳簿に記載されない未知の外部ノード（`UNKNOWN_LEAK`）へと資金が一方通行で抜き取られる**「簿外資産横領（大出血）」**を引き起こしており、極めて致命的な状態（CRITICAL）にあります。総資産が本来あるべき状態から大幅に欠損しており、物理的な質量保存則（キルヒホッフの第一法則）が完全に破綻しています。特筆すべきは、横領犯が一定額を規則的かつ機械的に抜き取ったため、その変動分散（分散・共分散行列）が「ゼロ」となり、統計的 AI が依存する共分散ベースの Z-Score（警告）を完全にすり抜けている（コールドスポット化）点です。物理エンジンによる質量保存の検証のみがこの病態を暴き出しました。

---

## 2. 従来型監査・静的分析の限界

伝統的な会計監査（集計レポート）や静的分析では、意図的な片端仕訳（簿外操作）によって現預金が抜き取られているため、B/S の借方と貸方は表面上「帳尻が合っている」ように見せかけられています。

*   **B/S 資産・資本の推移およびブロック構成:**
    ![Sample 2 BS Trend](../../../../samples/Sample_2_Embezzlement_Leak/readme_plots/000_0_1__BS_Trend.png)
    ![Sample 2 BS Block](../../../../samples/Sample_2_Embezzlement_Leak/readme_plots/000_0_1__BS_Block_Total.png)
*   **P/L 収益・費用の推移およびウォーターフォール構成:**
    ![Sample 2 PL Trend](../../../../samples/Sample_2_Embezzlement_Leak/readme_plots/000_0_1__PL_Trend.png)
    ![Sample 2 PL Waterfall](../../../../samples/Sample_2_Embezzlement_Leak/readme_plots/000_0_1__PL_Waterfall_Total.png)

このように、ウォーターフォール図上では正常な費用支出に見えますが、B/S上では資産の積み上がりが正常系に比べて不自然に低迷しています。しかし、「意図的に抜き取られた金額」そのものは簿外で処理されているため、静的な試算表やトレンドの傾きだけで「横領である」と物理的に断定することは困難です。

---

## 3. 根本病理の特定（根本的な病態生理）

本サンプルの病的因果は、ダミーデータ生成ロジック（`_0_0_generate_dummy_journal.py`）内の横領犯による以下の**「簿外不正出金ロジック」**にあります。

*   **第4週（t.00004）以降の一方通行流出:**
    *   Cash 口座から、毎週決まった定額の資金を抜き取る。
    *   この出金に対する相手勘定（貸方）を正規の帳簿に記録せず、システム外の隠しノード（`UNKNOWN_LEAK`）へ一方通行で流出（リーク）させる。

この行為は、物理的には「閉じた流体回路上に突如として開いた亀裂（ドレイン）からの資源の漏出」として記述されます。

---

## 4. 物理・数学エンジンによる数理証明（臨床検査証拠）

### 4.1. 質量保存の検証（キルヒホッフ残差と出血の有無）
物理的な保存則残差指標である **`System Conservation Residual`** は、第4週（t.00004）の横領開始の瞬間に `0.0` の水平線から一気に跳ね上がり、深刻な質量漏出（内出血）が発生していることを証明しています。
また、マクロ Z-Score（下段の青線）が横領開始直後にもかかわらず **`0.0` 付近に張り付いて無反応（警告が出ない）** である様子がはっきりと確認されます。これは、定額横領により「変動のばらつき」が生まれず、共分散行列がこの異常を「変化なし（分散ゼロ）」として学習（盲点化）してしまったためです。

*   **マクロ監視ダッシュボード（上: 本サンプル、下: 正常系）:**
    ![Sample 2 Macro Forensics](../../../../samples/Sample_2_Embezzlement_Leak/readme_plots/002_2_1__macro_forensics_dashboard.png)
    ![Sample 0 Macro Forensics](../../../../samples/Sample_0_Healthy/readme_plots/002_2_1__macro_forensics_dashboard.png)

### 4.2. 主成分分析による主要な要素の検証
PCA分析では、失われた資源の方向性（`UNKNOWN_LEAK` へのベクトル）が第一主成分に強く射影されます。統計的には盲点化されていても、固有値空間においては「エネルギーが外部へ吸い出されている次元」が明確に独立した固有軸として分離されます。
（正常系の均等な分散状態については [正常系臨床リファレンス](../Sample_0_Healthy/README.md#42-主成分分析による主要な要素の検証) を参照）

*   **PCA主要軸比率:**
    ![Sample 2 PCA Ratio](../../../../samples/Sample_2_Embezzlement_Leak/readme_plots/000_2_2__principal_axes_ratio.png)

### 4.3. 剛性行列力学ストレス
剛性行列の5定点観測において、横領が開始された第4週（t.00004）以降、`ACC_Cash` の接続剛性が著しく弱体化（骨折・剛性支持の喪失）し、システム全体の支柱が歪んでいく様子が証明されます。
（正常系の安定した結合遷移については [正常系臨床リファレンス](../Sample_0_Healthy/README.md#43-剛性行列力学ストレス) を参照）

*   **1枚目 [Start]**: `t.00000` (接続未確立・白紙状態)
*   **2枚目 [Just Before Change]**: `t.00003` (正常結合)
*   **3枚目 [The Exact Point of Change]**: `t.00004` (流出開始に伴う Cash 剛性リンクの亀裂発生)
*   **4枚目 [Immediately After Change]**: `t.00005` (Cash 部の剛性低下の進行)
*   **5枚目 [End]**: `t.00011` (支柱の強度が失われたまま崩壊状態で終了)

*   **構造剛性の推移シーケンス:**
    ![Sample 2 Stiffness t0](../../../../samples/Sample_2_Embezzlement_Leak/readme_plots/000_2_1__structural_stiffness.t.00000.png)
    ![Sample 2 Stiffness t3](../../../../samples/Sample_2_Embezzlement_Leak/readme_plots/000_2_1__structural_stiffness.t.00003.png)
    ![Sample 2 Stiffness t4](../../../../samples/Sample_2_Embezzlement_Leak/readme_plots/000_2_1__structural_stiffness.t.00004.png)
    ![Sample 2 Stiffness t5](../../../../samples/Sample_2_Embezzlement_Leak/readme_plots/000_2_1__structural_stiffness.t.00005.png)
    ![Sample 2 Stiffness t11](../../../../samples/Sample_2_Embezzlement_Leak/readme_plots/000_2_1__structural_stiffness.t.00011.png)

### 4.4. ネットワーク・トポロジーの可視化
トポロジー遷移において、第4週（t.00004）以降、`ACC_Cash` から境界外の暗黒領域（`UNKNOWN_LEAK`）へ向かって、太い「一方通行の流出リンク（ドレイン）」が突き刺さり、システム全体の資源を絶え間なく体外へ排出している致命的な構造が可視化されます。
（正常系のトポロジーについては [正常系臨床リファレンス](../Sample_0_Healthy/README.md#44-ネットワーク・トポロジーの可視化) を参照）

*   **1枚目 [Start]**: `t.00000` (初期状態)
*   **2枚目 [Just Before Change]**: `t.00003` (正常な分散)
*   **3枚目 [The Exact Point of Change]**: `t.00004` (簿外流出ドレインの出現)
*   **4枚目 [Immediately After Change]**: `t.00005` (流出ルートの太線化)
*   **5枚目 [End]**: `t.00011` (資産が枯渇しトポロジーが萎縮した状態)

*   **トポロジーの推移シーケンス:**
    ![Sample 2 Topology t0](../../../../samples/Sample_2_Embezzlement_Leak/readme_plots/002_1_2__network_topology.t.00000.png)
    ![Sample 2 Topology t3](../../../../samples/Sample_2_Embezzlement_Leak/readme_plots/002_1_2__network_topology.t.00003.png)
    ![Sample 2 Topology t4](../../../../samples/Sample_2_Embezzlement_Leak/readme_plots/002_1_2__network_topology.t.00004.png)
    ![Sample 2 Topology t5](../../../../samples/Sample_2_Embezzlement_Leak/readme_plots/002_1_2__network_topology.t.00005.png)
    ![Sample 2 Topology t11](../../../../samples/Sample_2_Embezzlement_Leak/readme_plots/002_1_2__network_topology.t.00011.png)

### 4.5. スペクトル半径における異常の検証
最大スペクトル半径は、還流取引（ループ）が存在しないため危険な上昇（`0.8` 超）は見せません。しかし、自由エネルギーが吸い出されているため、システム全体の固有ダイナミクスが「減衰・枯渇」に向かう特徴を示しています。
（正常系の安定した脈動については [正常系臨床リファレンス](../Sample_0_Healthy/README.md#45-スペクトル半径における異常の検証) を参照）

*   **システム安定性指標（スペクトル半径）:**
    ![Sample 2 System Stability](../../../../samples/Sample_2_Embezzlement_Leak/readme_plots/004_1_2__system_stability.png)

### 4.6. 熱力学的エネルギースタック
熱力学分析では、横領が継続するにつれて自由エネルギー（F）が急勾配で減少し、システムが空洞化していく様子が示されています。これは、熱散逸（エントロピー上昇）ではなく、システムの「内部エネルギー（質量）そのものの喪失（脱水症状）」を意味しています。
（正常系の安定したエネルギー保存については [正常系臨床リファレンス](../Sample_0_Healthy/README.md#46-熱力学的エネルギースタック) を参照）

*   **熱力学的エネルギースタック:**
    ![Sample 2 Thermodynamics Energy Stack](../../../../samples/Sample_2_Embezzlement_Leak/readme_plots/001_1_2__thermodynamics_energy_stack.png)

### 4.7. T-S軌跡
T-Sダイアグラムにおいて、本システムは元の状態に戻らない「不可逆的な開放曲線（体外への拡散軌跡）」を描き、エントロピー平面上で右下に脱落しています。これは、閉じた循環サイクルに戻ることのできない「持続的な血液損失（横領）」を示す決定的な物理署名です。
（正常系の平穏なサイクルについては [正常系臨床リファレンス](../Sample_0_Healthy/README.md#47-T-S軌跡) を参照）

*   **T-S軌跡:**
    ![Sample 2 TS Diagram](../../../../samples/Sample_2_Embezzlement_Leak/readme_plots/001_1_3__thermodynamics_ts_diagram.png)

---

## 5. 局所治療処方箋（Optimal Treatment / LQR制御）

*   **介入方針:** **流出ゲートの緊急閉鎖（キルヒホッフ残差に基づく自動サーキットブレーカー発動）**
*   **LQR制御による介入検証（LQR パフォーマンススペース）:**
    ![Sample 2 LQR Performance Space](../../../../samples/Sample_2_Embezzlement_Leak/output_plots/support/004_1_3__control_lqr_performance_space.png)
    
    上図の LQR Performance Space では、流出経路に対する制御ゲインをどれだけ積極的に高めるか（介入パラメータ設定）と、その際のシステム復旧コストの相関関係を示しています。本病態は統計的 Z-Score に反応しない特徴があるため、物理エンジン側の `System Conservation Residual > 0` をトリガーとし、LQR フィードバック設計から導出された最適なしきい値を適用します。これにより、正常な営業活動取引に干渉しすぎることなく、Cash 口座から `UNKNOWN_LEAK` への不正流出取引のみに的確に高い抵抗値（インピーダンス）を印加し、自動サーキットブレーカーを発動させて不正出金を即座に抑止することが可能となります。
*   **日常の運用アドバイス:**
    相手勘定が存在しない、あるいは承認されていない外部口座へのダイレクトな資金移動を検知するため、すべてのトランザクションに対して「Debit = Credit」がリアルタイムで一致しているかを監視する物理検証ルールの導入が不可欠です。

---

## 6. 🚨 警告アラート・反証可能性分析

### 6.1. 偽陽性（False Positive）判定
*   **事象:** 統計的 AI（Z-Score）は「正常（青信号）」を維持しているが、物理キルヒホッフ残差は「重大異常（赤信号）」を指し示す乖離。
*   **物理的接地:** 統計的モデルがコールドスタート期に無反応になることはありますが、物理的な保存則残差が定常的にプラスになる（資金が物理的に消滅する）現象は、自然界および簿記の数理上、絶対にあり得ません。よって、この乖離は統計モデルの「偽陰性（見落とし）」であり、物理キルヒホッフ残差による横領検知が「100%正しい」と臨床的に認定されます。

### 6.2. 反証可能性（Falsifiability）
本サンプルの「横領」という診断を否定するためには、以下のいずれかを提示する必要があります。
1.  **簿外勘定の正当性の証明:** 横領と判断された流出先口座が、実は「登記手続き中の関係会社仮払金」であり、かつその帳簿記載漏れ（仕訳未入力エラー）であったことを示す法的書類。
2.  **物理的インフラエラーの証明:** データベースサーバーのトランザクションログのバグにより、貸方レコードのみが一時的に消失したというインフラ障害の技術報告書。
