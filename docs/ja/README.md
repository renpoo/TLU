# Tensor-Link Utility (TLU)

## 🔬 結論：見えない「不正・劣化・崩壊」を物理法則で暴き出す

TLUの最大の結論は、**「表面上の帳尻合わせ（B/SやP/Lの粉飾）がいかに完璧であっても、『質量保存の法則』や『熱力学第二法則』といった普遍的な物理法則を欺くことは絶対に不可能である」**という証明です。

TLUは、金融取引、交通網、生体ネットワークなどのあらゆる複雑なデータ群を「流体」や「エネルギーの波」として再定義し、目に見えない不正（横領、循環取引）やシステム劣化（大渋滞、梗塞）を、客観的な**「物理的シグネチャ（剛性の崩壊、異常共振）」**として視覚化するメタ診断プラットフォームです。
出力された数学的証拠は、LLM（AI）によって解読され、専門家向けの実務的な「診断レポート」へと自動翻訳されます。

---

## 従来の限界と「物理数学」のアプローチ

なぜ、既存の監査ツールやダッシュボードでは不十分なのでしょうか？

### 従来の集計的アプローチの限界

従来のシステムは「借方と貸方が一致しているか」「売上が目標に達しているか」という「静的な結果」しか見ません。そのため、複数人が結託して帳尻を合わせた「循環取引（Wash Trade）」や、長年かけて少しずつ会社を蝕む「摩擦熱（過剰な非効率）」を見抜くことは数学的に困難です。

### 物理数学によるドメイン横断的解決

TLUは、データを単なる数字の足し算ではなく、以下の「物理的特性」を持った動的ネットワークとして計算します。

* **質量 / 慣性 (Inertia):** 資金やリソースの滞留規模。質量が突然消滅すれば「横領や梗塞」を意味します。
* **剛性 (Stiffness):** 取引関係の確実性（バネの強さ）。これが失われればシステムは「絶対硬直」に陥ります。
* **粘性 (Viscosity):** 資金回収や業務プロセスの遅延（摩擦熱）。

![Mass-Spring-Damper Model](../readme_plots/Mass-Spring-Damper-Model.jpg)

TLUは、ニュートン力学、熱力学、情報幾何学、制御工学を横断的に適用し、これらを見えない「異常検知センサー」として活用します。

---

## 証拠となる4つのコア・シグネチャ

AIメタ診断エンジンが実査（フォレンジック）の根拠とする、代表的な4つの物理的・数学的視覚証明です。

### 1. マクロフォレンジック（質量の保存と崩壊）

システム全体から「不自然に消滅・発生した資金（Residual）」がないかを監視します。帳簿外への資金流出が発生した場合、質量保存の法則が破綻し、強烈なスパイクとして検知されます。

【正常系の一例：サンプル 0 より】
![Macro Forensics: Normal](samples/Sample_0_Healthy/readme_plots/002_2_1__macro_forensics_dashboard.png)
【異常系の一例：サンプル 2 より】
![Macro Forensics: Abnormal](samples/Sample_2_Embezzlement_Leak/readme_plots/002_2_1__macro_forensics_dashboard.png)

### 2. 制御工学とシステム安定性（死の螺旋の検知）

**Spectral Radius（スペクトル半径）:** 取引ネットワーク内に「閉じたループ（循環取引）」が形成されていないかを監視します。赤色の軌跡線が1.0のオレンジ色の閾値線に近づく、あるいは突き抜けた場合、システムが人為的なループによって暴走（制御不能）していることを数学的に証明します。

【正常系の一例：サンプル 0 より】
![System Stability: Normal](samples/Sample_0_Healthy/readme_plots/004_1_2__system_stability.png)
【異常系の一例：サンプル 4 より】
![System Stability: Abnormal](samples/Sample_4_Composite_Chaos/readme_plots/004_1_2__system_stability.png)

### 3. 熱力学エネルギー・スタック（組織の疲弊と熱的死）

**自由エネルギー（Free Energy）:** 組織が健全に活動するための「余力」を示します。白色の線がゼロ以下のマイナス圏へ沈み込んでいる場合、システムが活動すればするほど無駄な摩擦熱（エントロピー）を生み出す「熱力学的な死」に向かっていることを証明します。

