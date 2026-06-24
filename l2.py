import pandas as pd

data = {
    'EMPLOYEE_ID':[102,101,101,201,114,122,200,176,176,200]
}

df = pd.DataFrame(data)

result = df['EMPLOYEE_ID'].value_counts()
print(result[result >= 2].index.tolist())
