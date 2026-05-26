# 🔬 メタ診断臨床検査レポート：資金流出による質量欠損 / 不正横領 (Sample 2)

## 1. 診断結論 (Executive Summary)

* **総合診断:** **質量保存則の破綻（簿外資金流出・大出血 / Mass Conservation Violation）**
* **重症度:** 🔴 **CRITICAL (極めて深刻な内部流出)**
* **臨床概要:**
    本システムは、閉鎖系ネットワークであるべき複式簿記システムから、説明のつかない資金が持続的に外部へ漏れ出す「質量欠損（横領・簿外資金流出）」を発症しています。
    シミュレーション期間を通じて、**累計 `$1,353.48`** の質量がシステムから消失し、未知の領域へ吸い込まれました。この流出規模は全体の総活動量に対して約 0.05% と微小（Micro-Leakage）ですが、この「小さな傷口」がダブルエントリー（貸借平衡）の緊張感を損ない、最終的にシステム全体を「絶対硬直（Rigid Lock＝資金ショート）」と、後半ステップにおける「壊滅的な共振現象（ノッキング）」に陥らせることが物理数理的に証明されました。
    確率的な Z-Score は、過去に履歴のない未知の経路に対する流出を捉えられず「正常（透過）」と判定する致命的な死角（偽陰性）を有していましたが、物理エンジンが計算する **`System Conservation Residual`（保存残差）が断続的に最大 `364.53` (2020-08)** に達する不整合を示すことで、不正流出の動かぬ数理的証拠（フォレンジック）を確立しました。

---

## 2. 伝統的表層分析の限界 (Limitations of Traditional Audits)

従来の会計監査や財務諸表分析（静的集計データの監視）のみで、この巧妙な「簿外資金流出」の早期検知は不可能です。

以下は、最終期における貸借対照表（B/S）および損益計算書（P/L）の構成・推移図です。

* **B/S 資産・資本推移:**
    ![B/S Trend](../../../../samples/Sample_2_Embezzlement_Leak/readme_plots/000_0_1__BS_Trend.png)
    ![B/S Block Total](../../../../samples/Sample_2_Embezzlement_Leak/readme_plots/000_0_1__BS_Block_Total.png)
* **P/L 売上・費用推移:**
    ![P/L Trend](../../../../samples/Sample_2_Embezzlement_Leak/readme_plots/000_0_1__PL_Trend.png)
    ![P/L Waterfall Total](../../../../samples/Sample_2_Embezzlement_Leak/readme_plots/000_0_1__PL_Waterfall_Total.png)

**【静的監査の死角】**
実務において、このような原因不明の差額が発生した際、経理担当者は決算を通すために一時的に「仮払金」や「雑損失」等のダミー勘定（`UNKNOWN_LEAK`）へ差額を放り込み、B/S の左右を「総資産 `$1,320,721.40`」で強制的にバランスさせることがあります。
その結果、P/L 上は **営業黒字** としてカモフラージュされ、静的な構成比率を見ているだけでは、システムに致命的な「穴（漏洩）」が開いており、企業の血流（資金）が失われつつある事実を直感的に視覚化することはできません。

---

## 3. 根本病理の特定 (Fundamental Pathophysiology)

本サンプルに注入された不正流出の発生機序は以下の通りです。

* **不正の実行（2020-02, 03, 08, 09, 11 の各ステップ）**:
  * 売掛金（`ACC_Accounts_Receivable`）が顧客から回収されたものとして減少処理（Credit）されます。
  * しかし、その回収資金は現預金（`ACC_Cash`）へ入金されず（Debit 側が $0.0 で起票されるなど）、システム外の私的口座等へとバイパス（着服）されます。

物理エンジンはこの「消失した質量」を計算上補正し、力学的閉鎖系を維持するために、メモリ上に仮想的なゴミ箱ノード **`UNKNOWN_LEAK`** を動的に構築し、失われた質量をそこへ流し込みます。これがどのように力学的異常を引き起こすかを以下に証明します。

---

## 4. 物理・数学エンジンによる数理証明 (Mathematical Evidence)

### 4.1. 保存則の破綻とキルヒホッフ物理残差

システム全体の「質量保存の残差（System Conservation Residual / 漏洩率）」は、資金流出が発生した月（2020-02に `307.30`、2020-03に `359.73`、2020-08に最大 `364.53`、2020-09に `260.74`、2020-11に `61.18`）において鋭いスパイクを記録しています。これは、貸借不一致（片面記帳による資金消失）の決定的な物理的署名（シグネチャ）です。

