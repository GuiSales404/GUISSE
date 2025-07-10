import streamlit as st
import sys
import os
import warnings

# Suprimir warnings específicos do hdbscan
warnings.filterwarnings("ignore", category=SyntaxWarning, module="hdbscan")
warnings.filterwarnings("ignore", message="invalid escape sequence")

# Adicionar o diretório atual ao PATH para importar componentes
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

from components.navigation import create_navigation
from components.simple_translator import create_translation_toggle
from components.logo import add_favicon, add_logo_to_sidebar, add_logo_to_navigation

st.set_page_config(
    page_title="GUISSE", 
    layout="wide",
    page_icon="🧠",
    initial_sidebar_state="expanded"
)

# Adicionar favicon personalizado
add_favicon()

# Adicionar logo na navegação
add_logo_to_navigation()

# Inicializar session_state para tradução
if 'translate_enabled' not in st.session_state:
    st.session_state.translate_enabled = False
if 'target_language' not in st.session_state:
    st.session_state.target_language = 'en'

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Fira+Sans:wght@300;400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Fira Sans', sans-serif !important;
    }
    
    /* Forçar navbar horizontal no topo */
    [data-testid="stNavigation"] {
        position: relative !important;
        display: flex !important;
        flex-direction: row !important;
        justify-content: center !important;
        align-items: center !important;
        background-color: #ffffff !important;
        border-radius: 8px !important;
        margin: 1rem auto 2rem auto !important;
        padding: 0.5rem 1rem !important;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1) !important;
        border: 1px solid rgba(68, 114, 196, 0.2) !important;
        max-width: 800px !important;
        width: auto !important;
    }
    
    /* Botões da navbar */
    [data-testid="stNavigation"] button {
        font-family: 'Fira Sans', sans-serif !important;
        font-weight: 500 !important;
        margin: 0 0.5rem !important;
        white-space: nowrap !important;
    }
    
    /* Ocultar navegação da sidebar */
    .stSidebar [data-testid="stNavigation"] {
        display: none !important;
    }
    
    /* Garantir que o conteúdo principal use toda a largura */
    .main .block-container {
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        max-width: none !important;
    }
</style>
""", unsafe_allow_html=True)

# Adicionar logo na sidebar
add_logo_to_sidebar()

# Criar e executar navegação
pg = create_navigation()

# Criar toggle de tradução na sidebar
create_translation_toggle()

pg.run()
