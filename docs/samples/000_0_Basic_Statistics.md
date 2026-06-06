# 000_0. Basic Statistics & Foundations

This guide explains basic statistics in Tensor-Link Utility (TLU).

---

## 000_0: Basic Statistics

### 1. Financial Statement Structure (B/S & P/L)

The B/S block total chart (`000_0_1__BS_Block_Total.png`) visualizes the B/S balance. The P/L waterfall chart (`000_0_1__PL_Waterfall_Total.png`) shows the profit structure. We compare these charts to evaluate the macro structure of the system.

#### 🟢 Sample 0 (Healthy Metabolism)
**Clinical Interpretation:**
Assets, liabilities, and equity balance symmetrically. Expenses subtract from revenues, leaving net income. The basic structure is healthy.
- ![Sample 0 BS Block Total](Sample_0_Healthy/readme_plots/000_0_1__BS_Block_Total.png)
- ![Sample 0 PL Waterfall](Sample_0_Healthy/readme_plots/000_0_1__PL_Waterfall_Total.png)

#### 🟡 Sample 1 (Wash Trade)
**Clinical Interpretation:**
Accounts receivable are bloated. The P/L displays large revenues but minimal expenses. This indicates circular matched trades to create sham profits.
- ![Sample 1 BS Block Total](Sample_1_Wash_Trade/readme_plots/000_0_1__BS_Block_Total.png)
- ![Sample 1 PL Waterfall](Sample_1_Wash_Trade/readme_plots/000_0_1__PL_Waterfall_Total.png)

#### 🔴 Sample 2 (Embezzlement Leak)
**Clinical Interpretation:**
Revenues are recorded normally. However, cash vanishes off-book during recovery. Cash on hand is depleted. A dummy `UNKNOWN_LEAK` asset node replaces the lost cash.
- ![Sample 2 BS Block Total](Sample_2_Embezzlement_Leak/readme_plots/000_0_1__BS_Block_Total.png)
- ![Sample 2 PL Waterfall](Sample_2_Embezzlement_Leak/readme_plots/000_0_1__PL_Waterfall_Total.png)

#### 🟡 Sample 3 (Unbalanced Bookkeeping Mistake)
**Clinical Interpretation:**
A transient bookkeeping mistake where only one side of a transaction is entered. The B/S is unbalanced, leaving a residual. Operating revenues remain normal.
- ![Sample 3 BS Block Total](Sample_3_Unbalanced_Mistake/readme_plots/000_0_1__BS_Block_Total.png)
- ![Sample 3 PL Waterfall](Sample_3_Unbalanced_Mistake/readme_plots/000_0_1__PL_Waterfall_Total.png)

#### 🔴 Sample 4 (Composite Chaos)
**Clinical Interpretation:**
Circular wash trading inflates receivables, while embezzlement drains cash. System bloat and active bleeding occur simultaneously.
- ![Sample 4 BS Block Total](Sample_4_Composite_Chaos/readme_plots/000_0_1__BS_Block_Total.png)
- ![Sample 4 PL Waterfall](Sample_4_Composite_Chaos/readme_plots/000_0_1__PL_Waterfall_Total.png)

#### 🔴 Sample 5 (Kyoto Traffic)
**Clinical Interpretation:**
Shows vehicle accumulation and flow balance at intersections. Vehicles concentrate at major intersections. The flow capacity collapsed due to blockages.
- ![Sample 5 BS Block Total](Sample_5_Kyoto_Traffic/readme_plots/000_0_1__BS_Block_Total.png)
- ![Sample 5 PL Waterfall](Sample_5_Kyoto_Traffic/readme_plots/000_0_1__PL_Waterfall_Total.png)

#### 🟢 Sample 6 (Market Stock Flow)
**Clinical Interpretation:**
Shows stock holding balances and trading volume. Volume is high, but real stock transfers are close to zero. Convection remains stable among USRs.
- ![Sample 6 BS Block Total](Sample_6_Market_Stock_Flow/readme_plots/000_0_1__BS_Block_Total.png)
- ![Sample 6 PL Waterfall](Sample_6_Market_Stock_Flow/readme_plots/000_0_1__PL_Waterfall_Total.png)

#### 🟢 Sample 7 (Market Cash Flow)
**Clinical Interpretation:**
Shows cash holding balances and direct cash flow volume. Media of exchange function is stable between accounts. There are no residuals.
- ![Sample 7 BS Block Total](Sample_7_Market_Cash_Flow/readme_plots/000_0_1__BS_Block_Total.png)
- ![Sample 7 PL Waterfall](Sample_7_Market_Cash_Flow/readme_plots/000_0_1__PL_Waterfall_Total.png)

