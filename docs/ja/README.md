# 🔬 Tensor-Link Utility (TLU)

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-red.svg)](https://www.gnu.org/licenses/agpl-3.0.html)
[![Python Version](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Docker Status](https://img.shields.io/badge/Docker-Compatible-emerald.svg)](https://www.docker.com/)
[![Engine Status](https://img.shields.io/badge/System_Verification-Passing-brightgreen.svg)](#-ユニットテスト検証ステータス)

### 物理数学による数理解析で会社の帳簿のような様々な「やりとりのデータ」を可視化する

Tensor-Link Utility (TLU) 技術デキュメント・ポータルへお越しいただきありがとうございます。
TLUが導き出した数理的・物理的帰結は：
**「会計帳簿（B/SやP/L）の上でどれほど仮装取引や粉飾を施そうとも、『質量保存の法則（貸借一致の原則）』や『熱力学の法則』といった普遍的な物理法則を欺くことは不可能である」**という点にあります。

TLUは、複式簿記、都市交通フロー、株式市場取引、および脳神経機能（fMRI）といった一見すると全く異なるドメインの、時系列トランザクション・データを、**質量・ばね・ダンパーで構成される連続弾性体（弾性ネットワーク）**を流れる「力の流れ」として再定義し、システム内に潜む病的異常（横領、循環取引、デッド・ロック、相場操縦、脳梗塞、てんかんなど）を**客観的な物理署名（シグネチャ）**（剛性の崩壊、病的共鳴、熱的異常、相関異常など）として可視化するメタ検査プラットフォームです。

物理数学エンジンが出力した数理解析の指標は、TLUをいっしょに使う AI エージェントによって、[`LLM_Diagnostic_Manual.md`](LLM_Diagnostic_Manual.md) に準拠して解読され、人間の監査人や専門家が直感的に理解できる客観的な「臨床検査カルテ」へと翻訳されます。

---

## 📚 ドキュメント構成 (Documentation Map)

再現性を担保し、AIのハルシネーションや人間の認知バイアスを排除するため、TLUは厳格に整理された構成になっています。すべてのドキュメントは `docs/` 直下に **5つのコアファイル**に集約されています。以下は、英語版と日本語版の統合マッピングです：

| # | ドキュメントタイトル（英語版） | 対応する日本語版（日本語推奨） | コアコンテンツと見どころ |
| :---: | :--- | :--- | :--- |
| **1** | **[📂 01. Physics-Mathematics Engine Theory & Interpretation Guide](../01_Physics_Mathematics_Engine_Theory_and_Interpretation.md)** | **[01. 物理・数理エンジン基礎理論と解釈ガイド](01_Physics_Mathematics_Engine_Theory_and_Interpretation.md)** | TLUの主要8コアモジュール（$F = U - TS$, $K$, $\rho$など）の数学的・物理的基礎と、3D相空間挙動プロットの解釈マニュアル。 |
| **2** | **[📂 02. System Architecture & Operations Guide](../02_System_Architecture_and_Operations.md)** | **[02. システム構造定義とパイプライン運用ガイド](02_System_Architecture_and_Operations.md)** | パイプライン・コンテナ運用、HSLテーマ可視化エンジン、病的ダミーデータ生成器、およびLQR介入フィードバック制御シミュレーションモデル。 |
| **3** | **[📂 03. Market Forensics & Compliance Rules](../03_Market_Forensics_Rules.md)** | **[03. 市場フォレンジック・監査ルール定義](03_Market_Forensics_Rules.md)** | ミリ秒単位の注文簿（オーダーブック）力学、ボット循環取引、二部グラフ投影 vs ユーザー間直接送金トポロジーによる共謀ネットワーク監査。 |
| **4** | **[📂 LLM Diagnostic Manual (Supreme prompt)](../LLM_Diagnostic_Manual.md)** | **[LLM臨床検査マニュアル (Supreme Prompt)](LLM_Diagnostic_Manual.md)** | 物理数学エンジンの数値からAIが客観的なカルテを自動生成するためのプロトコル。統計的偽陽性判定と、原本データへのファクトチェック義務化。 |
| **5** | **[📂 Verified Sample Registry & Catalog](../samples/README.md)** | **[検証サンプル比較・メタ検査総合カタログ](samples/README.md)** | TLUに実装されている全10種類の検証サンプルの判定判定、物理数学パラメータ限界値、およびLQR介入治療ガイド。 |

---

## ⚕️ コアパラダイム：物理的媒体としてのネットワーク力学

TLUは、トランザクション・データを単なる数値の羅列ではなく、**質量／ばね／ダンパーで連結された連続弾性体ネットワーク**としてモデル化します。

![ばね／質量／ダンパー・モデル](../readme_plots/Mass-Spring-Damper-Model.jpg)
*図1: たとえば会計上の帳簿を、物理的なばね／質量／ダンパー・システムに見立てる概念図*

### 東洋医学（漢方・気血水）の臨床メタファー

多数の複雑な物理数学パラメータを実務家が直感的に理解できるよう、TLUは東洋医学の語彙を用いて、システムを **「気血水」**（資金や活動のめぐり）が流れる **「経絡」** （取引経路）として検査します。血流が滞って血栓が生じている箇所（剛性の硬化・デッドロック）や、大出血を起こしている箇所（質量欠損・横領）を特定し、 **線形2次レギュレータ（LQR）の最適制御理論** を用いて、最も効果的に気血のめぐりを回復できる治療の急所 **「経穴（ツボ）」** を示唆します。

### 各ドメインから物理空間へのマッピング一覧

| 物理変数 | 古典力学・熱力学の定義 | 財務会計ドメイン | 都市交通ドメイン | 株式市場ドメイン | 生体脳神経 (fMRI) ドメイン |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **質量 ($m_i$)** | 慣性 / エネルギー貯蔵タンク | 勘定残高 | 交差点内の滞留車両数 | 口座保有資本金 | BOLD活性信号密度 |
| **流量 ($f_{ij}$)** | 速度 / 質量移動 | 仕訳取引金額 | 通過車両数（台/秒） | 約定資金・株式移動 | 神経間信号フラックス |
| **剛性 ($k_{ij}$)** | 弾性 / ばね定数 | 取引関係の固着度 | 道路の設計流入容量 | 注文対当の同期度 | 機能的コヒーレンス結合度 |
| **粘性 ($c_{ij}$)** | 摩擦 / ダンパー制動 | 回収遅延・滞留期間 | 渋滞抵抗度 | 約定レイテンシ・スリッページ | 信号伝播の伝達遅延 |
| **エントロピー ($S$)** | 無秩序度 / 摩擦熱損失 | 架空循環取引（売上水増し） | 速度分散（渋滞熱の発生） | ボット間の仮装対当取引 | 病的な神経過同期 (convulsion) |
| **自由エネルギー ($F$)** | 有効仕事ポテンシャル | 税引前純営業利益 | 航空車両の流動ポテンシャル | 市場の真の配分効率 | 脳の認知・情報処理キャパ |
| **治療点 (LQR)** | 制御入力ベクトル | 監査重点勘定科目の絞り込み | 信号サイクルフェーズ調整 | 操縦グループ口座の一時凍結 | 経頭蓋磁気刺激 (TMS) 焦点 |

---

## 🔬 4つの主要な物理署名 (Spatiotemporal Proofs)

TLUは、システム内に発生した病的アノマリーを検出するために **4つの物理シグネチャ** を抽出します。これらは、帳簿の偽装操作をすり抜ける客観的な指標です。

### 1. マクロ・フォレンジック (質量保存則とキルヒホッフの法則)

システム全体の資金流入と流出に「簿外の消失や生成（残差）」がないかを検証します。資金が簿外へ隠蔽されると、質量保存則が破綻し、フォレンジック残差プロットに巨大なスパイクが立ち上がります。

* **🟢 健常状態 (Sample 0):** システム保存残差（残差）は全期間を通じて `0.00`（誤差ゼロ）を維持し、資金の簿外リークがないことを物理的に証明します。
* **🚨 質量欠損状態 (Sample 2 / 横領):** 売掛金の回収資金が現預金口座にデポジットされず、簿外の隠蔽ノードへバイパスされています。質量保存則が崩壊し、横領の発生と同時に強力なマイナス・スパイクを検知します。

| 健常 steady-state (Sample 0) | 病的質量欠損 (Sample 2) |
| :---: | :---: |
| ![Macro Forensics Normal](../../samples/Sample_0_Healthy/readme_plots/002_2_1__macro_forensics_dashboard.png) | ![Macro Forensics Abnormal](../../samples/Sample_2_Embezzlement_Leak/readme_plots/002_2_1__macro_forensics_dashboard.png) |
| *図2a:（上段）質量保存の維持 (残差 = 0)* | *図2b:（上段）資金横領に伴う巨大なマイナス・スパイクの検知* |

---

### 2. トポロジーとシステム安定度 (スペクトル半径 $\rho$)

接続行列の最大固有値である「スペクトル半径」を計算し、ネットワーク内に閉じた還流閉路（自己循環）が形成されているかを検証します。スペクトル半径がオレンジ色の警報ライン `1.00` に達した場合、システムが自己循環にロックされ暴走していることを数学的に実証します。

* **🟢 健常状態 (Sample 0):** スペクトル半径は全期間を通じて `0.00` 付近に留まり、取引が循環せず正常に代謝・収束していることを示します。
* **🚨 還流固着状態 (Sample 4 / 複合アノマリー):** 架空売上の循環取引により、スペクトル半径が数学的限界境界である `1.00`（ペロン・フロベニウスの定理に基づく飽和点）に固着し、虚構ループが形成されていることを証明します。

| 健常 steady-state (Sample 0) | 病的還流ループ (Sample 4) |
| :---: | :---: |
| ![System Stability Normal](../../samples/Sample_0_Healthy/readme_plots/004_1_2__system_stability.png) | ![System Stability Abnormal](../../samples/Sample_4_Composite_Chaos/readme_plots/004_1_2__system_stability.png) |
| *図3a: 安全圏で収束するスペクトル半径* | *図3b: 限界境界 1.00 に近づくスペクトル半径* |

---

### 3. 熱力学エネルギー積層 (組織の疲弊と熱的死)

システムが持っている有効仕事能力である「自由エネルギー（$F = U - TS$）」を計算します。自由エネルギー（白色レイヤー）がゼロを下回ってマイナス領域に沈むと、システムは**「熱的死 (Heat Death)」**に至ります。これは、活動（内部エネルギー $U$）を行えば行うほど、無駄な還流摩擦熱（エントロピー $TS$）を排出し、組織を疲弊させる病的状態を意味します。

* **🟢 健常状態 (Sample 0):** 自由エネルギーが常にプラスの領域で推移し、活動に比例して余力（貯留エネルギー）が増大する健全な代謝プロセスを示します。
* **🚨 熱的死状態 (Sample 8 / fMRI):** fMRIの計測により、脳の活動（内部エネルギー $U$）が極めて高いにもかかわらず、脳循環の応答が遅れる（エントロピー $S$ 増大）ために、有効仕事能力 $F$ がゼロに近づいてゆく状態を暴き出します。

| 健常 steady-state (Sample 0) | 病的熱的死 (Sample 8) |
| :---: | :---: |
| ![Thermodynamics Normal](../../samples/Sample_0_Healthy/readme_plots/001_1_2__thermodynamics_energy_stack.png) | ![Thermodynamics Abnormal](../../samples/Sample_8_fMRI_Stroke/readme_plots/001_1_2__thermodynamics_energy_stack.png) |
| *図4a: 自由エネルギーの健全な蓄積* | *図4b: 自由エネルギーがゼロへと沈没してゆく熱的死状態* |

---

### 4. 3D空間幾何学歪み (KL Drift と局所温度)

各ノードの確率分布の幾何学的歪みを、3D空間上の多様体（マニホールド）としてモデル化します。特定の交差点での局所的デッドロック、特定のbotアカウントによる共謀取引、あるいは脳卒中（血流途絶）などの異常が発生すると、平坦な空間に鋭い黄緑色の「針状のタワー」がそびえ立ちます。

* **🟢 健常状態 (Sample 0):** 初期ステップ $T=0$ 付近での統計の不安定性（データ不足による端点効果「Edge Effect」）を除き、その後は穏やかなブルーの波が広がる安定した幾何空間（最大値でも10程度）を維持します。
* **🚨 幾何学的変異状態 (Sample 5 / 交通デッドロック):** 交差点 `23_四条烏丸` の封鎖によって確率分布が崩壊した瞬間、その時空間座標を正確に貫く鋭利な幾何学歪みの尖塔（数値にして600,000に達するほどの高さ）が屹立します。

| 健常 steady-state (Sample 0) | 病的時空間歪み (Sample 5) |
| :---: | :---: |
| ![3D Space Normal](../../samples/Sample_0_Healthy/readme_plots/002_2_2_2__3d_micro_z_score_X.png) | ![3D Space Abnormal](../../samples/Sample_5_Kyoto_Traffic/readme_plots/002_2_2_2__3d_micro_z_score_X.png) |
| *図5a: 平坦で平穏な幾何学的多様体* | *図5b: 局所異常の座標と発生時刻を正確に示す幾何学的歪みの尖塔* |

---

## 📂 10種類の検証用ケーススタディ

TLUには、物理数学エンジンのクロスドメインな検査精度を実証するため、社会科学（金融・インフラ）からライフサイエンス（脳科学）にまたがる **10のサンプルデータセット**がパッケージ化されています。

| ID | 検証サンプル事例名（個別レポートリンク） | ドメイン | 検査判定 | 数理パラメータ特性 | 東洋医学メタファー |
| :---: | :--- | :---: | :---: | :---: | :--- |
| **0** | **[🟢 正常定常代謝 (Healthy)](samples/Sample_0_Healthy/README.md)** | 金融 | **NORMAL (正常)** | $\rho = 0.00$, 残差 = $0.00$ | 気血和平、経絡疎通、健全対流 |
| **1** | **[🟡 循環取引 (Wash Trade)](samples/Sample_1_Wash_Trade/README.md)** | 金融 | **HIGH (架空還流)** | $\rho = 0.75$, 自由エネルギー枯渇 | 気血空転、還流閉路、無実の虚熱 |
| **2** | **[🔴 資金横領 (Embezzlement Leak)](samples/Sample_2_Embezzlement_Leak/README.md)** | 金融 | **CRITICAL (横領)** | 最大残差 = $364.53$, 終期共鳴 | 経絡大出血、質量欠損、気血漏洩 |
| **3** | **[🟡 単純記帳ミス (Unbalanced Mistake)](samples/Sample_3_Unbalanced_Mistake/README.md)** | 金融 | **WARNING (記帳ミス)** | 一時的な残差およびKL幾何タワー | 気血局部不均衡、経絡捻挫、自己治癒 |
| **4** | **[🔴 複合的崩壊 (Composite Chaos)](samples/Sample_4_Composite_Chaos/README.md)** | 金融 | **CRITICAL (複合崩壊)** | $\rho = 0.79$, 最大残差 = $4,773.57$ | 気血双亡、還流虚脱、熱的機能麻痺 |
| **5** | **[🔴 京都都市交通 (Kyoto Traffic)](samples/Sample_5_Kyoto_Traffic/README.md)** | 交通 | **CRITICAL (デッドロック)** | $\rho = 1.00$, 局所温度 $T = 547.06$ | 経絡閉塞、気滞血瘀、対流停止 |
| **6** | **[🟡 相場操縦における銘柄と株主の相互関係の二部グラフ (Market Bipartite)](samples/Sample_6_Market_Bipartite_Weekly/README.md)** | 株式市場 | **HIGH (仮装約定)** | $\rho = 1.00$, PC1説明比率 = $99.67\%$ | 市場経絡還流、相場脈操縦、虚偽共鳴 |
| **7** | **[🟡 相場操縦における株主間関係のみの一部グラフ (Market Users)](samples/Sample_7_Market_Users_Weekly/README.md)** | 株式市場 | **HIGH (共謀集団)** | 自由エネルギー偏歪度 = $-2.72$ | 共謀結託結節、暗流還流、偏在うっ血 |
| **8** | **[🔴 脳梗塞発症時を模した fMRI (fMRI Stroke)](samples/Sample_8_fMRI_Stroke/README.md)** | 脳機能 | **CRITICAL (血流途絶)** | 流入経路95%遮断、結合剛性固着 | 脳経絡閉塞、局所気血枯渇、組織壊死 |
| **9** | **[🔴 てんかん発症時を模した fMRI (fMRI Seizure)](samples/Sample_9_fMRI_Seizure/README.md)** | 脳機能 | **CRITICAL (異常共振)** | $\rho = 1.00$, エントロピー垂直落下 | 脳経絡過同期、気血暴走、アトラクター固着 |

---

## ⚕️ 最適制御理論（LQR）による動的治療アプローチ

TLUは、対象システムの異常を検知するだけでなく、ネットワークの状態空間モデルから、**LQR (線形2次レギュレータ)** を用いて、システムを健常な定常軌道へ引き戻すための最適介入点 **「ツボ」（介入感度が高く、コントロール効果が波及しやすいポイント）** を特定・示唆します。

* **金融市場 (Sample 7):** 相場操縦（仮装還流）のハブである `03_USR_004` や `04_USR_005` を特定し、共謀還流ループを破砕するために「執行遅延」や「取引枠制限」をどの程度の力加減で施すべきかという、外部システム（マッチングエンジン等）による介入ポリシーの明確な数理的根拠を提示します。
    ![LQRによる治療ポイントの示唆](../../samples/Sample_7_Market_Users_Weekly/readme_plots/004_1_3__control_lqr_performance_space.png)
* **脳神経科学 (Sample 9):** てんかんの病的同期の震源である側頭葉（`03_Temporal_Lobe`）をピンポイントの治療標的として浮き彫りにし、経頭蓋磁気刺激（TMS）などで「逆位相ノイズ」の注入で病的同期の打消しを効果的に施すための対象部位を提示します。
    ![LQRによる治療ポイントの示唆](../../samples/Sample_9_fMRI_Seizure/readme_plots/004_1_3__control_lqr_performance_space.png)

---

## 🚀 実行環境とクイックスタート (Docker)

TLUは、 stateless な Docker コンテナと TDD（テスト駆動開発）アプローチを採用しており、開発者のローカル環境やヒューマンエラーによるデータ解釈のゆらぎを100%排除します。

#### 準備：独自データの解析要件

あなた自身のデータを TLU で解析するには、`workspace/` ディレクトリに以下の2つのCSVファイルを配置してください。

1. **取引流量データ (`workspace/input_stream/`)**: 時系列トランザクションCSV。たとえば `Trans_Date` (発生日), `Account_Name` (勘定/ノード名), `Debit` (流入額), `Credit` (流出額) のカラムが必須。workspace/config/_set_params.csv で、それら4種のカラムを別途指定。数理解析にかける。
2. **勘定マッピング辞書 (`workspace/config/_account_mapping.csv`)**: 独自のアカウント名をTLUのB/S, P/Lカテゴリ（Asset, Liability, Revenue等）へマッピングするための定義ファイル。

#### 自動シミュレーションパイプライン実行手順

```bash
# 1. リポジトリをクローン
git clone https://github.com/renpoo/TLU.git
cd TLU

# 2. Docker コンテナを起動
docker compose up -d

# 3. パイプラインを実行 (Sample 1: 循環取引のシミュレーション例)
# * 解析ターゲットは samples/ 以下の任意のディレクトリに変更可能
bash bin/batch_processing.sh --target_env "samples/Sample_1_Wash_Trade"
bash bin/batch_visualize_graphs.sh --target_env "samples/Sample_1_Wash_Trade"

# 4. 生成された AI 自動カルテ（検査レポート）を確認
cat workspace/output_data/_99_diagnosis_report.md
```

---

## ⚠️ 反証可能性と臨床モデルの限界

TLUは、「この時空間ノードでキルヒホッフの質量保存則が $X$ だけ破綻している」「ネットワークのスペクトル半径が境界値 1.0 に固着した」といった、 **物理数学的な客観的事実のみを出力する「証拠提示計算機（Evidence Generator）」** にすぎません。

そのアノマリーの背後にある法的・道徳的意図が「意図的な犯罪（横領・粉飾・市場操縦）」なのか、あるいは「単なる入力ミスや正当な業務取引」なのかの最終判断（反証分析）は、TLUやAIの役割ではありません。算出された物理数学的指標と幾何学座標（日付、勘定科目など）を手がかりに、人間のプロの経理担当者や、監査人、臨床医が、現実世界の原本データ（銀行口座残高証明書の原本、取引所の生ログ原本、脳組織の生検結果など）と突き合わせて行う実地調査こそが、検査を確定させる最終決定要素となります。

---

**ライセンス**: AGPL-3.0  
**開発者**: Renpoo & Google DeepMind Agent (Antigravity)
