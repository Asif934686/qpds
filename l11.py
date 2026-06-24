import pandas as pd
import numpy as np

# Create DataFrame with random values
np.random.seed(0)
df = pd.DataFrame(
    np.random.randn(10, 4),
    columns=['A', 'B', 'C', 'D']
)

# Convert some values to NaN
df.iloc[1, 2] = np.nan
df.iloc[4, 0] = np.nan
df.iloc[7, 3] = np.nan
df.iloc[9, 1] = np.nan

print(df)

# Function to highlight NaN values
def highlight_nan(val):
    return 'background-color: yellow' if pd.isna(val) else ''

# Highlight NaN values
styled_df = df.style.map(highlight_nan)

# Save as HTML to view highlighting
styled_df.to_html("highlight_nan.html")
print("Output saved as highlight_nan.html")
