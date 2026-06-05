# 001_2. 局所エントロピー分析 (Local Entropy)

本ガイドは、Tensor-Link Utility (TLU) における「3次元局所エントロピー（`001_1_2_1__3d_local_entropy.png`）」について、各検証サンプルの出力と数値に基づく臨床解説を整理したものです。

---

## 🔬 物理数学理論：局所エントロピー $s_i$
TLUは、各ノード $i$ における流動遷移確率の無秩序さを「局所エントロピー $s_i$」と定義します。これは、ノードから流出する流量がどれだけ多様な接続先へ分散しているかを示す指標です。

$$s_i = -\sum_{j} P_{ij} \log P_{ij}$$

特定の接続先へ流路が固定されるか、あるいは流路が完全に遮断（フリーズ）された場合、エントロピー $s_i$ は極端に低下します。逆に、健全に分散している場合は高い値を維持します。

---

## 📊 3次元局所エントロピーと個別サンプルの所見

各ノードごとの空間的流路の分散度（エントロピー）の時空間変化を示す3次元グラフです。

#### 🟢 Sample 0 (正常代謝)
**臨床解説:**
各領域の空間的エントロピーはなだらかで均一に分布しており、局所的な流路の遮断や特定の接続先への病的偏在は生じていません。
- ![Sample 0 Local Entropy](Sample_0_Healthy/readme_plots/001_1_2_1__3d_local_entropy.png)

#### 🟡 Sample 1 (循環取引)
**臨床解説:**
循環取引発生期（1月、2月、5月）において、`ACC_Cash` が売掛金への異常な還流流路を形成したことで、局所エントロピーに明確な盛り上がりが検出されます。
- ![Sample 1 Local Entropy](Sample_1_Wash_Trade/readme_plots/001_1_2_1__3d_local_entropy.png)

#### 🔴 Sample 2 (資金横領)
**臨床解説:**
売掛金回収が正常に行われず、`UNKNOWN_LEAK` という一方向の流出先ノードへ資金流路が固定された結果、該当部位の局所エントロピーが異様に盛り上がり、漏洩経路の存在を示します。
- ![Sample 2 Local Entropy](Sample_2_Embezzlement_Leak/readme_plots/001_1_2_1__3d_local_entropy.png)

#### 🟡 Sample 3 (入力ミス)
**臨床解説:**
入力ミスがあったタイムステップ（$t=1$）において、売掛金ノード周辺の局所エントロピーに鋭い単一のスパイクが生じますが、翌ステップには速やかに消滅して平坦に戻ります。
- ![Sample 3 Local Entropy](Sample_3_Unbalanced_Mistake/readme_plots/001_1_2_1__3d_local_entropy.png)

#### 🔴 Sample 4 (複合アノマリー)
**臨床解説:**
還流ループによる局所エントロピーの盛り上がりと、横領による漏洩先ノード周辺の局所エントロピーの盛り上がりが並行し、重層的な流路歪みが発生しています。
- ![Sample 4 Local Entropy](Sample_4_Composite_Chaos/readme_plots/001_1_2_1__3d_local_entropy.png)

#### 🔴 Sample 5 (京都交差点網)
**臨床解説:**
交差点網の局所エントロピーです。ボトルネックである `21_四条室町` 周辺で、選択肢容量が著しく低下（車両の滞留・拘束）したことを示すエントロピー降下（$s_i=1.674$）が記録されています。
- ![Sample 5 Local Entropy](Sample_5_Kyoto_Traffic/readme_plots/001_1_2_1__3d_local_entropy.png)

#### 🟢 Sample 6 (株券流体)
**臨床解説:**
取引ボット群と少数の銘柄間で非常に活発かつ高速に対流が行われていますが、全体のやり取りは対称的かつ安定して循環しています。そのため、局所エントロピーは時間・空間を通して極めて均一かつ高い水準（約 $s_i=2.0$ 前後）で滑らかに維持されています。
- ![Sample 6 Local Entropy](Sample_6_Market_Stock_Flow/readme_plots/001_1_2_1__3d_local_entropy.png)

#### 🟢 Sample 7 (現金流体)
**臨床解説:**
ユーザー間の健全な送金・決済フロー。特定の口座や還流ループに資金が滞留することなく、多様な接続先へ流動性が滑らかに分散されているため、局所エントロピーは常に高水準かつ安定した状態を維持しています。
- ![Sample 7 Local Entropy](Sample_7_Market_Cash_Flow/readme_plots/001_1_2_1__3d_local_entropy.png)

#### 🔴 Sample 8 (fMRI 脳梗塞)
**臨床解説:**
脳梗塞が発生する $t=30$ (TR=150) 以降、虚血壊死した運動野領域のBOLD信号活動ポテンシャルがほぼ完全に消失します。流動の消失に伴い、該当部位周辺の局所エントロピーが劇的に平坦化（空間的崩壊）する様子が明瞭に記録されています。
- ![Sample 8 Local Entropy](Sample_8_fMRI_Stroke/readme_plots/001_1_2_1__3d_local_entropy.png)

#### 🔴 Sample 9 (fMRI てんかん発作)
**臨床解説:**
てんかんの過同期バースト期において、全脳の領域が単一のサイン波の如く極限まで同調します。すべての領域が同じパターンで均一に強制同期されるため、状態の無秩序さ（エントロピー）は極限まで低下し、グラフ全体が低いレベルで完全に平坦化（フリーズ）します。
- ![Sample 9 Local Entropy](Sample_9_fMRI_Seizure/readme_plots/001_1_2_1__3d_local_entropy.png)
