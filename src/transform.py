import pandas as pd

def transform(df):
    df['date'] = pd.to_datetime(df['date'], format='%Y-%m')
    df['country_code'] = 'DE'
    if df['unemployment_rate'].isnull().sum() > 0:
        print(f"Warning: {df['unemployment_rate'].isnull().sum()} null values in unemployment_rate")
    print(df.dtypes)
    print(df.head())
    print(df.isnull().sum())
    df.to_csv('data/unemployment_rate_germany_clean.csv', index=False)
    return df