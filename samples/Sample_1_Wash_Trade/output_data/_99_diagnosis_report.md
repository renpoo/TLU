# TLU Meta-Diagnosis Report (Descriptive Statistics V3)

**Target Environment:** `samples/Sample_1_Wash_Trade`
**Date Analyzed:** 2026-08-03 16:11:38

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
| Dynamics: acceleration_a | 0.0000 | 0.0000 | 0.0000 (21/120, 17.5%) | -112498.5800 | 68528.5000 | 181027.0800 | 8920.6950 | 25567.8366 | -0.8003 | 4.3066 | 2 |
| Dynamics: jerk_j | 0.0000 | 0.0000 | 0.0000 (30/120, 25.0%) | -123132.6200 | 128397.5100 | 251530.1300 | 11263.7825 | 33820.6086 | -0.0717 | 3.8649 | 2 |
| Dynamics: snap_s | 0.0000 | 0.0000 | 0.0000 (39/120, 32.5%) | -170241.7100 | 173962.6300 | 344204.3400 | 10822.6650 | 50147.0429 | 0.0901 | 3.9775 | 3 |
| Dynamics: state_X | 200000.0000 | 168745.8450 | 1000000.0000 (12/120, 10.0%) | -1094143.8900 | 1000000.0000 | 2094143.8900 | 448448.6150 | 432355.6175 | -0.4383 | 1.1320 | 0 |
| Dynamics: velocity_v | 0.0000 | 5264.7150 | 0.0000 (12/120, 10.0%) | -168987.2700 | 146967.9100 | 315955.1800 | 23572.7025 | 43352.8378 | -0.7342 | 3.7722 | 4 |
| Dynamics: viscosity_C | 32952.9989 | 24942.9202 | 100000.0000 (12/120, 10.0%) | 602.4700 | 101329.3915 | 100726.9215 | 42149.8787 | 31168.3689 | 0.9832 | -0.0769 | 0 |
| Forensics: conservation_residual | 0.0000 | 0.0000 | 0.0000 (12/12, 100.0%) | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | nan | nan | 0 |
| Forensics: kl_divergence_drift | 0.2113 | 0.1104 | 0.0660 (2/12, 16.7%) | -0.3353 | 1.2212 | 1.5565 | 0.2026 | 0.3946 | 1.4423 | 1.8286 | 0 |
| Stability: spectral_radius | 0.1634 | 0.0000 | 0.0000 (9/12, 75.0%) | 0.0000 | 0.7488 | 0.7488 | 0.1375 | 0.2986 | 1.2230 | -0.4067 | 0 |
| Stiffness: partial_corr | 0.1260 | 0.0000 | 0.0000 (380/1200, 31.7%) | -1.0000 | 1.0000 | 2.0000 | 1.2348 | 0.6841 | -0.1657 | -1.1275 | 0 |
| Stiffness: stiffness_k | 0.0000 | 0.0000 | 0.0000 (1200/1200, 100.0%) | -0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5015 | 94.7678 | 23 |
| Thermo: entropy_S | 1.5791 | 1.5551 | 1.5000 (4/12, 33.3%) | 1.3111 | 1.9326 | 0.6215 | 0.1641 | 0.1776 | 0.6010 | -0.4158 | 0 |
| Thermo: free_energy_F | 3140312.2 | 3119356.7 | 2263566.0 (1/12, 8.3%) | 2263565.6 | 4109087.9 | 1845522.3 | 1109076.0 | 641752.5 | 0.0847 | -1.4161 | 0 |
| Thermo: gross_activity_U | 3524568.2 | 3530896.4 | 2384573.0 (1/12, 8.3%) | 2384573.5 | 4427088.3 | 2042514.8 | 1023993.5 | 655565.2 | -0.2126 | -1.1493 | 0 |
| Thermo: temperature_T | 245382.1200 | 247432.1723 | 0.0000 (1/12, 8.3%) | 0.0000 | 328358.4626 | 328358.4626 | 74960.9407 | 86671.5027 | -1.9330 | 3.5774 | 0 |
| Topology: stress | 1.7061 | 0.9661 | 0.0000 (17/98, 17.3%) | 0.0000 | 18.0102 | 18.0102 | 1.8661 | 2.4680 | 3.6872 | 19.1053 | 2 |
| Topology: weight | 43239.6803 | 43395.0850 | 40433.6000 (2/98, 2.0%) | 1553.2900 | 168987.2700 | 167433.9800 | 42908.9850 | 35552.1255 | 1.1825 | 1.4907 | 2 |

---
## 3. Structural Evolution (Viscosity Classification)

- **Viscosity Range:** `238457.35 ~ 423147.22`
  - 🩸 **Diagnosis:** Thrombosis / High-Friction (Old-Generation Structure). The system relies on manual/human friction.

---
## 4. Quartile-based Diagnostic Candidates

### ⚠️ Shoulder Stiffness (Chronic Delay/Viscosity >= Q3: `44861.6956`)
| Node | Average Viscosity | Peak Time | Peak Viscosity |
| :--- | :---: | :---: | :---: |
| `07_ACC_Sales_Revenue` | 56302.3970 | `2020-12` | 101329.3915 |
| `04_ACC_Inventory` | 52231.0350 | `2020-12` | 56957.7977 |
| `03_ACC_Cash` | 44861.6956 | `2020-01` | 46831.8290 |

### 🎯 Acupuncture Points (Tsubo/Strain <= Q1: `4.5195`)
| Node | Average Strain Energy |
| :--- | :---: |
| `03_ACC_Cash` | 2.1413 |
| `01_ACC_Accounts_Receivable` | 2.2150 |
| `02_ACC_COGS` | 4.3436 |

### 🚫 Contraindications (Kinki/Strain >= Q3: `8.2976` or limit)
| Node | Average Strain Energy |
| :--- | :---: |
| `07_ACC_Sales_Revenue` | 8.7863 |
| `06_ACC_Rent_Exp` | 8.4552 |
| `09_ACC_Equity_Capital` | 8.3317 |

> *Generated automatically by the TLU Meta-Diagnosis Engine (Descriptive Statistics V3).* 

