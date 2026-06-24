import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("alphabet_stock_data.csv")

plt.scatter(df["Volume"], df["Close"])
plt.xlabel("Trading Volume")
plt.ylabel("Stock Price (Close)")
plt.title("Alphabet Inc. Trading Volume vs Stock Price")
plt.show()
