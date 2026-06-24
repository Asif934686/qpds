import pandas as pd

# Load dataset
df = pd.read_csv("world_alcohol.csv")

# Shape
print("Shape of Dataset:")
print(df.shape)

# Column Names
print("\nColumn Names:")
print(df.columns)