* **マクロ・フォレンジック・ダッシュボード (Macro Forensics):**
    ![Macro Forensics](../../../../samples/Sample_2_Embezzlement_Leak/readme_plots/002_2_1__macro_forensics_dashboard.png)

剛性行列（Stiffness Matrix）の時系列推移を見ると、流出が開始された 2020-02 (`t_idx=1`) 以降、それまで正常な「モザイク模様」を描いていた接続の柔軟性が失われ、特定のハブが濃い赤色に染まる **Rigid Lock（絶対硬直 ＝ 資金ショートに伴う流動性停止）** を引き起こしています。
弾性を失ったシステムは通常取引のインプット（加振）を減衰できなくなり、後半ステップの 3D マップ上で **10億（1e9）スケールに達する壊滅的な共振現象（ノッキング＝システミック・ランウェイ）** を誘発します。たった 0.05% の資金漏洩が、システム全体の骨組みを揺るがし破壊する証拠です。

* **3D動的外部力共振マップ (3D Dynamics External Force):**
    ![External Force 3D](../../../../samples/Sample_2_Embezzlement_Leak/readme_plots/000_1_6__3d_dynamics_external_force.png)

* **剛性行列のシネマティック5定点シーケンス:**
  * **① Start (t=0 / 2020-01):**
        ![Stiffness t0](../../../../samples/Sample_2_Embezzlement_Leak/readme_plots/000_2_1__structural_stiffness.t.00000.png)
        初期状態。各ノードは柔軟に結合しており、健全な剛性分布を示しています。
  * **② Just Before Change (t=1 / 2020-02):**
        ![Stiffness t1](../../../../samples/Sample_2_Embezzlement_Leak/readme_plots/000_2_1__structural_stiffness.t.00001.png)
        最初の質量欠損（資金流出）が発生した瞬間。`UNKNOWN_LEAK` の出現により、剛性分布がわずかに歪み始めています。
  * **③ The Exact Point of Change (t=2 / 2020-03):**
        ![Stiffness t2](../../../../samples/Sample_2_Embezzlement_Leak/readme_plots/000_2_1__structural_stiffness.t.00002.png)
        流出が継続した時点（横領額 `359.73`）。`ACC_Cash` および `ACC_Accounts_Receivable` の周辺剛性が異常硬化（赤色の固着セル）を示し、剛性ロックが顕著化しています。
  * **④ Immediately After Change (t=3 / 2020-04):**
        ![Stiffness t3](../../../../samples/Sample_2_Embezzlement_Leak/readme_plots/000_2_1__structural_stiffness.t.00003.png)
        一旦流出が停止した直後のステップ。しかし、失われた質量（資金）によるダメージは回復せず、剛性の硬直はシステム全体に波及しています。
  * **⑤ End (t=11 / 2020-12):**
        ![Stiffness t11](../../../../samples/Sample_2_Embezzlement_Leak/readme_plots/000_2_1__structural_stiffness.t.00011.png)
        最終観測時点。未回復の質量欠損により、ネットワーク全体がしなやかさを失った「慢性硬直」状態に陥っています。

主成分分析（PCA）において、2020-03 (`t_idx=2`) の PC0 固有値は `6.6203e9` に達し、説明分散比率は **`100.0%`** となっており、PC1ベクトルは `ACC_Accounts_Receivable` (`0.6221`) と `ACC_Cash` (`-0.5138`) に支配されています。これは、流出の衝撃が主要な主成分軸を占拠し、システムに極端な偏向が生じていることを示します。

* **PCA 主要軸比率 (PCA Principal Axes Ratio):**
    ![PCA Ratio](../../../../samples/Sample_2_Embezzlement_Leak/readme_plots/000_2_2__principal_axes_ratio.png)

### 4.2. トポロジー変容と還流安定性

ネットワーク・トポロジー図上において、`ACC_Cash` (現預金) から `UNKNOWN_LEAK` (未知の漏洩先) へ向けて、簿外流出を示すエッジが形成されているのが視覚化されます。

* **システム安定性指標 (Spectral Radius):**
    ![System Stability](../../../../samples/Sample_2_Embezzlement_Leak/readme_plots/004_1_2__system_stability.png)

