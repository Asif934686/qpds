import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(10, 4),
    columns=['A', 'B', 'C', 'D']
)

def color_negative_red(val):
    color = 'red' if val < 0 else 'black'
    return f'color: {color}'

styled_df = df.style.map(color_negative_red)

print(df)
styled_df
