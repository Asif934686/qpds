import pandas as pd

data = {
    'JOB_ID':['AD_PRES','AD_VP','AD_ASST','FI_MGR'],
    'JOB_TITLE':['President',
                 'Administration Vice President',
                 'Administration Assistant',
                 'Finance Manager']
}

df = pd.DataFrame(data)

result = df.sort_values(by='JOB_TITLE', ascending=False)

print(result)
