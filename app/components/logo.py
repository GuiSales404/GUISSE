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

def force_sidebar_open():
    """Forçar sidebar a permanecer sempre aberta em desktop, mas permitir fechar em mobile"""
    st.markdown("""
        <style>
        /* Desktop: forçar sidebar sempre visível */
        @media (min-width: 769px) {
            [data-testid="stSidebar"] {
                transform: translateX(0px) !important;
                visibility: visible !important;
                min-width: 280px !important;
                max-width: 280px !important;
            }
            
            /* Esconder botão de minimizar apenas em desktop */
            [data-testid="stSidebar"] button[aria-label="Close sidebar"] {
                display: none !important;
            }
            
            /* Garantir que não seja colapsada em desktop */
            [data-testid="stSidebar"][data-collapsed="true"] {
                transform: translateX(0px) !important;
                width: 280px !important;
            }
        }
        
        /* Tablet e Mobile: permitir comportamento normal */
        @media (max-width: 768px) {
            [data-testid="stSidebar"] {
                /* Comportamento padrão do Streamlit em mobile */
            }
            
            /* Mostrar botão de fechar em mobile */
            [data-testid="stSidebar"] button[aria-label="Close sidebar"] {
                display: block !important;
            }
        }
        
        /* Ajustar layout principal para todos os tamanhos */
        .main .block-container {
            padding-left: 1rem !important;
        }
        </style>
        
        <script>
        // Script para garantir que sidebar não seja fechada apenas em desktop
        function keepSidebarOpen() {
            // Verificar se é desktop (largura > 768px)
            if (window.innerWidth > 768) {
                const sidebar = document.querySelector('[data-testid="stSidebar"]');
                if (sidebar) {
                    sidebar.style.transform = 'translateX(0px)';
                    sidebar.style.visibility = 'visible';
                    
                    // Remover atributo de collapsed se existir
                    sidebar.removeAttribute('data-collapsed');
                    
                    // Esconder botão de fechar em desktop
                    const closeBtn = sidebar.querySelector('button[aria-label="Close sidebar"]');
                    if (closeBtn) {
                        closeBtn.style.display = 'none';
                    }
                }
            }
        }
        
        // Executar quando a página carrega
        document.addEventListener('DOMContentLoaded', keepSidebarOpen);
        
        // Executar quando a tela é redimensionada
        window.addEventListener('resize', keepSidebarOpen);
        
        // Executar periodicamente apenas se for desktop
        setInterval(() => {
            if (window.innerWidth > 768) {
                keepSidebarOpen();
            }
        }, 1000);
        </script>
        """, unsafe_allow_html=True)
