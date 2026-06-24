import pandas as pd
import matplotlib.pyplot as plt

# Sample Dataset
data = {
    'Weather':['Clear','Rainy','Fog','Clear','Rainy','Fog'],
    'Severity':['Minor','Serious','Fatal','Minor','Serious','Fatal'],
    'Casualties':[1,3,5,0,2,4],
    'Vehicles_Involved':[2,3,2,2,4,3]
}

df = pd.DataFrame(data)

# Create Subplots
fig, axes = plt.subplots(2, 2, figsize=(10,8))

# 1. Severity Count
df['Severity'].value_counts().plot(
    kind='bar',
    ax=axes[0,0],
    title='Severity Distribution'
)

# 2. Weather Count
df['Weather'].value_counts().plot(
    kind='pie',
    autopct='%1.1f%%',
    ax=axes[0,1],
    title='Weather Conditions'
)

# 3. Casualties
axes[1,0].plot(df['Casualties'], marker='o')
axes[1,0].set_title('Casualties Trend')

# 4. Vehicles Involved
axes[1,1].hist(df['Vehicles_Involved'])
axes[1,1].set_title('Vehicles Involved')

plt.tight_layout()
plt.show()
