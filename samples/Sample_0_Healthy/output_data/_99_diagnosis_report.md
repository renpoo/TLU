# TLU Meta-Diagnosis Report (Descriptive Statistics V3)

**Target Environment:** `samples/Sample_0_Healthy`
**Date Analyzed:** 2026-08-01 11:12:50

## 1. Final Diagnosis

### 🟢 Healthy System (Statistically Stable)
- **Severity:** NORMAL
- **Evidence:** All statistical moments (Mean, Variance, Skew, Kurtosis) remain within stable thresholds.
- **Interpretation:** The system is functioning efficiently with normal random-walk volatility.

---
## 2. Comprehensive Descriptive Statistics Table

The table below details the descriptive statistics computed individually for all active analytical scales across the TLU mathematical modules:

| Measure / Scale | Mean | Median | Mode (count / total, %) | Min | Max | Range | IQR | Std Dev | Skewness | Kurtosis | Z-Exceed |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Dynamics: acceleration_a | -0.0000 | 0.0000 | 0.0000 (21/120, 17.5%) | -78315.7700 | 65680.6400 | 143996.4100 | 9289.7075 | 24797.0934 | -0.4004 | 2.1287 | 1 |
| Dynamics: jerk_j | 0.0000 | 0.0000 | 0.0000 (30/120, 25.0%) | -97692.4700 | 99126.4500 | 196818.9200 | 10586.1525 | 31183.4104 | -0.0591 | 2.1139 | 3 |
| Dynamics: snap_s | 0.0000 | 0.0000 | 0.0000 (39/120, 32.5%) | -182722.6800 | 173213.7800 | 355936.4600 | 12835.0225 | 45950.5370 | 0.1709 | 5.3632 | 5 |
| Dynamics: state_X | 200000.0000 | 117007.8850 | 1000000.0000 (12/120, 10.0%) | -955157.5600 | 1000000.0000 | 1955157.5600 | 446223.2150 | 407963.5520 | -0.0835 | 0.7509 | 0 |
| Dynamics: velocity_v | -0.0000 | 6120.9900 | 0.0000 (12/120, 10.0%) | -124227.2200 | 95968.3000 | 220195.5200 | 31297.9175 | 38733.6714 | -0.8493 | 1.6166 | 2 |
| Dynamics: viscosity_C | 31042.1692 | 16346.4721 | 100000.0000 (12/120, 10.0%) | 618.1450 | 100000.0000 | 99381.8550 | 40474.2472 | 30478.5834 | 1.0891 | 0.1221 | 0 |
| Forensics: conservation_residual | 0.0000 | 0.0000 | 0.0000 (12/12, 100.0%) | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | nan | nan | 0 |
| Forensics: kl_divergence_drift | 0.2203 | 0.0736 | -0.3130 (1/12, 8.3%) | -0.3134 | 1.6140 | 1.9274 | 0.1074 | 0.5042 | 1.9914 | 3.0840 | 0 |
| Stability: spectral_radius | 0.0000 | 0.0000 | 0.0000 (12/12, 100.0%) | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | nan | nan | 0 |
| Stiffness: partial_corr | 0.1077 | 0.0000 | 0.0000 (380/1200, 31.7%) | -1.0000 | 1.0000 | 2.0000 | 1.2599 | 0.7020 | -0.1603 | -1.1884 | 0 |
| Stiffness: stiffness_k | -0.0000 | 0.0000 | 0.0000 (1200/1200, 100.0%) | -0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.1720 | 52.7618 | 26 |
| Thermo: entropy_S | 1.5286 | 1.6414 | 1.7000 (5/12, 41.7%) | 1.1817 | 1.8623 | 0.6806 | 0.3715 | 0.2436 | -0.3345 | -1.4302 | 0 |
| Thermo: free_energy_F | 2945002.8 | 2881969.5 | 2247309.0 (1/12, 8.3%) | 2247308.5 | 3869999.5 | 1622690.9 | 964997.0 | 548343.1 | 0.2529 | -1.2394 | 0 |
| Thermo: gross_activity_U | 3312641.4 | 3234295.4 | 2303842.0 (1/12, 8.3%) | 2303842.3 | 4132519.0 | 1828676.7 | 878458.4 | 595071.3 | -0.1227 | -1.1816 | 0 |
| Thermo: temperature_T | 238617.4807 | 253111.7540 | 0.0000 (1/12, 8.3%) | 0.0000 | 323855.8867 | 323855.8867 | 44101.9431 | 84361.9319 | -1.9588 | 3.5623 | 0 |
| Topology: stress | 1.9606 | 0.9192 | 0.0000 (14/94, 14.9%) | 0.0000 | 15.7769 | 15.7769 | 2.0836 | 2.8508 | 2.8694 | 9.9988 | 2 |
| Topology: weight | 40916.2638 | 34406.5750 | 1553.2900 (1/94, 1.1%) | 1553.2900 | 124227.2200 | 122673.9300 | 44424.0000 | 32124.7484 | 0.7774 | -0.2475 | 0 |

---
## 3. Structural Evolution (Viscosity Classification)

- **Viscosity Range:** `230384.23 ~ 396820.32`
  - 🩸 **Diagnosis:** Thrombosis / High-Friction (Old-Generation Structure). The system relies on manual/human friction.

---
## 4. Quartile-based Diagnostic Candidates

### ⚠️ Shoulder Stiffness (Chronic Delay/Viscosity >= Q3: `45422.2270`)
| Node | Average Viscosity | Peak Time | Peak Viscosity |
| :--- | :---: | :---: | :---: |
| `04_ACC_Inventory` | 52152.0574 | `2020-12` | 57092.6163 |
| `03_ACC_Cash` | 45762.7981 | `2020-06` | 48402.3453 |
| `07_ACC_Sales_Revenue` | 45422.2270 | `2020-12` | 87430.7585 |

### 🎯 Acupuncture Points (Tsubo/Strain <= Q1: `5.1406`)
| Node | Average Strain Energy |
| :--- | :---: |
| `02_ACC_COGS` | 3.6699 |
| `04_ACC_Inventory` | 4.7263 |
| `01_ACC_Accounts_Receivable` | 4.8460 |

### 🚫 Contraindications (Kinki/Strain >= Q3: `8.0784` or limit)
| Node | Average Strain Energy |
| :--- | :---: |
| `07_ACC_Sales_Revenue` | 8.3602 |
| `09_ACC_Equity_Capital` | 8.3317 |
| `06_ACC_Rent_Exp` | 8.1039 |

> *Generated automatically by the TLU Meta-Diagnosis Engine (Descriptive Statistics V3).* 

