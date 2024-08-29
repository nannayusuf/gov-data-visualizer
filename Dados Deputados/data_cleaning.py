import pandas as pd

def clean_data(df):
    df = df.drop(columns=['id', 'document_id'])
    df['date'] = pd.to_datetime(df['date'])
    df = df.dropna(subset=['document_value', 'net_value'])
    df['month'] = df['date'].dt.month
    df['year'] = df['date'].dt.year
    return df
