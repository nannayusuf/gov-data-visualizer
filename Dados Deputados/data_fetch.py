import requests
import pandas as pd

def get_deputy_expenses(token):
    url = "https://api.brasil.io/v1/dataset/gastos-deputados/cota_parlamentar/data/"
    headers = {"Authorization": f"Token {token}"}
    params = {"year": "2023"}
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    df = pd.DataFrame(data['results'])
    return df

