# 🔬 メタ診断臨床検査レポート：循環取引（架空売上の自己還流ループ） (Sample 1)

## 1. 診断結論 (Executive Summary)

*   **総合診断:** **位相幾何学的循環不全（Topological Feedback Loop / Wash Trade）**
*   **重症度:** 🟠 **HIGH (重篤な病態)**
*   **臨床概要:**
    本システムは、実質的な経済価値の移送を伴わない「売掛金と現預金の高速キャッチボール（還流ループ）」による深刻な機能不全（架空売上の水増し）を発症しています。
    総売上高 $1,067,391.62 のうち、かなりの割合がこの架空取引によって占められています。貸借平均の原則（保存則）は厳格に遵守されているため、従来の静的監査では発見が極めて困難ですが、物理数理エンジンが検知した隣接結合行列の最大固有値（**最大スペクトル半径 $\rho = 0.7488$**）が、システム内に自己還流するエネルギーの強固な閉回路が形成されていることを決定的に告発しています。
    無意味な往復取引によって生じる決済手数料や事務処理コストといった「摩擦熱（エントロピー損失）」により、有効余力である「自由エネルギー（Free Energy $F$）」は持続的に押し下げられており、このまま放置すれば「システム熱力学的死（資金ショート・融資限界）」へ至る危険性が極めて高いと診断されます。

---

## 2. 伝統的表層分析の限界 (Limitations of Traditional Audits)

伝統的な会計監査や財務諸表分析（静的集計データの監視）のみで、この巧妙な循環取引を見抜くことはほぼ不可能です。

以下は、シミュレーション最終ステップにおける損益計算書（P/L）および貸借対照表（B/S）の集計図です。

*   **B/S 資産・資本推移**
    ![B/S Trend](../../../../samples/Sample_1_Wash_Trade/readme_plots/000_0_1__BS_Trend.png)
    ![Sample 1 BS Block](../../../../samples/Sample_1_Wash_Trade/readme_plots/000_0_1__BS_Block_Total.png)
*   **P/L 売上・費用推移:**
    ![P/L Trend](../../../../samples/Sample_1_Wash_Trade/readme_plots/000_0_1__PL_Trend.png)
    ![Sample 1 PL Waterfall](../../../../samples/Sample_1_Wash_Trade/readme_plots/000_0_1__PL_Waterfall_Total.png)
 
**【静的監査の死角】**
循環取引の実行主体は、仕訳の記帳において「借方（Debit）と貸方（Credit）」を1円の誤差もなく完璧に一致させているため、B/S は貸借差額 $0.00 で綺麗にバランスしています。さらに、P/L 上は売上高が膨張し、結果として **+$156,838.99** という極めて健全に見える「営業黒字」が演出されています。
しかし、この見かけの利益は、裏に潜む「現金の自己還流サイクル」によって人工的に生み出されたものであり、実際のキャッシュフローを伴わない虚像です。

---

## 3. 根本病理の特定 (Fundamental Pathophysiology)

物理解析エンジンは、帳簿データの背後で実行された以下の「循環取引の偽装（架空仕訳を生成するスクリプト）」の発生機序を捉えています。

1.  **資金の不正迂回（Wash Funding）**: `CR Cash` (現預金) $\rightarrow$ `DR Accounts_Receivable` (売掛金)。ペーパーカンパニーや共謀先（DPT_Admin）へ秘密裏に資金を迂回。
2.  **架空売上の計上（Wash Sale）**: `CR Sales_Revenue` (売上高) $\rightarrow$ `DR Accounts_Receivable` (売掛金)。迂回させた資金を根拠に、架空の商取引による売上を計上。
3.  **資金の回収（Wash Collection）**: `CR Accounts_Receivable` $\rightarrow$ `DR Cash`。迂回させた資金を「売掛金の回収」という名目で元の現預金勘定に戻す。

この **現預金 ⇄ 売掛金** の往復回転（catch-balling）により、実質的な価値（内部エネルギー $U$）を何一つ生成しないまま、売上（流量 Flux）と売掛金（質量 Mass）だけを人工的に膨張させています。東洋医学的には「気血の還流（脈の暴走）」であり、脳内においててんかん発作（過同期発作）が起きている状態と数学的に同型です。

---

## 4. 物理・数学エンジンによる数理証明 (Mathematical Evidence)

### 4.1. 保存則の盲点と構造剛性 (Kirchhoff Residual & Stiffness Lock)
「質量保存の残差（System Conservation Residual）」は、グラフ上において完全に `0.0` の地平線上に張り付いています。これは、循環取引がシステムの内部ルール（ダブルエントリーの等価性）を逸脱せずに行われているため、単純な残差チェック（偽陽性の警告）をすり抜けていることを意味します。

