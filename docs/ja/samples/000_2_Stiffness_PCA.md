# 000. 財務基礎状態、構造剛性、および運動学 (Basic Statistics, Stiffness & Kinematics)

本ガイドは、Tensor-Link Utility (TLU) における統計分析、運動学、および構造剛性・PCAについて解説するものです。

---

## 000_2: 構造剛性と主成分分析

### 6. 時系列構造剛性行列 (`000_2_1__structural_stiffness.t*.png`)
ノード間の偏相関と流量ボラティリティから算出された、システムの剛性トポロジーの時系列進化を示す行列グラフです。

#### 🟢 Sample 0 (正常代謝)
**臨床解説:**
剛性行列は偏りがなく均一で穏やかな分散を示しており、特定のセル（取引ペア）だけが濃赤色に凝固する剛性ロックは一切発生していません。
![Sample 0 Stiffness Matrix](Sample_0_Healthy/readme_plots/000_2_1__structural_stiffness.t.00000.png)
![Sample 0 Stiffness Matrix](Sample_0_Healthy/readme_plots/000_2_1__structural_stiffness.t.00003.png)
![Sample 0 Stiffness Matrix](Sample_0_Healthy/readme_plots/000_2_1__structural_stiffness.t.00006.png)

#### 🟡 Sample 1 (循環取引)
**臨床解説:**
循環取引の実行ステップ（$t=0, t=4$）において、`Cash` と `Accounts_Receivable` の間の剛性セルが極端な濃赤色として描出され、強力な「剛性ロック」が起きています。
![Sample 1 Stiffness t0](Sample_1_Wash_Trade/readme_plots/000_2_1__structural_stiffness.t.00000.png)
![Sample 1 Stiffness t3](Sample_1_Wash_Trade/readme_plots/000_2_1__structural_stiffness.t.00003.png)
![Sample 1 Stiffness t4](Sample_1_Wash_Trade/readme_plots/000_2_1__structural_stiffness.t.00004.png)
![Sample 1 Stiffness t5](Sample_1_Wash_Trade/readme_plots/000_2_1__structural_stiffness.t.00005.png)
![Sample 1 Stiffness t11](Sample_1_Wash_Trade/readme_plots/000_2_1__structural_stiffness.t.00011.png)

#### 🔴 Sample 2 (資金横領)
**臨床解説:**
$t=4$ 以降の資金漏洩の進行に伴い、現金預金と流出ノード `UNKNOWN_LEAK` 間の剛性ロックが徐々に進行し、最終期（$t=11$）に向けて、流出アノマリーは沈黙したままです。
![Sample 2 Stiffness t0](Sample_2_Embezzlement_Leak/readme_plots/000_2_1__structural_stiffness.t.00000.png)
![Sample 2 Stiffness t1](Sample_2_Embezzlement_Leak/readme_plots/000_2_1__structural_stiffness.t.00001.png)
![Sample 2 Stiffness t2](Sample_2_Embezzlement_Leak/readme_plots/000_2_1__structural_stiffness.t.00002.png)
![Sample 2 Stiffness t3](Sample_2_Embezzlement_Leak/readme_plots/000_2_1__structural_stiffness.t.00003.png)
![Sample 2 Stiffness t4](Sample_2_Embezzlement_Leak/readme_plots/000_2_1__structural_stiffness.t.00004.png)
![Sample 2 Stiffness t11](Sample_2_Embezzlement_Leak/readme_plots/000_2_1__structural_stiffness.t.00011.png)
![Sample 2 Stiffness t11](Sample_2_Embezzlement_Leak/readme_plots/000_2_1__structural_stiffness.t.00011.png)

#### 🟡 Sample 3 (入力ミス)
**臨床解説:**
$t=1$（2020-02）の片面入力エラーにより一時的な剛性のねじれ（高負荷セル）が発生しますが、翌ステップ（$t=2$）の自己修正以降、最終期（$t=11$）まで行列は正常な分散状態を維持しています。
![Sample 3 Stiffness t0](Sample_3_Unbalanced_Mistake/readme_plots/000_2_1__structural_stiffness.t.00000.png)
![Sample 3 Stiffness t3](Sample_3_Unbalanced_Mistake/readme_plots/000_2_1__structural_stiffness.t.00003.png)
![Sample 3 Stiffness t4](Sample_3_Unbalanced_Mistake/readme_plots/000_2_1__structural_stiffness.t.00004.png)
![Sample 3 Stiffness t5](Sample_3_Unbalanced_Mistake/readme_plots/000_2_1__structural_stiffness.t.00005.png)
![Sample 3 Stiffness t11](Sample_3_Unbalanced_Mistake/readme_plots/000_2_1__structural_stiffness.t.00011.png)
![Sample 3 Stiffness t11](Sample_3_Unbalanced_Mistake/readme_plots/000_2_1__structural_stiffness.t.00011.png)