* **ネットワーク・トポロジー時系列の5定点シーケンス:**
  * **① Start (t=0 / 2020-01):**
        ![Topology t0](../../../../samples/Sample_2_Embezzlement_Leak/readme_plots/002_1_2__network_topology.t.00000.png)
        健全なトポロジー。`UNKNOWN_LEAK` ノードはまだ現れていません。
  * **② Just Before Change (t=1 / 2020-02):**
        ![Topology t1](../../../../samples/Sample_2_Embezzlement_Leak/readme_plots/002_1_2__network_topology.t.00001.png)
        最初の流出が発生し、トポロジー空間に `UNKNOWN_LEAK` ノードが接続され、資金が漏れ出し始めます。
  * **③ The Exact Point of Change (t=2 / 2020-03):**
        ![Topology t2](../../../../samples/Sample_2_Embezzlement_Leak/readme_plots/002_1_2__network_topology.t.00002.png)
        `UNKNOWN_LEAK` へ向かう流出ベクトルが太くなり、保存則の不一致がトポロジーの形状を破壊しています。
  * **④ Immediately After Change (t=3 / 2020-04):**
        ![Topology t3](../../../../samples/Sample_2_Embezzlement_Leak/readme_plots/002_1_2__network_topology.t.00003.png)
        流出が一時停止したフェーズ。しかし、`UNKNOWN_LEAK` はトポロジーから切り離されず、質量不足による構造的歪みが残存しています。
  * **⑤ End (t=11 / 2020-12):**
        ![Topology t11](../../../../samples/Sample_2_Embezzlement_Leak/readme_plots/002_1_2__network_topology.t.00011.png)
        最終状態。シミュレーション終了時点でも、システム境界外へのドレイン（漏洩管）が常態化しています。

### 4.3. 熱力学的散逸エネルギーと開放軌跡

資金の簿外漏洩に伴い、システムの内部エネルギー $U$（総代謝量）および自由エネルギー $F$（事業有効資源）は削り取られています。

* **熱力学エネルギースタック (Thermodynamics Energy Stack):**
    ![Thermodynamics Energy Stack](../../../../samples/Sample_2_Embezzlement_Leak/readme_plots/001_1_2__thermodynamics_energy_stack.png)
* **T-S ダイアグラム (T-S Diagram):**
    ![T-S Diagram](../../../../samples/Sample_2_Embezzlement_Leak/readme_plots/001_1_3__thermodynamics_ts_diagram.png)

1. **エネルギースタックの挙動:**
    質量欠損が発生した月（2020-02, 03, 08, 09, 11）において、自由エネルギー $F$（白い実線）の立ち上がりが健全な自然成長モデル（Sample 0）と比較して著しく低く抑え込まれています。これは、外見上いくら売上があっても、深層のエネルギー資源が外部へ流出しているため、システム維持のための「スタミナ（自己資本余力）」が実質的に痩せ細っていることを示します。
2. **T-S 軌跡（開放された散逸軌跡の証明）:**
    循環取引（Sample 1）が閉じた還流ループサイクルを描くのに対し、本サンプルの T-S ダイアグラムは **「永久に戻らない右側への開放軌跡（散逸曲線）」** を描いています。これは、エネルギーが自己還流せず、システム境界の外側へと一方的に放出され、システム全体の「生命線」が永久に失われつつあることの客観的証拠です。

### 4.4. 3D Ribbon / Surface 立体プロットによる統合アプローチ

3D立体プロットは、統計AIモデルが看過した「ゼロ・トゥ・ワン異常」の発生機序と、それがシステムに与えた局所熱力学的影響を全方位的に可視化します。

* **① 3D局所熱力学プロット:**
    ![3D Local Entropy](../../../../samples/Sample_2_Embezzlement_Leak/readme_plots/001_1_2_1__3d_local_entropy.png)
    ![3D Local Temperature](../../../../samples/Sample_2_Embezzlement_Leak/readme_plots/001_1_2_2__3d_local_temperature.png)
  * **局所エントロピー ($s_i$):** 空間的流路の分散度を示します。資金流出（横領）が発生する月において、`ACC_Accounts_Receivable` から `UNKNOWN_LEAK`（または `ACC_Cash` から `UNKNOWN_LEAK`）への異常なドレインチャネルが開通することで、`ACC_Cash` や周辺ノードの空間的フロー分散（エントロピー）に一時的な盛り上がりが検知されます。
  * **局所温度 ($T_i$):** 勘定残高の時系列ボラティリティ（標準偏差）を示します。資金が一方的に流出して消失する月（2月, 3月, 8月, 9月, 11月）において、`ACC_Cash`、`ACC_Accounts_Receivable`、および `UNKNOWN_LEAK` の残高が激しく変動するため、これらのノードの局所温度が同時に山のようにスパイク（過熱）しており、熱的な損失（摩擦）が局所的に発生していることを証明しています。

