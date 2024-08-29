import matplotlib.pyplot as plt

def plot_expenses_by_deputy(df):
    plt.figure(figsize=(10, 6))
    plt.bar(df['txnomeparlamentar'][:10], df['vlrliquido'][:10], color='skyblue')
    plt.xlabel('Deputado')
    plt.ylabel('Total de Gastos (R$)')
    plt.title('Top 10 Deputados por Gastos')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
