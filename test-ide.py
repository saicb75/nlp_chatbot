import pandas as pd

df = pd.read_csv('jan15.csv')

df['Actual Amt'] = df['Actual Amt'].replace('INR ', '', regex=True)
df['Actual Amt'] = df['Actual Amt'].replace(',', '', regex=True)
df['Actual Amt'] = df['Actual Amt'].astype('float')

print(df.head()['Actual Amt'])


