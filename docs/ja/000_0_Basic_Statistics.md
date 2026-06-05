# 000_0: 財務基礎状態と基本統計量 (Basic Statistics)

本ガイドは、Tensor-Link Utility (TLU) における統計分析モジュール（`000_0`）の各検証サンプルの出力と数値に基づく臨床解説をまとめたものです。

---

## 1. 貸借対照表（B/S）トレンド (`000_0_1__BS_Trend.png`)
資産および負債・資本の各項目の時系列推移を示したグラフです。資本の蓄積速度や流動性比率の動的変化を読み解くことができます。

#### 🟢 Sample 0 (正常代謝)
**臨床解説:**
資産（現預金、売掛金）と資本が対称的かつ滑らかに右肩上がりで成長しており、健全な自己資金調達が機能しています。
![Sample 0 BS Trend](../../samples/Sample_0_Healthy/output_plots/000_0_1__BS_Trend.png)

#### 🟡 Sample 1 (循環取引)
**臨床解説:**
売上水増しに伴い売掛金と現預金が交互に跳ね上がるように急増していますが、実物投資や経費支払いを伴わないため、B/S全体が人工的かつ無機質に肥大化しています。
![Sample 1 BS Trend](../../samples/Sample_1_Wash_Trade/output_plots/000_0_1__BS_Trend.png)

#### 🔴 Sample 2 (資金横領)
**臨床解説:**
流出アノマリーの進行により、手元の現金預金（質量）が右肩下がりで衰退しています。外部流出によって財務的な体力が枯渇している様子が分かります。
![Sample 2 BS Trend](../../samples/Sample_2_Embezzlement_Leak/output_plots/000_0_1__BS_Trend.png)

#### 🟡 Sample 3 (入力ミス)
**臨床解説:**
$t=1$（2020-02）の一時的な片面入力エラーにより、売掛金と現預金のバランスが崩れ、一時的に不自然な断絶が記録されています。
![Sample 3 BS Trend](../../samples/Sample_3_Unbalanced_Mistake/output_plots/000_0_1__BS_Trend.png)

#### 🔴 Sample 4 (複合アノマリー)
**臨床解説:**
架空売上の水増しによって売掛金は膨張していますが、現金横領が並行しているため手元現預金が全く蓄積されず、流動性の枯渇が進行しています。
![Sample 4 BS Trend](../../samples/Sample_4_Composite_Chaos/output_plots/000_0_1__BS_Trend.png)

#### 🔴 Sample 5 (京都交差点網)
**臨床解説:**
交通量における「車両数」を「B/S残高」に見立てた推移です。観光アノマリーの流入過多により、特定の主要交差点の滞留車両が急増している様子を示します。
![Sample 5 BS Trend](../../samples/Sample_5_Kyoto_Traffic/output_plots/000_0_1__BS_Trend.png)

#### 🟡 Sample 6 (株券流体システム)
**臨床解説:**
投資家口座と個別銘柄の資本保有高です。ボット間での超高頻度取引出来高が激増する一方で、参加口座全体の正味の資産は全く増えていません。
![Sample 6 BS Trend](../../samples/Sample_6_Market_Stock_Flow/output_plots/000_0_1__BS_Trend.png)

#### 🟡 Sample 7 (現金決済流体システム)
**臨床解説:**
直接送金関係にあるユーザー口座の残高推移です。特定のアカウントペア間で資金が往復しているだけで、外部からの資本純流入はありません。
![Sample 7 BS Trend](../../samples/Sample_7_Market_Cash_Flow/output_plots/000_0_1__BS_Trend.png)

#### 🔴 Sample 8 (fMRI 脳梗塞)
**臨床解説:**
脳領野의 BOLD蓄積（血液質量相当）です。TR=150（$t=30$）で運動野の血流供給が遮断され、蓄積が不連続に落下して低水準でフリーズしています。
![Sample 8 BS Trend](../../samples/Sample_8_fMRI_Stroke/output_plots/000_0_1__BS_Trend.png)

