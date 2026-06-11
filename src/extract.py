import requests
import pandas as pd

def extract():
    url = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/une_rt_m"

    params = {
        "geo": "DE",
        "unit": "PC_ACT",
        "age": "TOTAL",
        "sex": "T",
        "freq": "M",
        "format": "JSON",
        "lang": "EN",
        "sinceTimePeriod": "2015-01"
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise Exception(f"API error {response.status_code}")

    data = response.json()

    time_index = data['dimension']['time']['category']['index']
    values = data['value']

    df = pd.DataFrame({
        'date': list(time_index.keys()),
        'unemployment_rate': [values.get(str(i)) for i in range(len(time_index))]
    })

    print(df.head(10))
    print(df.shape)

    df.to_csv('data/unemployment_rate_germany.csv', index=False)

    return df