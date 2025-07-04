import streamlit as st
import shutil 
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

from components.banner import show_banner
from components.footer import show_footer

# Limpar arquivos temporários
if os.path.isdir('app/resultados'):
    shutil.rmtree('app/resultados')

if os.path.isfile('app/resultados.zip'):
    os.remove('app/resultados.zip')

show_banner(
    title="🧠 GUISSE - Graphical User Interface for Snippet Selection and Evaluation",
    subtitle="Uma ferramenta interativa para seleção de snippets em séries temporais via diferentes algoritmos, visualização interativa de resultados e análise comparativa de métricas de desempenho."
)

st.markdown("""
<div style="display: flex; gap: 1rem; margin: 2rem 0; flex-wrap: wrap;">
    <div style="flex: 1; min-width: 250px; background: white; padding: 1.5rem; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); border-left: 4px solid #4472c4;">
        <h3 style="color: #4472c4; margin: 0 0 0.5rem 0; font-size: 1.2rem;">📈 Visualizador de Resultados</h3>
        <p style="color: #666; margin: 0; font-size: 0.9rem;">Pensado para fornecer indicadores e recomendações para a melhoria da saúde dos seus usuários, ajudando as linhas de pesquisa a captar dados para análise.</p>
    </div>
    <div style="flex: 1; min-width: 250px; background: white; padding: 1.5rem; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); border-left: 4px solid #5b9bd5;">
        <h3 style="color: #5b9bd5; margin: 0 0 0.5rem 0; font-size: 1.2rem;">⚙️ Algoritmos Parametrizados</h3>
        <p style="color: #666; margin: 0; font-size: 0.9rem;">A prática que visa integrar o desenvolvimento, a operação e a manutenção de sistemas de aprendizado de máquina de forma eficiente e escalável.</p>
    </div>
    <div style="flex: 1; min-width: 250px; background: white; padding: 1.5rem; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); border-left: 4px solid #2f5597;">
        <h3 style="color: #2f5597; margin: 0 0 0.5rem 0; font-size: 1.2rem;">📊 Comparador de Métricas</h3>
        <p style="color: #666; margin: 0; font-size: 0.9rem;">O Kubeflow é um framework open source do Kubernetes usado no desenvolvimento, gerenciamento e execução de cargas de trabalho de machine learning (ML).</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Footer
show_footer()

