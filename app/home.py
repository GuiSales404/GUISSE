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

# Forçar tema light
st.markdown("""
<style>
/* Forçar tema light */
.stApp {
    background-color: #ffffff !important;
    color: #333333 !important;
}

[data-testid="stSidebar"] {
    background-color: #f8f9fa !important;
}

[data-testid="stHeader"] {
    background-color: #ffffff !important;
}

.main .block-container {
    background-color: #ffffff !important;
    color: #333333 !important;
}
</style>
""", unsafe_allow_html=True)

show_banner(
    title="🧠 GUISSE - Graphical User Interface for Snippet Selection and Evaluation",
    subtitle="Uma ferramenta interativa para seleção de snippets em séries temporais via diferentes algoritmos, visualização interativa de resultados e análise comparativa de métricas de desempenho."
)

st.markdown("""
<style>
.card-container {
    display: flex; 
    gap: 1rem; 
    margin: 2rem 0; 
    flex-wrap: wrap;
}

.feature-card {
    flex: 1; 
    min-width: 250px; 
    padding: 1.5rem; 
    border-radius: 8px; 
    background: #ffffff;
    color: #333333;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    transition: all 0.3s ease;
}

.feature-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}

.card-title {
    margin: 0 0 0.5rem 0; 
    font-size: 1.2rem;
    font-weight: 600;
}

.card-description {
    margin: 0; 
    font-size: 0.9rem;
    color: #666;
    line-height: 1.4;
}

.card-visualizador { border-left: 4px solid #4472c4; }
.card-algoritmos { border-left: 4px solid #5b9bd5; }
.card-metricas { border-left: 4px solid #2f5597; }

.card-visualizador .card-title { color: #4472c4; }
.card-algoritmos .card-title { color: #5b9bd5; }
.card-metricas .card-title { color: #2f5597; }
</style>

<div class="card-container">
    <div class="feature-card card-visualizador">
        <h3 class="card-title">📈 Visualizador de Resultados</h3>
        <p class="card-description">Pensado para fornecer indicadores e recomendações para a melhoria da saúde dos seus usuários, ajudando as linhas de pesquisa a captar dados para análise.</p>
    </div>
    <div class="feature-card card-algoritmos">
        <h3 class="card-title">⚙️ Algoritmos Parametrizados</h3>
        <p class="card-description">A prática que visa integrar o desenvolvimento, a operação e a manutenção de sistemas de aprendizado de máquina de forma eficiente e escalável.</p>
    </div>
    <div class="feature-card card-metricas">
        <h3 class="card-title">📊 Comparador de Métricas</h3>
        <p class="card-description">O Kubeflow é um framework open source do Kubernetes usado no desenvolvimento, gerenciamento e execução de cargas de trabalho de machine learning (ML).</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Footer
show_footer()

