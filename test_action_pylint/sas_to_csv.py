""""
This script converts a SAS file to a CSV file using pandas.
"""

import csv
import pandas as pd

# Replace 'your_sas_file.sas7bdat' with the actual filename
SAS_FILE = "C:\\temp\\sas_files\\servicecontacts_2021.sas7bdat"
CSV_FILE = "C:\\temp\\sas_files\\Service Contacts - year4.csv"

try:
    # Read the SAS file into a pandas DataFrame
    df = pd.read_sas(SAS_FILE, encoding='latin-1')

    # Write the DataFrame to a CSV file, excluding the index
    df.to_csv(CSV_FILE, index=False, quoting=csv.QUOTE_NONNUMERIC)

    print(f"Successfully converted {SAS_FILE} to {CSV_FILE}")


except FileNotFoundError:
    print(f"Error: File not found: {SAS_FILE}")