#### 🔴 Sample 4 (複合アノマリー)
**臨床解説:**
循環取引アノマリーの激化時に `Cash` と `Accounts_Receivable` の間、および横領の流出先に繋がるセルの双方が強烈に硬化し、剛性構造が破壊されています。
![Sample 4 Stiffness t0](Sample_4_Composite_Chaos/readme_plots/000_2_1__structural_stiffness.t.00000.png)
![Sample 4 Stiffness t3](Sample_4_Composite_Chaos/readme_plots/000_2_1__structural_stiffness.t.00003.png)
![Sample 4 Stiffness t4](Sample_4_Composite_Chaos/readme_plots/000_2_1__structural_stiffness.t.00004.png)
![Sample 4 Stiffness t5](Sample_4_Composite_Chaos/readme_plots/000_2_1__structural_stiffness.t.00005.png)
![Sample 4 Stiffness t8](Sample_4_Composite_Chaos/readme_plots/000_2_1__structural_stiffness.t.00008.png)
![Sample 4 Stiffness t11](Sample_4_Composite_Chaos/readme_plots/000_2_1__structural_stiffness.t.00011.png)

#### 🔴 Sample 5 (京都交差点網)
**臨床解説:**
正常時（$t=6$ など）には剛性は分散していますが、渋滞麻痺（$t=18$ 以降）が発生すると、`23_四条烏丸` や `21_四条室町` の周辺セルが濃赤色（剛性ロック）へと相転移します。
![Sample 5 Stiffness t0](Sample_5_Kyoto_Traffic/readme_plots/000_2_1__structural_stiffness.t.00000.png)
![Sample 5 Stiffness t6](Sample_5_Kyoto_Traffic/readme_plots/000_2_1__structural_stiffness.t.00006.png)
![Sample 5 Stiffness t12](Sample_5_Kyoto_Traffic/readme_plots/000_2_1__structural_stiffness.t.00012.png)
![Sample 5 Stiffness t18](Sample_5_Kyoto_Traffic/readme_plots/000_2_1__structural_stiffness.t.00018.png)
![Sample 5 Stiffness t23](Sample_5_Kyoto_Traffic/readme_plots/000_2_1__structural_stiffness.t.00023.png)
![Sample 5 Stiffness t12](Sample_5_Kyoto_Traffic/readme_plots/000_2_1__structural_stiffness.t.00012.png)
![Sample 5 Stiffness t18](Sample_5_Kyoto_Traffic/readme_plots/000_2_1__structural_stiffness.t.00018.png)
![Sample 5 Stiffness t23](Sample_5_Kyoto_Traffic/readme_plots/000_2_1__structural_stiffness.t.00023.png)
![Sample 5 Stiffness t23](Sample_5_Kyoto_Traffic/readme_plots/000_2_1__structural_stiffness.t.00023.png)

#### 🔴 Sample 8 (fMRI 脳梗塞)
**臨床解説:**
虚血梗塞（$t=30$）が起きた瞬間、運動野（`Motor_Cortex`）および頂頭葉の間の剛性が異常に跳ね上がって凝固（Rigid Lock）し、脳活動の柔軟性が喪失した様子を示します。
![Sample 8 Stiffness t0](Sample_8_fMRI_Stroke/readme_plots/000_2_1__structural_stiffness.t.00000.png)
![Sample 8 Stiffness t29](Sample_8_fMRI_Stroke/readme_plots/000_2_1__structural_stiffness.t.00029.png)
![Sample 8 Stiffness t11](Sample_8_fMRI_Stroke/readme_plots/000_2_1__structural_stiffness.t.00011.png)
![Sample 8 Stiffness t31](Sample_8_fMRI_Stroke/readme_plots/000_2_1__structural_stiffness.t.00031.png)
![Sample 8 Stiffness t59](Sample_8_fMRI_Stroke/readme_plots/000_2_1__structural_stiffness.t.00059.png)

