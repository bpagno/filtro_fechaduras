import pandas as pd
import streamlit as st

# Função para carregar os dados da planilha
@st.cache_data
def load_data(file_path):
    return pd.read_excel(file_path)

# Interface do Streamlit
st.title("Filtro de Fechaduras Digitais")
#file_path = st.file_uploader("caracteristicas_fechaduras.xlsx", type=["xlsx"])
# Caminho relativo para a planilha no repositório
file_path = 'caracteristicas_fechaduras.xlsx'

# Carregar a planilha
df = pd.read_excel(file_path)

# Exibir a tabela no Streamlit
#st.write(df)

# Caso a planilha der erro use esse para carregar o arquivo
# Permite ao usuário fazer upload do arquivo
#file = st.file_uploader("Carregar características da fechadura", type=["xlsx"])

# Se um arquivo for carregado, leia-o
#if file is not None:
#    df = pd.read_excel(file)
#    st.write(df)
#else:
#    st.warning("Por favor, carregue um arquivo Excel!")

if file_path:
    # Carrega os dados da planilha
    data = load_data(file_path)

    # Exibe os dados carregados (opcional, para verificação)
    st.write("Visualização inicial da planilha:")
    #st.dataframe(data)

    # Criar os filtros
    st.sidebar.header("Filtros")
    filtros = {}
    for col in data.columns[1:]:  # Ignora a primeira coluna (ex: Modelo)
        unique_values = data[col].dropna().unique()  # Valores únicos para cada coluna
        selected = st.sidebar.multiselect(f"Filtrar por {col}", unique_values)  # Caixa de seleção
        if selected:
            filtros[col] = selected  # Salva o filtro aplicado para a coluna

    # Adiciona botão para executar os filtros
    #if st.sidebar.button("Executar Filtro"):
        # Aplica os filtros de forma iterativa
        resultado = data.copy()  # Copia a tabela original
        #for col, valores in filtros.items():
            resultado = resultado[resultado[col].isin(valores)]  # Filtra linha por linha

        # Exibir os resultados filtrados
        st.subheader("Resultados da Busca")
        if not resultado.empty:
            st.dataframe(resultado)  # Exibe a tabela filtrada
        else:
            st.warning("Nenhum dispositivo encontrado com os critérios selecionados.")
    else:
        st.info("Selecione os filtros na barra lateral e clique em 'Executar Filtro'.")
