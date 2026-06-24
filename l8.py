import pandas as pd

df = pd.read_csv("sales_data.csv")

pivot = pd.pivot_table(
    df,
    values="Units",
    index="Item",
    aggfunc="sum"
)

print(pivot)
