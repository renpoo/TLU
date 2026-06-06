# 000_1. 運動学と動的状態空間 (Dynamics & State-Space)

本ガイドは、Tensor-Link Utility (TLU) における運動学について解説します。

---

## 000_1: 運動学と動的状態空間

### 5. 3次元動的軌道リボン・位相空間プロット (`000_1_8__phase_portrait_3d.png` 等)

位置 $X$、速度 $\dot{X}$、加速度 $\ddot{X}$ から構築される3次元の位相空間軌道、または外力影響下の3次元力学特性（`000_1_6__3d_dynamics_external_force.png`）を示すグラフです。システムの動的安定性とカオス性を判別します。

#### 🟢 Sample 0 (正常代謝)

**臨床解説:**
軌道リボンが特定の安定アトラクター（リミットサイクル）へ収束します。外部のショックを弾性的にいなします。定常軌道を維持します。位置、速度、加速度の時系列変化、および3次元の位相空間軌道は規則的です。

- ![Sample 0 Dynamics Position](Sample_0_Healthy/readme_plots/000_1_1__3d_dynamics_position.png)
- ![Sample 0 Dynamics Velocity](Sample_0_Healthy/readme_plots/000_1_2__3d_dynamics_velocity.png)
- ![Sample 0 Dynamics Acceleration](Sample_0_Healthy/readme_plots/000_1_3__3d_dynamics_acceleration.png)
- ![Sample 0 Phase Portrait](Sample_0_Healthy/readme_plots/000_1_8__phase_portrait_3d.png)
- ![Sample 0 Dynamics External Force](Sample_0_Healthy/readme_plots/000_1_6__3d_dynamics_external_force.png)

#### 🟡 Sample 1 (循環取引)

**臨床解説:**
軌道リボンが多次元的な広がりを失います。完全に平坦な二次元平面に押し潰されます。往復運動を繰り返します。自由度の大幅な喪失（還流ロック）を示します。

- ![Sample 1 Dynamics Position](Sample_1_Wash_Trade/readme_plots/000_1_1__3d_dynamics_position.png)
- ![Sample 1 Dynamics Velocity](Sample_1_Wash_Trade/readme_plots/000_1_2__3d_dynamics_velocity.png)
- ![Sample 1 Dynamics Acceleration](Sample_1_Wash_Trade/readme_plots/000_1_3__3d_dynamics_acceleration.png)
- ![Sample 1 Phase Portrait](Sample_1_Wash_Trade/readme_plots/000_1_8__phase_portrait_3d.png)
- ![Sample 1 Dynamics External Force](Sample_1_Wash_Trade/readme_plots/000_1_6__3d_dynamics_external_force.png)

#### 🔴 Sample 2 (資金横領)

**臨床解説:**
資金が流出します。系内の活動質量が失われます。結合バネ剛性が破綻します。外部加振に対して病的共振を起こします。位相空間ではアトラクターの滑らかさが失われます。特異な軌跡として歪みます。

- ![Sample 2 Dynamics Position](Sample_2_Embezzlement_Leak/readme_plots/000_1_1__3d_dynamics_position.png)
- ![Sample 2 Dynamics Velocity](Sample_2_Embezzlement_Leak/readme_plots/000_1_2__3d_dynamics_velocity.png)
- ![Sample 2 Dynamics Acceleration](Sample_2_Embezzlement_Leak/readme_plots/000_1_3__3d_dynamics_acceleration.png)
- ![Sample 2 Phase Portrait](Sample_2_Embezzlement_Leak/readme_plots/000_1_8__phase_portrait_3d.png)
- ![Sample 2 Dynamics External Force](Sample_2_Embezzlement_Leak/readme_plots/000_1_6__3d_dynamics_external_force.png)

#### 🟡 Sample 3 (入力ミス)

**臨床解説:**
仕訳入力ミスが発生します。その瞬間に軌道が平衡点から弾き飛ばされます。病的構造はありません。翌期に正常アトラクターへ自律復元します。過渡応答は位置、速度、加速度のすべてに鋭い変動として現れます。位相空間では一時的なループとして記録されます。

- ![Sample 3 Dynamics Position](Sample_3_Unbalanced_Mistake/readme_plots/000_1_1__3d_dynamics_position.png)
- ![Sample 3 Dynamics Velocity](Sample_3_Unbalanced_Mistake/readme_plots/000_1_2__3d_dynamics_velocity.png)
- ![Sample 3 Dynamics Acceleration](Sample_3_Unbalanced_Mistake/readme_plots/000_1_3__3d_dynamics_acceleration.png)
- ![Sample 3 Phase Portrait](Sample_3_Unbalanced_Mistake/readme_plots/000_1_8__phase_portrait_3d.png)
- ![Sample 3 Dynamics External Force](Sample_3_Unbalanced_Mistake/readme_plots/000_1_6__3d_dynamics_external_force.png)

#### 🔴 Sample 4 (複合アノマリー)

**臨床解説:**
循環取引の強制同期と横領による質量散逸が同時に発生します。アトラクターが崩壊します。軌道はカオス的無限発散へ突入します。位置・速度・加速度は期を追うごとに発散します。位相空間軌道は閉じない螺旋を描きます。

- ![Sample 4 Dynamics Position](Sample_4_Composite_Chaos/readme_plots/000_1_1__3d_dynamics_position.png)
- ![Sample 4 Dynamics Velocity](Sample_4_Composite_Chaos/readme_plots/000_1_2__3d_dynamics_velocity.png)
- ![Sample 4 Dynamics Acceleration](Sample_4_Composite_Chaos/readme_plots/000_1_3__3d_dynamics_acceleration.png)
- ![Sample 4 Phase Portrait](Sample_4_Composite_Chaos/readme_plots/000_1_8__phase_portrait_3d.png)
- ![Sample 4 Dynamics External Force](Sample_4_Composite_Chaos/readme_plots/000_1_6__3d_dynamics_external_force.png)

