import streamlit as st
from data_fetch import get_deputy_expenses
from data_cleaning import clean_data
from analysis import analyze_expenses_by_deputy
from visualization import plot_expenses_by_deputy

API_TOKEN = "749ce2abb6aa3e60d5f83c1c2c4abce9583e5883"

st.title("Análise de Gastos dos Deputados")

df_expenses = get_deputy_expenses(API_TOKEN)
df_cleaned = clean_data(df_expenses)

df_total_expenses = analyze_expenses_by_deputy(df_cleaned)

st.subheader("Gastos Totais por Deputado")
st.dataframe(df_total_expenses.head(10))

st.subheader("Top 10 Deputados por Gastos")
st.pyplot(plot_expenses_by_deputy(df_total_expenses))
