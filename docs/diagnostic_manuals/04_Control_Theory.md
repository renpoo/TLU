# Sub-Manual 04: Control Theory & System Stability (動的安定性と経絡秘孔)

## 1. 対象データとグラフ
* **System Stability:** `004_1_2__system_stability_dashboard.png`
* **LQR Control:** `004_1_3__control_lqr_performance_space.png`
* **Sensitivity (Acupressure):** `004_2_1__sensitivity_matrix.png`

## 2. 東洋医学的メタファー
* **脈の暴走 (Spectral Radius):** スペクトル半径が 1.0 に達している場合、システム内で「無限のフィードバックループ（架空循環、デッドロック、てんかん過同期）」が形成され、自律的なブレーキが効かない危険な状態（脈の暴走）です。
* **経絡秘孔・ツボ (Acupressure Score):** `FK Ripple / IK Strain` の比率が最も高いノード。最も少ない労力（低IK）で、システム全体に最大の好影響（高FK）を与えることができる「治療の急所」です。

## 3. 検査すべき事項と導出する所見
1. **ループの検知:** スペクトル半径を確認し、1.0（または極めて近い値）であれば、「システムが架空循環や完全な渋滞ロックに陥っている」という所見を下します。
2. **ツボの特定と治療方針 (Dynamic Treatment):** Sensitivity Matrixからツボを特定し、そこに対して「量」ではなく「動的プロパティ（位相のズレを直す、粘性を除去する、慣性を減らす）」を操作する処方箋を提示します。