#### 🔴 Sample 8 (fMRI Stroke)
**Clinical Interpretation:**
Shows BOLD signals and activity balance across brain regions. Signals in the motor cortex drop severely. This localized loss pulls down the total brain activity balance.
- ![Sample 8 BS Block Total](Sample_8_fMRI_Stroke/readme_plots/000_0_1__BS_Block_Total.png)
- ![Sample 8 PL Waterfall](Sample_8_fMRI_Stroke/readme_plots/000_0_1__PL_Waterfall_Total.png)

#### 🔴 Sample 9 (fMRI Seizure)
**Clinical Interpretation:**
Shows neural activity intensity and balance. Activity in the temporal lobe dominates the total oxygen resource. Pathological synchrony depletes overall cognitive potential.
- ![Sample 9 BS Block Total](Sample_9_fMRI_Seizure/readme_plots/000_0_1__BS_Block_Total.png)
- ![Sample 9 PL Waterfall](Sample_9_fMRI_Seizure/readme_plots/000_0_1__PL_Waterfall_Total.png)

---

### 2. Time-Series Trends (B/S & P/L Trends)

We compare cumulative trends (`BS_Trend` / `PL_Trend`) with periodic changes (`BS_Trend_Periodic` / `PL_Trend_Periodic`).

#### 🟢 Sample 0 (Healthy Metabolism)
**Clinical Interpretation:**
Revenues and expenses change in sync. Net income grows steadily over time.
- ![Sample 0 BS Trend](Sample_0_Healthy/readme_plots/000_0_1__BS_Trend.png)
- ![Sample 0 PL Trend](Sample_0_Healthy/readme_plots/000_0_1__PL_Trend.png)
- ![Sample 0 BS Trend Periodic](Sample_0_Healthy/readme_plots/000_0_1__BS_Trend_Periodic.png)
- ![Sample 0 PL Trend Periodic](Sample_0_Healthy/readme_plots/000_0_1__PL_Trend_Periodic.png)

#### 🟡 Sample 1 (Wash Trade)
**Clinical Interpretation:**
Revenues and receivables grow linearly. However, periodic expenses stay completely flat. The natural volatility of commercial transactions is missing.
- ![Sample 1 BS Trend](Sample_1_Wash_Trade/readme_plots/000_0_1__BS_Trend.png)
- ![Sample 1 PL Trend](Sample_1_Wash_Trade/readme_plots/000_0_1__PL_Trend.png)
- ![Sample 1 BS Trend Periodic](Sample_1_Wash_Trade/readme_plots/000_0_1__BS_Trend_Periodic.png)
- ![Sample 1 PL Trend Periodic](Sample_1_Wash_Trade/readme_plots/000_0_1__PL_Trend_Periodic.png)

#### 🔴 Sample 2 (Embezzlement Leak)
**Clinical Interpretation:**
Cash decreases steadily over time. The P/L shows cumulative profits. Cash increases are abnormally low during receivable collection steps. Capital leaks off-book repeatedly.
- ![Sample 2 BS Trend](Sample_2_Embezzlement_Leak/readme_plots/000_0_1__BS_Trend.png)
- ![Sample 2 PL Trend](Sample_2_Embezzlement_Leak/readme_plots/000_0_1__PL_Trend.png)
- ![Sample 2 BS Trend Periodic](Sample_2_Embezzlement_Leak/readme_plots/000_0_1__BS_Trend_Periodic.png)
- ![Sample 2 PL Trend Periodic](Sample_2_Embezzlement_Leak/readme_plots/000_0_1__PL_Trend_Periodic.png)

#### 🟡 Sample 3 (Unbalanced Bookkeeping Mistake)
**Clinical Interpretation:**
At $t=1$ (2020-02), an unbalanced entry error occurs. Periodic trends display sudden spikes. The error is corrected in the next step, absorbing the transient impact.
- ![Sample 3 BS Trend](Sample_3_Unbalanced_Mistake/readme_plots/000_0_1__BS_Trend.png)
- ![Sample 3 PL Trend](Sample_3_Unbalanced_Mistake/readme_plots/000_0_1__PL_Trend.png)
- ![Sample 3 BS Trend Periodic](Sample_3_Unbalanced_Mistake/readme_plots/000_0_1__BS_Trend_Periodic.png)
- ![Sample 3 PL Trend Periodic](Sample_3_Unbalanced_Mistake/readme_plots/000_0_1__PL_Trend_Periodic.png)

