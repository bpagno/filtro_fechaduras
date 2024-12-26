import pandas as pd
import streamlit as st

# Carregar os dados da planilha
file_path = 'caracteristicas_fechaduras.xlsx'
df = pd.read_excel(file_path)

# Configuração do título do aplicativo
st.title("Escolha sua Fechadura Digital")

# Ajuste de estilos com CSS
st.markdown(
    """
    <style>
    /* Estilo do menu lateral */
    section[data-testid="stSidebar"] {
        background-color: #2E8B57; /* Verde escuro */
        color: white;
    }
    section[data-testid="stSidebar"] .block-container {
        color: white;
    }

    /* Estilo dos itens de filtro */
    .collapsible {
        cursor: pointer;
        margin: 10px 0;
        padding: 5px 0;
        color: white;
        font-size: 16px;
        font-weight: bold;
    }

    .collapsible .arrow {
        float: right;
        font-size: 12px;
        margin-left: 5px;
    }

    .collapsible-content {
        display: none;
        background-color: #2E8B57; /* Fundo verde escuro */
        margin: 5px 0 10px 0;
        padding: 5px 0;
        border-radius: 5px;
    }

    .collapsible.expanded .arrow {
        transform: rotate(180deg);
    }

    .collapsible.expanded + .collapsible-content {
        display: block;
    }

    /* Estilo da área principal */
    .block-container {
        background-color: white;
        color: #2E8B57; /* Verde */
    }
    .css-18e3th9 { padding: 1rem; }  /* Reduz espaçamento */
    .css-1lcbmhc { font-size: 14px; } /* Ajusta o tamanho da fonte */
    </style>
    """,
    unsafe_allow_html=True,
)

# Filtros no menu lateral
st.sidebar.header("Filtros de Características")

# Criar filtros dinâmicos
selecoes = {}
for coluna in df.columns:
    # Título do filtro com comportamento de colapso
    st.sidebar.markdown(
        f"""
        <div class="collapsible" id="{coluna}">
            {coluna}
            <span class="arrow">▼</span>
        </div>
        <div class="collapsible-content" id="content-{coluna}">
        """,
        unsafe_allow_html=True,
    )

    valores_unicos = df[coluna].dropna().unique()
    selecionados = []
    for valor in valores_unicos:
        if st.sidebar.checkbox(f"{valor}", key=f"{coluna}-{valor}"):
            selecionados.append(valor)

    st.sidebar.markdown("</div>", unsafe_allow_html=True)
    selecoes[coluna] = selecionados

# Aplicar os filtros com base nos checkboxes selecionados
dados_filtrados = df.copy()
colunas_a_mostrar = [df.columns[0]]  # Sempre mostrar a primeira coluna

for coluna, valores in selecoes.items():
    if valores:  # Aplicar o filtro apenas se houver valores selecionados
        dados_filtrados = dados_filtrados[dados_filtrados[coluna].isin(valores)]
        if coluna not in colunas_a_mostrar:
            colunas_a_mostrar.append(coluna)

# Exibir a tabela filtrada
st.header("Resultados da Busca")
if len(colunas_a_mostrar) > 1:  # Verifica se há colunas selecionadas além da primeira
    if not dados_filtrados.empty:
        st.write(dados_filtrados[colunas_a_mostrar])
    else:
        st.warning("Nenhum item encontrado com os filtros selecionados.")
else:
    st.info("Selecione atributos no menu lateral para iniciar a busca.")