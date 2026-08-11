# TLU Meta-Diagnosis Report (Descriptive Statistics V3)

**Target Environment:** `samples/Sample_12_ERP_TABC`
**Date Analyzed:** 2026-08-11 16:52:37

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
| Dynamics: acceleration_a | 0.0000 | 0.0000 | 0.0000 (82/192, 42.7%) | -121597.2500 | 116149.4500 | 237746.7000 | 5920.7600 | 29774.6619 | -0.3242 | 5.6205 | 8 |
| Dynamics: jerk_j | -0.0000 | 0.0000 | 0.0000 (92/192, 47.9%) | -204881.5100 | 152359.2900 | 357240.8000 | 3653.1200 | 39559.2182 | -0.5668 | 6.7055 | 4 |
| Dynamics: snap_s | -0.0000 | 0.0000 | 0.0000 (102/192, 53.1%) | -313772.3400 | 271728.0100 | 585500.3500 | 0.0000 | 62738.0593 | -0.1471 | 8.3960 | 6 |
| Dynamics: state_X | 250000.0000 | 58954.4850 | 0.0000 (24/192, 12.5%) | -1433745.1100 | 2000000.0000 | 3433745.1100 | 510120.6575 | 608907.0227 | 1.0588 | 2.7098 | 0 |
| Dynamics: velocity_v | 0.0000 | 0.0000 | 0.0000 (72/192, 37.5%) | -184561.5600 | 143430.1600 | 327991.7200 | 14133.3900 | 47660.4669 | -0.8912 | 3.4976 | 7 |
| Dynamics: viscosity_C | 37942.8240 | 16289.9950 | 0.0000 (24/192, 12.5%) | 0.0000 | 200000.0000 | 200000.0000 | 45827.2434 | 51392.8863 | 2.0340 | 3.6030 | 12 |
| Forensics: conservation_residual | 0.0000 | 0.0000 | 0.0000 (12/12, 100.0%) | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | nan | nan | 0 |
| Forensics: kl_divergence_drift | 0.2447 | 0.0366 | 0.0000 (1/12, 8.3%) | 0.0000 | 1.2184 | 1.2184 | 0.1747 | 0.4323 | 1.6190 | 0.8846 | 0 |
| Stability: spectral_radius | 0.0000 | 0.0000 | 0.0000 (12/12, 100.0%) | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | nan | nan | 0 |
| Stiffness: partial_corr | 0.0761 | 0.0000 | 0.0000 (1636/3072, 53.3%) | -1.0000 | 1.0000 | 2.0000 | 0.2529 | 0.5679 | -0.0194 | -0.3370 | 0 |
| Stiffness: stiffness_k | -0.0000 | 0.0000 | 0.0000 (3072/3072, 100.0%) | -0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.3863 | 221.0154 | 33 |
| Thermo: entropy_S | 3.1100 | 3.1747 | 3.2000 (3/12, 25.0%) | 2.0553 | 3.3561 | 1.3008 | 0.1764 | 0.3504 | -2.4916 | 5.2065 | 1 |
| Thermo: free_energy_F | 5194413.1 | 5083643.7 | 4043663.0 (1/12, 8.3%) | 4043663.2 | 7106312.4 | 3062649.3 | 1446068.9 | 952841.7 | 0.5515 | -0.7212 | 0 |
| Thermo: gross_activity_U | 6447177.2 | 6379993.6 | 4586809.0 (1/12, 8.3%) | 4586809.3 | 7916715.2 | 3329905.8 | 1795170.7 | 1097985.6 | -0.1560 | -1.2644 | 0 |
| Thermo: temperature_T | 400747.0044 | 428490.1347 | 0.0000 (1/12, 8.3%) | 0.0000 | 526625.2143 | 526625.2143 | 81963.5671 | 141245.3115 | -2.0374 | 3.5918 | 0 |
| Topology: stress | 2.2658 | 0.8521 | 0.0000 (28/176, 15.9%) | 0.0000 | 77.8671 | 77.8671 | 1.8517 | 6.3361 | 9.9106 | 113.8221 | 1 |
| Topology: weight | 48871.2641 | 30602.4850 | 2818.3800 (1/176, 0.6%) | 2818.3800 | 184561.5600 | 181743.1800 | 61095.2425 | 42562.9105 | 1.1734 | 0.8557 | 2 |

---
## 3. Structural Evolution (Viscosity Classification)

- **Viscosity Range:** `458680.93 ~ 764784.00`
  - 🩸 **Diagnosis:** Thrombosis / High-Friction (Old-Generation Structure). The system relies on manual/human friction.

---
## 4. Quartile-based Diagnostic Candidates

### ⚠️ Shoulder Stiffness (Chronic Delay/Viscosity >= Q3: `41026.7225`)
| Node | Average Viscosity | Peak Time | Peak Viscosity |
| :--- | :---: | :---: | :---: |
| `12_ACC_Cash` | 100000.0000 | `2020-01` | 100000.0000 |
| `09_ACC_Sales_Revenue_DPT_Sales` | 68738.8828 | `2020-12` | 131996.7315 |
| `13_ACC_Raw_Materials` | 50000.0000 | `2020-01` | 50000.0000 |
| `14_ACC_Finished_Goods` | 50000.0000 | `2020-01` | 50000.0000 |

### 🎯 Acupuncture Points (Tsubo/Strain <= Q1: `4.1306`)
| Node | Average Strain Energy |
| :--- | :---: |
| `02_ACC_COGS_DPT_Prod_A` | 2.6807 |
| `05_ACC_Finished_Goods_DPT_Prod_A` | 2.8400 |
| `03_ACC_COGS_DPT_Prod_B` | 3.4319 |
| `10_ACC_Work_In_Process_DPT_Prod_A` | 3.8786 |

### 🚫 Contraindications (Kinki/Strain >= Q3: `8.3317` or limit)
| Node | Average Strain Energy |
| :--- | :---: |
| `09_ACC_Sales_Revenue_DPT_Sales` | 8.3334 |
| `12_ACC_Cash` | 8.3317 |
| `13_ACC_Raw_Materials` | 8.3317 |
| `14_ACC_Finished_Goods` | 8.3317 |
| `15_ACC_Equity_Capital` | 8.3317 |

> *Generated automatically by the TLU Meta-Diagnosis Engine (Descriptive Statistics V3).* 

