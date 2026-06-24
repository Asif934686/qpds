import pandas as pd

df = pd.DataFrame({
    'school_code':['s001','s002','s001','s003','s002','s001'],
    'class':['V','V','VI','VI','V','VI'],
    'name':['Anil','Ravi','Priya','Kiran','Sneha','Rahul'],
    'age':[12,11,13,12,11,14]
})

result = df.groupby('school_code')['age'].agg(['mean','min','max'])

print(result)
