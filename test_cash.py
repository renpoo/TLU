import pandas as pd

df = pd.read_csv("samples/Sample_0_Healthy/input_stream/Dummy_Journal_Stream.csv")
df['Trans_Date'] = pd.to_datetime(df['Trans_Date'])
df['Week'] = df['Trans_Date'].dt.isocalendar().week

cash_dr = df[df['Account_Name'] == 'Cash']['Debit'].sum()
cash_cr = df[df['Account_Name'] == 'Cash']['Credit'].sum()

print("Overall Cash Dr:", cash_dr, "Cr:", cash_cr)

weekly = df[df['Account_Name'] == 'Cash'].groupby('Week')[['Debit', 'Credit']].sum()
print(weekly.head(10))
