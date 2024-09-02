import pandas as pd
from typing import Optional

def casting_data(df: pd.DataFrame, column, dtype) -> Optional[pd.DataFrame]:
    
    # Check if dtype is 'numeric'
    if dtype == 'numeric':
        # Convert the specified column to numeric type
        df[column] = pd.to_numeric(df[column], errors='coerce')
    
    # Check if dtype is 'string'
    else if dtype == 'string':
        # Convert the specified column to string type
        df[column] = df[column].astype('string', errors='ignore')
    
    # Check if dtype is 'date'
    else if dtype == 'date':
        # Convert the specified column to datetime type
        df[column] = pd.to_datetime(df[column], errors='coerce')
    
    # Return the modified DataFrame
    return df