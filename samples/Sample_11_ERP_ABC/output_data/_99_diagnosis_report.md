# TLU Meta-Diagnosis Report (Descriptive Statistics V3)

**Target Environment:** `samples/Sample_11_ERP_ABC`
**Date Analyzed:** 2026-07-31 12:16:00

## 1. Final Diagnosis

### ⚠️ COMPOSITE PATHOLOGY DETECTED
The system is suffering from multiple overlapping structural failures.

### 🔴 Fat-Tailed Entropy Spikes (Systemic Flash Crashes)
- **Severity:** CRITICAL
- **Evidence:** Kurtosis: 5.21, Anomalies (Z>3): 1 times.
- **Interpretation:** The system experiences sudden, extreme bursts of friction (Black Swan events). The distribution is heavy-tailed, indicating unpredictable structural tearing rather than steady friction.

### 🟠 Abnormal Synchronization (Negative Entropy Skew)
- **Severity:** HIGH
- **Evidence:** Entropy Skewness: -2.49.
- **Interpretation:** Entropy occasionally drops far below its median, suggesting periodic forced synchronization (e.g., market manipulation or forced liquidation).

---
## 2. Comprehensive Descriptive Statistics Table

The table below details the descriptive statistics computed individually for all active analytical scales across the TLU mathematical modules:

| Measure / Scale | Mean | Median | Mode (count / total, %) | Min | Max | Range | IQR | Std Dev | Skewness | Kurtosis | Z-Exceed |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Dynamics: acceleration_a | 0.0000 | 0.0000 | 0.0000 (82/192, 42.7%) | -121597.2500 | 116149.4500 | 237746.7000 | 6518.2700 | 29845.9724 | -0.3252 | 5.5499 | 8 |
| Dynamics: jerk_j | -0.0000 | 0.0000 | 0.0000 (92/192, 47.9%) | -204881.5100 | 152359.2900 | 357240.8000 | 3280.4275 | 39639.2991 | -0.5646 | 6.6341 | 4 |
| Dynamics: snap_s | -0.0000 | 0.0000 | 0.0000 (102/192, 53.1%) | -313772.3400 | 271728.0100 | 585500.3500 | 0.0000 | 62833.9196 | -0.1452 | 8.3317 | 6 |
| Dynamics: state_X | 250000.0000 | 64690.7250 | 0.0000 (24/192, 12.5%) | -1433745.1100 | 2000000.0000 | 3433745.1100 | 504013.3475 | 609895.3174 | 1.0547 | 2.6751 | 0 |
| Dynamics: velocity_v | 0.0000 | 0.0000 | 0.0000 (72/192, 37.5%) | -184561.5600 | 143430.1600 | 327991.7200 | 17174.7575 | 47899.8286 | -0.8541 | 3.4207 | 4 |
| Dynamics: viscosity_C | 37927.0223 | 16289.9950 | 0.0000 (24/192, 12.5%) | 0.0000 | 200000.0000 | 200000.0000 | 45880.2651 | 51485.0162 | 2.0215 | 3.5618 | 12 |
| Forensics: conservation_residual | 0.0000 | 0.0000 | 0.0000 (12/12, 100.0%) | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | nan | nan | 0 |
| Forensics: kl_divergence_drift | 0.2827 | 0.0682 | -0.1080 (1/12, 8.3%) | -0.1078 | 2.0203 | 2.1281 | 0.2149 | 0.5787 | 2.5056 | 5.1142 | 1 |
| Stability: spectral_radius | 0.0000 | 0.0000 | 0.0000 (12/12, 100.0%) | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | nan | nan | 0 |
| Stiffness: partial_corr | 0.0753 | 0.0000 | 0.0000 (1636/3072, 53.3%) | -1.0000 | 1.0000 | 2.0000 | 0.2744 | 0.5695 | -0.0240 | -0.3464 | 0 |
| Stiffness: stiffness_k | -0.0000 | 0.0000 | 0.0000 (3072/3072, 100.0%) | -0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.0823 | 206.6272 | 34 |
| Thermo: entropy_S | 3.1100 | 3.1747 | 3.2000 (3/12, 25.0%) | 2.0553 | 3.3561 | 1.3008 | 0.1764 | 0.3504 | -2.4916 | 5.2065 | 1 |
| Thermo: free_energy_F | 5194616.2 | 5081556.2 | 4049318.0 (1/12, 8.3%) | 4049318.4 | 7103201.8 | 3053883.4 | 1453720.4 | 952987.7 | 0.5497 | -0.7329 | 0 |
| Thermo: gross_activity_U | 6444895.2 | 6379993.6 | 4586809.0 (1/12, 8.3%) | 4586809.3 | 7916715.2 | 3329905.8 | 1803969.1 | 1100067.3 | -0.1538 | -1.2723 | 0 |
| Thermo: temperature_T | 399995.2778 | 426622.9842 | 0.0000 (1/12, 8.3%) | 0.0000 | 524362.6570 | 524362.6570 | 78423.7049 | 140822.4526 | -2.0480 | 3.6194 | 0 |
| Topology: stress | 2.3363 | 0.8398 | 0.0000 (28/176, 15.9%) | 0.0000 | 77.8671 | 77.8671 | 1.9052 | 6.5523 | 9.2396 | 100.1002 | 2 |
| Topology: weight | 49215.4698 | 30602.4850 | 2818.3800 (1/176, 0.6%) | 2818.3800 | 184561.5600 | 181743.1800 | 59807.2075 | 42274.4535 | 1.1902 | 0.9036 | 2 |

---
## 3. Structural Evolution (Viscosity Classification)

- **Viscosity Range:** `458680.93 ~ 764784.00`
  - 🩸 **Diagnosis:** Thrombosis / High-Friction (Old-Generation Structure). The system relies on manual/human friction.

---
## 4. Quartile-based Diagnostic Candidates

### ⚠️ Shoulder Stiffness (Chronic Delay/Viscosity >= Q3: `41767.0743`)
| Node | Average Viscosity | Peak Time | Peak Viscosity |
| :--- | :---: | :---: | :---: |
| `12_ACC_Cash` | 100000.0000 | `2020-01` | 100000.0000 |
| `09_ACC_Sales_Revenue_DPT_Sales` | 68738.8828 | `2020-12` | 131996.7315 |
| `13_ACC_Raw_Materials` | 50000.0000 | `2020-01` | 50000.0000 |
| `14_ACC_Finished_Goods` | 50000.0000 | `2020-01` | 50000.0000 |

### 🎯 Acupuncture Points (Tsubo/Strain <= Q1: `4.1308`)
| Node | Average Strain Energy |
| :--- | :---: |
| `02_ACC_COGS_DPT_Prod_A` | 2.6811 |
| `05_ACC_Finished_Goods_DPT_Prod_A` | 2.8400 |
| `03_ACC_COGS_DPT_Prod_B` | 3.4321 |
| `10_ACC_Work_In_Process_DPT_Prod_A` | 3.8788 |

### 🚫 Contraindications (Kinki/Strain >= Q3: `8.3317` or limit)
| Node | Average Strain Energy |
| :--- | :---: |
| `09_ACC_Sales_Revenue_DPT_Sales` | 8.3336 |
| `12_ACC_Cash` | 8.3317 |
| `13_ACC_Raw_Materials` | 8.3317 |
| `14_ACC_Finished_Goods` | 8.3317 |
| `15_ACC_Equity_Capital` | 8.3317 |

> *Generated automatically by the TLU Meta-Diagnosis Engine (Descriptive Statistics V3).* 

