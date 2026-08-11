# ルールセット統合索引（草案・Gemini査読待ち）

**作成**: Claude (Cowork, 独立監査ロール) — 2026-08-10
**ステータス**: **DRAFT。** Geminiの査読と蓮風さんの承認を経るまで確定版として扱わないこと。
**対象**: `rulesets/` 配下17文書 ＋ `new-rulesets/` 配下8文書 ＝ **計25文書**

---

## 0. なぜこの文書が必要か

2026-08-07〜09の監査で、Claudeは `new-rulesets/` に8本の文書を追加した。
しかし**既存13本（＋`TLU Specific Constraints/`の4本）との関係を一度も整理しなかった。**

結果として、いま Gemini が置かれている状況はこうである。

- `rulesets/CLAUDE.md` はセッション開始時に `TLU_Meta_Procedure_Manual.md` を読めと指示するが、
  そのどちらも `new-rulesets/` の存在を知らない。
- `new-rulesets/role_definition.Consolidated_Epistemic_Engine.yaml` は既存3本を
  「今後はこちらを正とする」と宣言しているが、**その宣言を `rulesets/` 側から辿る経路がない。**
- どの文書がいつ適用されるのか、衝突したらどちらが優先なのか、全体像を示す文書がない。

つまり Gemini は「どれに従って動けばよいか」を自力で25文書から再構成しなければならない。
**これでは、監査結果を受け取ったあとの実装が始まらない。**

本文書は、その全体像を与えることを目的とする。**統合＝1本に融合すること**ではなく、
**統合＝どれをいつ読み、衝突時にどちらが勝つかが一意に決まること**、と定義する。
既存文書を破棄・改変しないのは、それらが蓮風さんとGeminiの資産であり、
Claudeが単独で判断してよい領域ではないためである（メタ空間の原則）。

---

## 1. 全25文書の分類

責務の性質で5層に分ける。この分類自体が査読対象である。

### 層1: 入口（セッション開始時に必ず読む）

| 文書 | 所在 | 役割 |
|---|---|---|
| `CLAUDE.md` | rulesets/ | LLMの一般的な振る舞い規範。冒頭でメタ手順書を読めと指示 |
| `TLU_Meta_Procedure_Manual.md` | rulesets/ | TLU固有の設計思想・起動チェックリスト・過去のAI失敗の教訓 |
| **`RULESET_INTEGRATION_INDEX.md`** | new-rulesets/ | **本文書。層1に追加すべき（後述の提案A）** |

### 層2: 思考エンジン（どう考えるか）

| 文書 | 所在 | 状態 |
|---|---|---|
| `role_definition.Consolidated_Epistemic_Engine.yaml` | new-rulesets/ | **正**。下3本を統合したもの |
| `role_definition.Recursive Thinker.v.2.0.yaml` | rulesets/ | 統合済み。履歴として残置 |
| `role_definition.Universal Polymath As Integrated Magus.yaml` | rulesets/ | 統合済み。履歴として残置 |
| `rule_definition.Hyper Integrated Epistemic Engine.yaml` | rulesets/ | 統合済み。履歴として残置 |
| `role_definition.HADCT Thinking Protocol.yaml` | rulesets/ | **現役。統合対象外**（理由は後述の論点1） |
| `meta_cognitive_ruleset.ArticulatedLogicalThinking.yaml` | rulesets/ | 現役。Attention分散の抑制と文脈境界の維持 |

### 層3: 適用範囲の制御（いつ重装備を使うか）

| 文書 | 所在 | 役割 |
|---|---|---|
| `protocol_scope_amendment.yaml` | new-rulesets/ | 重量級プロトコル（5層再帰＋認知状態ダンプ）の発動条件を限定 |
| `rule_definition.Unified_Output_Format_Master.yaml` | rulesets/ | 出力形式の統一。上記により発動範囲が制限される |
| `priority_rebalancing.yaml` | new-rulesets/ | GUI品質基準への過剰投資を抑制し、数理検証を優先 |

### 層4: 実装・運用の規律（どう手を動かすか）

| 文書 | 所在 | 役割 |
|---|---|---|
| `coding-refactoring-rules.yaml` | rulesets/ | パラダイム・デザインパターン・リファクタリング技法 |
| `tlu_development_meta_guidelines.yaml` | rulesets/TLU Specific Constraints/ | Unix哲学に基づく層分離（orchestration/math/presentation） |
| `tlu_architecture_blast_radius.yaml` | rulesets/TLU Specific Constraints/ | 変更時の波及範囲マップ。修正前に全件スキャン必須 |
| `tlu_dependency_map.yaml` | rulesets/TLU Specific Constraints/ | 依存関係の詳細（23KB） |
| `silent_workaround_prevention_protocol.yaml` | new-rulesets/ | 意図的な当座しのぎの記録義務 |
| `precommit_enforcement_protocol.yaml` | new-rulesets/ | 開発支援ツールのpre-commit強制配線 |
| `regression_history_ledger_protocol.yaml` | new-rulesets/ | 検証結果の追記専用台帳（journal.jsonl） |

