# Tensor-Link Utility (TLU)

> **"自律型AI監査のための、ドメインの複雑性を数学的透明性へと射影する"**

TLUは、**認知的トライアド（物理学 + 財務 + LLM）を動力とする自律型監査エンジン**です。財務元帳やサプライチェーンなどの方向性を持った取引データを純粋なテンソル空間に射影し、従来の会計モデルが見逃してしまう隠された構造的ダイナミクスを明らかにするよう設計された、高精度の数学的解析パイプラインです。

### 従来の会計の限界

従来の複式簿記では、いかなる計算を開始する前にも、すべての仕訳が完全に整合している必要があります。この絶対的な公理のゆえに、記録が欠落していたり、意図的に操作されていたり（例：循環取引/Wash Trading）する場合、背後にある真実を数学的に抽出することが困難になります。

TLUは、初期の解析フェーズから「バランス（貸借一致）している状態」という要件を取り除くことで、この問題を解決します。会計データを配管内の流体のような「エネルギーのフロー」として再定義することで、TLUはキルヒホッフの電流則や非平衡熱力学といった物理法則を適用し、不完全または「壊れた」データセットからでも真の財務ダイナミクスを計算します。

## 🤖 認知的トライアド（AIによる自律監査）

TLUは単なる視覚的なダッシュボード・ツールではありません。その究極の価値は、大規模言語モデル（LLM）のための「物理エンジン」として機能することにあります。

[**LLM メタ診断システムプロンプト＆操作手順書**](./LLM_Diagnostic_Manual.md)を読み込ませることで、あらゆるLLM（ChatGPT, Claude, Geminiなど）を即座に「メタ診断の専門医（メタ・ダイアグノスティック・ラジオロジスト）」へと変貌させることができます。このマニュアルには、AIがハルシネーションを起こすことなく、高次元の物理的指標（スペクトル半径や自由エネルギーなど）を取り込み、従来の財務諸表（B/S, P/L）とクロスリファレンスして、公認会計士レベルの人間が読める「カルテ（Medical Chart）」を出力するための、厳格な階層型論理フレームワーク（決定マトリックス）が提供されています。

このマニュアルを使用してLLMが自律的に生成した実際の英文監査レポートについては、`samples/` ディレクトリを参照してください！

## 理論的基盤：結合振動子ネットワークとしての元帳

会計に物理方程式を適用することに対する一般的な批判として、「元帳は文字通りの物理的質量や摩擦を持たない」という「カテゴリーエラー」のリスクが挙げられます。しかし、TLUの理論的基盤は文字通りの物理学にあるのではなく、**連続体力学と結合振動子（Coupled Oscillators）**という普遍的に適用される数学的抽象化にあります。

物理学者が固体の応力伝播、熱散逸、または共振周波数をモデル化する際、彼らはそれを目に見えない**バネ（$K$）**と**ダンパー（$C$）**で繋がれた**質点（$M$）**のネットワークに離散化します。TLUは、組織に対して全く同じ数学的に厳密な抽象化を適用します：

* **質量（$M$）/ 慣性**: ポテンシャルエネルギーを蓄積し、突然の状態変化に抵抗する口座の容量（過去のボリューム/ボラティリティに基づく）。
* **剛性（$K$）/ バネ**: 取引チャネルの構造的強度と決定論的な因果関係（例：売上 $\to$ 売掛金）。
* **粘性（$C$）/ ダンパー**: 取引フローに内在する時間的摩擦、散逸、および遅延。

組織を**離散的な弾性体（質量・バネ・ダンパーのネットワーク）**として扱うことで、TLUは運動方程式（$M\ddot{x} + C\dot{x} + Kx = F$）を正当に適用し、外部からの財務的ショック（異常、不正、市場の変化）がビジネス構造を通じてどのように伝播、共鳴、そして減衰するかを計算します。TLUは「企業がニュートンの法則に従う」と主張しているわけではありません。そうではなく、従来の会計というレントゲンでは見逃してしまう異常を浮き上がらせるための、極めて感度の高い**物理情報ベースの特徴量抽出器（Physics-Informed Feature Extractor）**としてこれらの方程式を利用しているのです。
![Mass-Spring-Damper-Modle](../readme_plots/Mass-Spring-Damper-Modle.jpg)

