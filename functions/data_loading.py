import os
import pandas as pd

def read_csv_files(dir):
    df_list = list()

    # Iterate over each file in the folder
    for file in os.listdir(dir,):
        # Read the CSV file into a datadrame
        df = pd.read_csv(str(dir)+"/"+file, index_col=0)

        # Append the dataframe to the list
        df_list.append(df)

    # Combine the dataframes into a single dataframe
    return pd.concat(df_list, ignore_index=True)