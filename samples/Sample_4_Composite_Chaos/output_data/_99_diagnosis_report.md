# TLU Meta-Diagnosis Report (Descriptive Statistics V3)

**Target Environment:** `samples/Sample_4_Composite_Chaos`
**Date Analyzed:** 2026-06-29 10:28:11

## 1. Final Diagnosis

### ⚠️ COMPOSITE PATHOLOGY DETECTED
The system is suffering from multiple overlapping structural failures.

### 🔴 Mass Conservation Violation (Leakage)
- **Severity:** CRITICAL
- **Evidence:** Relative Leak Ratio: 0.001358.
- **Interpretation:** Systemic flux is disappearing or materializing from nowhere.

### 🟠 Topological Feedback Loop (Wash Trade / Resonance)
- **Severity:** HIGH
- **Evidence:** Max Spectral Radius: 0.7861.
- **Interpretation:** An artificial loop of funds or extreme resonance has formed in the network.

---
## 2. Comprehensive Descriptive Statistics Table

The table below details the descriptive statistics computed individually for all active analytical scales across the TLU mathematical modules:

| Measure / Scale | Mean | Median | Mode (count / total, %) | Min | Max | Range | IQR | Std Dev | Skewness | Kurtosis | Z-Exceed |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Dynamics: acceleration_a | -0.0000 | 0.0000 | 0.0000 (28/132, 21.2%) | -133639.6600 | 73088.4100 | 206728.0700 | 7186.2300 | 26436.3653 | -0.8552 | 5.4984 | 1 |
| Dynamics: state_X | 181818.1818 | 98023.2600 | 1000000.0000 (12/132, 9.1%) | -1107242.3000 | 1000000.0000 | 2107242.3000 | 447895.5225 | 414360.7126 | -0.2890 | 1.2603 | 1 |
| Dynamics: velocity_v | 0.0000 | 4739.3400 | 0.0000 (20/132, 15.2%) | -170205.4700 | 149380.6400 | 319586.1100 | 21756.6750 | 42161.9809 | -0.7181 | 4.6368 | 4 |
| Dynamics: viscosity_C | 29911.3106 | 18805.5237 | 100000.0000 (12/132, 9.1%) | 0.0000 | 100328.4958 | 100328.4958 | 43531.7955 | 31023.3023 | 1.0694 | 0.1259 | 0 |
| Forensics: conservation_residual | 521.3325 | 0.0000 | 0.0000 (8/12, 66.7%) | 0.0000 | 4773.5700 | 4773.5700 | 258.4550 | 1363.7722 | 2.8339 | 6.3911 | 1 |
| Forensics: kl_divergence_drift | 0.2344 | 0.0691 | -0.3740 (1/12, 8.3%) | -0.3744 | 1.5864 | 1.9608 | 0.3020 | 0.5337 | 1.4352 | 1.5128 | 0 |
| Stability: spectral_radius | 0.1739 | 0.0000 | 0.0000 (9/12, 75.0%) | 0.0000 | 0.7861 | 0.7861 | 0.1488 | 0.3173 | 1.2109 | -0.4534 | 0 |
| Stiffness: partial_corr | 0.0921 | 0.0000 | 0.0000 (496/1452, 34.2%) | -1.0000 | 1.0000 | 2.0000 | 1.0553 | 0.6607 | -0.1285 | -1.0123 | 0 |
| Stiffness: stiffness_k | 0.0000 | 0.0000 | 0.0000 (1452/1452, 100.0%) | -0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.2986 | 46.5437 | 29 |
| Thermo: entropy_S | 1.5804 | 1.5018 | 1.4000 (3/12, 25.0%) | 1.3455 | 1.9049 | 0.5594 | 0.3493 | 0.2089 | 0.4660 | -1.3197 | 0 |
| Thermo: free_energy_F | 3126535.0 | 3113421.0 | 2332402.0 (1/12, 8.3%) | 2332402.3 | 4107352.8 | 1774950.5 | 896031.5 | 594029.6 | 0.2015 | -1.2205 | 0 |
| Thermo: gross_activity_U | 3516126.5 | 3475115.1 | 2406773.0 (1/12, 8.3%) | 2406773.0 | 4406644.0 | 1999870.9 | 1033056.9 | 643087.3 | -0.1302 | -1.1410 | 0 |
| Thermo: temperature_T | 245043.4425 | 246472.7347 | 0.0000 (1/12, 8.3%) | 0.0000 | 329268.6082 | 329268.6082 | 58619.2334 | 84996.2702 | -2.0789 | 4.0292 | 0 |
| Topology: stress | 1.7844 | 0.8205 | 0.0000 (20/103, 19.4%) | 0.0000 | 15.7769 | 15.7769 | 1.9387 | 2.7732 | 2.8233 | 8.8754 | 4 |
| Topology: weight | 41852.5992 | 42307.1600 | 51465.3600 (2/103, 1.9%) | 130.5500 | 170205.4700 | 170074.9200 | 52576.9700 | 35867.6689 | 1.0715 | 1.1355 | 1 |

---
## 3. Structural Evolution (Viscosity Classification)

- **Viscosity Range:** `240677.30 ~ 423217.59`
  - 🩸 **Diagnosis:** Thrombosis / High-Friction (Old-Generation Structure). The system relies on manual/human friction.

---
## 4. Quartile-based Diagnostic Candidates

### ⚠️ Shoulder Stiffness (Chronic Delay/Viscosity >= Q3: `40879.0952`)
| Node | Average Viscosity | Peak Time | Peak Viscosity |
| :--- | :---: | :---: | :---: |
| `07_ACC_Sales_Revenue` | 55323.2336 | `2020-12` | 100328.4958 |
| `04_ACC_Inventory` | 52088.2541 | `2020-12` | 56874.8048 |
| `03_ACC_Cash` | 46085.3025 | `2020-06` | 48161.8708 |

### 🎯 Acupuncture Points (Tsubo/Strain <= Q1: `4.1848`)
| Node | Average Strain Energy |
| :--- | :---: |
| `03_ACC_Cash` | 1.5982 |
| `01_ACC_Accounts_Receivable` | 1.7655 |
| `02_ACC_COGS` | 3.6643 |

### 🚫 Contraindications (Kinki/Strain >= Q3: `8.2768` or limit)
| Node | Average Strain Energy |
| :--- | :---: |
| `07_ACC_Sales_Revenue` | 8.3693 |
| `09_UNKNOWN_LEAK` | 8.3422 |
| `10_ACC_Equity_Capital` | 8.3317 |

> *Generated automatically by the TLU Meta-Diagnosis Engine (Descriptive Statistics V3).* 

