import streamlit as st
import os
import sys
import json
import zipfile
import tempfile
import pandas as pd
import plotly.graph_objects as go
import shutil

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from components.banner import show_banner
from components.footer import show_footer

st.set_page_config(page_title="RS4 - Métricas", layout="wide")

show_banner(
    title="Métricas Comparativas",
    subtitle="Compare o desempenho dos diferentes algoritmos de clustering através de métricas detalhadas"
)

st.markdown("""
<div style="display: flex; gap: 1rem; margin: 2rem 0; flex-wrap: wrap;">
    <div style="flex: 1; min-width: 250px; background: white; padding: 1.5rem; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); border-left: 4px solid #2E86AB;">
        <h3 style="color: #2E86AB; margin: 0 0 0.5rem 0; font-size: 1.2rem;">📈 Métricas Comparativas</h3>
        <p style="color: #666; margin: 0; font-size: 0.9rem;">Compare o desempenho de diferentes algoritmos com métricas detalhadas.</p>
    </div>
    <div style="flex: 1; min-width: 250px; background: white; padding: 1.5rem; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); border-left: 4px solid #A23B72;">
        <h3 style="color: #A23B72; margin: 0 0 0.5rem 0; font-size: 1.2rem;">⚡ Performance Analysis</h3>
        <p style="color: #666; margin: 0; font-size: 0.9rem;">Analise tempo de execução, memória e qualidade dos clusters.</p>
    </div>
    <div style="flex: 1; min-width: 250px; background: white; padding: 1.5rem; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); border-left: 4px solid #F18F01;">
        <h3 style="color: #F18F01; margin: 0 0 0.5rem 0; font-size: 1.2rem;">📊 Visualizações</h3>
        <p style="color: #666; margin: 0; font-size: 0.9rem;">Gráficos interativos para facilitar a interpretação dos resultados.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Sessão: controla se o zip já foi processado
if "metrics_zip_ready" not in st.session_state:
    st.session_state.metrics_zip_ready = False
    st.session_state.metrics_base_dir = ""
    st.session_state.metrics_temp_dir = ""

# === Botão para usar resultados da execução ===
st.markdown("### ⚙️ Opções de Execução")
use_existing = st.button("Usar resultados da execução do algoritmo")

if use_existing:
    default_zip_path = "resultados.zip"
    if os.path.exists(default_zip_path):
        tmpdir = tempfile.mkdtemp()
        with zipfile.ZipFile(default_zip_path, 'r') as zip_ref:
            zip_ref.extractall(tmpdir)
        st.session_state.metrics_base_dir = tmpdir
        st.session_state.metrics_zip_ready = True
        st.session_state.metrics_temp_dir = tmpdir
        st.success("Resultados carregados a partir do arquivo local.")
    else:
        st.error("Arquivo 'resultados.zip' não encontrado.")
elif uploaded_file := st.file_uploader("Envie o arquivo .zip com os resultados:", type="zip"):
    tmpdir = tempfile.mkdtemp()
    zip_path = os.path.join(tmpdir, "uploaded.zip")
    with open(zip_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(tmpdir)
        st.session_state.metrics_base_dir = tmpdir
        st.session_state.metrics_zip_ready = True
        st.session_state.metrics_temp_dir = tmpdir
        st.success("Resultados carregados com sucesso!")
    except zipfile.BadZipFile:
        st.error("Arquivo ZIP inválido.")
        st.session_state.metrics_zip_ready = False

# === UI e carregamento só se zip estiver pronto ===
if st.session_state.metrics_zip_ready:
    base_dir = st.session_state.metrics_base_dir
    possible_dirs = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]
    selected_root = st.selectbox("Pasta de Avaliação:", possible_dirs)
    root_path = os.path.join(base_dir, selected_root)

    series = sorted([d for d in os.listdir(root_path) if os.path.isdir(os.path.join(root_path, d))])
    selected_series = st.selectbox("Selecione a Série:", series)
    series_path = os.path.join(root_path, selected_series)

    methods = sorted([m for m in os.listdir(series_path) if os.path.isdir(os.path.join(series_path, m))])
    selected_methods = st.multiselect("Selecione os Métodos:", methods)

    if st.button("Carregar Métricas"):
        metrics_list = []
        for method in selected_methods:
            metrics_path = os.path.join(series_path, method, "metrics.json")
            if os.path.exists(metrics_path):
                with open(metrics_path) as f:
                    metrics = json.load(f)
                flat_metrics = {}
                for k, v in metrics.items():
                    if isinstance(v, dict):
                        for sub_k, sub_v in v.items():
                            flat_metrics[f"{k}.{sub_k}"] = sub_v
                    else:
                        flat_metrics[k] = v
                for metric_name, metric_value in flat_metrics.items():
                    metrics_list.append({
                        "Método": method,
                        "Métrica": metric_name,
                        "Valor": metric_value
                    })

        if metrics_list:
            metrics_df = pd.DataFrame(metrics_list)
            st.subheader("Tabela de Métricas")
            st.dataframe(metrics_df)

            st.subheader("Gráficos Comparativos")
            for metric in metrics_df["Métrica"].unique():
                metric_data = metrics_df[metrics_df["Métrica"] == metric].reset_index()
                if isinstance(metric_data["Valor"].iloc[0], list):
                    continue
                fig = go.Figure()
                fig.add_trace(go.Bar(
                    x=metric_data["Método"],
                    y=metric_data["Valor"],
                    text=metric_data["Valor"],
                    textposition="outside"
                ))
                fig.update_layout(
                    title=f"Métrica: {metric}",
                    xaxis_title="Método",
                    yaxis_title="Valor",
                    bargap=0.4
                )
                st.plotly_chart(fig, use_container_width=True)

# Footer
show_footer()
