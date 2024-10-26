# Importing the numpy library, which is useful for numerical operations
import numpy as np
import pandas as pd
import re as r # Import the regular expression module for pattern matching
from typing import Optional

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


def find_special_characters(df: pd.DataFrame):
    special_chars = {}  # Initialize an empty dictionary to store special characters by column
    # Define a regex pattern to find any character that is not a letter, number, or whitespace
    pattern = r.compile(r'[^a-zA-Z0-9\s]')
    # Iterate over each column in the DataFrame
    for column in df.columns:  
        # Convert all values in the column to strings, then combine them into a single string
        combined_text = " ".join(df[column].astype(str))
        # Use regex to find all special characters in the combined string and store them as a set
        matches = set(r.findall(pattern, combined_text))
        # If any special characters were found, add them to the dictionary with the column name as the key
        if matches:
            special_chars[column] = matches
    # Return the dictionary containing special characters by column
    return special_chars  