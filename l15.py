import pandas as pd
import numpy as np

# Create a DataFrame
data = {
    'A': [1, np.nan, np.nan, 4],
    'B': [np.nan, np.nan, 7, 8],
    'C': [9, 10, np.nan, np.nan],
    'D': [13, np.nan, 15, np.nan]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Keep rows with at least 2 NaN values
result = df[df.isna().sum(axis=1) >= 2]

print("\nRows with at least 2 NaN values:")
print(result)
