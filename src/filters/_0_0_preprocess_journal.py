#!/usr/bin/env python3
# _0_0_preprocess_journal.py
import pandas as pd
import sys

def main():
    # Receive input and output files from command line arguments (with defaults)
    input_file = sys.argv[1] if len(sys.argv) > 1 else 'workspace/input_stream/Dummy_Journal_Stream.csv'
    output_file = sys.argv[2] if len(sys.argv) > 2 else 'workspace/input_stream/Dummy_Journal_Stream_Amount.csv'

    # Read CSV
    df = pd.read_csv(input_file)

    # Sort by date
    df = df.sort_values(by='Trans_Date')

    # Add "ACC_" prefix to Account_Name
    df['Account_Name'] = df['Account_Name'].apply(lambda x: f"ACC_{x}")

    # Add "DPT_" prefix to Dept_Name
    # df['Dept_Name'] = df['Dept_Name'].apply(lambda x: f"DPT_{x}")
    df['Dept_Name'] = df['Dept_Name'].apply(lambda x: f"{x}")
    
    # Add Debit and Credit to create a new 'Amount' column
    df['Amount'] = df['Debit'] + df['Credit']


    # Sort by each field
    df = df.sort_values(by='Dept_Name')
    df = df.sort_values(by='Account_Name')
    df = df.sort_values(by='Trans_Date')
    df = df.sort_values(by='Entry_ID')

    # Save as a new CSV (do not output index numbers)
    df.to_csv(output_file, index=False)
    print(f"✅ Added 'Amount' column and saved to {output_file}.")

if __name__ == '__main__':
    main()
