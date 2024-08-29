import streamlit as st
from data_fetch import get_deputy_expenses
from data_cleaning import clean_data
from analysis import analyze_expenses_by_deputy
from visualization import plot_expenses_by_deputy

# Token de acesso à API

API_TOKEN = "749ce2abb6aa3e60d5f83c1c2c4abce9583e5883"

# Buscar os dados
df_expenses = get_deputy_expenses(API_TOKEN)

print("Colunas disponíveis no DataFrame:")
print(df_expenses.columns)

print("Primeiras linhas do DataFrame:")
print(df_expenses.head())

df_cleaned = clean_data(df_expenses)

if df_cleaned is not None:
    # Analisar os dados limpos
    df_total_expenses = analyze_expenses_by_deputy(df_cleaned)

    # Exibir os dados e gráficos no Streamlit
    st.title("Análise de Gastos dos Deputados")
    st.subheader("Gastos Totais por Deputado")
    st.dataframe(df_total_expenses.head(10))

    st.subheader("Top 10 Deputados por Gastos")
    st.pyplot(plot_expenses_by_deputy(df_total_expenses))
else:
    print("Erro ao processar os dados. Verifique se todas as colunas necessárias estão presentes.")
