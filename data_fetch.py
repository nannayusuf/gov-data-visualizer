
import requests
import pandas as pd

def get_deputy_expenses(token):
    url = "https://api.brasil.io/v1/dataset/gastos-deputados/cota_parlamentar/data/"
    headers = {
        "Authorization": f"Token {token}"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    df = pd.DataFrame(data['results'])
    return df
