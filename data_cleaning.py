import pandas as pd

def clean_data(df):
    required_columns = ['txnomeparlamentar', 'sgpartido', 'sguf', 'txtdescricao',
                        'txtfornecedor', 'vlrdocumento', 'vlrglosa', 'vlrliquido', 'datemissao']
    
    for col in required_columns:
        if col not in df.columns:
            print(f"A coluna {col} não foi encontrada no DataFrame.")
            return None
    
    if 'datemissao' in df.columns:
        df['datemissao'] = pd.to_datetime(df['datemissao'])

    df = df.dropna(subset=['vlrdocumento', 'vlrliquido'])

    if 'datemissao' in df.columns:
        df['month'] = df['datemissao'].dt.month
        df['year'] = df['datemissao'].dt.year

    return df
