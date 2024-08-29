import pandas as pd

def clean_data(df):
    columns_to_drop = ['id', 'document_id']
    existing_columns = [col for col in columns_to_drop if col in df.columns]
    
    if existing_columns:
        df = df.drop(columns=existing_columns)

    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'])

    df = df.dropna(subset=['document_value', 'net_value'])

    if 'date' in df.columns:
        df['month'] = df['date'].dt.month
        df['year'] = df['date'].dt.year

    return df
