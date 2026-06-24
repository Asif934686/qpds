import pandas as pd

df = pd.read_csv("sales_data.csv")

pivot = pd.pivot_table(
    df,
    values="Sale_Amount",
    index=["Region", "Manager", "Salesman"],
    aggfunc="sum"
)

print(pivot)