*   **マクロ・フォレンジック・ダッシュボード (Macro Forensics):**
    ![Sample 1 Macro Forensics](../../../../samples/Sample_1_Wash_Trade/readme_plots/002_2_1__macro_forensics_dashboard.png)
*   **3D動的外部力推移 (3D Dynamics External Force):**
    ![Sample 1 External Force 3D](../../../../samples/Sample_1_Wash_Trade/readme_plots/000_1_6__3d_dynamics_external_force.png)

しかし、剛性行列（Stiffness Matrix）の時系列推移を見ると、取引が発生したタイミング（Week 0 [`t.00000`] から Week 4 [`t.00004`] にかけて）で、`ACC_Cash` と `ACC_Accounts_Receivable` の間の結合が不自然に固着（Stiffness Lock）していることが観測されます。

*   **構造剛性の時系列シーケンス:**
    *   **Previous (t=3):** ![Stiffness t3](../../../../samples/Sample_1_Wash_Trade/readme_plots/000_2_1__structural_stiffness.t.00003.png) 
    *   **Onset (t=4):** ![Stiffness t4](../../../../samples/Sample_1_Wash_Trade/readme_plots/000_2_1__structural_stiffness.t.00004.png) （Cash ⇄ Accounts_Receivable 間の循環取引）
    *   **Post (t=5):** ![Stiffness t5](../../../../samples/Sample_1_Wash_Trade/readme_plots/000_2_1__structural_stiffness.t.00005.png) 

### 4.2. 主成分分析によるエネルギー分散 (PCA Vector Components)
本サンプルでは、正常な事業活動で見られる緩やかな分散とは異なり、第1主成分（PC1）のエネルギー寄与率が異常に突出しています。これは、システムを構成する多様な勘定科目の取引ベクトルのうち、特定の「現預金 ⇄ 売掛金」ペアだけで集中的かつ同期したエネルギー消費が行われていることを数学的に示唆しています。

*   **PCA 主要軸比率 (PCA Principal Axes Ratio):**
    ![PCA Ratio](../../../../samples/Sample_1_Wash_Trade/readme_plots/000_2_2__principal_axes_ratio.png)

### 4.3. 位相幾何学的アノマリーとスペクトル半径 (Topological Anomaly)
システムのトポロジー的結合の「自己還流強度」を示す最大スペクトル半径は、平常時の `0.0` からアノマリー注入開始の 2020-01 (`t_idx=0`) において **`0.7488`** に跳ね上がり、その後 2020-02 (`t_idx=1`) にも **`0.6615`** という極めて高い危険ゾーンを維持しています。これは、システムが「自律的なエネルギー還流閉路」を形成し、完全にロックされていることの数学的証明です。

*   **システム安定性指標 (Spectral Radius):**
    ![Sample 1 System Stability](../../../../samples/Sample_1_Wash_Trade/readme_plots/004_1_2__system_stability.png)

*   **ネットワーク・トポロジー時系列:**
    *   **Previous (t=3):** ![Topology t3](../../../../samples/Sample_1_Wash_Trade/readme_plots/002_1_2__network_topology.t.00003.png)
    *   **Onset (t=4):** ![Topology t4](../../../../samples/Sample_1_Wash_Trade/readme_plots/002_1_2__network_topology.t.00004.png) （Cash ⇄ Accounts_Receivable 間の循環取引）
    *   **Post (t=5):** ![Topology t5](../../../../samples/Sample_1_Wash_Trade/readme_plots/002_1_2__network_topology.t.00005.png)

### 4.4. 熱力学的エネルギー推移と T-S 軌跡 (Thermodynamic Energy Stack & T-S Diagram)
循環取引は、帳簿上の売上高（内部エネルギー $U$）を一時的に押し上げるものの、システム内部で無駄な資金往復摩擦を発生させ、エントロピー損失を急増させます。

*   **熱力学エネルギースタック (Thermodynamics Energy Stack):**
    ![Sample 1 Thermodynamics](../../../../samples/Sample_1_Wash_Trade/readme_plots/001_1_2__thermodynamics_energy_stack.png)
*   **T-S ダイアグラム (T-S Diagram):**
    ![Sample 1 T-S Diagram](../../../../samples/Sample_1_Wash_Trade/readme_plots/001_1_3__thermodynamics_ts_diagram.png)

**【熱力学的空転とカルノーサイクル的閉回路の証明】**
1.  **エネルギースタックの挙動**:
    循環取引が発生している月（2020-01, 2020-02, 2020-05）において、エントロピー損失を示す赤色の層（$-TS$）が急激に拡張し、有効な資金余力である自由エネルギー $F$（白い境界線）を下方向へ強く押し下げています。これは、見かけの売上成長が実質的な資本蓄積に結びついておらず、往復取引にかかる手数料や事務コストという「摩擦熱」で資金が熱死していることの証明です。