---

## コア哲学とアーキテクチャ (Ver 8.0.0)

TLUは巨大なモノリスを避け、**Unixの哲学**に基づいて構築されており、単一責任のフィルター群を標準ストリームで接続しています。

* **ローカル依存性ゼロ:** ホストOSを汚染しません。すべての解析エンジンはDockerコンテナ内に完全に隔離されています。
* **フェイルファスト UX:** データの不整合やパラメータの欠落が検出された場合、暗黙のフォールバックを行わず、システムは直ちに停止します。これにより、文脈の不一致による誤った経営判断を物理的に防ぎます。
* **宣言的実験制御（SSOT）:** 入力データセット、運動学の制約、LQRの重み、異常閾値など、すべての実験条件は単一の `workspace/config/_sys_params.csv` で集中的に定義されます。このファイルを変更することがパイプラインの動作を変える*唯一*の方法であり、絶対的な透明性を保証します。
* **イミュータブル・アーカイブの再現性:** 完了時、実行された `_sys_params.csv` と出力結果を含む `workspace/` 全体を、`bash bin/archive_experimental_run.sh` を使って `archives/` ディレクトリにスナップショットとして保存できます。アーカイブされたワークスペースをパイプラインのターゲットにするだけで、いつでも全く同じ数学的条件と可視化を再現できます。

### パイプラインの各フェーズ

* **Phase 0: 前処理（Pre-processing）:** ソースデータをクレンジングし、方向性のあるフラックス（流量）フォーマットに集約します。
* **Phase 1: 伝統的会計（IR）:** 人間のアナリストのためのベースラインとして、標準的な B/S と P/L を自動生成します。
* **Phase 3: 射影（Projection）:** ドメインの語彙を取り除き、データを純粋なテンソル空間（COOストリーム）に射影します。
* **Phase 4: コア解析（Core Analysis）:** 物理パラダイム（カテゴリ 000–005）に基づく純粋な数学的フィルター群です。
* **Phase 5: プレゼンテーション:** フェイルファスト・テーマエンジンによって駆動される高密度ダッシュボードのレンダリング。
* **Phase 6: オーケストレーション:** コンテナ環境内でのパイプライン制御と監査証跡の保存。

## 視覚的ショーケース（実証的証拠）

TLUは高度な「ダーク」可視化スイート（「ライト」や「カラーブラインド・セーフ」テーマも利用可能）を通じて、認知負荷を軽減します。以下は、自然科学の系譜を表す新しいタクソノミー（分類法）に基づく解析の軌跡です。

### 000_ 古典力学および固体力学

組織の「脈動」と「剛性」を観察します。TLUは純粋なフラックスから**速度（$v$）**と**加速度（$a$）**を計算し、過去の活動規模から**慣性（仮想質量）**と**粘性**を推定して、それらを位相空間にプロットします。

![1_3_1__3d_dynamics_velocity](../readme_plots/000_1_1__3d_dynamics_velocity.png)
![1_3_2__3d_dynamics_acceleration](../readme_plots/000_1_2__3d_dynamics_acceleration.png)
![1_3_3__3d_dynamics_inertia](../readme_plots/000_1_3__3d_dynamics_inertia.png)
![1_3_4__3d_dynamics_viscosity](../readme_plots/000_1_4__3d_dynamics_viscosity.png)
![1_3_8__phase_portrait_3d](../readme_plots/000_1_8__phase_portrait_3d.png)

### 主軸（PCA）

TLUはまた、共分散行列の固有値と固有ベクトルを計算することで、ネットワークの**主軸（Principal Axes）**を抽出します。これは、組織のリソースが自然に流れ、変動する主要な方向である、分散の支配的な「次元」を明らかにします。

