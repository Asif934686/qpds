import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("f24data.csv")

# Plot line chart
plt.figure(figsize=(10,5))
plt.plot(df['Date'], df['Open'], label='Open')
plt.plot(df['Date'], df['High'], label='High')
plt.plot(df['Date'], df['Low'], label='Low')
plt.plot(df['Date'], df['Close'], label='Close')

plt.title("Alphabet Inc. Financial Data (Oct 3 - Oct 7, 2016)")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid(True)

plt.show()