【正常系の一例：サンプル 0 より】
![Thermodynamics Energy Stack: Normal](samples/Sample_0_Healthy/readme_plots/001_1_2__thermodynamics_energy_stack.png)
【異常系の一例：サンプル 6 より】
![Thermodynamics Energy Stack: Abnormal](samples/Sample_6_Market_Bipartite_Weekly/readme_plots/001_1_2__thermodynamics_energy_stack.png)

### 4. 3D マイクロ・フォレンジック（発生座標のピンポイント特定）

**Z-Score & KL Drift 3D Surface:** 空間の幾何学的な歪みを計算し、**「何月何日の、どの特定の口座（ノード）」**で異常な操作が行われたのかを、鋭い黄緑色（Yellow-Green）のスパイクとしてピンポイントで刺し貫きます。

【正常系の一例：サンプル 0 より】
![Micro Z-Score 3D Surface: Normal](samples/Sample_0_Healthy/readme_plots/002_2_2_2__3d_micro_z_score_X.png)
【異常系の一例：サンプル 5 より】
![Micro Z-Score 3D Surface: Abnormal](samples/Sample_5_Kyoto_Traffic/readme_plots/002_2_2_2__3d_micro_z_score_X.png)

---

## 📚 TLU 公式ドキュメント（Hub & Spoke）

TLUは、その数学的客観性と反証可能性を担保するため、厳格な階層構造を持ったドキュメント体系を備えています。監査人やエンジニアは、以下のディレクトリを参照してください。

* **[📂 AI メタ診断マニュアル (`LLM_Diagnostic_Manual.md`)](LLM_Diagnostic_Manual.md)**
  * AIがTLUの物理データをどのように読み解き、プロの監査レポートへと翻訳するかのプロトコル。
* **[📂 10のサンプル事例比較 (`samples/`)](samples/README.md)**
  * 正常なベースラインと、横領・循環取引・てんかん発作などの「病跡（異常）」を比較検証した実証レポート群。
* **[📂 グラフ解釈ガイド (`interpretations/`)](interpretations/README.md)**
  * 専門家が生成されたグラフを視覚的にどう読み解き、どう実務に適用するかの公式マニュアル。
* **[📂 物理・数学エンジン理論 (`physics/`)](physics/README.md)**
  * 運動学や熱力学が、なぜ・どのようにして異常を検知するのかを定義した数理的マニフェスト。
* **[📂 システム・アーキテクチャ (`architecture/`)](architecture/README.md)**
  * 再現性（誰がやっても同じ結果になること）を100%保証するためのパイプライン・コンテナ運用思想。

---

## 🚀 実行環境とクイックスタート（TDDによる証明）

TLUは「フェイルファスト（データ異常時の即時停止）」と「ステートレスなコンテナ環境」によって、ローカル環境への依存性や人間のバイアスを完全に排除しています。

```bash
# 1. リポジトリのクローン
git clone https://github.com/renpoo/TLU.git
cd TLU

# 2. Docker環境の起動
docker compose up -d

# 3. パイプラインの全自動実行（Sample 1: 循環取引 のシミュレーション）
# ※ "samples/Sample_0_Healthy" に変更すると正常系のベースラインを確認できます
bash bin/batch_processing.sh --target_env "samples/Sample_1_Wash_Trade"
bash bin/batch_visualize_graphs.sh --target_env "samples/Sample_1_Wash_Trade"

# 4. AIメタ診断レポート（JSON/Markdown）の確認
cat workspace/output_data/_99_diagnosis_report.md
```

---

## ⚠️ 監査実務への適用（反証可能性とモデルの限界）

TLUは「システム内に質量欠損がある」「スペクトル半径が1.0に張り付いている」という**普遍的な物理数学的事実**を断定する最強の「証拠提示マシン（計算機）」です。

しかし、その異常が「意図的な犯罪（横領・粉飾）」なのか、「単なる入力ミスや正当なビジネス上の理由」なのかを最終判断するのはAIではありません。提示された物理的・幾何学的な座標（日時と口座）に基づき、請求書や約定ログなどの「現実世界の生データ（グラウンド・トゥルース）」を実査（追加検証）する人間の監査人こそが、最終的な「裁判官」なのです。

---
**License**: AGPL-3.0
**Built by**: Renpoo & Google DeepMind Agent (Antigravity)
