# Sample 3 (Unbalanced Mistake): 中小企業簿記・記帳ミス不一致モデル ダミーデータ解説

本サンプル（Sample 3）は、人間が手動で仕訳を入力する際に入力ミスをしてしまい、借方と貸方の金額が一致しないまま登録されてしまった**「記帳ミス（Bookkeeping Mistake）」**を注入した取引データです。

---

## 1. 生成スクリプトとパラメータ
* **使用スクリプト**: [`src/filters/_0_0_generate_dummy_journal.py`](file:///Users/renpoo/Documents/GitHub/TLU/src/filters/_0_0_generate_dummy_journal.py)
* **アノマリーパラメータ**:
  * `--unbalanced-mistake-prob`: `0.10` (売掛金回収の記帳時に $10\%$ の確率で入力ミスが発生)
  * `--sales-leak-prob` / `--purchase-leak-prob` / `--wash-trade-prob`: `0.0`

---

## 2. アノマリー（記帳ミス）の生成ロジック

売掛金の回収イベント（AR Collection）が発生した際、借方（現金）と貸方（売掛金）の金額が不一致となるようにデータを生成します。

* **通常の仕訳**:
  * `Debit: Cash` (+1,500.00) / `Credit: Accounts_Receivable` (-1,500.00)
* **記帳ミス時の仕訳 (Unbalanced)**:
  * `Debit: Cash` (**$150.00 \sim 1350.00$ のランダムな額**) / `Credit: Accounts_Receivable` (-1,500.00)
  * **現象**: 売掛金は 1,500円 回収されて減少した（Credit）と正しく記録されましたが、借方の現金（Debit）には、タイポや入力漏れによって本来より少ない額（例: 桁を間違えて 150円）が入力されてしまいます。

---

## 3. 資金横領（Sample 2）との違いと特徴

* **数学的な違い**:
  * **Sample 2 (横領)**: 盗まれたお金が綺麗に「0.0」として記帳されるため、流出先が意図的かつ極端に遮断された状態になります。
  * **Sample 3 (ミス)**: Debit額が `amount * random.uniform(0.0, 0.9)` として生成されるため、端数や中途半端な金額の「ズレ」が多数発生します。
* **財務諸表（B/S）における影響**:
  貸借の差額は、前処理段階で不一致の調整用勘定として `UNKNOWN_LEAK`（費用 / Expense）に吸収されます。Sample 2 と同様に、素のデータだけでは B/S は `❌ UNBALANCED` となり、貸借対照表の左と右が一致しません。
* **フォールセンシクス（Forensics）における検出**:
  タイポや端数不一致によるノイズは、時系列データの中では不規則な「ホワイトノイズ」に誓い振る舞いを示します。これにより、意図的な横領（一定の周期や割合で抜かれる）と、人間のケアレスミス（ランダムな不一致）を、情報曲率（Information Curvature）やノイズのスペクトル解析（Fractal Noise）で識別することが可能になります。
