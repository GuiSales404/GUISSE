import streamlit as st

st.set_page_config(page_title="Teste Navigation", layout="wide")

home_page = st.Page("home.py", title="Home", icon="🏠")
visualizador_page = st.Page("pages/visualizador.py", title="Visualizador", icon="📈")
algoritmos_page = st.Page("pages/rs4-parametrizado.py", title="Algoritmos", icon="⚙️")
metricas_page = st.Page("pages/metricas.py", title="Métricas", icon="📊")

pg = st.navigation([home_page, visualizador_page, algoritmos_page, metricas_page], position="top")

pg.run()
