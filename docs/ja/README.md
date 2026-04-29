# Tensor-Link Utility (TLU)

> **"自律型AI監査のための、ドメインの複雑性を数学的透明性へと射影する"**

TLUは、**認知的トライアド（物理学 + 財務 + LLM）を動力とする自律型監査処理系**です。財務元帳やサプライチェーンなどの方向性を持った取引データを純粋なテンソル空間に**射影**し、従来の会計モデルが見逃してしまう隠された構造的ダイナミクスや異常発火（アノマリー）を明らかにするよう設計された、高精度の数学的・フォレンジック的解析パイプラインです。

### 従来の会計の限界

従来の複式簿記では、いかなる計算を開始する前にも、すべての仕訳が完全に整合している必要があります。この絶対的な公理のゆえに、記録が欠落していたり、意図的に改竄・隠蔽されていたり（例：**循環取引**による帳簿の水増し）する場合、現実世界の現象と**突合・比較衡量**して背後にある真実を数学的に抽出することが困難になります。

TLUは、初期の解析フェーズから「バランス（貸借一致）している状態」という要件を取り除くことで、この問題を解決します。会計データを配管内の流体のような「エネルギーのフロー」として再定義し、キルヒホッフの電流則や非平衡熱力学といった物理法則を適用することで、不完全または「壊れた」データセットからでも、企業という有機体の真の財務ダイナミクスを計算します。

## 🤖 認知的トライアド（AIによる自律監査）

TLUは単なる視覚的なダッシュボード・ツールではありません。その究極の価値は、大規模言語モデル（LLM）のための「物理的処理系」として機能することにあります。

[**LLM メタ診断マニュアル**](./LLM_Diagnostic_Manual.md)を読み込ませることで、あらゆるLLM（ChatGPT, Claude, Geminiなど）を即座に「メタ診断の専門医」へと変貌させることができます。このマニュアルには、AIがハルシネーションを起こすことなく、高次元の物理的指標（スペクトル半径や自由エネルギーなど）を取り込み、従来の財務諸表（B/S, P/L）と突合して、公認会計士レベルの人間が読める「カルテ（Medical Chart）」を出力するための、厳格な階層型論理フレームワークが提供されています。

実際の英文監査レポートについては、`samples/` ディレクトリを参照してください！

## 理論的基盤：連成振動ネットワークとしての元帳

会計に物理方程式を適用することに対する一般的な批判として、「元帳は文字通りの物理的質量や摩擦を持たない」というカテゴリーエラーのリスクが挙げられます。しかし、TLUの理論的基盤は文字通りの物理学にあるのではなく、**連続体力学と連成振動（Coupled Oscillators）**という普遍的に適用される数学的抽象化にあります。

TLUは、組織に対して全く同じ数学的に厳密な抽象化を適用します：

* **質量（$M$）/ 慣性**: ポテンシャルエネルギーを蓄積し、突然の状態変化に抵抗する口座の容量（過去の取引ボリュームやボラティリティに基づく）。
* **剛性（$K$）**: 取引チャネルの構造的強度と決定論的な因果関係（例：売上 $\to$ 売上債権）。
* **粘性・摩擦（$C$）**: 取引フローに内在する時間的摩擦、散逸、および決済の遅延。

組織を**離散的な弾性体のネットワーク**として扱うことで、TLUは運動方程式（$M\ddot{x} + C\dot{x} + Kx = F$）を正当に適用し、外部からの財務的ショック（アノマリー、改竄、市場の変化）がビジネス構造を通じてどのように伝播、共鳴、そして減衰するかを計算します。TLUは「企業がニュートンの法則に従う」と主張しているわけではなく、従来の会計というレントゲンでは見逃してしまう巧妙な隠蔽工作を浮き上がらせるための、極めて感度の高い「処理系（Physics-Informed Feature Extractor）」として機能します。
![Mass-Spring-Damper-Modle](../readme_plots/Mass-Spring-Damper-Modle.jpg)

---

## コア哲学とアーキテクチャ (Ver 8.0.0)

TLUは巨大なモノリスを避け、単一責任のフィルター群を標準ストリームで接続しています。

* **ローカル依存性ゼロ:** すべての解析エンジンはコンテナ内に完全に隔離されています。
* **フェイルファスト UX:** データの不整合が検出された場合、暗黙のフォールバックを行わず、システムは直ちに停止します。
* **宣言的実験制御（SSOT）:** すべての実験条件は単一の `workspace/config/_sys_params.csv` で集中的に定義され、絶対的な透明性を保証します。
* **イミュータブル・アーカイブ:** 完了時、実行環境全体をアーカイブし、いつでも全く同じ数学的条件を再現できます。

