import pandas as pd
import numpy as np

# Create a DataFrame with missing values
data = {
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, 7, 8],
    'C': [9, 10, np.nan, 12],
    'D': [13, 14, 15, np.nan]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Replace missing values with 0
df.fillna(0, inplace=True)

print("\nDataFrame after replacing missing values:")
print(df)
