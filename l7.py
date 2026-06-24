import pandas as pd

df = pd.read_csv("sales_data.csv")

pivot = pd.pivot_table(
    df,
    values="Sale_Amount",
    index="Item",
    aggfunc=["max", "min"]
)

print(pivot)
