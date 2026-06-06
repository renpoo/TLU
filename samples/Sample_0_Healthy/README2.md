# Sample 0 (Healthy): 中小企業簿記・健康モデル ダミーデータ解説

本サンプル（Sample 0）は、健全に稼働している中小企業（SME）の取引ネットワークを模擬した複式簿記データです。

---

## 1. 生成スクリプトとパラメータ
* **使用スクリプト**: [`src/filters/_0_0_generate_dummy_journal.py`](file:///Users/renpoo/Documents/GitHub/TLU/src/filters/_0_0_generate_dummy_journal.py)
* **実行コマンド例**:
  ```bash
  python src/filters/_0_0_generate_dummy_journal.py --months 12 --seed 42 --out-initial-state samples/Sample_0_Healthy/ephemeral/_initial_state.csv > samples/Sample_0_Healthy/input_stream/Dummy_Journal_Stream.csv
  ```
* **アノマリーパラメータ**:
  * `--sales-leak-prob`: `0.0` (売掛金回収のリークなし)
  * `--purchase-leak-prob`: `0.0` (買掛金支払のリークなし)
  * `--wash-trade-prob`: `0.0` (架空売上・還流なし)
  * `--unbalanced-mistake-prob`: `0.0` (記帳ミスなし)

---

## 2. 物理・会計ダイナミクスと質量保存則

本ジェネレータは、簿記の二面性（Debit/Credit）を質量保存の法則としてモデリングしています。

### A. 初期状態 (Day 0)
システムの初期質量（資産と自己資本）は、以下のようにバランスした状態で投入されます：
* **資産（Assets / Dr）**: 
  * `Cash` (現金): 500,000.00
  * `Inventory` (在庫): 500,000.00
* **純資産（Equity / Cr）**:
  * `Equity_Capital` (自己資本): 1,000,000.00

開始時点で 資産 100万円 ＝ 純資産 100万円 が成立しており、システム全体の「初期質量」は 100万円 と定義されます。

### B. ローカル質量保存の強制 (Mass Conservation)
取引の実行時、アセットノード（`Cash`、`Accounts_Receivable`、`Inventory`）からの流出が発生する場合、現在の残高を超えてお金を支払ったり、在庫を払い出したりすることはできません。
スクリプト内の `attempt_entry` 関数は、流出量が利用可能な質量（残高）を超える場合、取引額を残高上限まで自動的に削減し、マイナスバランスを防止します。

---

## 3. シミュレートされる取引サイクル (Causal Chain)

本データは、時間経過に伴う因果関係をイベントキューに登録し、タイムラグを持たせて回収・決済を行うことで、流動性の「粘性」を表現しています。

1. **売上と原価のサイクル (Sales & COGS)**:
   * 季節変動ウェーブ（サイン波）に基づいて日々の売上が発生。
   * 売上と同時に `Accounts_Receivable` (売掛金) と `Sales_Revenue` (売上高) が計上され、同時に売上高の $40\% \sim 70\%$ が `Inventory` (在庫) から `COGS` (売上原価) へと振り替えられます。
2. **売掛金の回収 (Viscosity / 粘性)**:
   * 売上発生から $30 \sim 90$ 日後に、売掛金が回収され、`Cash`（現金）に変わるイベントが実行されます。このタイムラグ（遅延）がシステムの「粘性（Viscosity）」を決定します。
3. **在庫の補充と決済 (Purchase & AP)**:
   * 7日ごとに定期的に `Inventory` を購入し、`Accounts_Payable` (買掛金) を計上。
   * 購入から $30 \sim 90$ 日後に現金で買掛金を支払います。
4. **毎月の固定費 (Rent & Payroll)**:
   * 毎月25日に、`Payroll_Exp` (給与費) および `Rent_Exp` (地代家賃) が `Cash` から支払われます。

---

## 4. 本サンプルの特徴と限界

* **特徴 (Healthy)**:
  * 意図的な資金リーク（横領）や還流取引（架空売上）、人間の転記ミスが一切ないため、仕訳の貸借（Debit/Credit）は常に $1:1$ で完璧に一致しています。
  * 財務諸表ジェネレータで解析すると、全期間を通じて不一致額が $0.00$（`✅ BALANCED`）になります。
* **モデルの限界**:
  * 企業活動を維持するための固定費（人件費や家賃）の支払いが営業キャッシュフロー（売掛金の回収）を上回って赤字が累積すると、内部の `Cash` が枯渇し、取引がスケールダウンして自動停止します。
