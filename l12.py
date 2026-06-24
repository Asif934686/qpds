import pandas as pd
import numpy as np

# Create a DataFrame with 10 rows and 4 columns of random values
np.random.seed(0)
df = pd.DataFrame(
    np.random.rand(10, 4),
    columns=['A', 'B', 'C', 'D']
)

print(df)

# Set background color to black and font color to yellow
styled_df = df.style.set_properties(**{
    'background-color': 'black',
    'color': 'yellow'
})

# Save the styled DataFrame as an HTML file
styled_df.to_html("black_yellow_dataframe.html")

print("Output saved as black_yellow_dataframe.html")