2.  **T-S 軌跡（閉じた永久空転環）**:
    T-Sダイアグラム（温度-エントロピー軌跡）は極めて異常な形状を示しています。健全な組織がエントロピーを単調に発散させて外部と代謝するのに対し、本サンプルは **「T-S 平面上で反時計回りに閉じた卵型の軌跡（ループ）」** を描いています。
    これは熱力学における「サイクル（循環機関）」そのものであり、外部に一切の仕事（実質的経済価値）を提供することなく、内部でエネルギーを自律的に往復させて摩擦熱（エントロピー）のみを発生させ続ける「永久空転エンジン（Wash Trade）」が稼働していることの、これ以上ない物理学的・反証不可能な客観的証拠です。

### 4.5. 3Dミクロ情報幾何学（KL Drift）と統計的汚染（茹でガエル現象）
3DのKL Drift（情報幾何学変位）およびZ-Scoreプロットは、統計AIモデルの死角を突く「偽装の性質」を極めて鮮やかに証明しています。

*   **3D Micro Z-Score (Position):** ![Sample 1 3D Z-Score](../../../../samples/Sample_1_Wash_Trade/readme_plots/002_2_2_2__3d_micro_z_score_X.png)
*   **3D Micro KL Drift:** ![Sample 1 Micro Forensics](../../../../samples/Sample_1_Wash_Trade/readme_plots/002_2_2_1__3d_micro_kl_drift.png)

**【茹でガエル現象（Model Pollution）の証明】**
2020-01〜02の「最初の犯行」の時点では、過去データとの乖離を示す KL Drift は巨大なスパイク（警告）を突き立てています。しかし、シミュレーション後半で同様の循環取引が繰り返されると、スパイクは徐々に小さくなっています。
これは、統計的なAIが「異常な循環取引データ」を学習し、それを「新しい正常なベースライン」として取り込んでしまった（モデルが汚染された）ことを意味します。この現象は、統計モデル（Z-Scoreや単純なMLモデル）だけを用いたアプローチの限界を示しており、歴史（過去の統計）に依存しない「保存則（物理）」や「スペクトル半径（トポロジー）」による二重検証の必要性を証明しています。

---

## 5. 局所治療処方箋 (LQR Control Treatment)

*   **治療方針: 位相的デトックスと強制介入**
*   **LQR 感度介入（ツボの特定）:**
    本ネットワークにおける感度解析（Sensitivity Matrix）では、`ACC_Accounts_Receivable` (売掛金) ノードへの介入効果（改善感度）がもっとも高く検出されています。
    ![Sample 1 LQR Control](../../../../samples/Sample_1_Wash_Trade/readme_plots/004_1_3__control_lqr_performance_space.png)
*   **経営・内部統制上のアクション:**
    1.  **還流パスの遮断 (Phase Disruption)**:
        `ACC_Cash` と `ACC_Accounts_Receivable` 間の同期関係を破壊するため、入金消込処理の自動突合ルール（バッチ処理ではなく個別振込ID検証）を導入。
    2.  **LQR的制御（ハブの凍結）**:
        循環取引の受け皿となっている特定のペーパーカンパニー（顧客・仕入先）への取引をピンポイントで「強制一時停止」します。これにより、一般の営業活動（全身麻酔）を止めることなく、不正の「ツボ（発火点）」だけを切除できます。


---

## 6. 🚨 Forensic Alert & 反証可能性 (Falsification Analytics)

### 6.1. 偽陽性評価 (False Positive Assessment)
*   **異議申し立て:** 「これは短期間での正当な短期融資の実行と回収、および別の無関係な売掛金の回収が、偶然同じタイムステップで発生したに過ぎない」という反論が考えられます。
*   **棄却の論拠:**
    もし正当な商取引であれば、対応する「商品の出荷指示書（配送履歴）」や「受領書（現物取引の動脈）」が一致するはずです。物流（Mass Flow）が伴わず、資金（Money Flow）だけが同一口座間を高速往復しているため、この反論は物理的に棄却されます。

### 6.2. 本診断に対する反証条件 (Falsifiability)
もし本システムが「循環取引ではない」と反証するためには、以下の証拠 of the 提示が必要です：
1.  **物流の実在証明:** 循環している取引金額と完全に一致する、第三者物流業者（ヤマト、佐川等）の独立した「出荷伝票」および「検収書」の現物。
2.  **独立性の証明:** 現金の送金元と送金先の銀行口座の名義人が、実質的な支配関係（親子会社、親族関係等）を有していないことを示す登記簿および株主構成。
