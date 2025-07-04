import streamlit as st

st.set_page_config(
    page_title="GUISSE - Análise de Séries Temporais", 
    layout="wide",
    page_icon="📊"
)

# Apenas importar a fonte Fira Sans e configurar navbar no topo
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Fira+Sans:wght@300;400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Fira Sans', sans-serif !important;
    }
    
    /* Garantir que a navbar apareça no topo */
    .stNavigation {
        background-color: #ffffff !important;
        border-radius: 8px !important;
        margin-bottom: 1rem !important;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1) !important;
        border: 1px solid rgba(68, 114, 196, 0.2) !important;
    }
    
    /* Botões da navbar */
    .stNavigation button {
        font-family: 'Fira Sans', sans-serif !important;
        font-weight: 500 !important;
    }
    
    /* Garantir que o menu hambúrguer seja visível */
    .stMainMenu {
        visibility: visible !important;
        opacity: 1 !important;
    }
    
    /* Garantir que o header seja visível para acessar configurações */
    .stAppHeader {
        visibility: visible !important;
        opacity: 1 !important;
    }
    
    /* Garantir que o conteúdo principal use toda a largura */
    .main .block-container {
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        max-width: none !important;
    }
</style>
""", unsafe_allow_html=True)

home_page = st.Page("home.py", title="Home", icon="🏠")
visualizador_page = st.Page("pages/visualizador.py", title="Visualizador", icon="📈")
algoritmos_page = st.Page("pages/rs4-parametrizado.py", title="Algoritmos", icon="⚙️")
metricas_page = st.Page("pages/metricas.py", title="Métricas", icon="📊")

pg = st.navigation([
    home_page,
    visualizador_page, 
    algoritmos_page,
    metricas_page
], position="top")

pg.run()
