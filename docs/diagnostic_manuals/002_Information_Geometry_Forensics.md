# 002: Information Geometry & Forensics (トポロジーと異常検知)

## 1. 対象モジュールとグラフ (Prefix: `002_1_X`, `002_2_X`)
* **情報幾何学 (Topology & Stress):** `002_1_2__info_stress_scatter.png`, `002_1_2__network_topology.t.*.png` (Cinematic Sequence), `002_1_3__manifold_dimensionality.png`
* **異常検知 (Macro/Micro Forensics):** `002_2_1__macro_forensics_dashboard.png`, `002_2_2__micro_forensics_scatter.png`, `002_2_2_1__3d_micro_kl_drift.png`, `002_2_2_2__3d_micro_z_score_X.png`

## 2. 東洋医学的メタファー (Epistemology)
* **経絡の断裂 (Stress Zeroing):** ネットワークのEdge Stressが 0.0 になることは、ノード間の情報の伝達や血流（取引）が完全に停止し、パイプが切断されたこと（流動性の死）を意味します。
* **出血 (Mass Leakage):** Leak Ratioが正の値を示すことは、閉鎖系であるはずのシステムから質量（現金や血液）が外部へ不当に漏れ出ている（出血・横領・貸借不一致）ことを意味します。
* **病巣の特定 (Micro Pathology):** KL-DriftやZ-Scoreが突出した特定ノードは、病気の発生源（病原体の侵入箇所）です。

## 3. 検査基準と導出する一次所見
1. **ネットワークの形状変化:** Cinematic Sequence（5点固定観測）を用いて、病気がネットワークの構造をどのように歪めていったか（中央集権化、断絶など）を観察します。
2. **質量保存の法則の確認:** `Leak Ratio` を検査し、0より大きければ「物理的な質量欠損（出血）」という最も重い🚨Forensic Alertの一次所見を導出します。
3. **病因のピンポイント特定:** マクロな異常の原因となっている具体的なノード（勘定科目や脳領野）を Micro Forensics (KL-Drift / Z-Score) から特定し、「ここが病因（震源地）である」と宣告します。
