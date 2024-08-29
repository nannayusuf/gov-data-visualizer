def analyze_expenses_by_deputy(df):
    total_expenses = df.groupby('deputy_name')['net_value'].sum().reset_index()
    total_expenses = total_expenses.sort_values(by='net_value', ascending=False)
    return total_expenses
