# TLU Meta-Diagnosis Report (Descriptive Statistics V3)

**Target Environment:** `samples/Sample_2_Embezzlement_Leak`
**Date Analyzed:** 2026-07-06 07:15:44

## 1. Final Diagnosis

### 🔴 Mass Conservation Violation (Leakage)
- **Severity:** CRITICAL
- **Evidence:** Relative Leak Ratio: 0.000111.
- **Interpretation:** Systemic flux is disappearing or materializing from nowhere.

---
## 2. Comprehensive Descriptive Statistics Table

The table below details the descriptive statistics computed individually for all active analytical scales across the TLU mathematical modules:

| Measure / Scale | Mean | Median | Mode (count / total, %) | Min | Max | Range | IQR | Std Dev | Skewness | Kurtosis | Z-Exceed |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Dynamics: acceleration_a | 0.0000 | 0.0000 | 0.0000 (25/132, 18.9%) | -88679.1300 | 72837.3800 | 161516.5100 | 5986.1150 | 24407.3373 | -0.6322 | 3.0307 | 1 |
| Dynamics: state_X | 181818.1818 | 92479.1100 | 1000000.0000 (12/132, 9.1%) | -955157.5600 | 1000000.0000 | 1955157.5600 | 452553.7200 | 392954.6133 | 0.0460 | 0.9554 | 0 |
| Dynamics: velocity_v | -0.0000 | 4727.3800 | 0.0000 (19/132, 14.4%) | -124227.2200 | 96581.3900 | 220808.6100 | 23939.4375 | 37127.1973 | -0.8501 | 2.1324 | 3 |
| Dynamics: viscosity_C | 28134.1313 | 14424.8384 | 100000.0000 (12/132, 9.1%) | 0.0000 | 100000.0000 | 100000.0000 | 41795.8723 | 30480.3723 | 1.1760 | 0.3341 | 0 |
| Forensics: conservation_residual | 112.7900 | 0.0000 | 0.0000 (7/12, 58.3%) | 0.0000 | 364.5300 | 364.5300 | 272.3800 | 158.3409 | 0.7517 | -1.2984 | 0 |
| Forensics: kl_divergence_drift | 0.1683 | 0.0343 | -0.4640 (1/12, 8.3%) | -0.4635 | 1.1792 | 1.6427 | 0.1089 | 0.4329 | 1.2692 | 1.0471 | 0 |
| Stability: spectral_radius | 0.0000 | 0.0000 | 0.0000 (12/12, 100.0%) | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | nan | nan | 0 |
| Stiffness: partial_corr | 0.1306 | 0.0000 | 0.0000 (460/1452, 31.7%) | -1.0000 | 1.0000 | 2.0000 | 1.0503 | 0.6922 | -0.2008 | -1.1494 | 0 |
| Stiffness: stiffness_k | -0.0000 | 0.0000 | 0.0000 (1452/1452, 100.0%) | -0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.2028 | 23.4628 | 41 |
| Thermo: entropy_S | 1.4925 | 1.4661 | 1.4000 (3/12, 25.0%) | 1.1654 | 1.8832 | 0.7178 | 0.2712 | 0.2405 | 0.3873 | -0.9200 | 0 |
| Thermo: free_energy_F | 2944448.0 | 2893947.9 | 2215302.0 (1/12, 8.3%) | 2215302.0 | 3824909.9 | 1609607.9 | 959409.4 | 560199.5 | 0.1674 | -1.3717 | 0 |
| Thermo: gross_activity_U | 3297679.6 | 3267881.8 | 2303842.0 (1/12, 8.3%) | 2303842.3 | 4087077.4 | 1783235.1 | 915676.4 | 588279.2 | -0.1645 | -1.2313 | 0 |
| Thermo: temperature_T | 237145.8378 | 253001.2908 | 0.0000 (1/12, 8.3%) | 0.0000 | 319277.4547 | 319277.4547 | 48616.9880 | 83935.0431 | -1.9480 | 3.5277 | 0 |
| Topology: stress | 1.9184 | 0.9767 | 0.0000 (16/99, 16.2%) | 0.0000 | 15.7769 | 15.7769 | 2.0470 | 2.8144 | 2.8991 | 10.0249 | 3 |
| Topology: weight | 38895.5195 | 30465.7300 | 61.1800 (1/99, 1.0%) | 61.1800 | 129251.1200 | 129189.9400 | 49179.3150 | 32993.2285 | 0.8295 | -0.0373 | 0 |

---
## 3. Structural Evolution (Viscosity Classification)

- **Viscosity Range:** `230384.23 ~ 394457.53`
  - 🩸 **Diagnosis:** Thrombosis / High-Friction (Old-Generation Structure). The system relies on manual/human friction.

---
## 4. Quartile-based Diagnostic Candidates

### ⚠️ Shoulder Stiffness (Chronic Delay/Viscosity >= Q3: `40246.5119`)
| Node | Average Viscosity | Peak Time | Peak Viscosity |
| :--- | :---: | :---: | :---: |
| `04_ACC_Inventory` | 52569.2200 | `2020-12` | 57275.0845 |
| `03_ACC_Cash` | 45680.1844 | `2020-06` | 47887.2388 |
| `07_ACC_Sales_Revenue` | 45422.2270 | `2020-12` | 87430.7585 |

### 🎯 Acupuncture Points (Tsubo/Strain <= Q1: `5.6154`)
| Node | Average Strain Energy |
| :--- | :---: |
| `02_ACC_COGS` | 3.6526 |
| `04_ACC_Inventory` | 4.6059 |
| `01_ACC_Accounts_Receivable` | 5.0984 |

### 🚫 Contraindications (Kinki/Strain >= Q3: `8.3408` or limit)
| Node | Average Strain Energy |
| :--- | :---: |
| `09_UNKNOWN_LEAK` | 9.7349 |
| `07_ACC_Sales_Revenue` | 8.7620 |
| `06_ACC_Rent_Exp` | 8.3500 |

> *Generated automatically by the TLU Meta-Diagnosis Engine (Descriptive Statistics V3).* 

