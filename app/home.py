import streamlit as st
import shutil 
import os

# Remover config desnecessária - será feita no main.py
# st.set_page_config já não é necessário aqui

if os.path.isdir('app/resultados'):
    shutil.rmtree('app/resultados')

if os.path.isfile('app/resultados.zip'):
    os.remove('app/resultados.zip')

# Conteúdo da página Home
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

st.write("Bem-vindo! Use a barra de navegação acima para acessar os serviços:")

# Cards informativos para as funcionalidades
col1, col2, col3 = st.columns(3)

with col1:
    st.info("📈 **Visualizador de Resultados**\n\nVisualize e analise os resultados das análises")

with col2:
    st.info("⚙️ **Algoritmos Parametrizados**\n\nExecute algoritmos com parâmetros customizados")

with col3:
    st.info("📊 **Comparador de Métricas**\n\nCompare diferentes métricas de performance")

