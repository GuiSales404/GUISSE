import streamlit as st
import shutil 
import os
import sys

# Adicionar o diretório atual ao PATH para importar componentes
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

from components.banner import show_banner

# Limpar arquivos temporários
if os.path.isdir('app/resultados'):
    shutil.rmtree('app/resultados')

if os.path.isfile('app/resultados.zip'):
    os.remove('app/resultados.zip')

# Banner principal da home
show_banner(
    title="Projeto GUISSE Documentação",
    subtitle="De tutoriais passo a passo, a referências detalhadas, nossa documentação é sua fonte confiável para dominar todas as nuances dos projetos de análise de séries temporais e alcançar seus objetivos com facilidade."
)

# Cards informativos das funcionalidades
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

# Rodapé
st.markdown("""
<div style="
    text-align: center;
    margin-top: 4rem;
    padding: 2rem;
    background: #f8f9fa;
    border-radius: 10px;
    border-top: 3px solid #4472c4;
">
    <p style="
        font-family: 'Fira Sans', sans-serif;
        color: #666;
        margin: 0;
        font-size: 0.9rem;
    ">
        Copyright © 2025 GUISSE, Inc. Built with Streamlit
    </p>
</div>
""", unsafe_allow_html=True)

