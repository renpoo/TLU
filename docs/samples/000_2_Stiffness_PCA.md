# 000_2. Stiffness & PCA

This guide explains structural stiffness and PCA in Tensor-Link Utility (TLU).

---

## 000_2: Stiffness & PCA

### 6. Time-Series Stiffness Matrix (e.g., `000_2_1__structural_stiffness.t*.png`)

This matrix graph displays the spatiotemporal evolution of system stiffness. It is calculated from partial correlations and flux volatility.

#### 🟢 Sample 0 (Healthy Metabolism)
**Clinical Interpretation:**
The stiffness matrix remains uniform. No stiffness locks occur in specific transaction pairs.
- ![Sample 0 Stiffness Matrix](Sample_0_Healthy/readme_plots/000_2_1__structural_stiffness.t.00000.png)
- ![Sample 0 Stiffness Matrix](Sample_0_Healthy/readme_plots/000_2_1__structural_stiffness.t.00003.png)
- ![Sample 0 Stiffness Matrix](Sample_0_Healthy/readme_plots/000_2_1__structural_stiffness.t.00006.png)

#### 🟡 Sample 1 (Wash Trade)
**Clinical Interpretation:**
During wash trades ($t=0, t=4$), stiffness cells between `Cash` and `Accounts_Receivable` turn dark red, showing a stiffness lock.
- ![Sample 1 Stiffness t0](Sample_1_Wash_Trade/readme_plots/000_2_1__structural_stiffness.t.00000.png)
- ![Sample 1 Stiffness t3](Sample_1_Wash_Trade/readme_plots/000_2_1__structural_stiffness.t.00003.png)
- ![Sample 1 Stiffness t4](Sample_1_Wash_Trade/readme_plots/000_2_1__structural_stiffness.t.00004.png)
- ![Sample 1 Stiffness t5](Sample_1_Wash_Trade/readme_plots/000_2_1__structural_stiffness.t.00005.png)
- ![Sample 1 Stiffness t11](Sample_1_Wash_Trade/readme_plots/000_2_1__structural_stiffness.t.00011.png)

#### 🔴 Sample 2 (Embezzlement Leak)
**Clinical Interpretation:**
As embezzlement progresses from $t=4$, a stiffness lock forms between `Cash` and `UNKNOWN_LEAK`. The leak anomaly remains silent at $t=11$.
- ![Sample 2 Stiffness t0](Sample_2_Embezzlement_Leak/readme_plots/000_2_1__structural_stiffness.t.00000.png)
- ![Sample 2 Stiffness t1](Sample_2_Embezzlement_Leak/readme_plots/000_2_1__structural_stiffness.t.00001.png)
- ![Sample 2 Stiffness t2](Sample_2_Embezzlement_Leak/readme_plots/000_2_1__structural_stiffness.t.00002.png)
- ![Sample 2 Stiffness t3](Sample_2_Embezzlement_Leak/readme_plots/000_2_1__structural_stiffness.t.00003.png)
- ![Sample 2 Stiffness t4](Sample_2_Embezzlement_Leak/readme_plots/000_2_1__structural_stiffness.t.00004.png)
- ![Sample 2 Stiffness t11](Sample_2_Embezzlement_Leak/readme_plots/000_2_1__structural_stiffness.t.00011.png)

#### 🟡 Sample 3 (Unbalanced Bookkeeping Mistake)
**Clinical Interpretation:**
A transient stiffness distortion occurs at $t=1$ due to the one-sided entry mistake. After self-correction at $t=2$, the matrix returns to normal.
- ![Sample 3 Stiffness t0](Sample_3_Unbalanced_Mistake/readme_plots/000_2_1__structural_stiffness.t.00000.png)
- ![Sample 3 Stiffness t3](Sample_3_Unbalanced_Mistake/readme_plots/000_2_1__structural_stiffness.t.00003.png)
- ![Sample 3 Stiffness t4](Sample_3_Unbalanced_Mistake/readme_plots/000_2_1__structural_stiffness.t.00004.png)
- ![Sample 3 Stiffness t5](Sample_3_Unbalanced_Mistake/readme_plots/000_2_1__structural_stiffness.t.00005.png)
- ![Sample 3 Stiffness t11](Sample_3_Unbalanced_Mistake/readme_plots/000_2_1__structural_stiffness.t.00011.png)

#### 🔴 Sample 4 (Composite Chaos)
**Clinical Interpretation:**
Both the wash trade cells (`Cash`-`Accounts_Receivable`) and the embezzlement cells harden, showing structural collapse.
- ![Sample 4 Stiffness t0](Sample_4_Composite_Chaos/readme_plots/000_2_1__structural_stiffness.t.00000.png)
- ![Sample 4 Stiffness t3](Sample_4_Composite_Chaos/readme_plots/000_2_1__structural_stiffness.t.00003.png)
- ![Sample 4 Stiffness t4](Sample_4_Composite_Chaos/readme_plots/000_2_1__structural_stiffness.t.00004.png)
- ![Sample 4 Stiffness t5](Sample_4_Composite_Chaos/readme_plots/000_2_1__structural_stiffness.t.00005.png)
- ![Sample 4 Stiffness t8](Sample_4_Composite_Chaos/readme_plots/000_2_1__structural_stiffness.t.00008.png)
- ![Sample 4 Stiffness t11](Sample_4_Composite_Chaos/readme_plots/000_2_1__structural_stiffness.t.00011.png)

