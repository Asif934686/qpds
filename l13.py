import pandas as pd
import numpy as np

# Create a DataFrame
data = {
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, 7, 8],
    'C': [9, 10, 11, np.nan],
    'D': [13, 14, 15, 16]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Detect missing values
print("\nMissing Values (True/False):")
print(df.isnull())
