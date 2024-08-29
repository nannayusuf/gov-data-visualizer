def analyze_expenses_by_deputy(df):
    total_expenses = df.groupby('txnomeparlamentar')['vlrliquido'].sum().reset_index()
    
    total_expenses = total_expenses.sort_values(by='vlrliquido', ascending=False)
    return total_expenses
