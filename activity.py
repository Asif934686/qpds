import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("telecom_churn.csv")

# 1. Churn Distribution
sns.countplot(x='Churn', data=df)
plt.title("Customer Churn Distribution")
plt.show()

# 2. Complaints vs Churn
sns.barplot(x='Churn', y='Complaints', data=df)
plt.title("Complaints vs Churn")
plt.show()

# 3. Call Drop Rate vs Complaints
sns.scatterplot(x='CallDropRate', y='Complaints',
                hue='Churn', data=df)
plt.title("Call Drop Rate vs Complaints")
plt.show()

# 4. Monthly Charges vs Churn
sns.boxplot(x='Churn', y='MonthlyCharges', data=df)
plt.title("Monthly Charges vs Churn")
plt.show()

# 5. Correlation Heatmap
numeric_df = df.select_dtypes(include=['int64','float64'])

sns.heatmap(numeric_df.corr(),
            annot=True,
            cmap='coolwarm')

plt.title("Correlation Matrix")
plt.show()

# 6. Plan Type vs Churn
sns.countplot(x='PlanType',
              hue='Churn',
              data=df)

plt.title("Plan Type vs Churn")
plt.show()
