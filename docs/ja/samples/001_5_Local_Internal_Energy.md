# 001_5. 局所内部エネルギー分析 (Local Internal Energy)

本ガイドは、Tensor-Link Utility (TLU) における「3次元局所内部エネルギー（`001_1_2_7__3d_local_internal_energy.png`）」について、各検証サンプルの出力と数値に基づく臨床解説を整理したものです。

---

## 🔬 物理数学理論：局所内部エネルギー $u_i$

TLUは、各ノード $i$ を通過する総流量（流入量と流出量の絶対値和）を「局所内部エネルギー $u_i$」と定義します。これは、ネットワークトポロジーにおけるノードの「**活動規模・ボリューム (Scale & Volume)**」を物理数学的に表現したものです。

$$u_i(t) = \sum_{j \in \text{neighbors}(i)} ( |F_{ji}(t)| + |F_{ij}(t)| )$$

ここで $F_{ij}(t)$ はノード $j$ からノード $i$ への有向流量です。システム全体の中で特定の経路や勘定、交差点に流量が集中すると、該当ノード of 局所内部エネルギーが突出し、偏った「エネルギーの壁」を形成します。

---

## 📊 3次元局所内部エネルギーと個別サンプルの所見

各ノードごとの空間的流量規模（内部エネルギー）の時空間変化を示す3次元グラフです。

#### 🟢 Sample 0 (正常代謝)

**臨床解説:**
システム内の各領域に流量が均等に分散されています。特定のノードへの流量の異常集中はありません。極端な過負荷は発生していません。エネルギーは平穏かつ適正な分布を維持しています。

- ![Sample 0 Local Internal Energy](../../../samples/Sample_0_Healthy/readme_plots/001_1_2_7__3d_local_internal_energy.png)

#### 🟡 Sample 1 (循環取引)

**臨床解説:**
循環取引が発生します。これに伴い、往復還流の軸となる3ノードに活動流量が集中します。該当ノードは `ACC_Cash`、`ACC_Accounts_Receivable`、`ACC_Sales_Revenue` です。他の一般経費口座などを圧倒する巨大なエネルギーの山（壁）が形成されます。

- ![Sample 1 Local Internal Energy](../../../samples/Sample_1_Wash_Trade/readme_plots/001_1_2_7__3d_local_internal_energy.png)

#### 🔴 Sample 2 (資金横領)

**臨床解説:**
売掛金が正常回収されません。特定のバイパス口座 `UNKNOWN_LEAK` へと資金が一方通行で流出します。この期間中、漏洩元である預金口座および漏洩先ノードにエネルギーが偏在します。持続的な活動ボリュームの隆起として検出されます。

- ![Sample 2 Local Internal Energy](../../../samples/Sample_2_Embezzlement_Leak/readme_plots/001_1_2_7__3d_local_internal_energy.png)

#### 🟡 Sample 3 (入力ミス)

**臨床解説:**
$t=1$ に片面入力エラーが生じました。貸借不一致の整合性を保つための仮の調整流量が発生します。これは売掛金ノード周辺に発生します。そのため、その瞬間だけ極めて高くて鋭い単一のエネルギーの塔が立ち上がります。翌ステップの修正とともに消失します。

- ![Sample 3 Local Internal Energy](../../../samples/Sample_3_Unbalanced_Mistake/readme_plots/001_1_2_7__3d_local_internal_energy.png)

#### 🔴 Sample 4 (複合アノマリー)

**臨床解説:**
還流ループによるエネルギー増加が発生します。また、横領による漏洩流路のエネルギー偏在が発生します。これらがネットワーク上の異なる領域で同時に発生します。これにより、複数の箇所でエネルギーの突出が並立します。重層的な流路歪みが可視化されます。

- ![Sample 4 Local Internal Energy](../../../samples/Sample_4_Composite_Chaos/readme_plots/001_1_2_7__3d_local_internal_energy.png)

#### 🔴 Sample 5 (京都交差点網)

**臨床解説:**
ボトルネックである `21_四条室町`・`23_四条烏丸` 周辺に車両の流入量および滞留が集中します。これにより、該当交差点ノード周辺の局所内部エネルギーが著しく上昇します。ネットワークのキャパシティ上限に達している領域が物理的に特定されます。

- ![Sample 5 Local Internal Energy](../../../samples/Sample_5_Kyoto_Traffic/readme_plots/001_1_2_7__3d_local_internal_energy.png)

#### 🟢 Sample 6 (株券流体)

**臨床解説:**
取引ボット群と少数の銘柄間で対称取引が行われています。これは非常に高頻度かつ大ボリュームです。そのため、システム全体の内部エネルギーは極めて高い水準にあります。しかし、空間的にはボット口座群へ極めて平坦かつ対称的に分散されています。

- ![Sample 6 Local Internal Energy](../../../samples/Sample_6_Market_Stock_Flow/readme_plots/001_1_2_7__3d_local_internal_energy.png)

#### 🟢 Sample 7 (現金流体)

**臨床解説:**
一般ユーザー間の健全な送金・決済網です。特定の口座や還流ループに資金が滞留することはありません。多様な接続先へ流動性が分散されています。そのため、局所エントロピーは高水準で安定しています。

- ![Sample 7 Local Internal Energy](../../../samples/Sample_7_Market_Cash_Flow/readme_plots/001_1_2_7__3d_local_internal_energy.png)

#### 🔴 Sample 8 (fMRI 脳梗塞)

**臨床解説:**
脳梗塞が発生します（$t=30$ 以降）。血流および活動が途絶した運動野領域の活動ポテンシャルが完全に消失します。この虚血壊死部位の局所内部エネルギーは絶対零度の平地のように不可主に陥没（平坦化）します。活動の喪失範囲を明瞭に描き出します。

- ![Sample 8 Local Internal Energy](../../../samples/Sample_8_fMRI_Stroke/readme_plots/001_1_2_7__3d_local_internal_energy.png)

#### 🔴 Sample 9 (fMRI てんかん発作)

**臨床解説:**
てんかん発作（過同期）が発生します。これにより全脳領域のBOLD信号活動が一斉に同調・暴走します。すべての領域のエネルギーが最高水準（全脳過活動状態）に押し上げられます。空間的なエネルギー差がほぼ完全に消失します。グラフ全体が高いレベルで一様に真っ平らにフリーズします。

- ![Sample 9 Local Internal Energy](../../../samples/Sample_9_fMRI_Seizure/readme_plots/001_1_2_7__3d_local_internal_energy.png)
