# 001. 熱力学とエントロピー (Thermodynamics & Entropy)

本ガイドは、Tensor-Link Utility (TLU) における熱力学・エントロピー分析モジュール（`001_1`、`001_2`）について、グラフの種類ごとに各検証サンプルの出力と数値に基づく臨床解説を縦列に整理したものです。

---

## 🔬 熱力学の物理数学理論

TLUは、ネットワーク全体の活動量を「内部エネルギー $U$」、ノード間の流動遷移確率の無秩序さを「エントロピー $S$」、流量ボラティリティ（標準偏差）を「温度 $T$」と定義します。これらを用いて、システムが外部に有益な仕事をしたり構造を維持するために残されている真のポテンシャルである**「自由エネルギー $F$」**を算出します。

$$F = U - T \cdot S$$

不可逆な実体システムでは、活動に伴って摩擦熱損失（$T \times S$）が発生し、自由エネルギーが健全に消費（散逸）されます。しかし、病的還流閉路（循環取引、車両デッドロック、共謀送金など）が形成されると、内部エネルギー $U$ は激しい空回りで高い数値を維持しますが、それが実体活動（外部接続）を伴わないため、すべて摩擦熱（$TS$）の膨張として相殺され、自由エネルギー $F$ が極度に圧縮されて枯渇へと向かいます。

---

## 📊 マクロ熱力学グラフと個別サンプルの所見

### 1. 熱力学エネルギースタック (`001_1_2__thermodynamics_energy_stack.png`)
内部エネルギー $U$、摩擦熱損失 $TS$、および自由エネルギー $F$ の累積構成推移を示すスタックグラフです。

#### 🟢 Sample 0 (正常代謝)
**臨床解説:**
自由エネルギー $F$（白い実線）が、底部の摩擦熱損失 $TS$（エンジ色）に圧縮されることなく、事業規模の拡大（$U$ の成長）とともになだらかな右肩上がりで安定成長しています。
![Sample 0 Energy Stack](Sample_0_Healthy/readme_plots/001_1_2__thermodynamics_energy_stack.png)

#### 🟡 Sample 1 (循環取引)
**臨床解説:**
循環取引の実行月（1月、2月、5月）に、激しい往復残高ボラティリティにより局所温度がスパイクし、摩擦熱損失 $TS$ が急激に拡張して自由エネルギー $F$ を強く押し潰しています。
![Sample 1 Energy Stack](Sample_1_Wash_Trade/readme_plots/001_1_2__thermodynamics_energy_stack.png)

#### 🔴 Sample 2 (資金横領)
**臨床解説:**
簿外への資金吸い出し（大出血）により、活動の源泉である現金（質量）が失われたため、内部エネルギー $U$ 自体が右肩下がりで衰退しています。
![Sample 2 Energy Stack](Sample_2_Embezzlement_Leak/readme_plots/001_1_2__thermodynamics_energy_stack.png)

#### 🟡 Sample 3 (入力ミス)
**臨床解説:**
片面入力エラーが発生した $t=1$（2月）の瞬間、一時的なノイズとして温度とエントロピーが鋭く上方向へ跳ね上がり、エネルギースタック上に棘状の摩擦が記録されています。
![Sample 3 Energy Stack](Sample_3_Unbalanced_Mistake/readme_plots/001_1_2__thermodynamics_energy_stack.png)

#### 🔴 Sample 4 (複合アノマリー)
**臨床解説:**
循環取引の還流による温度上昇（$T$ スパイク）と、横領による資産の系外流出（$U$ の減衰）が同時進行した結果、赤色の摩擦熱エリアが極限まで拡大して自由エネルギー $F$ が完全に底へ押し潰されています。
![Sample 4 Energy Stack](Sample_4_Composite_Chaos/readme_plots/001_1_2__thermodynamics_energy_stack.png)

#### 🔴 Sample 5 (京都交差点網)
**臨床解説:**
デッドロック発生後、車両の身動きが取れなくなる一方で流入は続くため、速度ボラティリティによる摩擦熱損失が急増し、マクロ自由エネルギー（車両流動ポテンシャル）が圧縮・損失されています。
![Sample 5 Energy Stack](Sample_5_Kyoto_Traffic/readme_plots/001_1_2__thermodynamics_energy_stack.png)

#### 🟢 Sample 6 (株券流体)
**臨床解説:**
内部エネルギー $U$ は株券流体の対流規模を反映して適正水準で安定し、摩擦熱損失 $TS$ も低く抑えられ、自由エネルギー $F$ はプラスの活動余力を維持しています。
![Sample 6 Energy Stack](Sample_6_Market_Stock_Flow/readme_plots/001_1_2__thermodynamics_energy_stack.png)

#### 🟢 Sample 7 (現金流体)
**臨床解説:**
決済流動性の対流に伴い、摩擦熱損失 $TS$ は穏やかに推移し、余力である自由エネルギー $F$ が健全に確保され、システム全体の資金効率が維持されています。
![Sample 7 Energy Stack](Sample_7_Market_Cash_Flow/readme_plots/001_1_2__thermodynamics_energy_stack.png)

