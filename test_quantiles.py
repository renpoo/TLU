import pandas as pd
import numpy as np

df = pd.read_csv("samples/Sample_0_Healthy/output_data/result.002_2_2_filter_micro_forensics.analysis.csv")
z_scores = df['node_univariate_z_score'].values

print("Max Z-score:", np.max(z_scores))
print("95th percentile:", np.percentile(z_scores, 95))
print("98th percentile:", np.percentile(z_scores, 98))
print("99th percentile:", np.percentile(z_scores, 99))