#### 🔴 Sample 9 (fMRI てんかん発作)
**臨床解説:**
全脳領域が異常放電によって過同期バーストを起こすと、剛性行列のほぼ全セルが最大値（濃赤色）にフリーズし、脳全体の情報変形能力（思考自由度）が失われます。
![Sample 9 Stiffness t0](Sample_9_fMRI_Seizure/readme_plots/000_2_1__structural_stiffness.t.00000.png)
![Sample 9 Stiffness t29](Sample_9_fMRI_Seizure/readme_plots/000_2_1__structural_stiffness.t.00029.png)
![Sample 9 Stiffness t11](Sample_9_fMRI_Seizure/readme_plots/000_2_1__structural_stiffness.t.00011.png)
![Sample 9 Stiffness t31](Sample_9_fMRI_Seizure/readme_plots/000_2_1__structural_stiffness.t.00031.png)
![Sample 9 Stiffness t59](Sample_9_fMRI_Seizure/readme_plots/000_2_1__structural_stiffness.t.00059.png)

---

### 7. PCA主要軸比率 (`000_2_2__principal_axes_ratio.png`)
剛性行列 $K$ に対する固有値分解による、主成分累積説明分散比率（Explained Variance Ratio）のプロットです。特定の少数の主成分に系の自由度がハックされているかを判別します。

#### 🟢 Sample 0 (正常代謝)
**臨床解説:**
各成分比率がなだらかに減衰しており、支配的な PC1 寄与率が低く、系のエネルギーが特定のルートに独占されずに「しなやか」に分散しています。
![Sample 0 PCA Ratio](Sample_0_Healthy/readme_plots/000_2_2__principal_axes_ratio.png)

#### 🟡 Sample 1 (循環取引)
**臨床解説:**
PC1寄与率がアノマリー実行時に **`95.28%`** まで跳ね上がり、系のすべての力学的変形エネルギーが架空取引の往復運動のみに独占されたことを証明します。
![Sample 1 PCA Ratio](Sample_1_Wash_Trade/readme_plots/000_2_2__principal_axes_ratio.png)

#### 🔴 Sample 2 (資金横領)
**臨床解説:**
横領の進行に伴い、PC1寄与率が継続的かつ不可逆に高まり、系の活動が `UNKNOWN_LEAK` と現金預金口座との間の偏ったエネルギー支配にハックされていく様子を示します。
![Sample 2 PCA Ratio](Sample_2_Embezzlement_Leak/readme_plots/000_2_2__principal_axes_ratio.png)

#### 🟡 Sample 3 (入力ミス)
**臨床解説:**
$t=1$ 前後に一時的に PC1 寄与率が **`100.0%`** に達する過剰なハックが生じますが、ミス修正後はすぐに元のなだらかな正常分散へと回帰します。
![Sample 3 PCA Ratio](Sample_3_Unbalanced_Mistake/readme_plots/000_2_2__principal_axes_ratio.png)

#### 🔴 Sample 4 (複合アノマリー)
**臨床解説:**
循環取引のピークである $t=2$ に PC1 寄与率が **`100.0%`** に達し、還流閉路が系の支配軸を強力にハイジャックしていることを示します。
![Sample 4 PCA Ratio](Sample_4_Composite_Chaos/readme_plots/000_2_2__principal_axes_ratio.png)

#### 🟢 Sample 6 (株券流体)
**臨床解説:**
PC1寄与率は極めて低く、特定の取引口座による支配やハイジャックはなく、エネルギーが健全に分散していることを示します。
![Sample 6 PCA Ratio](Sample_6_Market_Stock_Flow/readme_plots/000_2_2__principal_axes_ratio.png)

#### 🟢 Sample 7 (現金流体)
**臨床解説:**
PC1寄与率は低水準で安定しており、特定の口座群による流動性の拘束や剛性ロックがないことを示します。
![Sample 7 PCA Ratio](Sample_7_Market_Cash_Flow/readme_plots/000_2_2__principal_axes_ratio.png)

#### 🔴 Sample 8 (fMRI 脳梗塞)
**臨床解説:**
梗塞発生の瞬間から PC1 寄与率が不連続に急上昇し、脳全体の信号活動が梗塞野周辺の異常剛性（Rigid Lock）に力学的に支配されたことを示します。
![Sample 8 PCA Ratio](Sample_8_fMRI_Stroke/readme_plots/000_2_2__principal_axes_ratio.png)