#### 🔴 Sample 9 (fMRI てんかん発作)
**臨床解説:**
てんかん時のBOLD信号量蓄積です。側頭葉を起点とする異常放電と同調し、全脳の領域で同一周期の激しい質量揺らぎが同期して発生しています。
![Sample 9 BS Trend](../../samples/Sample_9_fMRI_Seizure/output_plots/000_0_1__BS_Trend.png)

---

## 2. 損益計算書（P/L）トレンド (`000_0_1__PL_Trend.png`)
売上や費用、および純利益の動的変化を示すトレンド推移グラフです。

#### 🟢 Sample 0 (正常代謝)
**臨床解説:**
売上の増加に伴い費用が健全に連動しており、季節性の出来高変動を吸収しながら安定した期末純利益が創出されています。
![Sample 0 PL Trend](../../samples/Sample_0_Healthy/output_plots/000_0_1__PL_Trend.png)

#### 🟡 Sample 1 (循環取引)
**臨床解説:**
売上高が急激に右肩上がりに成長していますが、それに対応するはずの販売管理費や実体経費が完全に「平坦」であり、事業活動の実態と矛盾します。
![Sample 1 PL Trend](../../samples/Sample_1_Wash_Trade/output_plots/000_0_1__PL_Trend.png)

#### 🔴 Sample 2 (資金横領)
**臨床解説:**
帳簿上は期末純利益 `+$64,795.44` の黒字ですが、実際には回収された売掛金が簿外へ漏洩しているため、P/L上の利益数値は架空の虚像となっています。
![Sample 2 PL Trend](../../samples/Sample_2_Embezzlement_Leak/output_plots/000_0_1__PL_Trend.png)

#### 🟡 Sample 3 (入力ミス)
**臨床解説:**
片面入力エラーが発生した $t=1$ 前後に大きなノイズが生じていますが、最終的な純利益 `+$41,368.85` 自体は大きく歪まずに推移しています。
![Sample 3 PL Trend](../../samples/Sample_3_Unbalanced_Mistake/output_plots/000_0_1__PL_Trend.png)

#### 🔴 Sample 4 (複合アノマリー)
**臨床解説:**
売上・利益（純利益 `+$200,478.42`）が爆発的に急増しているように見えますが、これは激しい還流による「粉飾」と「横領」が裏で同時に進行しているためです。
![Sample 4 PL Trend](../../samples/Sample_4_Composite_Chaos/output_plots/000_0_1__PL_Trend.png)

#### 🔴 Sample 5 (京都交差点網)
**臨床解説:**
交通量ポテンシャルの累積収支（利益相当）です。アノマリー期（観光シーズン・事故）の渋滞発生後、ポテンシャルは一気に `-$2,500,000.00` へ崩壊しています。
![Sample 5 PL Trend](../../samples/Sample_5_Kyoto_Traffic/output_plots/000_0_1__PL_Trend.png)

#### 🟡 Sample 6 (株券流体システム)
**臨床解説:**
出来高（P/L相当）は異常急増し最大出来高 Z-Score は **`80.53`** に達しますが、投資家全体の正味の実現損益（実質利益）は `$0.00` で硬直しています。
![Sample 6 PL Trend](../../samples/Sample_6_Market_Stock_Flow/output_plots/000_0_1__PL_Trend.png)

#### 🟡 Sample 7 (現金決済流体システム)
**臨床解説:**
直接送金による出来高推移です。ボット口座間のキャッチボールにより見かけの出来高は激増しますが、本物の市場流動性や価値は全く生まれていません。
![Sample 7 PL Trend](../../samples/Sample_7_Market_Cash_Flow/output_plots/000_0_1__PL_Trend.png)

#### 🔴 Sample 8 (fMRI 脳梗塞)
**臨床解説:**
全脳の機能的な活動収支（利益相当）です。梗塞発生の $t=30$ 以降、機能ポテンシャルは急激なマイナスへと転じ、脳活動の致命的虚脱（`-$500,000` 相当）を示します。
![Sample 8 PL Trend](../../samples/Sample_8_fMRI_Stroke/output_plots/000_0_1__PL_Trend.png)

