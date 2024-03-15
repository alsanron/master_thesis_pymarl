import pandas as pd
import numpy as np
from plt_tools import load_data
from tl_metrics import auc_ratio

# List of file paths to read
file_paths = ['/path/to/file1.csv', '/path/to/file2.csv', '/path/to/file3.csv']

# Create an empty DataFrame to store the data
data = pd.DataFrame()

# Read each file and append the data to the DataFrame
for file_path in file_paths:
    df = pd.read_csv(file_path)
    data = data.append(df)

# Save the data to an ods format file
output_file_path = '/path/to/output.ods'
data.to_excel(output_file_path, engine='odf')