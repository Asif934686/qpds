import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Alphabet.csv')

df['Date'] = pd.to_datetime(df['Date'])

filtered = df[(df['Date'] >= '2023-01-02') &
              (df['Date'] <= '2023-01-06')]

plt.bar(filtered['Date'], filtered['Volume'])
plt.title('Alphabet Trading Volume')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.show()
