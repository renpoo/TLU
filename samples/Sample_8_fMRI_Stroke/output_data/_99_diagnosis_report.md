# TLU Meta-Diagnosis Report (Descriptive Statistics V3)

**Target Environment:** `samples/Sample_8_fMRI_Stroke`
**Date Analyzed:** 2026-07-09 11:12:50

## 1. Final Diagnosis

### 🟠 Topological Feedback Loop (Wash Trade / Resonance)
- **Severity:** HIGH
- **Evidence:** Max Spectral Radius: 1.0000.
- **Interpretation:** An artificial loop of funds or extreme resonance has formed in the network.

---
## 2. Comprehensive Descriptive Statistics Table

The table below details the descriptive statistics computed individually for all active analytical scales across the TLU mathematical modules:

| Measure / Scale | Mean | Median | Mode (count / total, %) | Min | Max | Range | IQR | Std Dev | Skewness | Kurtosis | Z-Exceed |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Dynamics: acceleration_a | 0.0000 | 1.6700 | 0.0000 (6/300, 2.0%) | -2174.6500 | 570.2400 | 2744.8900 | 93.9150 | 165.3958 | -7.1097 | 99.3646 | 5 |
| Dynamics: jerk_j | 0.0000 | 0.0000 | 0.0000 (10/300, 3.3%) | -2076.7100 | 1890.3600 | 3967.0700 | 140.4875 | 205.5789 | -0.7932 | 57.0344 | 2 |
| Dynamics: snap_s | -0.0000 | 0.0000 | 0.0000 (15/300, 5.0%) | -1987.9600 | 3967.0700 | 5955.0300 | 218.4500 | 350.0430 | 3.6015 | 59.1670 | 4 |
| Dynamics: state_X | 100000.0000 | 100103.4500 | 99890.1000 (2/300, 0.7%) | 40052.4300 | 115335.5900 | 75283.1600 | 6139.4325 | 12305.1357 | -2.6938 | 8.3169 | 11 |
| Dynamics: velocity_v | 0.0000 | 33.3600 | -26.9000 (2/300, 0.7%) | -2793.2000 | 755.9400 | 3549.1400 | 442.6975 | 731.3105 | -2.3075 | 5.0750 | 12 |
| Dynamics: viscosity_C | 10000.0000 | 10005.7325 | 9988.5900 (3/300, 1.0%) | 8453.3436 | 10408.2263 | 1954.8827 | 109.5951 | 288.4300 | -2.9853 | 10.9328 | 11 |
| Forensics: conservation_residual | 0.0000 | 0.0000 | 0.0000 (60/60, 100.0%) | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | nan | nan | 0 |
| Forensics: kl_divergence_drift | 0.4101 | 0.2732 | 0.0010 (12/60, 20.0%) | 0.0000 | 1.2882 | 1.2882 | 0.7605 | 0.4392 | 0.3831 | -1.3802 | 0 |
| Stability: spectral_radius | 1.0000 | 1.0000 | 1.0000 (60/60, 100.0%) | 1.0000 | 1.0000 | 0.0000 | 0.0000 | 0.0000 | nan | nan | 0 |
| Stiffness: partial_corr | 0.3665 | 0.3058 | 1.0000 (300/1500, 20.0%) | -1.0000 | 1.0000 | 2.0000 | 0.5016 | 0.4005 | 0.1194 | -0.0081 | 12 |
| Stiffness: stiffness_k | 0.0000 | -0.0000 | 0.0000 (1500/1500, 100.0%) | -0.0030 | 0.0037 | 0.0067 | 0.0001 | 0.0003 | 0.7537 | 54.1729 | 23 |
| Thermo: entropy_S | 9.3574 | 9.3571 | 8.7000 (30/60, 50.0%) | 8.7024 | 9.9994 | 1.2970 | 1.2814 | 0.6458 | -0.0001 | -1.9999 | 0 |
| Thermo: free_energy_F | 413922.4 | 494070.2 | 167265.0 (1/60, 1.7%) | 167265.4 | 500000.0 | 332734.6 | 165510.9 | 107638.1 | -0.9050 | -0.6530 | 0 |
| Thermo: gross_activity_U | 500000.0 | 500000.0 | 500000.0 (60/60, 100.0%) | 500000.0 | 500000.0 | 0.0 | 0.0 | 0.0 | nan | nan | 0 |
| Thermo: temperature_T | 9854.1633 | 651.5900 | 0.0000 (1/60, 1.7%) | 0.0000 | 38176.0157 | 38176.0157 | 19024.6374 | 12366.7427 | 0.9036 | -0.6559 | 0 |
| Topology: stress | 1.0956 | 1.0033 | 0.0000 (40/1200, 3.3%) | 0.0000 | 4.1920 | 4.1920 | 1.1160 | 0.8604 | 0.9985 | 0.8287 | 8 |
| Topology: weight | 470.6102 | 525.0500 | 20.1900 (2/1200, 0.2%) | 16.1900 | 775.5900 | 759.4000 | 222.3100 | 191.4944 | -0.9899 | 0.3975 | 0 |

---
## 3. Structural Evolution (Viscosity Classification)

- **Viscosity Range:** `50000.00 ~ 50000.00`
  - 🩸 **Diagnosis:** Thrombosis / High-Friction (Old-Generation Structure). The system relies on manual/human friction.

---
## 4. Quartile-based Diagnostic Candidates

### ⚠️ Shoulder Stiffness (Chronic Delay/Viscosity >= Q3: `10085.8974`)
| Node | Average Viscosity | Peak Time | Peak Viscosity |
| :--- | :---: | :---: | :---: |
| `02_Prefrontal_Cortex` | 10098.9986 | `2024-01-01 10:09:50` | 10408.2263 |
| `03_Temporal_Lobe` | 10085.8974 | `2024-01-01 10:09:50` | 10398.6110 |

### 🎯 Acupuncture Points (Tsubo/Strain <= Q1: `0.4438`)
| Node | Average Strain Energy |
| :--- | :---: |
| `00_Motor_Cortex` | 0.4349 |
| `02_Prefrontal_Cortex` | 0.4438 |

### 🚫 Contraindications (Kinki/Strain >= Q3: `0.4534` or limit)
| Node | Average Strain Energy |
| :--- | :---: |
| `01_Parietal_Lobe` | 0.4681 |
| `03_Temporal_Lobe` | 0.4534 |

> *Generated automatically by the TLU Meta-Diagnosis Engine (Descriptive Statistics V3).* 

