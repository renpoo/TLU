# Sample 5: Kyoto Traffic (Spatial Network Control Experiment)

## Dataset Overview
This dataset is entirely different from the previous financial samples; it is a **traffic volume data stream (a pure spatial network) between intersections**.

- Instead of accounting data, it records the volume of movement (flow) between nodes, such as "how many cars moved from Ichijo-Horikawa to Nijo-Horikawa."
- It is a pure **"Open System"** where the concept of "perfectly matching debits and credits" found in double-entry bookkeeping does not exist.

## TLU Analysis Results (What to look for)

This sample serves as a control experiment to prove that TLU is not merely an "accounting tool," but a **universal engine capable of analyzing the physical dynamics of any tensor network (directed graph)**.

### 1. Differences in the Concept of Mass Conservation
In accounting data, the `Conservation Residual` was perfectly flat at zero. However, in traffic data, the inflow and outflow at each intersection do not always match (cars may park at the intersection or leave the measured area entirely). Therefore, the residual constantly fluctuates from the baseline, displaying true "open system behavior."

### 2. Identifying Spatial Hubs (Principal Axes)
- `000_2_2__principal_axes.png`
- In traffic data, "central intersections" like Shijo-Karasuma exert overwhelming influence as the Principal Components of the network, which is vividly visualized here.

### 3. Information Geometry and Topology
In spatial networks, concepts like "physical distance" or "formation of detours" (which differ from financial flows) manifest clearly in the Ricci Curvature (Information Geometry) and Fractal Dimension (Manifold Dimensionality). This directly applies to the physical diagnosis of urban traffic jams and network bottlenecks.

### Conclusion
The mathematical foundations behind TLU—Thermodynamics, Kinematics, and Control Theory—function universally, whether the subject is "money," "cars," or "data packets." This experiment confirms that TLU is an extremely versatile framework that automatically exposes the inherent physical properties (e.g., closed vs. open systems) of the underlying data.
