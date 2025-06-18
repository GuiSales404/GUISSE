import streamlit as st
import shutil 
import os

print(os.listdir())

if os.path.isdir('app/resultados'):
    shutil.rmtree('app/resultados')

if os.path.isfile('app/resultados.zip'):
    os.remove('app/resultados.zip')

col1, col2 = st.columns([3, 1])

with col1:
    try:
        st.image("logo.png", use_container_width=True)
    except:
        st.image("https://raw.githubusercontent.com/GuiSales404/GUISSE/refs/heads/main/app/logo.png", use_container_width=True)

with col2:
    try:
        st.image("logo-ai.png", use_container_width=True)
    except:
        st.image("https://raw.githubusercontent.com/GuiSales404/GUISSE/refs/heads/main/app/logo-ai.png", use_container_width=True)
    
st.markdown("<h1 style='text-align: center; color: white;'>GUISSE - Ferramentas de Análise de Séries Temporais</h1>", unsafe_allow_html=True)

st.write("Bem-vindo! Selecione abaixo o serviço que deseja utilizar:")

st.page_link("pages/visualizador.py", label="Visualizador de Resultados", icon="📈")
st.page_link("pages/rs4-parametrizado.py", label="Executar Algoritmos Parametrizados", icon="⚙️")
st.page_link("pages/metricas.py", label="Comparador de Métricas", icon="📊")