* **② 3Dミクロ情報幾何学プロット:**
    ![3D Micro KL Drift](../../../../samples/Sample_2_Embezzlement_Leak/readme_plots/002_2_2_1__3d_micro_kl_drift.png)
    ![3D Micro Z-Score](../../../../samples/Sample_2_Embezzlement_Leak/readme_plots/002_2_2_2__3d_micro_z_score_X.png)

    情報幾何学（3D Micro KL Drift）において、最初の資金流出が発生した 2020-02〜03 のタイムステップにおいて、`ACC_Cash` および `ACC_Accounts_Receivable` のノード空間上に **「天を突き刺すような巨大な尖塔（KL Drift スパイクの壁）」** が出現しています。これは、統計的な異常検知（Z-Score）が「過去に存在しないノードへの送金（ゼロ除算）」によって沈黙（正常判定）している状態であっても、確率分布の変異を逃さずに捉え、フォレンジック監査において「何年何月何日、どのノードから流出したか」を直接的に指し示す最たる証拠となります。

---

## 5. 局所治療処方箋 (LQR Control Treatment)

* **治療方針: 大出血の即時止血および流路の閉塞**
* **LQR 感度介入（ツボの特定）:**
    流動性制御理論（LQR）による感度解析（Sensitivity Matrix）において、本ネットワークでは `ACC_Accounts_Receivable` (売掛金) ノードへの介入効果（改善感度）が最大と算出されています。
    ![LQR Control](../../../../samples/Sample_2_Embezzlement_Leak/readme_plots/004_1_3__control_lqr_performance_space.png)
* **実務上の治療介入計画:**
    1. **止血（Mass Block）の導入:**
        売掛金減少（Credit）が発生したにもかかわらず、現預金（Debit Cash）の増加が伴わないような不対仕訳（片面仕訳）の入力を、会計ソフトのスキーマ定義レベルで強制的に「起票拒否・バリデーションエラー」となるように設定します。
    2. **ハブ口座の物理的凍結:**
        `UNKNOWN_LEAK` へのバイパスを構成している特定の取引ID（例：`E_000213`）を特定し、その仕訳を実行したオペレーターアカウントおよび承認プロセスの強制凍結を行います。これにより、流出の「傷口」を物理的に閉塞できます。

---

## 6. 🚨 Forensic Alert & 反証可能性 (Falsification Analytics)

### 6.1. 統計的モデルの限界とトリアージ (False Negative Assessment)

* **観測事実:** 2020-02〜03の質量欠損期において、Z-Score（流動性変化の確率統計）がしきい値 `3.0` を超えず、アラートが発生していない（偽陰性）。
* **物理的判断:**
    これは統計モデルの「ゼロ・トゥ・ワン死角」による偽陰性です。過去の取引履歴において `UNKNOWN_LEAK` との結合が定義されていなかったため、学習された共分散行列が新規接続の確率的異常を正しく評価できず、アラートをスルーしたものです。
    トリアージにおいて、確率統計モデルの正常判定を棄却し、物理指標である「キルヒホッフ保存残差の非ゼロスパイク（最大 `364.53`）」を絶対的真実として優先し、大出血病態であると診断を確定します。

### 6.2. 本診断に対する反証条件 (Falsifiability)

もし本システムが「横領・資金流出ではない」と反証するためには、以下の**「データ外の物理的原本または第三者証拠」**の提示が必要です：

1. **金融機関の通帳・API原本証明:**
    質量欠損が検知された該当仕訳の日付（2020-02, 03, 08, 09, 11）において、対象となる金額（計 `$1,353.48`）が実際に法人の正規の銀行口座に入金されていることを示す、偽造不可能な「銀行預金通帳原本（紙）」または「オンラインバンクのAPI生ログ（編集不可能な通信レコード）」。
2. **未達勘定の即時調整仕訳の提示:**
    システム間で消失したと判定された残高が、翌ステップまでに「未達資金」として他の正規ノード（関係会社等）へ実際に送金され、かつ相殺消込が完了していることを示す契約書および口座確認書。
