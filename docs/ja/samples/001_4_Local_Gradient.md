# 001_4. 局所熱力学勾配分析 (Local Temperature Gradient)

本ガイドは、Tensor-Link Utility (TLU) における「局所熱力学勾配・温度勾配（`001_1_2_3__3d_local_gradient.png` 等）」について、各検証サンプルの出力と数値に基づく臨床解説を整理したものです。

---

## 🔬 物理数学理論：局所温度勾配 $\nabla T_i$
TLUは、システム内の隣接ノード間における温度差（ボラティリティ差）の空間的な傾きを「局所温度勾配 $\nabla T_i$」と定義します。

$$\nabla T_i = \sum_{j \in \text{neighbors}(i)} W_{ij} (T_i - T_j)$$

急峻な温度勾配が存在する領域は、流動の不均衡、ボトルネックの発生位置、または熱的な障壁（流動インピーダンスの高い境界）を意味します。

---

## 📊 局所熱力学勾配・温度勾配と個別サンプルの所見

システム内のノード間における温度差の空間的傾きを示すグラフです。流動の不均衡やボトルの位置を特定します。

#### 🟢 Sample 0 (正常代謝)
**臨床解説:**
全体が均一に活性化しており、特定のエリアへの流動の偏りや抵抗が生じていないため、局所熱力学勾配は終始平坦です。流動インピーダンスや「熱の壁」は存在しません。
- ![Sample 0 Local Grad](Sample_0_Healthy/readme_plots/001_1_2_3__3d_local_gradient.png)
- ![Sample 0 Thermo Gradient](Sample_0_Healthy/readme_plots/001_1_2_6__local_thermo_gradient.png)

#### 🟡 Sample 1 (循環取引)
**臨床解説:**
還流取引の軸である `ACC_Cash` 等の過熱部と、それ以外の低活性な一般費用・負債口座との境界において、非常に急峻な温度勾配が局所的に生じ、還流の「熱的孤立」を物語っています。
- ![Sample 1 Local Grad](Sample_1_Wash_Trade/readme_plots/001_1_2_3__3d_local_gradient.png)
- ![Sample 1 Thermo Gradient](Sample_1_Wash_Trade/readme_plots/001_1_2_6__local_thermo_gradient.png)

#### 🔴 Sample 2 (資金横領)
**臨床解説:**
過熱している現金口座から、一方向に資金が抜けていく `UNKNOWN_LEAK` への接続部において、不連続で急激な温度勾配が立ち上がり、隠れたバイパス流出の物理的境界を捉えています。
- ![Sample 2 Local Grad](Sample_2_Embezzlement_Leak/readme_plots/001_1_2_3__3d_local_gradient.png)
- ![Sample 2 Thermo Gradient](Sample_2_Embezzlement_Leak/readme_plots/001_1_2_6__local_thermo_gradient.png)

#### 🟡 Sample 3 (入力ミス)
**臨床解説:**
片面入力エラーが生じた $t=1$ にのみ、貸借不一致となったノードのローカルボラティリティが一時的に爆発するため、その瞬間に鋭い温度勾配の局所スパイクが生じますが、エラー修正とともに翌ステップには平坦化します。
- ![Sample 3 Local Grad](Sample_3_Unbalanced_Mistake/readme_plots/001_1_2_3__3d_local_gradient.png)
- ![Sample 3 Thermo Gradient](Sample_3_Unbalanced_Mistake/readme_plots/001_1_2_6__local_thermo_gradient.png)

#### 🔴 Sample 4 (複合アノマリー)
**臨床解説:**
往復還流による強烈な過熱と、横領による漏洩流出、およびその他の無活動領域（冷温部）がモザイク状に混在しています。これにより、ネットワーク各所で複数の急峻な局所熱力学勾配が競合するように発生し、構造の著しい破綻を示します。
- ![Sample 4 Local Grad](Sample_4_Composite_Chaos/readme_plots/001_1_2_3__3d_local_gradient.png)
- ![Sample 4 Thermo Gradient](Sample_4_Composite_Chaos/readme_plots/001_1_2_6__local_thermo_gradient.png)

#### 🔴 Sample 5 (京都交差点網)
**臨床解説:**
デッドロックでフリーズした `23_四条烏丸`（コールドスポット）と、その上流で車列が動けず滞留する交差点（ホットスポット）との間で、強烈な温度差（熱力学勾配）が発生している様子を捉えています。
- ![Sample 5 Local Grad](Sample_5_Kyoto_Traffic/readme_plots/001_1_2_3__3d_local_gradient.png)
- ![Sample 5 Thermo Gradient](Sample_5_Kyoto_Traffic/readme_plots/001_1_2_6__local_thermo_gradient.png)

#### 🟢 Sample 6 (株券流体)
**臨床解説:**
ボット間取引は超高速ですが、保存則に基づき出来高と保有量は空間的に均等に対流しています。局所温度が全体として適正値で均一であるため、急峻な温度勾配は発生せず、滑らかな平坦面を維持しています。
- ![Sample 6 Local Grad](Sample_6_Market_Stock_Flow/readme_plots/001_1_2_3__3d_local_gradient.png)
- ![Sample 6 Thermo Gradient](Sample_6_Market_Stock_Flow/readme_plots/001_1_2_6__local_thermo_gradient.png)

#### 🟢 Sample 7 (現金流体)
**臨床解説:**
決済流動性が多様な口座間で健全に循環しており、ボラティリティの急激な断絶や偏在は見られません。ノード間の温度変化が穏やかであるため、急峻な局所勾配は発生せず、健全な熱的拡散状態が維持されています。
- ![Sample 7 Local Grad](Sample_7_Market_Cash_Flow/readme_plots/001_1_2_3__3d_local_gradient.png)
- ![Sample 7 Thermo Gradient](Sample_7_Market_Cash_Flow/readme_plots/001_1_2_6__local_thermo_gradient.png)

#### 🔴 Sample 8 (fMRI 脳梗塞)
**臨床解説:**
梗塞が発生した壊死野（極低温）と、その周囲で血流低下を補うために代償的に過活動となっている半影帯（ペナンブラ：高温）との境界で、非常に急峻な局所熱力学勾配（温度勾配）が発生します。
- ![Sample 8 Local Grad](Sample_8_fMRI_Stroke/readme_plots/001_1_2_3__3d_local_gradient.png)
- ![Sample 8 Thermo Gradient](Sample_8_fMRI_Stroke/readme_plots/001_1_2_6__local_thermo_gradient.png)

#### 🔴 Sample 9 (fMRI てんかん発作)
**臨床解説:**
てんかん同調（過同期）によって、脳の全領域が一様に最高温度まで沸騰（過熱）します。全脳が同じパターンで均一に過熱してしまうため、領域間の温度差（勾配）は逆に完全に平坦化（消失）し、熱的な還流駆動力そのものが機能停止している様子を示します。
- ![Sample 9 Local Grad](Sample_9_fMRI_Seizure/readme_plots/001_1_2_3__3d_local_gradient.png)
- ![Sample 9 Thermo Gradient](Sample_9_fMRI_Seizure/readme_plots/001_1_2_6__local_thermo_gradient.png)
