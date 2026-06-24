import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    'school_code':['s001','s002','s001','s003','s002','s001'],
    'class':['V','V','VI','VI','V','VI'],
    'name':['Anil','Ravi','Priya','Kiran','Sneha','Rahul'],
    'age':[12,11,13,12,11,14]
})

# Group by school_code
grouped = df.groupby('school_code')

# Display groups
for name, group in grouped:
    print("\nSchool Code:", name)
    print(group)

# Type of GroupBy object
print("\nType:", type(grouped))
