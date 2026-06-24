# Air Quality and Environmental Impact Assessment
import os

print("Current Folder:", os.getcwd())
print("Files in Folder:")
print(os.listdir())
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("air_quality.csv")

# Display First Records
print("First 5 Records")
print(df.head())

# Dataset Information
print("\nDataset Info")
print(df.info())

# Data Cleaning
df.drop_duplicates(inplace=True)

# Convert Date Column
df['Date'] = pd.to_datetime(df['Date'])

# Check Missing Values
print("\nMissing Values")
print(df.isnull().sum())

# Statistical Summary
print("\nStatistical Summary")
print(df.describe())

# ==================================================
# 1. AQI Trend Over Time
# ==================================================

plt.figure(figsize=(10,5))
daily_aqi = df.groupby('Date')['AQI'].mean()

plt.plot(daily_aqi.index, daily_aqi.values, marker='o')
plt.title("AQI Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Average AQI")
plt.grid(True)
plt.show()

# ==================================================
# 2. Top Polluted Cities
# ==================================================

city_aqi = df.groupby('City')['AQI'].mean().sort_values(ascending=False)

plt.figure(figsize=(10,5))
city_aqi.plot(kind='bar')
plt.title("Average AQI by City")
plt.xlabel("City")
plt.ylabel("AQI")
plt.show()

# ==================================================
# 3. PM2.5 Distribution
# ==================================================

plt.figure(figsize=(8,5))
plt.hist(df['PM2.5'], bins=10)
plt.title("PM2.5 Distribution")
plt.xlabel("PM2.5")
plt.ylabel("Frequency")
plt.show()

# ==================================================
# 4. Correlation Heatmap
# ==================================================

plt.figure(figsize=(10,8))

corr = df[['AQI','PM2.5','PM10','NO2','SO2',
           'CO','O3','Temperature',
           'Humidity','Wind_Speed']].corr()

sns.heatmap(corr, annot=True, cmap='coolwarm')

plt.title("Correlation Heatmap")
plt.show()

# ==================================================
# 5. AQI vs PM2.5
# ==================================================

plt.figure(figsize=(8,5))

plt.scatter(df['PM2.5'], df['AQI'])

plt.title("AQI vs PM2.5")
plt.xlabel("PM2.5")
plt.ylabel("AQI")

plt.show()

# ==================================================
# 6. Monthly AQI Analysis
# ==================================================

df['Month'] = df['Date'].dt.month

monthly_aqi = df.groupby('Month')['AQI'].mean()

plt.figure(figsize=(8,5))
monthly_aqi.plot(marker='o')

plt.title("Monthly AQI Trend")
plt.xlabel("Month")
plt.ylabel("Average AQI")
plt.grid(True)

plt.show()

# ==================================================
# 7. AQI Box Plot
# ==================================================

plt.figure(figsize=(6,5))

sns.boxplot(y=df['AQI'])

plt.title("AQI Box Plot")
plt.show()

# ==================================================
# 8. Geographic AQI Distribution
# ==================================================

plt.figure(figsize=(10,6))

plt.scatter(df['Longitude'],
            df['Latitude'],
            s=df['AQI'],
            alpha=0.6)

for i in range(len(df)):
    plt.text(df['Longitude'][i],
             df['Latitude'][i],
             df['City'][i],
             fontsize=8)

plt.title("Geographic AQI Distribution")
plt.xlabel("Longitude")
plt.ylabel("Latitude")

plt.show()

# ==================================================
# Findings
# ==================================================

print("\nAverage AQI :", round(df['AQI'].mean(),2))
print("Maximum AQI :", df['AQI'].max())
print("Minimum AQI :", df['AQI'].min())

print("\nTop 5 Polluted Cities")
print(city_aqi.head())

print("\nAnalysis Completed Successfully")