![000_2_2__principal_axes_ratio](../readme_plots/000_2_2__principal_axes_ratio.png)

### 001_ 熱力学および統計力学

あなたの組織は効率的ですか？全体的な**自由エネルギー（$F$）**と**エントロピー（$S$）**を測定します。エントロピーが高く、仕事の出力が低い場合は、システム内に「熱（散逸コスト/無駄）」が蓄積していることを示します。局所的な複雑性とボラティリティも、3D多様体として捉えられます。

![1_3_5__3d_dynamics_entropy](../readme_plots/001_1_2_1__3d_local_entropy.png)
![1_3_6__3d_dynamics_complexity](../readme_plots/001_1_2_5__local_thermo_complexity.png)
![1_5_1__thermodynamics_dashboard](../readme_plots/001_1_1__thermodynamics_dashboard.png)
![1_5_2__thermodynamics_energy_stack](../readme_plots/001_1_2__thermodynamics_energy_stack.png)
![1_5_3__thermodynamics_ts_diagram](../readme_plots/001_1_3__thermodynamics_ts_diagram.png)

### 002_ 情報幾何学およびフォレンジック

データの「血管」に潜む異常の仮面を剥ぎ取ります。TLUはZ-Scoreに基づいて**位相幾何学的なエッジのストレス（Topological Edge Stress）**を計算し、特定の経路における過剰な負荷（破裂リスク）を明らかにし、構造的な歪みをネットワーク・グラフとして可視化します。

![1_12__network_topology t 00000](../readme_plots/002_1_2__network_topology.t.00000.png)
![1_12__network_topology t 00001](../readme_plots/002_1_2__network_topology.t.00001.png)
![1_12__network_topology t 00002](../readme_plots/002_1_2__network_topology.t.00002.png)
![1_12__network_topology t 00003](../readme_plots/002_1_2__network_topology.t.00003.png)

### 多様体の次元性（SVD）

遷移行列に対して特異値分解（SVD）を実行することで、TLUはネットワークの**有効ランク（Effective Rank）**を計算します。ネットワークが過度に中央集権化したり、少数のハブに崩壊したりすると、有効次元数が低下し、構造的脆弱性の早期警戒シグナルとして機能します。

![002_1_3__manifold_dimensionality](../readme_plots/002_1_3__manifold_dimensionality.png)

### 003_ 応用運動学およびロボット工学

*(仮想的な投資の波及効果をシミュレートするための順運動学（Forward Kinematics）、および剛性のペナルティを考慮しながら必要なターゲット介入力を計算するための逆運動学（Inverse Kinematics）をサポートします。)*

![1_1__3d_kinematics_fk](../readme_plots/003_1_1__3d_kinematics_fk.png)
![1_2__3d_kinematics_ik](../readme_plots/003_1_2__3d_kinematics_ik.png)

### 004_ 制御工学およびシステム工学

当てずっぽうはもうやめましょう。**最適レギュレータ（Linear-Quadratic Regulator: LQR）**理論を使用して、組織の摩擦（ひずみエネルギー）を最小限に抑えながら目標状態に到達するための、数学的に最適なリソース配分軌道を計算します。

![1_7_2__control_error_convergence](../readme_plots/004_1_2__control_error_convergence.png)
![1_7_3__control_lqr_performance_space](../readme_plots/004_1_3__control_lqr_performance_space.png)

### システム安定性（スペクトル半径）

システムは制御不能に陥っていませんか？遷移行列の最大固有値（**スペクトル半径**）を計算することで、TLUは位相幾何学的なサイクル（例：循環取引や再帰的ループ）を検出します。半径が1.0に近づくかそれを超える場合、システムは数学的に不安定であり、指数関数的に発散する傾向があります。

![004_1_2__system_stability](../readme_plots/004_1_2__system_stability.png)

