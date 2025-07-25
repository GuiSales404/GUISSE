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
from components.simple_translator import t

st.set_page_config(page_title="RS4 - Métricas", layout="wide")

show_banner(
    title=t("Métricas Comparativas"),
    subtitle=t("Compare o desempenho dos diferentes algoritmos de clustering através de métricas detalhadas")
)

st.markdown(f"""
<div style="display: flex; gap: 1rem; margin: 2rem 0; flex-wrap: wrap;">
    <div style="flex: 1; min-width: 250px; background: white; padding: 1.5rem; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); border-left: 4px solid #2E86AB;">
        <h3 style="color: #2E86AB; margin: 0 0 0.5rem 0; font-size: 1.2rem;">📈 {t("Métricas Comparativas")}</h3>
        <p style="color: #666; margin: 0; font-size: 0.9rem;">{t("Compare o desempenho de diferentes algoritmos com métricas detalhadas.")}</p>
    </div>
    <div style="flex: 1; min-width: 250px; background: white; padding: 1.5rem; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); border-left: 4px solid #A23B72;">
        <h3 style="color: #A23B72; margin: 0 0 0.5rem 0; font-size: 1.2rem;">⚡ {t("Performance Analysis")}</h3>
        <p style="color: #666; margin: 0; font-size: 0.9rem;">{t("Analise tempo de execução, memória e qualidade dos clusters.")}</p>
    </div>
    <div style="flex: 1; min-width: 250px; background: white; padding: 1.5rem; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); border-left: 4px solid #F18F01;">
        <h3 style="color: #F18F01; margin: 0 0 0.5rem 0; font-size: 1.2rem;">📊 {t("Visualizações")}</h3>
        <p style="color: #666; margin: 0; font-size: 0.9rem;">{t("Gráficos interativos para facilitar a interpretação dos resultados.")}</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Sessão: controla se o zip já foi processado
if "metrics_zip_ready" not in st.session_state:
    st.session_state.metrics_zip_ready = False
    st.session_state.metrics_base_dir = ""
    st.session_state.metrics_temp_dir = ""

# === Botão para usar resultados da execução ===
st.markdown(f"### ⚙️ {t('Opções de Execução')}")
use_existing = st.button(t("Usar resultados da execução do algoritmo"))

if use_existing:
    default_zip_path = "resultados.zip"
    if os.path.exists(default_zip_path):
        tmpdir = tempfile.mkdtemp()
        with zipfile.ZipFile(default_zip_path, 'r') as zip_ref:
            zip_ref.extractall(tmpdir)
        st.session_state.metrics_base_dir = tmpdir
        st.session_state.metrics_zip_ready = True
        st.session_state.metrics_temp_dir = tmpdir
        st.success(t("Resultados carregados a partir do arquivo local."))
    else:
        st.error(t("Arquivo 'resultados.zip' não encontrado."))
elif uploaded_file := st.file_uploader(t("Envie o arquivo .zip com os resultados:"), type="zip"):
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
        st.success(t("Resultados carregados com sucesso!"))
    except zipfile.BadZipFile:
        st.error(t("Arquivo ZIP inválido."))
        st.session_state.metrics_zip_ready = False

# === UI e carregamento só se zip estiver pronto ===
if st.session_state.metrics_zip_ready:
    base_dir = st.session_state.metrics_base_dir
    possible_dirs = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]
    selected_root = st.selectbox(t("Pasta de Avaliação:"), possible_dirs)
    root_path = os.path.join(base_dir, selected_root)

    series = sorted([d for d in os.listdir(root_path) if os.path.isdir(os.path.join(root_path, d))])
    selected_series = st.selectbox(t("Selecione a Série:"), series)
    series_path = os.path.join(root_path, selected_series)

    methods = sorted([m for m in os.listdir(series_path) if os.path.isdir(os.path.join(series_path, m))])
    selected_methods = st.multiselect(t("Selecione os Métodos:"), methods)

    if st.button(t("Carregar Métricas")):
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
                        t("Método"): method,
                        t("Métrica"): metric_name,
                        t("Valor"): metric_value
                    })

        if metrics_list:
            metrics_df = pd.DataFrame(metrics_list)
            st.subheader(t("Tabela de Métricas"))
            st.dataframe(metrics_df)

            st.subheader(t("Gráficos Comparativos"))
            for metric in metrics_df[t("Métrica")].unique():
                metric_data = metrics_df[metrics_df[t("Métrica")] == metric].reset_index()
                if isinstance(metric_data[t("Valor")].iloc[0], list):
                    continue
                fig = go.Figure()
                fig.add_trace(go.Bar(
                    x=metric_data[t("Método")],
                    y=metric_data[t("Valor")],
                    text=metric_data[t("Valor")],
                    textposition="outside"
                ))
                fig.update_layout(
                    title=f"{t('Métrica')}: {metric}",
                    xaxis_title=t("Método"),
                    yaxis_title=t("Valor"),
                    bargap=0.4
                )
                st.plotly_chart(fig, use_container_width=True)

# Footer
show_footer()
