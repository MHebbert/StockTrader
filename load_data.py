#function for loading data, into readible databases
import pandas as pd

def load_data(csv_files):
    """
    Load data from a list of CSV files and concatenate them into a single DataFrame.
    
    Parameters:
        csv_files (list): List of paths to CSV files.
    
    Returns:
        pd.DataFrame: Concatenated DataFrame.
    """
    # Initialize an empty list to store individual DataFrames
    dfs = []
    
    # Iterate through each CSV file
    for csv_file in csv_files:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(csv_file)
        # Append the DataFrame to the list
        dfs.append(df)
    
    # Concatenate all DataFrames in the list along the rows
    concatenated_df = pd.concat(dfs, ignore_index=True)
    
    return concatenated_df
