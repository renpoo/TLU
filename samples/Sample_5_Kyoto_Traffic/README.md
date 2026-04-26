# Sample 5: Kyoto Traffic (Spatial Network Control Experiment)

## Dataset Overview
This dataset is entirely different from the previous financial samples; it is a **traffic volume data stream (a pure spatial network) between intersections**.

- Instead of accounting data, it records the volume of movement (flow) between nodes, such as "how many cars moved from Ichijo-Horikawa to Nijo-Horikawa."
- It is a pure **"Open System"** where the concept of "perfectly matching debits and credits" found in double-entry bookkeeping does not exist.

## How to Visualize
To keep the repository lightweight, pre-rendered graph images (.png) are excluded. You can generate the full suite of visualizations for this specific dataset by running the following command from the project root:
```bash
bash bin/batch_visualize_graphs.sh --target_env samples/Sample_5_Kyoto_Traffic
```
The generated graphs will be saved in the `samples/Sample_5_Kyoto_Traffic/output_plots/` directory.

## TLU Analysis Results (What to look for)

This sample serves as a control experiment to prove that TLU is not merely an "accounting tool," but a **universal engine capable of analyzing the physical dynamics of any tensor network (directed graph)**.

### 1. Differences in the Concept of Mass Conservation
- **Data**: `output_data/002_2_1__macro_forensics.csv`
- **Graph**: `output_plots/002_2_1__macro_forensics_dashboard.png` (if generated)
- In accounting data, the `conservation_residual` was perfectly flat at zero. However, in traffic data, the inflow and outflow at each intersection do not always match (cars may park at the intersection or leave the measured area entirely). Therefore, the residual constantly fluctuates from zero, displaying true "open system behavior" in the data.

### 2. Identifying Spatial Hubs (Principal Axes)
- **Data**: `output_data/000_2_2__principal_axes.csv`
- **Graph**: `output_plots/000_2_2__principal_axes.png` (if generated)
- In traffic data, "central intersections" like Shijo-Karasuma exert overwhelming influence as the Principal Components (`PC_1`, `PC_2`, etc.) of the network, which is vividly captured in the eigenvectors.

### 3. Information Geometry and Topology
- **Data**: `output_data/002_1_1__info_geometry.csv`, `output_data/002_1_3__manifold_dimensionality.csv`
- **Graphs**: `output_plots/002_1_1__ricci_curvature.png`, `output_plots/002_1_3__manifold_dimensionality.png` (if generated)
- In spatial networks, concepts like "physical distance" or "formation of detours" (which differ from financial flows) manifest clearly in the `ricci_curvature` and `fractal_dimension` metrics. This directly applies to the physical diagnosis of urban traffic jams and network bottlenecks.

### Conclusion
The mathematical foundations behind TLU—Thermodynamics, Kinematics, and Control Theory—function universally, whether the subject is "money," "cars," or "data packets." This experiment confirms that TLU is an extremely versatile framework that automatically exposes the inherent physical properties (e.g., closed vs. open systems) of the underlying data.
