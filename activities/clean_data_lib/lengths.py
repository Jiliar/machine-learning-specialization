# Importing the numpy library, which is useful for numerical operations
import numpy as np
import pandas as pd

def lenght_standarize(df: pd.DataFrame , column: str, size: int) -> Optional[pd.DataFrame]:
    # Filtering rows from the DataFrame `df` where the length of the 'NIT' column values is greater than 9
    long_values = df[df[column].astype(str).apply(len) > size]
    # Checking if there are any rows in `long_values` (i.e., if any NITs were longer than 9 characters)
    if long_values[column].size > 0:
        # Updating 'NIT' values in the original DataFrame `df`:
        # If the length of 'NIT' is greater than 9, truncate it to the first 9 characters;
        # otherwise, keep it as is
        df[column] = np.where(df[column].astype(str).apply(len) > size, df[column].astype(str).str[:size], df[column])
        return df
    else:
        # Print a message if no 'NIT' values with length greater than 9 were found
        print(f'There are not values in column {column} with length greater than zero (0)')
        return None