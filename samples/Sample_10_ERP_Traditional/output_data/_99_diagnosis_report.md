# TLU Meta-Diagnosis Report (Descriptive Statistics V3)

**Target Environment:** `samples/Sample_10_ERP_Traditional`
**Date Analyzed:** 2026-07-31 17:56:46

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
| Dynamics: acceleration_a | 0.0000 | 0.0000 | 0.0000 (82/192, 42.7%) | -121597.2500 | 116149.4500 | 237746.7000 | 6288.2500 | 29890.5039 | -0.3386 | 5.5286 | 8 |
| Dynamics: jerk_j | 0.0000 | 0.0000 | 0.0000 (92/192, 47.9%) | -204881.5100 | 152359.2900 | 357240.8000 | 3350.8850 | 39622.2652 | -0.5718 | 6.6566 | 4 |
| Dynamics: snap_s | -0.0000 | 0.0000 | 0.0000 (102/192, 53.1%) | -313772.3400 | 271728.0100 | 585500.3500 | 0.0000 | 62715.9385 | -0.1473 | 8.4081 | 6 |
| Dynamics: state_X | 250000.0000 | 23721.9200 | 0.0000 (24/192, 12.5%) | -1433745.1100 | 2000000.0000 | 3433745.1100 | 540089.3550 | 614221.2708 | 1.0391 | 2.5298 | 0 |
| Dynamics: velocity_v | 0.0000 | 0.0000 | 0.0000 (72/192, 37.5%) | -184561.5600 | 143430.1600 | 327991.7200 | 16914.8000 | 48856.0789 | -0.7080 | 3.1644 | 4 |
| Dynamics: viscosity_C | 38237.1955 | 16446.3425 | 0.0000 (24/192, 12.5%) | 0.0000 | 200000.0000 | 200000.0000 | 46603.5913 | 51610.5700 | 1.9920 | 3.4537 | 12 |
| Forensics: conservation_residual | 0.0000 | 0.0000 | 0.0000 (12/12, 100.0%) | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | nan | nan | 0 |
| Forensics: kl_divergence_drift | 0.2815 | 0.0612 | -0.0960 (1/12, 8.3%) | -0.0965 | 2.0236 | 2.1201 | 0.2114 | 0.5790 | 2.5252 | 5.1789 | 1 |
| Stability: spectral_radius | 0.0000 | 0.0000 | 0.0000 (12/12, 100.0%) | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | nan | nan | 0 |
| Stiffness: partial_corr | 0.0752 | 0.0000 | 0.0000 (1636/3072, 53.3%) | -1.0000 | 1.0000 | 2.0000 | 0.2702 | 0.5694 | -0.0224 | -0.3435 | 0 |
| Stiffness: stiffness_k | 0.0000 | 0.0000 | 0.0000 (3072/3072, 100.0%) | -0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.2670 | 212.8255 | 37 |
| Thermo: entropy_S | 2.6568 | 2.6818 | 2.7000 (3/12, 25.0%) | 2.0553 | 2.9929 | 0.9376 | 0.3057 | 0.2667 | -0.6975 | 0.2541 | 0 |
| Thermo: free_energy_F | 5413814.5 | 5286660.2 | 4368745.0 (1/12, 8.3%) | 4368745.1 | 7176549.8 | 2807804.7 | 1635903.7 | 952829.1 | 0.4580 | -1.1117 | 0 |
| Thermo: gross_activity_U | 6502658.4 | 6418224.5 | 4586809.0 (1/12, 8.3%) | 4586809.3 | 7989978.3 | 3403169.0 | 1823384.5 | 1120340.5 | -0.1640 | -1.2450 | 0 |
| Thermo: temperature_T | 409221.3383 | 438931.7320 | 0.0000 (1/12, 8.3%) | 0.0000 | 544151.6585 | 544151.6585 | 96474.0684 | 145214.4912 | -1.9745 | 3.4320 | 0 |
| Topology: stress | 2.2307 | 0.8575 | 0.0000 (28/176, 15.9%) | 0.0000 | 77.8671 | 77.8671 | 1.8425 | 6.2697 | 10.1914 | 118.9420 | 1 |
| Topology: weight | 49215.4697 | 30602.4850 | 1622.1200 (1/176, 0.6%) | 1622.1200 | 184561.5600 | 182939.4400 | 58720.0525 | 42469.2322 | 1.1517 | 0.8692 | 2 |

---
## 3. Structural Evolution (Viscosity Classification)

- **Viscosity Range:** `458680.93 ~ 773064.08`
  - 🩸 **Diagnosis:** Thrombosis / High-Friction (Old-Generation Structure). The system relies on manual/human friction.

---
## 4. Quartile-based Diagnostic Candidates

### ⚠️ Shoulder Stiffness (Chronic Delay/Viscosity >= Q3: `44712.6721`)
| Node | Average Viscosity | Peak Time | Peak Viscosity |
| :--- | :---: | :---: | :---: |
| `12_ACC_Cash` | 100000.0000 | `2020-01` | 100000.0000 |
| `09_ACC_Sales_Revenue_DPT_Sales` | 68738.8828 | `2020-12` | 131996.7315 |
| `13_ACC_Raw_Materials` | 50000.0000 | `2020-01` | 50000.0000 |
| `14_ACC_Finished_Goods` | 50000.0000 | `2020-01` | 50000.0000 |

### 🎯 Acupuncture Points (Tsubo/Strain <= Q1: `4.5080`)
| Node | Average Strain Energy |
| :--- | :---: |
| `02_ACC_COGS_DPT_Prod_A` | 2.3699 |
| `05_ACC_Finished_Goods_DPT_Prod_A` | 2.3882 |
| `03_ACC_COGS_DPT_Prod_B` | 3.6621 |
| `10_ACC_Work_In_Process_DPT_Prod_A` | 3.8791 |

### 🚫 Contraindications (Kinki/Strain >= Q3: `8.3317` or limit)
| Node | Average Strain Energy |
| :--- | :---: |
| `09_ACC_Sales_Revenue_DPT_Sales` | 8.3343 |
| `12_ACC_Cash` | 8.3317 |
| `13_ACC_Raw_Materials` | 8.3317 |
| `14_ACC_Finished_Goods` | 8.3317 |
| `15_ACC_Equity_Capital` | 8.3317 |

> *Generated automatically by the TLU Meta-Diagnosis Engine (Descriptive Statistics V3).* 