### パイプラインの各フェーズ

* **Phase 0: 前処理:** ソースデータをクレンジングし、方向性のあるフラックス（流量）フォーマットへと**事前集約**します。
* **Phase 1: 伝統的会計（IR）:** 人間のアナリストとの**比較衡量**のベースラインとして、標準的な B/S と P/L を自動生成します。
* **Phase 3: 射影（Projection）:** ドメインの語彙を取り除き、データを純粋なテンソル空間（COOストリーム）に**射影**します。
* **Phase 4: コア解析:** 物理パラダイムに基づく純粋な数学的フィルター群の処理系です。
* **Phase 5: プレゼンテーション:** ダッシュボードのレンダリング。
* **Phase 6: オーケストレーション:** パイプライン制御と監査証跡の保存。

## 視覚的ショーケース（実証的証拠）

### 000_ 古典力学および固体力学
組織の「脈動」と「結合の強さ」を観察します。TLUは純粋なフラックスから速度と加速度を計算し、過去の活動規模から慣性と**粘性（摩擦）**を推定して、それらを位相空間にプロットします。

![1_3_1__3d_dynamics_velocity](../readme_plots/000_1_1__3d_dynamics_velocity.png)
![1_3_2__3d_dynamics_acceleration](../readme_plots/000_1_2__3d_dynamics_acceleration.png)
![1_3_3__3d_dynamics_inertia](../readme_plots/000_1_3__3d_dynamics_inertia.png)
![1_3_4__3d_dynamics_viscosity](../readme_plots/000_1_4__3d_dynamics_viscosity.png)
![1_3_8__phase_portrait_3d](../readme_plots/000_1_8__phase_portrait_3d.png)

### 主軸（PCA）
共分散行列の固有値解析により、ネットワークの主軸を抽出します。これは組織のリソースが変動する主要な方向（次元）を明らかにします。
![000_2_2__principal_axes_ratio](../readme_plots/000_2_2__principal_axes_ratio.png)

### 001_ 熱力学および統計力学
全体的な自由エネルギーとエントロピーを測定します。エントロピーが高く、仕事の出力が低い場合は、システム内に「熱（散逸コスト/無駄）」が蓄積していることを示します。

![1_3_5__3d_dynamics_entropy](../readme_plots/001_1_2_1__3d_local_entropy.png)
![1_3_6__3d_dynamics_complexity](../readme_plots/001_1_2_5__local_thermo_complexity.png)
![1_5_1__thermodynamics_dashboard](../readme_plots/001_1_1__thermodynamics_dashboard.png)
![1_5_2__thermodynamics_energy_stack](../readme_plots/001_1_2__thermodynamics_energy_stack.png)
![1_5_3__thermodynamics_ts_diagram](../readme_plots/001_1_3__thermodynamics_ts_diagram.png)

### 002_ 情報幾何学およびフォレンジック
データの「血管」に潜むアノマリーの仮面を剥ぎ取ります。TLUはZ-Scoreに基づいてエッジのストレスを計算し、構造的な歪みをネットワーク・グラフとして可視化します。また、SVDを用いてネットワークの有効ランクを計算し、マクロな**相転移（レジームチェンジ）**の早期警戒シグナルとして機能します。

![1_12__network_topology t 00000](../readme_plots/002_1_2__network_topology.t.00000.png)
![1_12__network_topology t 00001](../readme_plots/002_1_2__network_topology.t.00001.png)
![1_12__network_topology t 00002](../readme_plots/002_1_2__network_topology.t.00002.png)
![1_12__network_topology t 00003](../readme_plots/002_1_2__network_topology.t.00003.png)
![002_1_3__manifold_dimensionality](../readme_plots/002_1_3__manifold_dimensionality.png)

### 003_ 応用運動学およびロボット工学
順運動学による順運動学のシミュレーション、および逆運動学を用いたターゲット介入計算をサポートします。

![1_1__3d_kinematics_fk](../readme_plots/003_1_1__3d_kinematics_fk.png)
![1_2__3d_kinematics_ik](../readme_plots/003_1_2__3d_kinematics_ik.png)

### 004_ 制御工学およびシステム工学
最適レギュレータ（LQR）理論を使用して、組織の摩擦を最小限に抑えながら目標状態に到達するための最適なリソース配分軌道を計算します。
また、遷移行列の最大固有値（**スペクトル半径/スペクトル半径**）を計算することで、位相幾何学的なサイクル（**循環取引**による帳簿改竄のループなど）を検出します。

