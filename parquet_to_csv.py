import os
import pandas as pd

# Specify the root directory containing the Parquet files
root_directory = 'ebnerd_demo'

# Walk through the directory tree
for dirpath, _, filenames in os.walk(root_directory):
    for filename in filenames:
        # Check if the file is a Parquet file
        if filename.endswith('.parquet'):
            # Construct the full path to the Parquet file
            parquet_file = os.path.join(dirpath, filename)
            
            # Read the Parquet file into a DataFrame
            df = pd.read_parquet(parquet_file)
            
            # Construct the path for the output CSV file
            csv_file = os.path.join(dirpath, filename.replace('.parquet', '.csv'))
            
            # Write the DataFrame to a CSV file
            df.to_csv(csv_file, index=False)
            
            print(f"Parquet file {parquet_file} has been converted to CSV file {csv_file}.")