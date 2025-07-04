import streamlit as st
import os
import sys
import json
import numpy as np
import plotly.graph_objects as go
import zipfile
import shutil
from PIL import Image

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from components.banner import show_banner
from components.footer import show_footer

st.set_page_config(page_title="RS4 - Visualização", layout="wide")

show_banner(
    title="Visualização dos Snippets",
    subtitle="Explore e analise os resultados dos algoritmos de clustering de séries temporais"
)

st.markdown("""
<div style="display: flex; gap: 1rem; margin: 2rem 0; flex-wrap: wrap;">
    <div style="flex: 1; min-width: 250px; background: white; padding: 1.5rem; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); border-left: 4px solid #2E86AB;">
        <h3 style="color: #2E86AB; margin: 0 0 0.5rem 0; font-size: 1.2rem;">📊 Visualização Interativa</h3>
        <p style="color: #666; margin: 0; font-size: 0.9rem;">Explore os snippets extraídos com gráficos interativos e análises detalhadas.</p>
    </div>
    <div style="flex: 1; min-width: 250px; background: white; padding: 1.5rem; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); border-left: 4px solid #A23B72;">
        <h3 style="color: #A23B72; margin: 0 0 0.5rem 0; font-size: 1.2rem;">🔍 Análise Detalhada</h3>
        <p style="color: #666; margin: 0; font-size: 0.9rem;">Examine cada snippet individualmente com informações de contexto e métricas.</p>
    </div>
    <div style="flex: 1; min-width: 250px; background: white; padding: 1.5rem; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); border-left: 4px solid #F18F01;">
        <h3 style="color: #F18F01; margin: 0 0 0.5rem 0; font-size: 1.2rem;">📈 Resultados Comparativos</h3>
        <p style="color: #666; margin: 0; font-size: 0.9rem;">Compare diferentes algoritmos e suas respectivas extrações de snippets.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# === BOTÃO PARA USAR RESULTADO LOCAL ===
st.markdown("### ⚙️ Opções de Execução")
use_existing = st.button("Usar resultados da execução do algoritmo")

uploaded_file = None
is_uploaded = False

if use_existing:
    default_zip_path = "resultados.zip"
    if os.path.exists(default_zip_path):
        uploaded_file = open(default_zip_path, "rb")
        is_uploaded = False
        st.success("Resultados carregados a partir do arquivo local.")
    else:
        st.error("Arquivo 'resultados.zip' não encontrado no diretório do projeto.")
else:
    uploaded_file = st.file_uploader("Envie o arquivo .zip com os resultados:", type="zip")
    is_uploaded = True if uploaded_file else False

# === EXTRAÇÃO PERSISTENTE ===
if uploaded_file:
    persistent_dir = os.path.join("cache", "zip_extract")
    os.makedirs(persistent_dir, exist_ok=True)

    # Limpa o conteúdo anterior
    for filename in os.listdir(persistent_dir):
        file_path = os.path.join(persistent_dir, filename)
        if os.path.isdir(file_path):
            shutil.rmtree(file_path)
        else:
            os.remove(file_path)

    zip_path = os.path.join(persistent_dir, "uploaded.zip")
    with open(zip_path, "wb") as f:
        if is_uploaded:
            f.write(uploaded_file.getbuffer())
        else:
            f.write(uploaded_file.read())
            uploaded_file.close()

    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(persistent_dir)
    except zipfile.BadZipFile:
        st.error("O arquivo fornecido não é um arquivo ZIP válido.")
        st.stop()

    st.session_state.zip_extracted_path = persistent_dir

# === INTERFACE PRINCIPAL ===
if "zip_extracted_path" in st.session_state:
    base_candidates = [d for d in os.listdir(st.session_state.zip_extracted_path)
                       if os.path.isdir(os.path.join(st.session_state.zip_extracted_path, d))]

    if not base_candidates:
        st.warning("Nenhuma pasta encontrada no arquivo ZIP extraído.")
        st.stop()

    selected_root = st.selectbox("Pasta de Avaliação:", base_candidates)
    base_dir = os.path.join(st.session_state.zip_extracted_path, selected_root)

    series = sorted([d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))])
    selected_series = st.selectbox("Selecione a Série:", series)
    methods_path = os.path.join(base_dir, selected_series)
    methods = sorted(os.listdir(methods_path))

    time_series_dir = os.path.join("time_series")
    serie_txt_path = os.path.join(time_series_dir, f"{selected_series}.txt")
    serie = None
    if os.path.exists(serie_txt_path):
        with open(serie_txt_path, 'r') as f:
            line = f.readline()
            serie = np.array([float(val) for val in line.strip().split(',')])
        st.success("Série original carregada com sucesso!")

    selected_methods = st.multiselect("Selecione os Métodos a Comparar:", methods)

    if selected_methods:
        threshold = st.slider("Valor de Threshold", min_value=0.0, max_value=20.0, value=5.0, step=0.5,
                              help="Diferença máxima permitida ponto a ponto entre o snippet e o trecho da série.")
        if "start_visualization" not in st.session_state:
            st.session_state.start_visualization = False

        if st.button("Iniciar"):
            st.session_state.start_visualization = True

        if st.session_state.start_visualization:
            fig_shapes = go.Figure()
            fig_series = go.Figure()

            if serie is not None:
                fig_series.add_trace(go.Scatter(
                    y=serie,
                    mode='lines',
                    name='Série Original',
                    line=dict(color='lightgray'),
                    opacity=0.7
                ))

            for method in selected_methods:
                output_dir = os.path.join(methods_path, method)
                snippets_path = os.path.join(output_dir, 'snippets.json')
                snippets = None
                if os.path.exists(snippets_path):
                    with open(snippets_path) as f:
                        snippets = json.load(f)

                if snippets:
                    for i, snip in enumerate(snippets[:3]):
                        fig_shapes.add_trace(go.Scatter(
                            y=snip['subsequence'],
                            mode='lines',
                            name=f'{method} - Snippet {i+1}'
                        ))

                    if serie is not None:
                        for snip_idx, snip in enumerate(snippets[:3]):
                            subseq_size = len(snip['subsequence'])
                            snippet_array = np.array(snip['subsequence'])
                            for i in range(len(serie) - subseq_size):
                                window = serie[i:i + subseq_size]
                                if np.all(np.abs(window - snippet_array) <= threshold):
                                    fig_series.add_trace(go.Scatter(
                                        x=list(range(i, i + subseq_size)),
                                        y=window,
                                        mode='lines',
                                        line=dict(color=f"rgba({50 + snip_idx * 60}, 180, 60, 0.5)", width=2),
                                        name=f"Match {method} - Snippet {snip_idx + 1}",
                                        showlegend=False
                                    ))

            st.subheader("Shapes dos Snippets")
            st.plotly_chart(fig_shapes, use_container_width=True)

            st.subheader("Snippets sobrepostos na Série")
            st.plotly_chart(fig_series, use_container_width=True)

# Footer
show_footer()