#### 🔴 Sample 4 (Composite Chaos)
**Clinical Interpretation:**
Receivables and profits accumulate from wash trades. At the same time, cash leaks off-book. Window-dressing and real cash drain contrast sharply.
- ![Sample 4 BS Trend](Sample_4_Composite_Chaos/readme_plots/000_0_1__BS_Trend.png)
- ![Sample 4 PL Trend](Sample_4_Composite_Chaos/readme_plots/000_0_1__PL_Trend.png)
- ![Sample 4 BS Trend Periodic](Sample_4_Composite_Chaos/readme_plots/000_0_1__BS_Trend_Periodic.png)
- ![Sample 4 PL Trend Periodic](Sample_4_Composite_Chaos/readme_plots/000_0_1__PL_Trend_Periodic.png)

#### 🔴 Sample 5 (Kyoto Traffic)
**Clinical Interpretation:**
Shows vehicle inflow and congestion losses. When the anomaly is injected, vehicle counts rise, and periodic delays expand. The flow potential drops.
- ![Sample 5 BS Trend](Sample_5_Kyoto_Traffic/readme_plots/000_0_1__BS_Trend.png)
- ![Sample 5 PL Trend](Sample_5_Kyoto_Traffic/readme_plots/000_0_1__PL_Trend.png)
- ![Sample 5 BS Trend Periodic](Sample_5_Kyoto_Traffic/readme_plots/000_0_1__BS_Trend_Periodic.png)
- ![Sample 5 PL Trend Periodic](Sample_5_Kyoto_Traffic/readme_plots/000_0_1__PL_Trend_Periodic.png)

#### 🟢 Sample 6 (Market Stock Flow)
**Clinical Interpretation:**
Shows trade volumes and stock holdings. Cumulative volume rises. Convection occurs periodically, and stock balances stay stable.
- ![Sample 6 BS Trend](Sample_6_Market_Stock_Flow/readme_plots/000_0_1__BS_Trend.png)
- ![Sample 6 PL Trend](Sample_6_Market_Stock_Flow/readme_plots/000_0_1__PL_Trend.png)
- ![Sample 6 BS Trend Periodic](Sample_6_Market_Stock_Flow/readme_plots/000_0_1__BS_Trend_Periodic.png)
- ![Sample 6 PL Trend Periodic](Sample_6_Market_Stock_Flow/readme_plots/000_0_1__PL_Trend_Periodic.png)

#### 🟢 Sample 7 (Market Cash Flow)
**Clinical Interpretation:**
Shows cash holdings and direct cash transfer volumes. Both cumulative and periodic trends show no abnormalities or sudden drops. Convection balances remain stable.
- ![Sample 7 BS Trend](Sample_7_Market_Cash_Flow/readme_plots/000_0_1__BS_Trend.png)
- ![Sample 7 PL Trend](Sample_7_Market_Cash_Flow/readme_plots/000_0_1__PL_Trend.png)
- ![Sample 7 BS Trend Periodic](Sample_7_Market_Cash_Flow/readme_plots/000_0_1__BS_Trend_Periodic.png)
- ![Sample 7 PL Trend Periodic](Sample_7_Market_Cash_Flow/readme_plots/000_0_1__PL_Trend_Periodic.png)

#### 🔴 Sample 8 (fMRI Stroke)
**Clinical Interpretation:**
BOLD signal cumulative trends turn negative after `t=30` (TR=150). Periodic charts show a sharp drop in blood flow during the stroke, remaining flat thereafter.
- ![Sample 8 BS Trend](Sample_8_fMRI_Stroke/readme_plots/000_0_1__BS_Trend.png)
- ![Sample 8 PL Trend](Sample_8_fMRI_Stroke/readme_plots/000_0_1__PL_Trend.png)
- ![Sample 8 BS Trend Periodic](Sample_8_fMRI_Stroke/readme_plots/000_0_1__BS_Trend_Periodic.png)
- ![Sample 8 PL Trend Periodic](Sample_8_fMRI_Stroke/readme_plots/000_0_1__PL_Trend_Periodic.png)

#### 🔴 Sample 9 (fMRI Seizure)
**Clinical Interpretation:**
Shows BOLD signal intensities during epilepsy. The cumulative potential decreases. Periodic trends show continuous signal oscillations matching the seizure cycles.
- ![Sample 9 BS Trend](Sample_9_fMRI_Seizure/readme_plots/000_0_1__BS_Trend.png)
- ![Sample 9 PL Trend](Sample_9_fMRI_Seizure/readme_plots/000_0_1__PL_Trend.png)
- ![Sample 9 BS Trend Periodic](Sample_9_fMRI_Seizure/readme_plots/000_0_1__BS_Trend_Periodic.png)
- ![Sample 9 PL Trend Periodic](Sample_9_fMRI_Seizure/readme_plots/000_0_1__PL_Trend_Periodic.png)
