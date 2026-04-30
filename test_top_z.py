import pandas as pd
df = pd.read_csv("samples/Sample_0_Healthy/output_data/result.002_2_2_filter_micro_forensics.analysis.csv")
print(df.nlargest(10, 'node_univariate_z_score'))
