import streamlit as st
from .simple_translator import t

def create_navigation():
    """Componente de navegação reutilizável para todas as páginas"""
    
    home_page = st.Page("home.py", title=t("Home"), icon="🏠")
    visualizador_page = st.Page("pages/visualizador.py", title=t("Visualizador"), icon="📈")
    algoritmos_page = st.Page("pages/rs4-parametrizado.py", title=t("Algoritmos"), icon="⚙️")
    metricas_page = st.Page("pages/metricas.py", title=t("Métricas"), icon="📊")

    navigation_pages = {
        "GUISSE": [home_page, visualizador_page, algoritmos_page, metricas_page]
    }

    pg = st.navigation(navigation_pages, position="top")
    return pg