#### 🔴 Sample 5 (Kyoto Traffic)
**Clinical Interpretation:**
Stiffness is distributed normally at $t=6$. When the deadlock occurs ($t \ge 18$), cells around `23_Shijo_Karasuma` and `21_Shijo_Muromachi` turn dark red, showing a stiffness lock.
- ![Sample 5 Stiffness t0](Sample_5_Kyoto_Traffic/readme_plots/000_2_1__structural_stiffness.t.00000.png)
- ![Sample 5 Stiffness t6](Sample_5_Kyoto_Traffic/readme_plots/000_2_1__structural_stiffness.t.00006.png)
- ![Sample 5 Stiffness t12](Sample_5_Kyoto_Traffic/readme_plots/000_2_1__structural_stiffness.t.00012.png)
- ![Sample 5 Stiffness t18](Sample_5_Kyoto_Traffic/readme_plots/000_2_1__structural_stiffness.t.00018.png)
- ![Sample 5 Stiffness t23](Sample_5_Kyoto_Traffic/readme_plots/000_2_1__structural_stiffness.t.00023.png)

#### 🔴 Sample 8 (fMRI Stroke)
**Clinical Interpretation:**
At the stroke onset ($t=30$), stiffness between the motor cortex (`Motor_Cortex`) and parietal lobe spikes abnormally. The brain loses informational flexibility.
- ![Sample 8 Stiffness t0](Sample_8_fMRI_Stroke/readme_plots/000_2_1__structural_stiffness.t.00000.png)
- ![Sample 8 Stiffness t29](Sample_8_fMRI_Stroke/readme_plots/000_2_1__structural_stiffness.t.00029.png)
- ![Sample 8 Stiffness t31](Sample_8_fMRI_Stroke/readme_plots/000_2_1__structural_stiffness.t.00031.png)
- ![Sample 8 Stiffness t59](Sample_8_fMRI_Stroke/readme_plots/000_2_1__structural_stiffness.t.00059.png)

#### 🔴 Sample 9 (fMRI Seizure)
**Clinical Interpretation:**
Abnormal synchronous discharges freeze almost all stiffness matrix cells to their maximum value (dark red). The brain loses all cognitive degrees of freedom.
- ![Sample 9 Stiffness t0](Sample_9_fMRI_Seizure/readme_plots/000_2_1__structural_stiffness.t.00000.png)
- ![Sample 9 Stiffness t29](Sample_9_fMRI_Seizure/readme_plots/000_2_1__structural_stiffness.t.00029.png)
- ![Sample 9 Stiffness t31](Sample_9_fMRI_Seizure/readme_plots/000_2_1__structural_stiffness.t.00031.png)
- ![Sample 9 Stiffness t59](Sample_9_fMRI_Seizure/readme_plots/000_2_1__structural_stiffness.t.00059.png)

---

### 7. PCA Explained Variance Ratio (`000_2_2__principal_axes_ratio.png`)

Displays the cumulative explained variance ratio of PCA. It identifies if a few principal components dominate the system.

#### 🟢 Sample 0 (Healthy Metabolism)
**Clinical Interpretation:**
Variance ratios decay smoothly. The PC1 contribution is low, showing that energy is distributed.
- ![Sample 0 PCA Ratio](Sample_0_Healthy/readme_plots/000_2_2__principal_axes_ratio.png)

#### 🟡 Sample 1 (Wash Trade)
**Clinical Interpretation:**
The PC1 ratio jumps to **`95.28%`** during wash trading. This proves that circular matched orders dominate the system's energy.
- ![Sample 1 PCA Ratio](Sample_1_Wash_Trade/readme_plots/000_2_2__principal_axes_ratio.png)

#### 🔴 Sample 2 (Embezzlement Leak)
**Clinical Interpretation:**
As embezzlement progresses, the PC1 ratio rises. The system's energy is dominated by the `UNKNOWN_LEAK` and `Cash` accounts.
- ![Sample 2 PCA Ratio](Sample_2_Embezzlement_Leak/readme_plots/000_2_2__principal_axes_ratio.png)

#### 🟡 Sample 3 (Unbalanced Bookkeeping Mistake)
**Clinical Interpretation:**
The PC1 ratio transiently reaches **`100.0%`** around $t=1$. It returns to a healthy distribution after the error is corrected.
- ![Sample 3 PCA Ratio](Sample_3_Unbalanced_Mistake/readme_plots/000_2_2__principal_axes_ratio.png)

#### 🔴 Sample 4 (Composite Chaos)
**Clinical Interpretation:**
The PC1 ratio reaches **`100.0%`** at the peak of wash trading ($t=2$), proving that the circular loop dominates the system.
- ![Sample 4 PCA Ratio](Sample_4_Composite_Chaos/readme_plots/000_2_2__principal_axes_ratio.png)