#### 🔴 Sample 9 (fMRI てんかん発作)
**臨床解説:**
てんかん同調時の活動収支です。過同期放電により莫大なBOLD信号消費が発生しますが、認知機能（自由エネルギー相当）は壊滅的に低下（`-$500,000`）しています。
![Sample 9 PL Trend](../../samples/Sample_9_fMRI_Seizure/output_plots/000_0_1__PL_Trend.png)

---

## 3. 損益計算書（P/L）ウォーターフォール (`000_0_1__PL_Waterfall_Total.png`)
売上から各費用を差し引き、最終純利益に至る会計上の累積収支構造を示したウォーターフォール図です。

#### 🟢 Sample 0 (正常代謝)
**臨床解説:**
売上総利益から営業費用が段階的かつ合理的に差し引かれ、正味の期末純利益が残る、極めて教科書的で健全な営業活動を示しています。
![Sample 0 PL Waterfall](../../samples/Sample_0_Healthy/output_plots/000_0_1__PL_Waterfall_Total.png)

#### 🟡 Sample 1 (循環取引)
**臨床解説:**
巨大な売上総利益に対して営業費用（SG&A）が不自然なほど極小であり、循環取引による仮装売上のみで純利益が形成されている様子が記録されています。
![Sample 1 PL Waterfall](../../samples/Sample_1_Wash_Trade/output_plots/000_0_1__PL_Waterfall_Total.png)

#### 🔴 Sample 2 (資金横領)
**臨床解説:**
帳簿上は黒字収支として純利益が計上されていますが、実際には売上回収金の相当部分が簿外（系外）にバイパスされており、実態のキャッシュフローと断絶しています。
![Sample 2 PL Waterfall](../../samples/Sample_2_Embezzlement_Leak/output_plots/000_0_1__PL_Waterfall_Total.png)

#### 🟡 Sample 3 (入力ミス)
**臨床解説:**
仕訳片面入力エラーによる一時的な不一致が残差（ノイズ）として差し引かれていますが、最終的な営業収支の基本骨格は正常範囲内に収まっています。
![Sample 3 PL Waterfall](../../samples/Sample_3_Unbalanced_Mistake/output_plots/000_0_1__PL_Waterfall_Total.png)

#### 🔴 Sample 4 (複合アノマリー)
**臨床解説:**
架空売上の水増しによって売上が巨大化している一方で、横領による資金損失が別の差し引き項目として並び立ち、病的肥大と出血の同時発生を示しています。
![Sample 4 PL Waterfall](../../samples/Sample_4_Composite_Chaos/output_plots/000_0_1__PL_Waterfall_Total.png)

#### 🔴 Sample 5 (京都交差点網)
**臨床解説:**
ネットワーク内の流入車両数と、交差点の通過限界による「車両損失（渋滞滞留）」の収支バランスです。損失エリアが流入量を遥かに引けを取らないことを示します。
![Sample 5 PL Waterfall](../../samples/Sample_5_Kyoto_Traffic/output_plots/000_0_1__PL_Waterfall_Total.png)

#### 🟡 Sample 6 (株券流体システム)
**臨床解説:**
市場に投入された全注文と、ボット間の過同期によって「空回り」した取引量の対照です。全体の出来高のうち、実需を伴う割合がほぼゼロに等しいことを示します。
![Sample 6 PL Waterfall](../../samples/Sample_6_Market_Stock_Flow/output_plots/000_0_1__PL_Waterfall_Total.png)

#### 🔴 Sample 8 (fMRI 脳梗塞)
**臨床解説:**
脳全体で消費された総酸素エネルギー（BOLD）と、虚血壊死領域における「活動低下の損失」の対比です。梗塞領野による損失が全体を押し潰しています。
![Sample 8 PL Waterfall](../../samples/Sample_8_fMRI_Stroke/output_plots/000_0_1__PL_Waterfall_Total.png)