---

## サンプル・データセットとハンズオン・チュートリアル

混在するシグナルによる認知負荷なしに、TLUが実際どのように機能するかを理解していただくために、**6つの独立したサンプル・データセット**のスイートを提供しています。これらのデータセットは、様々な制御された病理状態（例：循環取引、横領、仕訳エラー）の下での財務元帳や空間的な交通ネットワークをシミュレートしています。

これらは `samples/` ディレクトリにあります。各サンプルには、注入された異常、その背後にある物理的推論、および**ローカルマシン上で可視化グラフを生成するために実行すべき正確なコマンド**を説明した専用の `README.md` が含まれています。

* [`samples/Sample_0_Healthy/`](../../samples/Sample_0_Healthy/): 完全にバランスの取れたベースライン。[メタ診断レポート](../../samples/Sample_0_Healthy/README.md) を参照。
* [`samples/Sample_1_Wash_Trade/`](../../samples/Sample_1_Wash_Trade/): システム安定性（固有値）について解説。[メタ診断レポート](../../samples/Sample_1_Wash_Trade/README.md) を参照。
* [`samples/Sample_2_Embezzlement_Leak/`](../../samples/Sample_2_Embezzlement_Leak/): 熱力学（自由エネルギー）について解説。[メタ診断レポート](../../samples/Sample_2_Embezzlement_Leak/README.md) を参照。
* [`samples/Sample_3_Unbalanced_Mistake/`](../../samples/Sample_3_Unbalanced_Mistake/): マクロ・フォレンジック（保存則）について解説。[メタ診断レポート](../../samples/Sample_3_Unbalanced_Mistake/README.md) を参照。
* [`samples/Sample_4_Composite_Chaos/`](../../samples/Sample_4_Composite_Chaos/): すべての異常が混在した現実世界のカオス。[メタ診断レポート](../../samples/Sample_4_Composite_Chaos/README.md) を参照。
* [`samples/Sample_5_Kyoto_Traffic/`](../../samples/Sample_5_Kyoto_Traffic/): 純粋な空間ネットワーク（開放系）の対照実験。[メタ診断レポート](../../samples/Sample_5_Kyoto_Traffic/README.md) を参照。
* [`samples/Sample_6_Market_Bipartite_Weekly/`](../../samples/Sample_6_Market_Bipartite_Weekly/): 循環取引を検出する株式市場監査（二部グラフ）。[詳細レポート](../../samples/Sample_6_Market_Bipartite_Weekly/Sample_6_Market_Analysis_Report.md) を参照。
* [`samples/Sample_7_Market_Users_Weekly/`](../../samples/Sample_7_Market_Users_Weekly/): 結託シンジケートを暴くトレーダー・ネットワーク監査（ユーザーグラフ）。[詳細レポート](../../samples/Sample_7_Market_Users_Weekly/Sample_7_User_Analysis_Report.md) を参照。
* 🔍 **メタ比較 (金融):** TLUが市場レベルとユーザーレベルの監査の視点を切り替えて、いかに正確に犯人を特定するかについては、[株式市場向けメタ比較レポート](../../samples/Meta_Comparison_Report_for_Stock_Market.md) をお読みください。
* [`samples/Sample_8_fMRI_Stroke/`](../../samples/Sample_8_fMRI_Stroke/): 重度な動脈閉塞（脳梗塞）を検出する生体ネットワーク監査（fMRI）。[詳細レポート](../../samples/Sample_8_fMRI_Stroke/Sample_8_Diagnostic_Report.md) を参照。
* [`samples/Sample_9_fMRI_Seizure/`](../../samples/Sample_9_fMRI_Seizure/): てんかん性過剰同期（発作）を検出する生体ネットワーク監査（fMRI）。[詳細レポート](../../samples/Sample_9_fMRI_Seizure/Sample_9_Diagnostic_Report.md) を参照。
* 🔍 **メタ比較 (生物学):** 金融不正（循環取引/横領）と医療的病理（てんかん/脳梗塞）の同型的な関係については、[生体ネットワーク向けメタ比較レポート](../../samples/Meta_Comparison_Report_for_Biological_Networks.md) をお読みください。

