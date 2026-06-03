import pandas as pd

df = pd.read_csv('data/unemployment_rate_germany.csv')
df['date'] = pd.to_datetime(df['date'], format='%Y-%m')
df['country_code'] = 'DE'
print(df.dtypes)
print(df.head())
print(df.isnull().sum())
df.to_csv('data/unemployment_rate_germany_clean.csv', index=False)