# 🔬 Tensor-Link Utility (TLU)

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-red.svg)](https://www.gnu.org/licenses/agpl-3.0.html)
[![Python Version](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Docker Status](https://img.shields.io/badge/Docker-Compatible-emerald.svg)](https://www.docker.com/)

### 物理数学による数理解析で「やりとりのデータ」を可視化する

Tensor-Link Utility (TLU) は、データ内の病的異常を可視化するプラットフォームです。
TLUの物理数学的な帰結は以下です。
「会計帳簿の上で仮装取引や粉飾を行っても、質量保存の法則（貸借一致の原則）や熱力学の法則を欺くことは不可能である。」

TLUは、時系列データを「力の流れ」として再定義します。対象は複式簿記、都市交通、株式市場、および脳fMRIです。弾性ネットワークモデルを用います。システム内には様々な異常が発生します（横領、循環取引、デッドロック、相場操縦、脳梗塞、てんかんなど）。これらを物理数学的署名（剛性の崩壊、病的共鳴、熱的異常、相関異常など）として可視化します。

物理数学エンジンは各種指標を出力します。AIエージェントがこれらの指標を解読します。解読には [`LLM_Diagnostic_Manual.md`](LLM_Diagnostic_Manual.md) を用います。AIは指標を「臨床検査カルテ」へ翻訳します。

---

## 📚 ドキュメント構成 (Documentation Map)

すべてのドキュメントは `docs/` 配下に集約されています。以下は英語版と日本語版のマッピングです。

| # | ドキュメントタイトル（英語版） | 対応する日本語版 | コアコンテンツ |
| :---: | :--- | :--- | :--- |
| **1** | **000-005 Mathematical Analysis Guides** (placed in `samples/`):<br>・**[000_0: Statistics](../samples/000_0_Basic_Statistics.md)** / **[000_1: Kinematics](../samples/000_1_Dynamics_Kinematics.md)** / **[000_2: Stiffness & PCA](../samples/000_2_Stiffness_PCA.md)**<br>・**[001_1: Thermodynamics](../samples/001_1_Thermodynamics.md)** / **[001_2: Local Entropy](../samples/001_2_Local_Entropy.md)** / **[001_3: Local Temperature](../samples/001_3_Local_Temperature.md)** / **[001_4: Local Energy Gradient](../samples/001_4_Local_Gradient.md)** / **[001_5: Local Internal Energy](../samples/001_5_Local_Internal_Energy.md)**<br>・**[002_1: Information Geometry](../samples/002_1_Information_Geometry.md)** / **[002_2: Conservation & Auditing](../samples/002_2_Forensics.md)**<br>・**[003_1: Kinematics](../samples/003_1_Kinematics.md)**<br>・**[004_1: LQR Control](../samples/004_1_Control_Theory.md)** / **[004_2: Intervention Sensitivity](../samples/004_2_Stability.md)**<br>・**[005_1: Wave Mechanics](../samples/005_1_Wave_Mechanics.md)** / **[005_2: 1/f Fluctuation](../samples/005_2_Coherence.md)** | 000〜005番系 数理解析ガイド（`samples/` 以下に配置）：<br>・**[000_0: 統計](samples/000_0_Basic_Statistics.md)** / **[000_1: 運動学](samples/000_1_Dynamics_Kinematics.md)** / **[000_2: 剛性・PCA](samples/000_2_Stiffness_PCA.md)**<br>・**[001_1: 熱力学](samples/001_1_Thermodynamics.md)** / **[001_2: 局所エントロピー](samples/001_2_Local_Entropy.md)** / **[001_3: 局所温度](samples/001_3_Local_Temperature.md)** / **[001_4: 局所エネルギー・勾配](samples/001_4_Local_Gradient.md)** / **[001_5: 局所内部エネルギー](samples/001_5_Local_Internal_Energy.md)**<br>・**[002_1: 情報幾何](samples/002_1_Information_Geometry.md)** / **[002_2: 保存則・監査](samples/002_2_Forensics.md)**<br>・**[003_1: 逆運動学](samples/003_1_Kinematics.md)**<br>・**[004_1: LQR制御](samples/004_1_Control_Theory.md)** / **[004_2: 介入感度](samples/004_2_Stability.md)**<br>・**[005_1: 波動力学](samples/005_1_Wave_Mechanics.md)** / **[005_2: 1/fゆらぎ](samples/005_2_Coherence.md)** | TLUの主要8コアモジュール（000〜005番系）の数理的・物理的基礎理論と、全10個の検証サンプルに対応する実機可視化グラフをモジュールごとに分割し、診断解釈ガイド群として再編したものです。 |
| **2** | **[System Architecture & Simulation Operations Guide](../System_Architecture_and_Operations.md)** | **[システムアーキテクチャとシミュレーション運用ガイド](System_Architecture_and_Operations.md)** | パイプライン・コンテナ運用、デザインテーマ管理（JSON）、障害込みダミー・データ生成スクリプト、および線形最適制御（LQR）シミュレーションモデル。 |
| **3** | **[LLM Diagnostic Manual (Supreme prompt & Operations)](../LLM_Diagnostic_Manual.md)** | **[LLM メタ検査マニュアル（最高メタレベルシステムプロンプト＆運用手順）](LLM_Diagnostic_Manual.md)** | 物理数学エンジンの数値からAIが客観的なカルテを自動生成するためのプロトコル。統計的偽陽性判定と、原本データへのファクトチェック義務化。 |
| **4** | **[Universal Forensic Cross-Verification Registry](../samples/README.md)** | **[数理解析ガイド＆検証サンプル総合目次](samples/README.md)** | TLUに実装されている全10種類の検証サンプルの判定判定、物理数学パラメータ限界値、および線形最適制御（LQR）介入ポイント・ガイド。 |

---

## ⚕️ コアパラダイム：物理的媒体としてのネットワーク力学

TLUは、トランザクション・データを質量／バネ／ダンパーで連結された連続弾性体ネットワークとしてモデル化します。

![質量／バネ／ダンパー・モデル](../readme_plots/Mass-Spring-Damper-Model.jpg)
*図1: 勘定科目を質量／バネ／ダンパー・システムに見立てる概念図*

### 東洋医学（漢方・気血水）の臨床メタファー

TLUは、東洋医学 of 語彙を用います。システムを「経絡」（取引経路）として検査します。そこを「気血水」（資金や活動のめぐり）が流れます。血流が滞り、血栓が生じている箇所（剛性の硬化やデッドロック）を特定します。あるいは、大出血を起こしている箇所（資金の漏出や横領）を特定します。線形最適制御（LQR）理論を用います。治療の急所である「経穴（ツボ）」を特定します。

### 各ドメインから物理空間へのマッピング一覧

| 物理変数 | 古典力学・熱力学の定義 | 財務会計ドメイン | 都市交通ドメイン | 株式市場ドメイン | 生体脳神経 (fMRI) ドメイン |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **質量 ( $m_i$ )** | 慣性 / エネルギー貯蔵タンク | 勘定残高 | 交差点内の滞留車両数 | 口座保有の資本金 | BOLD信号の変化量 |
| **流量 ( $f_{ij}$ )** | 速度 / 質量移動 | 仕訳の金額 | 通過車両数（台/秒） | 約定資金や株式の移動 | 神経間の信号流量 |
| **剛性 ( $k_{ij}$ )** | 弾性 / ばね定数 | 取引関係の固着度 | 交差点の流出入の許容量 | 注文対当の同期度 | 活動の同調度 |
| **粘性 ( $c_{ij}$ )** | 摩擦 / ダンパー制動 | 決済までのタイムラグ（30〜90日） | 渋滞の抵抗度 | 約定遅延、注文・成立価格のズレ | 信号伝播の伝達遅延 |
| **エントロピー ( $S$ )** | 無秩序度 / 摩擦熱損失 | 架空循環取引（売上水増し） | 渋滞による摩擦熱の発生 | USR間の仮装対当取引 | 脳神経の過同期 (てんかんなど) |
| **自由エネルギー ( $F$ )** | 有効仕事ポテンシャル | 税引前純営業利益 | 航空車両の流動ポテンシャル | 市場の真の配分効率 | 脳の認知・情報処理キャパシティ |
| **治療点 (LQR)** | 制御入力ベクトル | 重点勘定科目の絞り込み | 道路信号周期の調整 | 相場操縦口座の特定 | 経頭蓋磁気刺激 (TMS) の焦点 |

---

## 🔬 4つの主要な物理署名 (Spatiotemporal Proofs)

TLUは、システム内に発生した異常を検出するために4つの物理シグネチャを抽出します。

### 1. マクロ・フォレンジック (質量保存則とキルヒホッフの法則)

システム全体の資金流入と流出の残差を検証します。資金が簿外へ隠蔽された場合、質量保存則が破綻します。残差プロットに巨大なスパイクが立ち上がります。

* **🟢 健常状態 (Sample 0):** 保存残差は全期間を通じて `0.00` を維持します。資金の簿外リークがないことを物理的に証明します。
* **🚨 質量欠損状態 (Sample 2 / 横領):** 売掛金の回収資金が簿外の隠蔽ノードへバイパスされています。質量保存則が崩壊します。絶対値としての保存残差が正方向のスパイクとして検知されます。

| 健常 steady-state (Sample 0) | 病的質量欠損 (Sample 2) |
| :---: | :---: |
| ![Macro Forensics Normal](../../samples/Sample_0_Healthy/readme_plots/002_2_1__macro_forensics_dashboard.png) | ![Macro Forensics Abnormal](../../samples/Sample_2_Embezzlement_Leak/readme_plots/002_2_1__macro_forensics_dashboard.png) |
| *図2a:（上段）質量保存の維持 (残差 = 0)* | *図2b:（上段）資金横領に伴う絶対値残差のスパイク検知* |

---

### 2. トポロジーとシステム安定度 (スペクトル半径 $\rho$ )

接続行列の最大固有値である「スペクトル半径」を計算します。ネットワーク内に還流閉路（自己循環）が形成されているかを検証します。スペクトル半径が警報ライン `1.00` に達したとします。この場合、システムは自己循環にロックされて暴走します。これを数学的に実証します。

* **🟢 健常状態 (Sample 0):** スペクトル半径は全期間を通じて `0.00` 配下に留まります。取引が循環せず正常に収束していることを示します。
* **🚨 還流固着状態 (Sample 4 / 複合アノマリー):** 循環取引によりスペクトル半径が最大 `0.79` へ急上昇します。これにより、虚構ループの形成を証明します。

| 健常 steady-state (Sample 0) | 病的還流ループ (Sample 4) |
| :---: | :---: |
| ![System Stability Normal](../../samples/Sample_0_Healthy/readme_plots/004_1_2__system_stability.png) | ![System Stability Abnormal](../../samples/Sample_4_Composite_Chaos/readme_plots/004_1_2__system_stability.png) |
| *図3a: 安全圏で収束するスペクトル半径* | *図3b: 限界境界に向けて上昇するスペクトル半径* |

---

### 3. 熱力学エネルギー積層 (組織の疲弊と熱的死)

システムの有効仕事能力である「自由エネルギー（$F = U - TS$）」を計算します。自由エネルギーがマイナス領域に沈むと、システムは熱的死に至ります。活動（内部エネルギー $U$）を行うほど、無駄な還流摩擦熱（エントロピー $TS$）が排出されます。これによりシステムが疲弊します。

* **🟢 健常状態 (Sample 0):** 自由エネルギーが常にプラスの領域で推移します。活動に比例して貯留エネルギーが増大する代謝プロセスを示します。
* **🚨 熱的死状態 (Sample 8 / fMRI):** 運動野への血流が遮断されます。それにより機能的結合がフリーズし、エントロピー $S$ が急激に低下します。一方で摩擦熱（マクロ温度 $T$）が急上昇します。そのため、有効仕事能力 $F$ が急激に減少します。システムは熱的死へ沈下します。

| 健常 steady-state (Sample 0) | 病的熱的死 (Sample 8) |
| :---: | :---: |
| ![Thermodynamics Normal](../../samples/Sample_0_Healthy/readme_plots/001_1_2__thermodynamics_energy_stack.png) | ![Thermodynamics Abnormal](../../samples/Sample_8_fMRI_Stroke/readme_plots/001_1_2__thermodynamics_energy_stack.png) |
| *図4a: 自由エネルギーの健全な蓄積* | *図4b: 自由エネルギーが減少してゆく熱的死状態* |

---

### 4. 3D空間幾何学歪み (KL Drift と局所温度)

各ノードの確率分布の幾何学的歪みをモデル化します。3D空間上の多様体として扱います。システムに異常が発生したとします（特定の交差点でのデッドロック、特定のアカウントによる共謀取引、あるいは脳梗塞など）。このとき、平坦な空間に鋭い黄緑色の「針状のタワー」がそびえ立ちます。

* **🟢 健常状態 (Sample 0):** 初期ステップでのデータ不足による端点効果（Edge Effect）を除き、その後は平穏なブルーの空間を維持します。
* **🚨 幾何学的変異状態 (Sample 5 / 交通デッドロック):** 交差点 `23_四条烏丸` が封鎖されます。その瞬間、確率分布が崩壊します。時空間座標を正確に貫く鋭利な幾何学歪みの尖塔が屹立します。高さは数値にして600,000に達します。

| 健常 steady-state (Sample 0) | 病的時空間歪み (Sample 5) |
| :---: | :---: |
| ![3D Space Normal](../../samples/Sample_0_Healthy/readme_plots/002_2_2_2__3d_micro_z_score_X.png) | ![3D Space Abnormal](../../samples/Sample_5_Kyoto_Traffic/readme_plots/002_2_2_2__3d_micro_z_score_X.png) |
| *図5a: 平坦で平穏な幾何学的多様体* | *図5b: 局所異常の座標と発生時刻を正確に示す幾何学的歪みの尖塔* |

---

## 📂 10種類の検証用ケーススタディ

TLUには、物理数学エンジンの精度を実証するため、10のサンプルデータセットがパッケージ化されています。

| ID | 検証サンプル事例名（個別レポートリンク） | ドメイン | 検査判定 | 数理パラメータ特性 | 東洋医学メタファー |
| :---: | :--- | :---: | :---: | :---: | :--- |
| **0** | **[🟢 会計上の正常な定常的代謝 (Healthy)](samples/Sample_0_Healthy/README.md)** | 金融 | **NORMAL (正常)** | $\rho$ = 0.00, 残差 = 0.00 | 気血が滞っていない |
| **1** | **[🟡 会計上の循環取引（架空還流） (Wash Trade)](samples/Sample_1_Wash_Trade/README.md)** | 金融 | **HIGH (架空還流)** | $\rho$ = 0.75, 自由エネルギーの枯渇 | 気血が空転、還流が閉路を為している |
| **2** | **[🔴 会計上の資金横領（漏出） (Embezzlement Leak)](samples/Sample_2_Embezzlement_Leak/README.md)** | 金融 | **CRITICAL (横領)** | 最大残差 = 364.53, 終期共鳴 | 経絡上の出血、質量の欠損、気血の漏洩 |
| **3** | **[🟡 会計上の単純な記帳ミス (Unbalanced Mistake)](samples/Sample_3_Unbalanced_Mistake/README.md)** | 金融 | **WARNING (記帳ミス)** | 一時的な残差およびKL幾何タワー | 気血の局部不均衡、自己治癒の余地 |
| **4** | **[🔴 会計上の複合的な崩壊 (Composite Chaos)](samples/Sample_4_Composite_Chaos/README.md)** | 金融 | **CRITICAL (複合崩壊)** | $\rho$ = 0.79, 最大残差 = 4,773.57 | 気血の空転と出血 |
| **5** | **[🔴 仮想京都の都市交通（デッド・ロック） (Kyoto Traffic)](samples/Sample_5_Kyoto_Traffic/README.md)** | 交通 | **CRITICAL (デッドロック)** | $\rho$ = 1.00, マクロ温度 $T$ = 16,264.61 | 経絡の閉塞、滞血、対流の停止 |
| **6** | **[🟢 相場操縦における銘柄と株主の相互関係の二部グラフ (Market Bipartite)](samples/Sample_6_Market_Stock_Flow/README.md)** | 株式市場 | **NORMAL (正常)** | $\rho$ = 1.00, 残差 = 0.00 | 株式流体平衡・定常対流 |
| **7** | **[🟢 相場操縦における株主間関係のみの一部グラフ (Market Cash Flow)](samples/Sample_7_Market_Cash_Flow/README.md)** | 株式市場 | **NORMAL (正常)** | $\rho$ = 1.00, 残差 = 0.00 | 現金流体平衡・定常対流 |
| **8** | **[🔴 脳梗塞発症時を模した fMRI (fMRI Stroke)](samples/Sample_8_fMRI_Stroke/README.md)** | 脳機能 | **CRITICAL (血流途絶)** | 流入経路95%遮断、結合剛性固着 | 脳経絡の閉塞、局所の気血の枯渇、組織の壊死 |
| **9** | **[🔴 てんかん発症時を模した fMRI (fMRI Seizure)](samples/Sample_9_fMRI_Seizure/README.md)** | 脳機能 | **CRITICAL (異常共振)** | $\rho$ = 1.00, エントロピー垂直落下 | 脳経絡過同期・気血暴走 |

---

## ⚕️ 線形最適制御（LQR）理論による動的治療アプローチ

TLUはシステムの異常を検知します。さらに、ネットワークの状態空間モデルから線形最適制御 (LQR) を用います。システムを健常な軌道へ引き戻すための最適介入点「ツボ」を特定します。「ツボ」は介入感度が高く、コントロール効果が波及しやすいポイントです（Cumulative Control Effort > 0.00）。

| 金融市場 (Sample 7) | 脳神経科学 (Sample 9) |
| :---: | :---: |
| ![相場操縦のハブを特定](../../samples/Sample_7_Market_Cash_Flow/readme_plots/004_1_3__control_lqr_performance_space.png) | ![てんかんの震源である側頭葉を特定](../../samples/Sample_9_fMRI_Seizure/readme_plots/004_1_3__control_lqr_performance_space.png) |
| 図6a：相場操縦のハブである `USR_004` や `USR_005` を特定 | 図6b：てんかんの病的同期の震源である側頭葉（`Temporal_Lobe`）を特定 |

---

## 🚀 実行環境とクイックスタート (Docker)

TLUは、statelessなDockerコンテナとTDDを採用しています。開発者の環境による影響や人為的ミスを排除します。

#### 準備：独自データの解析要件

独自データを解析する場合、`workspace/` ディレクトリに以下の2つのCSVファイルを配置してください。

1. **取引流量データ (`workspace/input_stream/`)**: 時系列トランザクションCSVです。`Trans_Date` (発生日), `Account_Name` (勘定名), `Debit` (流入額), `Credit` (流出額) のカラムが必要です。
2. **勘定マッピング辞書 (`workspace/config/_account_mapping.csv`)**: 勘定科目をTLUのB/S, P/Lカテゴリ（Asset, Liability, Revenue等）へマッピングする定義ファイルです。

#### 自動シミュレーションパイプライン実行手順

```bash
# 1. リポジトリをクローン
git clone https://github.com/renpoo/TLU.git
cd TLU

# 2. Docker コンテナを起動
docker compose up -d

# 3. パイプラインを実行 (Sample 1: 循環取引のシミュレーション例)
bash bin/batch_processing.sh --target_env "samples/Sample_1_Wash_Trade"
bash bin/batch_visualize_graphs.sh --target_env "samples/Sample_1_Wash_Trade"
```

---

## ⚠️ 反証可能性と臨床モデルの限界

TLUは、物理数学的な客観的事実のみを出力する計算機です。

アノマリーの背後には法的・道徳的意図があります。それが犯罪（横領・粉飾・市場操縦）であるか、あるいは入力ミスや正当な取引であるかどうかの最終判断は、TLUやAIの役割ではありません。算出された物理数学的指標と幾何学座標（日付、勘定科目など）を手がかりにします。人間が現実世界の原本データ（銀行口座残高証明書、取引所の生ログ、脳組織 of 生検結果など）と突き合わせて実地調査を行います。この実地調査が、検査を確定させる決定要素となります。

---

**ライセンス**: AGPL-3.0  
**開発者**: Renpoo & Google Gemini Agent (Antigravity)