#### 🔴 Sample 8 (fMRI 脳梗塞)
**臨床解説:**
脳梗塞発生（$t=30$）の直後、運動野への血流質量供給が完全に断たれるため、エネルギー生産（$U$）が急降下し、活動能力である自由エネルギーが奈落の底へ落下しています。
![Sample 8 Energy Stack](Sample_8_fMRI_Stroke/readme_plots/001_1_2__thermodynamics_energy_stack.png)

#### 🔴 Sample 9 (fMRI てんかん発作)
**臨床解説:**
てんかんの全脳過同期バーストにより、ボラティリティ（温度）は極大化しますが、情報探索の自由度が失われ、活動ポテンシャルである自由エネルギーは壊滅的に低下しています。
![Sample 9 Energy Stack](Sample_9_fMRI_Seizure/readme_plots/001_1_2__thermodynamics_energy_stack.png)

### 2. 温度-エントロピー (T-S) ダイアグラム (`001_1_3__thermodynamics_ts_diagram.png`)
温度 $T$ とエントロピー $S$ の相関推移から、システムの不可逆的な熱力学サイクル軌道を証明するグラフです。

#### 🟢 Sample 0 (正常代謝)
**臨床解説:**
T-S曲線は閉じておらず、外部環境と接続しながらエントロピーを放出する健全な「開放経路（探索の自由度が高い状態）」を描いています。
![Sample 0 TS Diagram](Sample_0_Healthy/readme_plots/001_1_3__thermodynamics_ts_diagram.png)

#### 🟡 Sample 1 (循環取引)
**臨床解説:**
T-S線図は極めて不自然な「反時計回りに閉じた卵型の軌跡（永久空転回路）」を描いており、内部だけで無駄に放出した熱量（摩擦）の存在を数理的に証明しています。
![Sample 1 TS Diagram](Sample_1_Wash_Trade/readme_plots/001_1_3__thermodynamics_ts_diagram.png)

#### 🔴 Sample 2 (資金横領)
**臨床解説:**
質量（資金）の系外流出に伴い、温度・エントロピーの活動スケール自体が徐々に縮小し、T-S曲線は左下の原点方向へと不可逆に縮退していく「熱的飢餓」の様子を示します。
![Sample 2 TS Diagram](Sample_2_Embezzlement_Leak/readme_plots/001_1_3__thermodynamics_ts_diagram.png)

#### 🟡 Sample 3 (入力ミス)
**臨床解説:**
入力ミスがあったステップで棘状の異常突出を見せますが、翌ステップの修正により速やかに元の健全な開放型T-S軌道へと復帰し、病的還流は定着していません。
![Sample 3 TS Diagram](Sample_3_Unbalanced_Mistake/readme_plots/001_1_3__thermodynamics_ts_diagram.png)

#### 🔴 Sample 4 (複合アノマリー)
**臨床解説:**
還流アノマリーの強制駆動と横領による質量衰退が折り重なり、T-S曲線は正常なリミットサイクルから離脱して激しくのたうち回りながら無限縮退へと向かっています。
![Sample 4 TS Diagram](Sample_4_Composite_Chaos/readme_plots/001_1_3__thermodynamics_ts_diagram.png)

#### 🔴 Sample 5 (京都交差点網)
**臨床解説:**
アノマリー期のボトルネック発生により、T-S曲線は「閉じた時計回りの病的ループ」へと急転移し、道路網の車両流動能力が局所に閉じ込められ死滅した様子を捉えています。
![Sample 5 TS Diagram](Sample_5_Kyoto_Traffic/readme_plots/001_1_3__thermodynamics_ts_diagram.png)

#### 🟢 Sample 6 (株券流体)
**臨床解説:**
T-Sダイアグラムは閉じた病的ループを形成せず、外部環境と接続しながら探索の自由度が高い開放型対流プロセスを描いています。
![Sample 6 TS Diagram](Sample_6_Market_Stock_Flow/readme_plots/001_1_3__thermodynamics_ts_diagram.png)

#### 🟢 Sample 7 (現金流体)
**臨床解説:**
T-Sダイアグラムは穏やかに揺らぎながら開放的な軌道を描いており、人工的な還流ロックや送金ループの同調歪みは検出されません。
![Sample 7 TS Diagram](Sample_7_Market_Cash_Flow/readme_plots/001_1_3__thermodynamics_ts_diagram.png)

#### 🔴 Sample 8 (fMRI 脳梗塞)
**臨床解説:**
虚血（$t=30$）の発生後、T-S曲線はそれまでのダイナミックな機能的軌道空間から完全に切り離され、活動ゼロに近い極小の平衡点へと不可逆にフリーズしています。
![Sample 8 TS Diagram](Sample_8_fMRI_Stroke/readme_plots/001_1_3__thermodynamics_ts_diagram.png)

#### 🔴 Sample 9 (fMRI てんかん発作)
**臨床解説:**
脳全体が異常同期放電にハックされた結果、多様な状態探索能力が失われ、T-S曲線は単一振動を往復するだけの「一本の病的閉じた直線」へと完全にフリーズしています。
![Sample 9 TS Diagram](Sample_9_fMRI_Seizure/readme_plots/001_1_3__thermodynamics_ts_diagram.png)