### 層5: 検査・記述（何を確かめ、どう書くか）

| 文書 | 所在 | 役割 |
|---|---|---|
| `audit_criteria_checklist.yaml` | new-rulesets/ | 監査基準。カテゴリA〜E、19項目 |
| `tlu_technical_writing_protocol.yaml` | rulesets/TLU Specific Constraints/ | ミント・ピラミッド原則等 |
| `AI_GUI_Debugging_Profiling_Protocol.md` | rulesets/ | GUI（App-3向け）のデバッグ手順 |
| `XP_Autonomous_3in1_Role_Protocol.md` | rulesets/ | 一人三役XP開発プロトコル（App-4向け） |

### 層外: ルールセットではないもの

| 文書 | 所在 | 実態 |
|---|---|---|
| `memo_development_process.md` | rulesets/ | 開発記録（38KB）。規則ではなく**ログ**。参照専用 |
| `CLAUDE_AUDIT_HANDOFF.md` | new-rulesets/ | 一回性の引き継ぎ文書。**規則ではない**（提案B参照） |

---

## 2. 適用順序（Geminiがセッション開始時にすべきこと）

```
1. rulesets/CLAUDE.md                                 ← 一般規範
2. rulesets/TLU_Meta_Procedure_Manual.md              ← TLU固有・起動チェックリスト
3. new-rulesets/RULESET_INTEGRATION_INDEX.md（本文書）  ← 全体像と優先順位
4. new-rulesets/protocol_scope_amendment.yaml         ← いま重装備が要るかの判定
5. 作業内容に応じて層4・層5から必要なものを選ぶ
```

`rulesets/TLU_Meta_Procedure_Manual.md` の「6. Startup Checklist for New Sessions」に
本文書への参照を1行足すことを提案する（後述の提案A）。

---

## 3. 衝突時の優先順位（提案）

以下は**Claudeの提案であり、確定ではない**。査読対象。

1. **蓮風さん（アーキテクト）の直接の指示**が最優先。
2. **`new-rulesets/` が `rulesets/` に優先する**（新しい方が監査を経ているため）。
   ただし後述の未解決論点に該当する場合を除く。
3. **適用範囲の制御（層3）が、思考エンジン（層2）に優先する。**
   `protocol_scope_amendment.yaml` が「重装備不要」と判定した場合、
   `Consolidated_Epistemic_Engine` の5層再帰は発動しない。
4. **TLU固有の制約（`TLU Specific Constraints/`）が、汎用ルール（`coding-refactoring-rules.yaml`）に優先する。**
   具体が抽象に勝つ。
5. 同層内で衝突した場合は、**解消せず両論を記録し、蓮風さんの判断を仰ぐ。**
   `CLAUDE_AUDIT_HANDOFF.md` 第6節の「不一致は雑音ではなく信号」の原則に従う。

---

## 4. 未解決の論点（Geminiと蓮風さんの判断が要る）

Claudeが単独で決めるべきでない、あるいは決められなかった事項。

### 論点1: HADCT を統合対象から外したのは妥当か

`Consolidated_Epistemic_Engine` は既存3本を統合したが、
`role_definition.HADCT Thinking Protocol.yaml` は対象外とした。

**Claudeの判断根拠**: HADCTは「Human-AI Distributed Critical Thinking」——
人間との対話を通じて思考を深化させる枠組みであり、他3本の「AI内部の推論構造」とは
目的が異なる。同じ「思考」を扱っていても層が違う、と見た。

**しかし確信はない。** 実際にHADCTのR10（安易な同意への警戒）は、他3本の
自己反証プロセスと重なる部分がある。統合すべきか、別立てのままか、判断を仰ぐ。

### 論点2: App-3向け／App-4向けプロトコルの現在の地位

`AI_GUI_Debugging_Profiling_Protocol.md` は TLU-App-3（Tauri v2 + React 18）向け、
`XP_Autonomous_3in1_Role_Protocol.md` は TLU-App-4 向けと明記されている。

