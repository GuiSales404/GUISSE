import streamlit as st
import os
import base64

def add_logo_to_sidebar():
    """Adicionar logo pequeno na sidebar"""
    # Usar apenas SVG
    logo_path = "app/assets/images/logo.svg"
    
    if os.path.exists(logo_path):
        try:
            with open(logo_path, "rb") as f:
                logo_base64 = base64.b64encode(f.read()).decode()
            
            st.sidebar.markdown(f"""
                <div style="text-align: center; padding: 0.5rem 0; margin-bottom: 0.5rem;">
                    <img src="data:image/svg+xml;base64,{logo_base64}" 
                         style="max-height: 80px; max-width: 200px; object-fit: contain;" 
                         alt="AI4Wellness Logo">
                </div>
                <style>
                /* Manter sidebar sempre aberta */
                [data-testid="stSidebar"] {{
                    min-width: 280px !important;
                    max-width: 280px !important;
                    width: 280px !important;
                }}
                
                /* Esconder botão de fechar sidebar */
                [data-testid="stSidebar"] button[kind="header"] {{
                    display: none !important;
                }}
                
                /* Ajustar conteúdo principal */
                .main .block-container {{
                    padding-left: 1rem !important;
                    max-width: none !important;
                }}
                </style>
                """, unsafe_allow_html=True)
        except:
            pass

def add_favicon():
    """Adicionar favicon personalizado"""
    favicon_path = "app/assets/images/favicon.ico"
    
    if os.path.exists(favicon_path):
        try:
            with open(favicon_path, "rb") as f:
                favicon_base64 = base64.b64encode(f.read()).decode()
            
            st.markdown(f"""
                <link rel="icon" type="image/x-icon" href="data:image/x-icon;base64,{favicon_base64}">
                """, unsafe_allow_html=True)
        except:
            pass

def add_logo_to_navigation():
    """Adicionar logo na área de navegação principal"""
    logo_path = "app/assets/images/logo.svg"
    
    if os.path.exists(logo_path):
        try:
            with open(logo_path, "rb") as f:
                logo_base64 = base64.b64encode(f.read()).decode()
            
            st.markdown(f"""
                <style>
                /* Logo na navegação */
                .stApp > header {{
                    background-image: url("data:image/svg+xml;base64,{logo_base64}");
                    background-repeat: no-repeat;
                    background-position: 20px center;
                    background-size: 160px auto;
                    padding-left: 190px !important;
                }}
                
                /* Ajustar espaçamento da navegação */
                [data-testid="stNavigation"] {{
                    margin-left: 190px;
                }}
                </style>
                """, unsafe_allow_html=True)
        except:
            pass
