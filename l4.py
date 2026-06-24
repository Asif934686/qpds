import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Alphabet.csv")

df['Date'] = pd.to_datetime(df['Date'])

start_date = '2023-01-01'
end_date = '2023-12-31'

filtered = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

plt.plot(filtered['Date'], filtered['Close'])

plt.title("Historical Stock Prices of Alphabet Inc.")
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.xticks(rotation=45)

plt.show()
