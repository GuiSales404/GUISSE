import streamlit as st

st.set_page_config(page_title="Teste Navigation", layout="wide")

# Teste com seções organizadas
home_page = st.Page("home.py", title="Home", icon="🏠")
visualizador_page = st.Page("pages/visualizador.py", title="Visualizador", icon="📈")
algoritmos_page = st.Page("pages/rs4-parametrizado.py", title="Algoritmos", icon="⚙️")
metricas_page = st.Page("pages/metricas.py", title="Métricas", icon="📊")

# Organizar em seções
navigation_pages = {
    "Ferramentas": [home_page, visualizador_page, algoritmos_page, metricas_page]
}

pg = st.navigation(navigation_pages, position="top")

pg.run()
