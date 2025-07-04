import streamlit as st

def create_navigation():
    """Componente de navegação reutilizável para todas as páginas"""
    
    home_page = st.Page("home.py", title="Home", icon="🏠")
    visualizador_page = st.Page("pages/visualizador.py", title="Visualizador", icon="📈")
    algoritmos_page = st.Page("pages/rs4-parametrizado.py", title="Algoritmos", icon="⚙️")
    metricas_page = st.Page("pages/metricas.py", title="Métricas", icon="📊")

    navigation_pages = {
        "GUISSE": [home_page, visualizador_page, algoritmos_page, metricas_page]
    }

    pg = st.navigation(navigation_pages, position="top")
    return pg
