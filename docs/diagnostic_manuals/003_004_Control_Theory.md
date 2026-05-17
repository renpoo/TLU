# 003_004: Control Theory & System Stability (動的安定性と経絡秘孔)

## 1. 対象モジュールとグラフ (Prefix: `003_1_X`, `004_1_X`, `004_2_X`)
* **シミュレーション (FK/IK):** `003_1_1_run_fk_simulation.sh`, `003_1_2_run_ik_optimization.sh` (出力はSensitivityに統合)
* **安定性・LQR制御:** `004_1_2__system_stability_dashboard.png`, `004_1_3__control_lqr_performance_space.png`
* **ツボ・感度 (Sensitivity):** `004_2_1__sensitivity_matrix.png`, `004_2_1__sensitivity_series_heatmaps.*.png`

## 2. 東洋医学的メタファー (Epistemology)
* **脈の暴走 (Spectral Radius):** スペクトル半径が 1.0 に達している場合、システム内で「無限のフィードバックループ（架空循環、デッドロック、てんかん過同期）」が形成され、自律的なブレーキが効かない危険な状態（脈の暴走）です。
* **経絡秘孔・ツボ (Acupressure Score):** 順運動学（FK Ripple）と逆運動学（IK Strain）の比率が最も高いノード。最も少ない労力（低IK Strain）で、システム全体に最大の好影響（高FK Ripple）を与えることができる「治療の急所」です。

## 3. 検査基準と導出する一次所見
1. **ループの検知 (Stability):** スペクトル半径を確認し、1.0（または極めて近い値）であれば、「システムが架空循環や完全な渋滞ロックに陥っている」という所見を下します。
2. **ツボの特定と治療方針 (Dynamic Treatment):** Sensitivity Matrixからツボ（Acupressure Score最大ノード）を特定し、そこに対して「量（Volume）」ではなく「動的プロパティ（位相のズレを直す、粘性を除去する、慣性を減らす）」を操作する処方箋（LQR制御アプローチ）を提示します。