#### 🟢 Sample 6 (Market Stock Flow)
**Clinical Interpretation:**
The PC1 ratio remains very low, showing that trading energy is distributed across multiple accounts.
- ![Sample 6 PCA Ratio](Sample_6_Market_Stock_Flow/readme_plots/000_2_2__principal_axes_ratio.png)

#### 🟢 Sample 7 (Market Cash Flow)
**Clinical Interpretation:**
The PC1 ratio stays low, indicating no liquidity locks or stiffness concentrations in specific accounts.
- ![Sample 7 PCA Ratio](Sample_7_Market_Cash_Flow/readme_plots/000_2_2__principal_axes_ratio.png)

#### 🔴 Sample 8 (fMRI Stroke)
**Clinical Interpretation:**
The PC1 ratio spikes at the onset of the stroke. System activities are dominated by the localized stiffness lock around the stroke focus.
- ![Sample 8 PCA Ratio](Sample_8_fMRI_Stroke/readme_plots/000_2_2__principal_axes_ratio.png)

#### 🔴 Sample 9 (fMRI Seizure)
**Clinical Interpretation:**
All brain regions sync during a seizure. Variance ratios show no distinction between components. The PC1 ratio remains flat around `37.5%`.
- ![Sample 9 PCA Ratio](Sample_9_fMRI_Seizure/readme_plots/000_2_2__principal_axes_ratio.png)

---

### 8. PCA Eigenvector Evolution (`000_2_3__eigenvector_evolution.png`)

Shows the time-series loadings of each node on the first principal component (PC1).

#### 🟢 Sample 0 (Healthy Metabolism)
**Clinical Interpretation:**
Loadings fluctuate smoothly. PC1 does not concentrate on specific accounts.
- ![Sample 0 Eigenvector Evolution](Sample_0_Healthy/readme_plots/000_2_3__eigenvector_evolution.png)

#### 🟡 Sample 1 (Wash Trade)
**Clinical Interpretation:**
During collusion, PC1 loadings concentrate on `Accounts_Receivable` (`-0.7162`), `Sales_Revenue` (`0.5183`), and `Cash` (`0.3524`), proving that wash trades dominate system energy.
- ![Sample 1 Eigenvector Evolution](Sample_1_Wash_Trade/readme_plots/000_2_3__eigenvector_evolution.png)

#### 🔴 Sample 2 (Embezzlement Leak)
**Clinical Interpretation:**
After the leak starts ($t=4$), loadings on `UNKNOWN_LEAK` and `Cash` dominate the network. This indicates structural collapse.
- ![Sample 2 Eigenvector Evolution](Sample_2_Embezzlement_Leak/readme_plots/000_2_3__eigenvector_evolution.png)

#### 🟡 Sample 3 (Unbalanced Bookkeeping Mistake)
**Clinical Interpretation:**
Loadings on `Accounts_Receivable` and `Sales_Revenue` spike during the error step. They disperse to normal levels after correction.
- ![Sample 3 Eigenvector Evolution](Sample_3_Unbalanced_Mistake/readme_plots/000_2_3__eigenvector_evolution.png)

#### 🔴 Sample 4 (Composite Chaos)
**Clinical Interpretation:**
Loadings concentrate persistently on both circular wash trade nodes and the embezzlement node `UNKNOWN_LEAK`, indicating complex parallel fraud.
- ![Sample 4 Eigenvector Evolution](Sample_4_Composite_Chaos/readme_plots/000_2_3__eigenvector_evolution.png)

#### 🟢 Sample 6 (Market Stock Flow)
**Clinical Interpretation:**
Loadings remain dispersed over time. Energy does not concentrate on specific accounts or tickers.
- ![Sample 6 Eigenvector Evolution](Sample_6_Market_Stock_Flow/readme_plots/000_2_3__eigenvector_evolution.png)

#### 🟢 Sample 7 (Market Cash Flow)
**Clinical Interpretation:**
PC1 loadings stay dispersed across all user accounts up to the final step ($t=23$).
- ![Sample 7 Eigenvector Evolution](Sample_7_Market_Cash_Flow/readme_plots/000_2_3__eigenvector_evolution.png)

#### 🔴 Sample 8 (fMRI Stroke)
**Clinical Interpretation:**
At the stroke onset ($t=30$), PC1 loadings freeze on the motor cortex (`Motor_Cortex`) and parietal lobe (`Parietal_Lobe`), showing a localized ischemia lock.
- ![Sample 8 Eigenvector Evolution](Sample_8_fMRI_Stroke/readme_plots/000_2_3__eigenvector_evolution.png)

#### 🔴 Sample 9 (fMRI Seizure)
**Clinical Interpretation:**
During a seizure, all nodes synch. Loadings freeze into flat, uniform lines across all regions. The brain loses its informational capacity.
- ![Sample 9 Eigenvector Evolution](Sample_9_fMRI_Seizure/readme_plots/000_2_3__eigenvector_evolution.png)
