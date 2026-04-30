import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("samples/Sample_0_Healthy/output_data/result.002_2_2_filter_micro_forensics.analysis.csv")
pivot_z = df.pivot(index='node_idx', columns='t_idx', values='node_univariate_z_score').fillna(0)

print("Values at t_idx=3:")
print(pivot_z[3])

# To find out what seaborn robust=True does:
calc_data = pivot_z.values.ravel()
calc_data = pd.Series(calc_data)
vmin = calc_data.quantile(0.02)
vmax = calc_data.quantile(0.98)
print(f"Robust vmin: {vmin}, vmax: {vmax}")