#### 🔴 Sample 9 (fMRI てんかん発作)
**臨床解説:**
てんかんバーストによる異常代謝酸素消費の割合です。同期放電が脳全体の酸素資源を無駄に食いつぶし、他部位へのエネルギー伝達を阻害しています。
![Sample 9 PL Waterfall](../../samples/Sample_9_fMRI_Seizure/output_plots/000_0_1__PL_Waterfall_Total.png)

---

## 4. 貸借対照表（B/S）ブロック総計 (`000_0_1__BS_Block_Total.png`)
資産と負債・資本の各科目をブロック状に視覚化し、構造バランスの健全性を表す図です。

#### 🟢 Sample 0 (正常代謝)
**臨床解説:**
流動資産（現預金など）が適度な割合で配置され、負債と自己資本（利益剰余金）がバランスよく左右対称に並ぶ、健全な財務体格が示されています。
![Sample 0 BS Block Total](../../samples/Sample_0_Healthy/output_plots/000_0_1__BS_Block_Total.png)

#### 🟡 Sample 1 (循環取引)
**臨床解説:**
売掛金のブロックが不自然に巨大化しており、現預金との自己還流取引だけで資産サイドが歪に膨張している様子を視覚的に告発しています。
![Sample 1 BS Block Total](../../samples/Sample_1_Wash_Trade/output_plots/000_0_1__BS_Block_Total.png)

#### 🔴 Sample 2 (資金横領)
**臨床解説:**
売掛金回収が行われているにもかかわらず、手元現預金ブロックが異常に圧縮され、代わりに簿外の `UNKNOWN_LEAK` ノードが裏で実質資産を構成しています。
![Sample 2 BS Block Total](../../samples/Sample_2_Embezzlement_Leak/output_plots/000_0_1__BS_Block_Total.png)

#### 🟡 Sample 3 (入力ミス)
**臨床解説:**
貸借の一方のみの入力エラーにより、ブロックの左右の合計値が一致せず、一時的に「帳簿の歪み（アンバランス）」が発生した痕跡を捉えています。
![Sample 3 BS Block Total](../../samples/Sample_3_Unbalanced_Mistake/output_plots/000_0_1__BS_Block_Total.png)

#### 🔴 Sample 4 (複合アノマリー)
**臨床解説:**
売掛金の巨大化と手元現預金の過度な縮小が同居しており、粉飾による表面の虚像と、横領による内部の空洞化がブロックの歪みから一目で判別できます。
![Sample 4 BS Block Total](../../samples/Sample_4_Composite_Chaos/output_plots/000_0_1__BS_Block_Total.png)

#### 🔴 Sample 5 (京都交差点網)
**臨床解説:**
京都市内のエリア別の滞留車両ブロックです。中京区（四条烏丸など）の滞留ボリュームが極端に巨大化し、周辺エリアの車流が途切れていることを示します。
![Sample 5 BS Block Total](../../samples/Sample_5_Kyoto_Traffic/output_plots/000_0_1__BS_Block_Total.png)

#### 🟡 Sample 6 (株券流体システム)
**臨床解説:**
投資家別・銘柄別の保有バランスです。一般市場の保有シェアが薄く、ボット群と標的銘柄の間だけで出来高ブロックが寡占・ロックされています。
![Sample 6 BS Block Total](../../samples/Sample_6_Market_Stock_Flow/output_plots/000_0_1__BS_Block_Total.png)

#### 🔴 Sample 8 (fMRI 脳梗塞)
**臨床解説:**
脳葉別の酸素BOLD信号ブロックです。梗塞が発生した運動野（額葉）のブロック容積が激減し、脳全体の信号量バランスが不可逆に失われています。
![Sample 8 BS Block Total](../../samples/Sample_8_fMRI_Stroke/output_plots/000_0_1__BS_Block_Total.png)

#### 🔴 Sample 9 (fMRI てんかん発作)
**臨床解説:**
てんかん時の脳活動強度ブロックです。側頭葉ブロックが全体の活動を独占し、他領域のBOLD活動を強制同期によって均一なパターンに染め上げています。
![Sample 9 BS Block Total](../../samples/Sample_9_fMRI_Seizure/output_plots/000_0_1__BS_Block_Total.png)