---

## ドキュメント（ハブ＆スポーク）

詳細な数学的論理、運用プロトコル、および API リファレンスについては、以下の「スポーク」マニュアル（和訳版）を参照してください：

* [01_System_Philosophy_and_Operations.md](./architecture/01_System_Philosophy_and_Operations.md)
* [02_Data_Topology_and_Projection.md](./architecture/02_Data_Topology_and_Projection.md)
* [03_Visualizer_and_Theme_Engine.md](./architecture/03_Visualizer_and_Theme_Engine.md)
* [04_Simulation_and_TDD.md](./architecture/04_Simulation_and_TDD.md)
* [05_Meta_Analytical_Methodology_and_AI_Collaboration.md](./architecture/05_Meta_Analytical_Methodology_and_AI_Collaboration.md)
* [06_Dummy_Data_Generators.md](./architecture/06_Dummy_Data_Generators.md)
* [07_Theoretical_Limits_and_Edge_Effects.md](./architecture/07_Theoretical_Limits_and_Edge_Effects.md)

* [000_Classical_Mechanics.md](./physics/000_Classical_Mechanics.md)
* [001_Thermodynamics_and_Fluctuations.md](./physics/001_Thermodynamics_and_Fluctuations.md)
* [002_Information_Geometry_and_Forensics.md](./physics/002_Information_Geometry_and_Forensics.md)
* [003_Applied_Kinematics.md](./physics/003_Applied_Kinematics.md)
* [004_Control_Theory_and_Systems_Engineering.md](./physics/004_Control_Theory_and_Systems_Engineering.md)
* [005_Signal_Processing_and_Wave_Mechanics.md](./physics/005_Signal_Processing_and_Wave_Mechanics.md)

* [Graph_Interpretation_Guide.md](./interpretations/TLU_Graph_Interpretation_Guide.md)
* [LLM_Diagnostic_Manual.md](./LLM_Diagnostic_Manual.md)

---

## クイックスタート

TLUは完全にコンテナ化されています。数分でゼロから完全な3D分析ダッシュボードを構築できます。

```bash
# 1. リポジトリをクローン
git clone https://github.com/renpoo/TLU.git
cd TLU

# 2. 環境を立ち上げる（ローカルへの依存ゼロ）
docker compose up -d

# 3. 生成されたサンプルデータでフルパイプラインを実行
# (ユニットテストを実行するには: bash bin/batch_unittest.sh)
bash bin/batch_generate_dummy_journal_data.sh
bash bin/batch_processing.sh
bash bin/batch_visualize_graphs.sh

# 4. 診断結果を確認する
# batch_processing.sh スクリプトは一番最後に自動的にメタ診断エンジンを実行します。
# 出力ディレクトリで最終的なカルテを確認してください：
cat workspace/output_data/_99_diagnosis_report.md

# 5. 完全な再現性のために実験をスナップショット保存する
bash bin/archive_experimental_run.sh

# 6. (オプション) クロス環境比較
# 複数の実験やサンプルを横並びで比較します
bash bin/batch_meta_analysis.sh --envs "samples/Sample_*" --out "samples"
```

# ライセンス: AGPL-3.0

このプロジェクトは数学的透明性の遺産です。AGPL-3.0 ライセンスの下、コアロジックがオープンであり、コミュニティによって検証可能であることを保証します。もしあなたがこのエンジンをベースに構築を行うなら、世界はその数学（数式）を見る権利があります。

# 開発: Renpoo & Google Gemini

TLUは、XP（エクストリーム・プログラミング）および TDD（テスト駆動開発）プロトコルを厳格に遵守して開発されています。すべてのコアな数学関数は、理論的なエッジケースに対して検証されています。
