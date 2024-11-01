import streamlit as st
import pandas as pd

# Carregar os dados da planilha
@st.cache
def load_data():
    return pd.read_excel('relatorio_planilhas_01nov2024.xlsx')

data = load_data()

# Título do dashboard
st.title("Dashboard de Planilhas")

# Mostrar a tabela completa
st.header("Tabela Completa")
st.dataframe(data)

# Gráfico de barras
st.header("Distribuição de Abas por Planilha")
st.bar_chart(data.set_index("Nome da Planilha")["Quantidade de Abas"])

# Tabela com total de planilhas e abas
st.header("Totais")
total_planilhas = len(data)
total_abas = data["Quantidade de Abas"].sum()
st.write(f"Total de Planilhas: {total_planilhas}")
st.write(f"Total de Abas: {total_abas}")