#### 🔴 Sample 9 (fMRI てんかん発作)
**臨床解説:**
てんかん時は全領域が完全に過同期するため、各成分の分散比率に差が生まれず、PC1寄与率が `37.5%` 付近で完全に平坦（無変動）のまま沈黙するという「統計の死角」が発生します。
![Sample 9 PCA Ratio](Sample_9_fMRI_Seizure/readme_plots/000_2_2__principal_axes_ratio.png)

---

### 8. PCA固有ベクトル進化時系列 (`000_2_3__eigenvector_evolution.png`)
PCAの第1主成分（PC1）を構成する各ノードの固有ベクトル重み係数（Loading）の時系列推移を示したグラフです。

#### 🟢 Sample 0 (正常代謝)
**臨床解説:**
各ノードの固有ベクトル係数がなだらかに変動しており、特定の勘定科目に系のエネルギー支配軸が長期にわたって固着（偏在）することはありません。
![Sample 0 Eigenvector Evolution](Sample_0_Healthy/readme_plots/000_2_3__eigenvector_evolution.png)

#### 🟡 Sample 1 (循環取引)
**臨床解説:**
アノマリー期に PC1 のロードが `Accounts_Receivable` (`-0.7162`) と `Sales_Revenue` (`0.5183`)、および `Cash` (`0.3524`) に異常集中し、全活動がこの還流のみにハイジャックされた証拠を示します。
![Sample 1 Eigenvector Evolution](Sample_1_Wash_Trade/readme_plots/000_2_3__eigenvector_evolution.png)

#### 🔴 Sample 2 (資金横領)
**臨床解説:**
$t=4$ のアノマリー開始以降、流出先 `UNKNOWN_LEAK` と預金口座の係数が不可逆的に他ノードを圧倒し続け、資金の漏出トポロジーへの完全な固着（構造破壊）を証明します。
![Sample 2 Eigenvector Evolution](Sample_2_Embezzlement_Leak/readme_plots/000_2_3__eigenvector_evolution.png)

#### 🟡 Sample 3 (入力ミス)
**臨床解説:**
ミス発生期に `Accounts_Receivable` と `Sales_Revenue` のロードが跳ね上がりますが、エラー修正後はすぐに他の経費科目などへロードが正常分散されています。
![Sample 3 Eigenvector Evolution](Sample_3_Unbalanced_Mistake/readme_plots/000_2_3__eigenvector_evolution.png)

#### 🔴 Sample 4 (複合アノマリー)
**臨床解説:**
還流ノードの重み係数と、流出先 `UNKNOWN_LEAK` の重み係数の双方が異常なスパイクと偏在を持続的に形成し、複雑な不正の同時進行機序を裏付けています。
![Sample 4 Eigenvector Evolution](Sample_4_Composite_Chaos/readme_plots/000_2_3__eigenvector_evolution.png)

#### 🟢 Sample 6 (株券流体)
**臨床解説:**
固有ベクトル係数は時間とともに穏やかに分散して推移しており、特定の口座や銘柄への異常なエネルギー固着はありません。
![Sample 6 Eigenvector Evolution](Sample_6_Market_Stock_Flow/readme_plots/000_2_3__eigenvector_evolution.png)

#### 🟢 Sample 7 (現金流体)
**臨床解説:**
最終ステップ（$t=23$）に至るまで、PC1のロードは特定のユーザー口座に異常固着することなく、全域に穏やかに分散しています。
![Sample 7 Eigenvector Evolution](Sample_7_Market_Cash_Flow/readme_plots/000_2_3__eigenvector_evolution.png)

#### 🔴 Sample 8 (fMRI 脳梗塞)
**臨床解説:**
梗塞（$t=30$）の瞬間、PC1のロードが運動野（`Motor_Cortex`）および頂頭葉（`Parietal_Lobe`）に急激かつ永続的に固着し、脳の活動エネルギーの偏り（虚血ロック）を証明します。
![Sample 8 Eigenvector Evolution](Sample_8_fMRI_Stroke/readme_plots/000_2_3__eigenvector_evolution.png)

#### 🔴 Sample 9 (fMRI てんかん発作)
**臨床解説:**
てんかん同期中は全ノードが同一波形で同調するため、固有ベクトルのロードが全領域で完全にフラット（均等）な一本線にフリーズし、情報探索能力が皆無となった状態を示します。
![Sample 9 Eigenvector Evolution](Sample_9_fMRI_Seizure/readme_plots/000_2_3__eigenvector_evolution.png)