![1_7_2__control_error_convergence](../readme_plots/004_1_2__control_error_convergence.png)
![1_7_3__control_lqr_performance_space](../readme_plots/004_1_3__control_lqr_performance_space.png)
![004_1_2__system_stability](../readme_plots/004_1_2__system_stability.png)

---

## サンプル・データセットとハンズオン・チュートリアル

混在するシグナルによる認知負荷なしに、TLUが実際どのように機能するかを理解していただくために、**6つの独立したサンプル・データセット**のスイートを提供しています。これらは、循環取引、資金着服（横領）、仕訳エラーなどの病理状態をシミュレートしています。

* [`samples/Sample_0_Healthy/`](../../samples/Sample_0_Healthy/): 完全にバランスの取れたベースライン。
* [`samples/Sample_1_Wash_Trade/`](../../samples/Sample_1_Wash_Trade/): 発散リスク（固有値）と循環取引について解説。
* [`samples/Sample_2_Embezzlement_Leak/`](../../samples/Sample_2_Embezzlement_Leak/): 資金着服と熱力学（自由エネルギー）について解説。
* [`samples/Sample_3_Unbalanced_Mistake/`](../../samples/Sample_3_Unbalanced_Mistake/): マクロ・フォレンジック（保存則）とアノマリーについて解説。
* [`samples/Sample_4_Composite_Chaos/`](../../samples/Sample_4_Composite_Chaos/): すべての異常が混在した現実世界のカオス。
* [`samples/Sample_5_Kyoto_Traffic/`](../../samples/Sample_5_Kyoto_Traffic/): 純粋な空間ネットワークの対照実験。
* [`samples/Sample_6_Market_Bipartite_Weekly/`](../../samples/Sample_6_Market_Bipartite_Weekly/): 循環取引を検出する株式市場監査（二部グラフ）。
* [`samples/Sample_7_Market_Users_Weekly/`](../../samples/Sample_7_Market_Users_Weekly/): 結託シンジケートを暴くトレーダー・ネットワーク監査。
* 🔍 **メタ比較 (金融):** [株式市場向けメタ比較レポート](../../samples/Meta_Comparison_Report_for_Stock_Market.md) を参照。
* [`samples/Sample_8_fMRI_Stroke/`](../../samples/Sample_8_fMRI_Stroke/): 生体ネットワーク監査（fMRI: 脳梗塞）。
* [`samples/Sample_9_fMRI_Seizure/`](../../samples/Sample_9_fMRI_Seizure/): 生体ネットワーク監査（fMRI: てんかん性発作）。
* 🔍 **メタ比較 (生物学):** [生体ネットワーク向けメタ比較レポート](../../samples/Meta_Comparison_Report_for_Biological_Networks.md) を参照。

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

## ユーザーが用意すべきもの (User Prerequisites)

TLUのディレクトリ構成は一般的なGNUシステム（`src/`、`bin/`、`docs/`等）に準拠しています。一般ユーザーが自分自身のデータでTLUを動作させるために用意・編集すべきファイルは、すべて `workspace/` ディレクトリ内に集約されています。

1. **生の仕訳データ (Input Data)**
   * **場所:** `workspace/input_stream/` (例: `Dummy_Journal_Stream.csv`)
   * **内容:** 会計ソフト等からエクスポートした時系列の仕訳データ（CSV形式）。最低限「日付 (Trans_Date)」「勘定科目名 (Account_Name)」「借方金額 (Debit)」「貸方金額 (Credit)」の列が含まれている必要があります。

2. **勘定科目のマッピング設定ファイル**
   * **場所:** `workspace/config/_account_mapping.csv`
   * **内容:** ユーザー独自の勘定科目名（例：「みずほ銀行口座」）を、TLUが理解できる標準カテゴリ（`Asset`, `Liability`, `Revenue`, `Expense` 等）に紐付けるための設定ファイルです。

※ 詳細なシミュレーション設定（時間粒度や物理係数）は `workspace/config/_sys_params.csv` で行いますが、最初はデフォルトのままで動作します。

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
bash bin/batch_generate_dummy_journal_data.sh
bash bin/batch_processing.sh
bash bin/batch_visualize_graphs.sh

# 4. 診断結果を確認する
cat workspace/output_data/_99_diagnosis_report.md

# 5. 完全な再現性のために実験をスナップショット保存する
bash bin/archive_experimental_run.sh
```

# ライセンス: AGPL-3.0
このプロジェクトは数学的透明性の遺産です。AGPL-3.0 ライセンスの下、コアロジックがオープンであり、コミュニティによって検証可能であることを保証します。

# 開発: Renpoo & Google Gemini
TLUは、XPおよび TDD プロトコルを厳格に遵守して開発されています。
