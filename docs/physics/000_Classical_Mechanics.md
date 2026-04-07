# 000. Classical Mechanics & Solid Mechanics

> **"Before we can move the system, we must understand how heavy it is, and how rigidly it is bound together."**

Category **000** serves as the absolute foundation for all subsequent analyses in the Tensor-Link Utility (TLU). It refuses to predict the future or optimize for goals; instead, its sole purpose is rigorous *observation*.

By treating the network's nodes as physical "point masses" and its edges as "springs" (structural constraints), this paradigm calculates the inherent physical properties—Mass, Friction, and Stiffness—derived inductively from historical flow data.

---

## 1. Phase Space Mechanics (000_1_1)

In classical mechanics, the state of a system is fully described by its position and momentum in Phase Space. TLU translates organizational flux into these physical equivalents to answer a fundamental question: *How hard is it to change the current state of a given department or account?*

### The Variables of Motion

* **Position (q):** The cumulative net flux flowing into or out of a node.
* **Velocity (v):** The rate of change of the net flux over time (the first derivative).
* **Acceleration (a):** The rate of change of the velocity (the second derivative).

### Defining Inertia and Friction

Not all nodes react to change equally. A massive, historically stable core department resists change much more than an agile, peripheral team.

* **Virtual Mass / Inertia (M):** Calculated as the historical average of absolute flux: `M = mean(|q(t)|)`. The larger the historical volume of activity, the greater the node's "Inertia" (resistance to being moved).
* **Virtual Viscosity / Friction (C):** Calculated as the inverse of velocity volatility: `C = 1 / std(v(t))`. Nodes that exhibit highly stable, unchanging velocities are modeled as having high "Friction" dragging them down.
* **External Force Residual (F_ext):** Using Newton's Second Law combined with damping (`F = M * a + C * v`), TLU calculates the unknown, external force that must be acting upon the node to produce its currently observed motion.

## 2. Structural Stiffness & Partial Correlation (000_2_1)

While Phase Space Mechanics focuses on individual nodes, Solid Mechanics examines the "rigidity" of the connections between them. If you pull on Node A, does Node B follow instantly, or does the connection stretch and absorb the shock?

### The Precision Matrix (K)

TLU calculates the covariance matrix of velocity changes across the entire network, and then computes its safe pseudo-inverse. The resulting inverse covariance matrix is known as the **Precision Matrix (K)**.

* A higher value in the Precision Matrix indicates a mathematically "stiff" relationship between two nodes. They move together rigidly, meaning a shock to one will violently transfer to the other.

### The Partial Correlation Pivot (Ver 8.0.0)

Simple correlation is often deceptive in complex networks (spurious correlation). Just because Node A and Node B both increase doesn't mean they are directly connected; they might both be driven by Node C.

To isolate the *true* structural constraints, TLU normalizes the Precision Matrix into a **Partial Correlation Matrix**:
`R_ij = -K_ij / sqrt(K_ii * K_jj)`

This normalization projects the stiffness into a strict `[-1.0, 1.0]` space:

* **Positive Stiffness (Coupling):** Direct, unmediated linkage. They rise and fall together.
* **Negative Stiffness (Trade-off):** A direct zero-sum constraint. Investing energy here mathematically drains energy from there.
* **Zero Stiffness:** They are structurally independent, even if they appear correlated on the surface.

## 3. Business Implications

By visualizing Phase Space and Structural Stiffness, leadership can definitively answer:

1. **Which initiatives will face the most friction?** (High M and C nodes).
2. **Where are the hidden organizational trade-offs?** (Negative partial correlations).
3. **If we push the system, will it bend or break?** (Overall network rigidity).
