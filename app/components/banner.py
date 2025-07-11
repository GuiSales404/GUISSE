import streamlit as st

def show_banner(title="Projeto GUISSE", subtitle="Ferramentas avançadas para análise de séries temporais e machine learning"):
    """Banner principal do GUISSE para usar em todas as páginas"""
    
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #4472c4 0%, #5b9bd5 100%); padding: 3rem 2rem; border-radius: 15px; text-align: center; margin-bottom: 2rem; box-shadow: 0 8px 32px rgba(68, 114, 196, 0.3); position: relative; overflow: hidden;">
        <div style="background: rgba(255, 255, 255, 0.1); backdrop-filter: blur(10px); border-radius: 10px; padding: 2rem; border: 1px solid rgba(255, 255, 255, 0.2);">
            <h1 style="font-family: 'Fira Sans', sans-serif; font-size: 2.5rem; font-weight: 700; color: white; margin-bottom: 1rem; text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);">{title}</h1>
            <p style="font-family: 'Fira Sans', sans-serif; font-size: 1.1rem; color: rgba(255, 255, 255, 0.9); margin-bottom: 0; line-height: 1.6; max-width: 600px; margin-left: auto; margin-right: auto;">{subtitle}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
