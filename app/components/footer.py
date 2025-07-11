import streamlit as st

def show_footer():
    """Footer fixo para usar em todas as páginas - modo light"""
    
    st.markdown("""
    <div style="height: 80px;"></div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        text-align: center;
        padding: 1rem;
        background: #ffffff;
        z-index: 1000;
        border-top: 1px solid #e0e0e0;
    ">
        <p style="
            font-family: 'Fira Sans', sans-serif;
            color: #333333;
            margin: 0;
            font-size: 0.9rem;
        ">
            Copyright © 2025 GUISSE, Inc. Built with Streamlit
        </p>
    </div>
    """, unsafe_allow_html=True)
