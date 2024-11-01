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

# Filtro por quantidade de abas
st.sidebar.header("Filtrar por Quantidade de Abas")
min_abas = st.sidebar.slider("Mínimo de Abas", 0, int(data["Quantidade de Abas"].max()), 0)
max_abas = st.sidebar.slider("Máximo de Abas", 0, int(data["Quantidade de Abas"].max()), int(data["Quantidade de Abas"].max()))

filtered_data = data[(data["Quantidade de Abas"] >= min_abas) & (data["Quantidade de Abas"] <= max_abas)]

# Mostrar a tabela filtrada
st.header("Tabela Filtrada")
st.dataframe(filtered_data)

# Gráfico de barras
st.header("Distribuição de Abas por Planilha")
st.bar_chart(data["Quantidade de Abas"].value_counts().sort_index())

# Mostrar detalhes de uma planilha específica
st.sidebar.header("Detalhes da Planilha")
planilha_selecionada = st.sidebar.selectbox("Selecione uma Planilha", data["Nome da Planilha"])
detalhes_planilha = data[data["Nome da Planilha"] == planilha_selecionada]

st.header(f"Detalhes da Planilha: {planilha_selecionada}")
st.write(detalhes_planilha)
