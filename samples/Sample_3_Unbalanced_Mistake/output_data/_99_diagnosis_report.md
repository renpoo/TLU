# TLU Meta-Diagnosis Report (Descriptive Statistics V3)

**Target Environment:** `samples/Sample_3_Unbalanced_Mistake`
**Date Analyzed:** 2026-08-03 16:13:55

## 1. Final Diagnosis

### 🔴 Mass Conservation Violation (Leakage)
- **Severity:** CRITICAL
- **Evidence:** Relative Leak Ratio: 0.000275.
- **Interpretation:** Systemic flux is disappearing or materializing from nowhere.

---
## 2. Comprehensive Descriptive Statistics Table

The table below details the descriptive statistics computed individually for all active analytical scales across the TLU mathematical modules:

| Measure / Scale | Mean | Median | Mode (count / total, %) | Min | Max | Range | IQR | Std Dev | Skewness | Kurtosis | Z-Exceed |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Dynamics: acceleration_a | 0.0000 | 0.0000 | 0.0000 (28/132, 21.2%) | -79991.2700 | 73062.5100 | 153053.7800 | 6640.4825 | 22035.4986 | -0.0891 | 3.2983 | 5 |
| Dynamics: jerk_j | 0.0000 | 0.0000 | 0.0000 (37/132, 28.0%) | -82865.7100 | 87509.1800 | 170374.8900 | 7128.7350 | 26872.0380 | -0.1801 | 2.0712 | 2 |
| Dynamics: snap_s | 0.0000 | 0.0000 | 0.0000 (46/132, 34.8%) | -131339.9400 | 123728.6000 | 255068.5400 | 5359.8600 | 39299.9430 | -0.3107 | 2.9683 | 2 |
| Dynamics: state_X | 181818.1818 | 96012.9100 | 1000000.0000 (12/132, 9.1%) | -955157.5600 | 1000000.0000 | 1955157.5600 | 453397.7400 | 392458.6489 | 0.0431 | 0.9720 | 0 |
| Dynamics: velocity_v | -0.0000 | 4413.4150 | 0.0000 (21/132, 15.9%) | -124227.2200 | 95968.3000 | 220195.5200 | 22675.9200 | 36387.1053 | -0.9068 | 2.3474 | 3 |
| Dynamics: viscosity_C | 28144.9790 | 14184.9305 | 100000.0000 (12/132, 9.1%) | 0.0000 | 100000.0000 | 100000.0000 | 41720.1769 | 30419.1315 | 1.1812 | 0.3545 | 0 |
| Forensics: conservation_residual | 117.7400 | 0.0000 | 0.0000 (9/12, 75.0%) | 0.0000 | 906.2900 | 906.2900 | 41.6450 | 269.4042 | 2.3636 | 4.3580 | 0 |
| Forensics: kl_divergence_drift | 0.2259 | 0.0242 | -0.3180 (1/12, 8.3%) | -0.3178 | 1.8723 | 2.1901 | 0.1211 | 0.5704 | 2.2362 | 4.0422 | 0 |
| Stability: spectral_radius | 0.0000 | 0.0000 | 0.0000 (12/12, 100.0%) | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | nan | nan | 0 |
| Stiffness: partial_corr | 0.1095 | 0.0000 | 0.0000 (514/1452, 35.4%) | -1.0000 | 1.0000 | 2.0000 | 0.8404 | 0.6309 | -0.1162 | -0.8881 | 0 |
| Stiffness: stiffness_k | -0.0000 | 0.0000 | 0.0000 (1452/1452, 100.0%) | -0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3132 | 34.3378 | 38 |
| Thermo: entropy_S | 1.5249 | 1.4949 | 1.4000 (3/12, 25.0%) | 1.2712 | 1.9169 | 0.6457 | 0.2460 | 0.1928 | 0.6760 | -0.5163 | 0 |
| Thermo: free_energy_F | 2944787.8 | 2890151.9 | 2238208.0 (1/12, 8.3%) | 2238207.9 | 3810764.0 | 1572556.1 | 989310.4 | 548435.9 | 0.1996 | -1.3655 | 0 |
| Thermo: gross_activity_U | 3300434.7 | 3235199.7 | 2303842.0 (1/12, 8.3%) | 2303842.3 | 4105871.3 | 1802029.0 | 921345.7 | 592377.2 | -0.1294 | -1.2452 | 0 |
| Thermo: temperature_T | 231731.7446 | 244801.6953 | 0.0000 (1/12, 8.3%) | 0.0000 | 317154.0141 | 317154.0141 | 44955.0872 | 82146.4761 | -1.9193 | 3.5136 | 0 |
| Topology: stress | 2.0064 | 0.8829 | 0.0000 (16/97, 16.5%) | 0.0000 | 17.6380 | 17.6380 | 2.0014 | 3.1374 | 3.0750 | 10.5717 | 3 |
| Topology: weight | 39859.7668 | 33614.2100 | 166.5800 (1/97, 1.0%) | 166.5800 | 124227.2200 | 124060.6400 | 47838.5700 | 32202.2059 | 0.7635 | -0.2252 | 0 |

---
## 3. Structural Evolution (Viscosity Classification)

- **Viscosity Range:** `230384.23 ~ 395402.52`
  - 🩸 **Diagnosis:** Thrombosis / High-Friction (Old-Generation Structure). The system relies on manual/human friction.

---
## 4. Quartile-based Diagnostic Candidates

### ⚠️ Shoulder Stiffness (Chronic Delay/Viscosity >= Q3: `40371.1440`)
| Node | Average Viscosity | Peak Time | Peak Viscosity |
| :--- | :---: | :---: | :---: |
| `04_ACC_Inventory` | 52070.6915 | `2020-12` | 56817.5903 |
| `03_ACC_Cash` | 45606.0156 | `2020-06` | 47469.7562 |
| `07_ACC_Sales_Revenue` | 45422.2270 | `2020-12` | 87430.7585 |

### 🎯 Acupuncture Points (Tsubo/Strain <= Q1: `5.4447`)
| Node | Average Strain Energy |
| :--- | :---: |
| `02_ACC_COGS` | 3.6648 |
| `04_ACC_Inventory` | 4.7277 |
| `01_ACC_Accounts_Receivable` | 4.8484 |

### 🚫 Contraindications (Kinki/Strain >= Q3: `8.2186` or limit)
| Node | Average Strain Energy |
| :--- | :---: |
| `09_UNKNOWN_LEAK` | 8.3630 |
| `07_ACC_Sales_Revenue` | 8.3384 |
| `10_ACC_Equity_Capital` | 8.3317 |

> *Generated automatically by the TLU Meta-Diagnosis Engine (Descriptive Statistics V3).* 

