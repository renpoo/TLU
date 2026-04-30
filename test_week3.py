import pandas as pd

df = pd.read_csv("samples/Sample_0_Healthy/input_stream/Dummy_Journal_Stream.csv")
df['Trans_Date'] = pd.to_datetime(df['Trans_Date'])
df['Week'] = df['Trans_Date'].dt.isocalendar().week

for acc in ['Accounts_Payable', 'Cash', 'Travel_Exp']:
    weekly = df[df['Account_Name'] == acc].groupby('Week')[['Debit', 'Credit']].sum()
    print(f"--- {acc} ---")
    print(weekly.head(6))