#### 🔴 Sample 5 (京都交差点網)

**臨床解説:**
主要交差点の容量飽和（粘性ダンピングの無限大化）が発生します。状態の動的軌道が「特異平面」に固定化されます。渋滞デッドロックを示します。位置、速度、加速度は一定値（フリーズ）に収束します。位相空間でも単一の不働点へ吸い込まれるように停止します。

- ![Sample 5 Dynamics Position](Sample_5_Kyoto_Traffic/readme_plots/000_1_1__3d_dynamics_position.png)
- ![Sample 5 Dynamics Velocity](Sample_5_Kyoto_Traffic/readme_plots/000_1_2__3d_dynamics_velocity.png)
- ![Sample 5 Dynamics Acceleration](Sample_5_Kyoto_Traffic/readme_plots/000_1_3__3d_dynamics_acceleration.png)
- ![Sample 5 Phase Portrait](Sample_5_Kyoto_Traffic/readme_plots/000_1_8__phase_portrait_3d.png)
- ![Sample 5 Dynamics External Force](Sample_5_Kyoto_Traffic/readme_plots/000_1_6__3d_dynamics_external_force.png)

#### 🟢 Sample 6 (株券流体)

**臨床解説:**
株式市場における株券対流状態です。粘性と慣性が市場全体でバランスします。位置・速度・加速度は滑らかに連動します。位相空間では閉じられた3次元リミットサイクルが安定して維持されます。

- ![Sample 6 Dynamics Position](Sample_6_Market_Stock_Flow/readme_plots/000_1_1__3d_dynamics_position.png)
- ![Sample 6 Dynamics Velocity](Sample_6_Market_Stock_Flow/readme_plots/000_1_2__3d_dynamics_velocity.png)
- ![Sample 6 Dynamics Acceleration](Sample_6_Market_Stock_Flow/readme_plots/000_1_3__3d_dynamics_acceleration.png)
- ![Sample 6 Phase Portrait](Sample_6_Market_Stock_Flow/readme_plots/000_1_8__phase_portrait_3d.png)
- ![Sample 6 Dynamics External Force](Sample_6_Market_Stock_Flow/readme_plots/000_1_6__3d_dynamics_external_force.png)

#### 🟢 Sample 7 (現金流体)

**臨床解説:**
市場ネットワーク内での現金対流状態です。定常的なキャッシュの往来が摩擦熱を抑えます。急激なショックに対してもしなやかに復元します。時系列変化は周期的です。位相空間上でも調和のとれたコンパクトなアトラクターを示します。

- ![Sample 7 Dynamics Position](Sample_7_Market_Cash_Flow/readme_plots/000_1_1__3d_dynamics_position.png)
- ![Sample 7 Dynamics Velocity](Sample_7_Market_Cash_Flow/readme_plots/000_1_2__3d_dynamics_velocity.png)
- ![Sample 7 Dynamics Acceleration](Sample_7_Market_Cash_Flow/readme_plots/000_1_3__3d_dynamics_acceleration.png)
- ![Sample 7 Phase Portrait](Sample_7_Market_Cash_Flow/readme_plots/000_1_8__phase_portrait_3d.png)
- ![Sample 7 Dynamics External Force](Sample_7_Market_Cash_Flow/readme_plots/000_1_6__3d_dynamics_external_force.png)

#### 🔴 Sample 8 (fMRI 脳梗塞)

**臨床解説:**
$t=30$ に梗塞が発生します。その瞬間、運動野の活動質量が消滅します。軌道は別の低機能状態アトラクターへと不連続にジャンプ（相転移）します。そこで固定化されます。位置、速度、加速度、および3次元位相空間プロットでアトラクターの縮退と形状変化が描かれています。

- ![Sample 8 Dynamics Position](Sample_8_fMRI_Stroke/readme_plots/000_1_1__3d_dynamics_position.png)
- ![Sample 8 Dynamics Velocity](Sample_8_fMRI_Stroke/readme_plots/000_1_2__3d_dynamics_velocity.png)
- ![Sample 8 Dynamics Acceleration](Sample_8_fMRI_Stroke/readme_plots/000_1_3__3d_dynamics_acceleration.png)
- ![Sample 8 Phase Portrait](Sample_8_fMRI_Stroke/readme_plots/000_1_8__phase_portrait_3d.png)
- ![Sample 8 Dynamics External Force](Sample_8_fMRI_Stroke/readme_plots/000_1_6__3d_dynamics_external_force.png)

#### 🔴 Sample 9 (fMRI てんかん発作)

**臨床解説:**
全脳領域が異常周波数にハックされます。3次元軌道リボンは複雑性をすべて失います。単一サイン波の単調な円軌道へと完全にフリーズ（過同期）します。位置、速度、加速度、および3次元位相空間プロットで異常な規則性と複雑性の欠如が確認できます。

- ![Sample 9 Dynamics Position](Sample_9_fMRI_Seizure/readme_plots/000_1_1__3d_dynamics_position.png)
- ![Sample 9 Dynamics Velocity](Sample_9_fMRI_Seizure/readme_plots/000_1_2__3d_dynamics_velocity.png)
- ![Sample 9 Dynamics Acceleration](Sample_9_fMRI_Seizure/readme_plots/000_1_3__3d_dynamics_acceleration.png)
- ![Sample 9 Phase Portrait](Sample_9_fMRI_Seizure/readme_plots/000_1_8__phase_portrait_3d.png)
- ![Sample 9 Dynamics External Force](Sample_9_fMRI_Seizure/readme_plots/000_1_6__3d_dynamics_external_force.png)