しかし **App-4のReact GUI経路は現在凍結中**であり、Excel/Google Sheetsアドイン方式への
転換を検討している（`TLU-App-4/new-TLU-App-SDLs/packaging_strategy_open_decision.yaml`）。
`priority_rebalancing.yaml` も、これら2本の高すぎる品質基準を抑制する趣旨で書かれた。

**判断が要る**: この2本を「凍結中」として層5から一時的に外すべきか、
現状のまま残すべきか。アドイン方式に転換した場合、両者に代わる新しいプロトコルが要る。

### 論点3: `memo_development_process.md` の位置づけ

38KBあり、`rulesets/` 配下で最大。しかし内容は開発記録であって規則ではない。
`silent_workaround_prevention_protocol.yaml` rule_1 は、意図的な当座しのぎを
このファイルへ記録することを義務づけており、**規則の出力先**として機能している。

「規則」と「記録」が同じディレクトリに混在している状態は、
`sagyou-journal.md`（日常生活再発見の会）が journal と ruleset を分離したのと
対照的である。移動すべきか、現状維持か。

### 論点4: `new-rulesets/` という名前をいつまで使うか

「new-」という接頭辞は、監査中の暫定的な置き場であることを示すために付けた。
しかし実装が進み、これらが常用されるようになれば、「new」であり続けるのは不自然になる。

`rulesets/` へ統合するのか、`rulesets/v2/` のような形にするのか、
別ディレクトリのまま運用するのか。**ただし統合の前に、
`new-TLU-SDLs/` について指摘したのと同じ注意が必要**——
実装が伴っていない規則を正式なルールセットへ昇格させると、
「守られていない規則」が増えるだけになる。

---

## 5. Claudeからの提案

### 提案A: `TLU_Meta_Procedure_Manual.md` の起動チェックリストに1行足す

現状、`rulesets/` 側から `new-rulesets/` へ辿る経路が一切ない。
これが今回の問題の根本である。`TLU_Meta_Procedure_Manual.md` の
「6. Startup Checklist for New Sessions」に、本文書への参照を追加することを提案する。

**ただしこれは `rulesets/` の改変にあたるため、Claudeは実行しない。**
蓮風さんの承認、またはGeminiの手による実施を求める。

### 提案B: `CLAUDE_AUDIT_HANDOFF.md` を `new-rulesets/` から出す

これは規則ではなく、一回性の引き継ぎ文書である。ルールセットのディレクトリに
置いていること自体が分類の誤り（`audit_criteria_checklist.yaml` A3
「名前と実体の対応」に自分で抵触している）。

リポジトリルート、または `docs/` 相当の場所へ移すことを提案する。

### 提案C: 層4・層5の新規4本は、実装が伴うまで「提案」と明示する

`silent_workaround_prevention_protocol.yaml`、`precommit_enforcement_protocol.yaml`、
`regression_history_ledger_protocol.yaml`、`audit_criteria_checklist.yaml` は、
いずれも**まだ一度も実運用されていない。**
`.pre-commit-config.yaml` も `regression_history/journal.jsonl` も存在しない。

これらを「正式なルール」として提示すると、
`AUDIT_REPORT.md` §5 で指摘した「反省ログに書いたが実行されなかった」パターンを
Claude自身が繰り返すことになる。各ファイル冒頭に運用開始状況を明記すべきである。

---

## 6. Geminiへの査読依頼

以下について、賛成・反対いずれでも根拠を添えて返してほしい。
不一致は解消せず、そのまま記録する（`CLAUDE_AUDIT_HANDOFF.md` 第6節）。

- **R1**: 第1節の5層分類は妥当か。責務の切り方として不自然な箇所はないか。
- **R2**: 第3節の優先順位（特に「新が旧に優先」「具体が抽象に優先」）は運用可能か。
  実装中に判断に迷う具体的なケースが想像できるか。
- **R3**: 論点1（HADCTを統合対象から外した判断）について、どう考えるか。
- **R4**: 論点2（App-3/App-4向けプロトコルの地位）について、
  実装当事者としての見解を聞きたい。
- **R5**: **最も重要**。この索引には、**Geminiが実際に参照している文書のうち、
  ここに載っていないものはないか。** Claudeは `rulesets/` と `new-rulesets/` しか
  見ていない。Geminiが日常的に参照している別の文書・慣行・暗黙の取り決めが
  あるなら、それこそがこの索引の最大の欠落である。

---

## 7. 規範の状態区分(2026-08-11 新設)

### なぜ必要か

蓮風さんの指摘。

> あなたたちそれぞれが新規スレッドであたらしく動作を開始するときの制約条件が
> `rulesets/` である場合、その挙動は古い制約条件に縛られる、つまりゆるゆるでは。

**その通りである。** 2026-08-07〜11の監査で導入した規律
(E1/E2/E3、A6/A7、D1の格上げ、【照会】、要約規約、命名規約)は
**すべて `new-rulesets/` にあり、そこは「草案」と明記されている。**
したがって「まず `rulesets/` を読め」と指示された新セッションは、
**監査以前のゆるい規範の下で動く。**

**さらに悪いことに、現在「有効な規範」はファイルではなく蓮風さんのプロンプトの中にある。**
Geminiの返信は命名規約にも確度ラベルにも従っていたが、
**それは蓮風さんが伝えたからであって、文書が効いていたからではない。**
規律であって構造ではない — 本監査が繰り返し潰してきた形が、
**規範それ自体の適用のところに残っていた。**

そして**締まった輪がある。** `new-rulesets/` が草案なのはGeminiの査読待ちだからだが、
**査読する側は何らかの規範の下で動く必要がある。**
それが旧規範なら、**査読そのものが旧規律の下で書かれる。**

### 診断: 状態ラベルが二値であること

現状は「**確定**」か「**草案**」しかない。
そのため **「査読なしで承認する」か「何も適用しない」かの二択**になる。**中間がない。**

### 三段階へ拡張する

| 状態 | 意味 | 従うか |
|---|---|---|
| **確定** | 査読・承認済み | **従う** |
| **暫定適用** | いま従う。**ただし査読で覆りうる** | **従う** |
| **草案** | まだ従わない。検討中 | 従わない |

**「暫定適用」の運用条件:**

1. **適用中の版を出力に記録する。**
   規範が変われば、前後の記録は同じ言葉でも同じ主張ではない
   (P14「チェックリストの自己改訂と版の記録」と同型)。
   文書の冒頭に **`準拠: audit_criteria_checklist v1.2.0(暫定適用)`** のように書く。
2. **期限を置く。** 期限までに査読が来なければ、**自動的に確定へ昇格するのではなく、
   草案へ戻す。** 暫定期限の暫定値は **2026-08-25**(蓮風さんが調整する)。
3. **覆すコストを低く保つ。** Geminiの「却下」一つで暫定適用は解除される。
   蓮風さんの裁定も同じ。

### この提案の危険(先に書く)

**「暫定適用」は、Claudeが起草した規則を査読前に有効化する仕組みである。**
「草案」という状態は、**まさにClaudeが単独で立法するのを防ぐため**にあった。
**Claudeはここで、自分の立法権を強める提案をしている。**

**だから第2項(期限つきで草案へ戻す)が必須である。**
これがないと「暫定」が既定で永続化する。
**まさにそうやって `rulesets/` が古びたはずである。**

### 2026-08-11 時点の状態

| 文書 | 状態 |
|---|---|
| `audit_criteria_checklist.yaml` v1.2.0 | **暫定適用**(Q1〜Q5 査読待ち) |
| `document_naming_convention.md` | **暫定適用**(N1〜N3。Geminiは既にファイル名で採用済み) |
| `session_summary_protocol.md` | **暫定適用**(S1〜S3) |
| `SAMPLES_REGENERATION_PROTOCOL.md` | **草案**(G1〜G4 未回答。**実行前に回答が要る**) |
| `GEMINI.md` | **草案**(未査読。設置も未) |
| `RULESET_INTEGRATION_INDEX.md`(本書) | **暫定適用**(R1〜R5) |
| `regression_history_ledger_protocol.yaml` schema_v2 | **草案**(D-2 の閾値が未合意) |

**`SAMPLES_REGENERATION_PROTOCOL.md` を草案のままにしたのは、
G4(Claudeが一版を書くか査読に徹するか)が未回答であり、
かつ R-1(三権分立の役割対応表)が係争中だからである。**
**役割の話が片付く前に手順を有効化すると、比喩が実務判断を先取りする。**

### 入口を繋ぐ

`rulesets/` の入口文書に、`new-rulesets/` への経路を1段落足す必要がある。
**Claudeはメタ空間を直接編集しないため、差し込み文面のみ用意した。**
`new-rulesets/PATCH_rulesets_entry_pointer.md` を参照。**適用は蓮風さんが行う。**

### 査読依頼(追加)

- **R6**: 三段階(確定 / 暫定適用 / 草案)は運用可能か。
  **とりわけ「期限までに査読が来なければ草案へ戻す」は、
  あなたの作業速度から見て現実的か。** 短すぎるなら言ってほしい。
- **R7**: **Claudeが自分の立法権を強める提案をしている**という自己申告について、
  他に付けるべき歯止めはあるか。

