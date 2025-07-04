import streamlit as st
import os
import sys
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import shutil
import zipfile
from datetime import datetime
import tracemalloc
import hdbscan
import stumpy
from tslearn.clustering import KShape
from tslearn.preprocessing import TimeSeriesScalerMeanVariance
from sklearn.metrics.pairwise import cosine_distances
from sklearn.cluster import AgglomerativeClustering, MiniBatchKMeans
from scipy.cluster.hierarchy import linkage as scipy_linkage, fcluster, dendrogram
from scipy.spatial.distance import pdist
from sklearn.metrics import silhouette_score
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from components.banner import show_banner

show_banner(
    title="GUISSE - Clustering Parametrizável",
    subtitle="Execute algoritmos avançados de clustering em séries temporais com parâmetros customizáveis"
)

st.markdown("""
<div style="display: flex; gap: 1rem; margin: 2rem 0; flex-wrap: wrap;">
    <div style="flex: 1; min-width: 250px; background: white; padding: 1.5rem; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); border-left: 4px solid #2E86AB;">
        <h3 style="color: #2E86AB; margin: 0 0 0.5rem 0; font-size: 1.2rem;">🤖 Algoritmos Avançados</h3>
        <p style="color: #666; margin: 0; font-size: 0.9rem;">K-Shape, HDBSCAN, Hierarchical e outros algoritmos de clustering de ponta.</p>
    </div>
    <div style="flex: 1; min-width: 250px; background: white; padding: 1.5rem; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); border-left: 4px solid #A23B72;">
        <h3 style="color: #A23B72; margin: 0 0 0.5rem 0; font-size: 1.2rem;">⚙️ Parâmetros Flexíveis</h3>
        <p style="color: #666; margin: 0; font-size: 0.9rem;">Configure todos os parâmetros dos algoritmos para otimizar seus resultados.</p>
    </div>
    <div style="flex: 1; min-width: 250px; background: white; padding: 1.5rem; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); border-left: 4px solid #F18F01;">
        <h3 style="color: #F18F01; margin: 0 0 0.5rem 0; font-size: 1.2rem;">📊 Resultados Detalhados</h3>
        <p style="color: #666; margin: 0; font-size: 0.9rem;">Obtenha métricas completas e arquivos prontos para visualização.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# ======================== UTILITÁRIAS ========================
def parse_number_list(s: str):
    cleaned = s.replace('\n', ',').replace(' ', '')
    parts = [x for x in cleaned.split(',') if x]  
    return [float(x) for x in parts]

def save_results(output_dir, snippets, metrics, ts, series_name):
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(os.path.join(output_dir), exist_ok=True)

    snippets_json = [
        {"index": int(idx), "subsequence": subseq.tolist()} for idx, subseq in snippets
    ]
    with open(os.path.join(output_dir, 'snippets.json'), 'w') as f:
        json.dump(snippets_json, f, indent=4)

    metrics_serializable = {k: (v.tolist() if isinstance(v, np.ndarray) else v) for k, v in metrics.items()}
    with open(os.path.join(output_dir, 'metrics.json'), 'w') as f:
        json.dump(metrics_serializable, f, indent=4)

    ts_dir = os.path.join("time_series")
    os.makedirs(ts_dir, exist_ok=True)
    ts_path = os.path.join(ts_dir, series_name)
    with open(ts_path, 'w') as f:
        f.write(','.join(map(str, ts)))

def zip_folder(folder_path, output_path):
    shutil.make_archive(output_path, 'zip', root_dir='.', base_dir=folder_path)

# ======================== FUNÇÕES DE CLUSTERING E SNIPPETS ========================
def clustering_subsequences(segments_norm, num_clusters=None, method='kshape', linkage='ward', min_cluster_size=5, batch_size=100):
    if method == 'kshape':
        kshape = KShape(n_clusters=num_clusters, random_state=0)
        kshape.fit(segments_norm)
        return kshape.labels_, kshape.cluster_centers_.squeeze()
    elif method == 'agglomerative':
        clustering = AgglomerativeClustering(n_clusters=num_clusters, linkage=linkage)
        labels = clustering.fit_predict(segments_norm)
        centroids = [segments_norm[labels == i].mean(axis=0) if len(segments_norm[labels == i]) > 0 else np.zeros(segments_norm.shape[1]) for i in range(num_clusters)]
        return labels, np.array(centroids)
    elif method == 'hierarchical':
        distance_matrix = pdist(segments_norm, metric='euclidean')
        Z = scipy_linkage(distance_matrix, method=linkage)
        labels = fcluster(Z, t=num_clusters, criterion='maxclust') - 1
        centroids = [segments_norm[labels == i].mean(axis=0) if len(segments_norm[labels == i]) > 0 else np.zeros(segments_norm.shape[1]) for i in range(num_clusters)]
        return labels, np.array(centroids)
    elif method == 'hdbscan':
        clusterer = hdbscan.HDBSCAN(min_cluster_size=min_cluster_size)
        labels = clusterer.fit_predict(segments_norm)
        unique = set(labels) - {-1}
        centroids = [segments_norm[labels == i].mean(axis=0) if len(segments_norm[labels == i]) > 0 else np.zeros(segments_norm.shape[1]) for i in unique]
        return labels, np.array(centroids)
    elif method == 'minibatchkmeans':
        mbk = MiniBatchKMeans(n_clusters=num_clusters, batch_size=batch_size, random_state=0)
        mbk.fit(segments_norm)
        return mbk.labels_, mbk.cluster_centers_
    raise ValueError("Método inválido")

def find_snippets_clustering(ts, subseq_size, num_snippets=5, num_clusters=None, clustering_method='kshape', linkage='ward', min_cluster_size=5, batch_size=50):
    start = datetime.now()
    tracemalloc.start()

    segments_raw = np.array([ts[i:i + subseq_size] for i in range(len(ts) - subseq_size + 1)])
    segments_norm = TimeSeriesScalerMeanVariance().fit_transform(segments_raw).squeeze()

    labels, centroids = clustering_subsequences(segments_norm, num_clusters, clustering_method, linkage, min_cluster_size, batch_size)
    unique_clusters = set(labels) - {-1}

    medoides = []
    all_profiles = []
    for i, cluster_id in enumerate(unique_clusters):
        cluster_idxs = np.where(labels == cluster_id)[0]
        dists = np.linalg.norm(segments_norm[cluster_idxs] - centroids[i], axis=1)
        medoid_local_idx = cluster_idxs[np.argmin(dists)]
        medoides.append((medoid_local_idx, segments_raw[medoid_local_idx]))
        all_profiles.append(np.linalg.norm(segments_norm - segments_norm[medoid_local_idx], axis=1))

    min_profile = np.min(np.array(all_profiles), axis=0)
    min_idx_per_segment = np.argmin(np.array(all_profiles), axis=0)
    profile_area = [(min_idx_per_segment == i).sum() / len(min_idx_per_segment) for i in range(len(medoides))]
    cover_area = np.sum(min_profile)

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    elapsed = (datetime.now() - start).total_seconds()

    metrics = {
        'execution_time_sec': elapsed,
        'memory_usage_mb': round(current / (1024 ** 2), 2),
        'peak_memory_mb': round(peak / (1024 ** 2), 2),
        'profile_area': profile_area,
        'min_profile_area': min_profile.tolist(),
        'cover_area': float(cover_area),
    }

    return medoides, metrics

def find_snippets_stumpy(ts, subseq_size, num_snippets):
    start = datetime.now()
    tracemalloc.start()

    (
        snippets_array,
        snippets_indices,
        snippets_profiles,
        snippets_fractions,
        snippets_areas,
        snippets_regimes
    ) = stumpy.snippets(ts, m=subseq_size, k=num_snippets)

    snippets = list(zip(snippets_indices, snippets_array))
    min_profile = np.min(snippets_profiles, axis=0)
    cover_area = np.sum(min_profile)

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    elapsed = (datetime.now() - start).total_seconds()

    metrics = {
        'execution_time_sec': elapsed,
        'memory_usage_mb': round(current / (1024 ** 2), 2),
        'peak_memory_mb': round(peak / (1024 ** 2), 2),
        'profile_area': snippets_fractions.tolist(),
        'min_profile_area': min_profile.tolist(),
        'cover_area': float(cover_area),
    }

    return snippets, metrics

# ======================== INTERFACE ========================
subseq_size = st.number_input("Tamanho da subsequência:", min_value=10, max_value=1000, value=150)
k_min = st.number_input("k mínimo:", 2, 100, 2)
k_max = st.number_input("k máximo:", 2, 100, 5)
num_snippets = st.number_input("Quantidade de Snippets:", 1, 100, 1)
k_range = (k_min, k_max)
methods = ['agglomerative', 'hierarchical', 'hdbscan', 'minibatchkmeans', 'kshape', 'snippet_finder']
selected_methods = st.multiselect("Selecione métodos:", methods)
params = {}

for method in selected_methods:
    if method in ['agglomerative', 'hierarchical']:
        params[method] = {'linkage': st.selectbox(f"Linkage para {method}", ['ward', 'complete', 'average', 'single'], key=method)}
    elif method == 'hdbscan':
        params[method] = {'min_cluster_size': st.number_input("min_cluster_size para HDBSCAN", 2, 100, 5)}
    elif method == 'minibatchkmeans':
        params[method] = {'batch_size': st.number_input("batch_size para MiniBatchKMeans", 10, 500, 50)}
    elif method in ['kshape', 'snippet_finder']:
        params[method] = {}

# ======================== SELEÇÃO OU UPLOAD DE SÉRIE ========================
series_option = st.radio("Como deseja fornecer a série temporal?", ["Selecionar existente", "Fazer upload"])

dataset = {}
series_label = ""

if series_option == "Selecionar existente":
    base_path = 'app/time_series'
    for file in os.listdir(base_path):
        with open(os.path.join(base_path, file), 'r') as f:
            dataset[file] = parse_number_list(f.read())
    selected_series = st.multiselect("Selecione séries para processar:", list(dataset.keys()))

elif series_option == "Fazer upload":
    uploaded_file = st.file_uploader("Faça upload de um arquivo .txt com a série temporal", type=["txt"])
    if uploaded_file is not None:
        try:
            content = uploaded_file.read().decode("utf-8")
            ts_values = parse_number_list(content)
            filename = uploaded_file.name
            dataset[filename] = ts_values
            st.success(f"Série '{filename}' carregada com sucesso!")
            selected_series = st.multiselect("Selecione séries para processar:", [filename], default=[filename])
        except Exception as e:
            st.error(f"Erro ao ler a série: {e}")
    else:
        selected_series = []


if st.button("Executar Clusterizações"):
    output_folder = "resultados"
    os.makedirs(output_folder, exist_ok=True)

    for series_name in selected_series:
        ts = dataset[series_name]
        for method in selected_methods:
            method_output = os.path.join(output_folder, series_name.replace('.txt', ''), method)
            os.makedirs(method_output, exist_ok=True)
            kwargs = {
                'ts': ts,
                'subseq_size': subseq_size,
                'num_snippets': num_snippets,
                'num_clusters': k_max if method != 'hdbscan' else None,
                'clustering_method': method,
            }
            kwargs.update(params.get(method, {}))

            if method == 'snippet_finder':
                snippets, metrics = find_snippets_stumpy(ts, subseq_size, 5)
            else:
                snippets, metrics = find_snippets_clustering(**kwargs)

            save_results(method_output, snippets, metrics, ts, series_name)

    zip_path = "resultados"
    zip_folder(output_folder, zip_path)
    with open(f"{zip_path}.zip", "rb") as f:
        st.download_button("Baixar Resultados (.zip)", f, file_name=f"{'_'.join(selected_methods)}-{'_'.join(selected_series)}.zip")
        
    st.success("Processamento finalizado!")
    st.markdown("### 📊 Prévia de Métricas da Última Série Processada")

    # Tabela principal
    flat_metrics = {
        "Tempo de Execução (s)": metrics["execution_time_sec"],
        "Uso de Memória Atual (MB)": metrics["memory_usage_mb"],
        "Pico de Memória (MB)": metrics["peak_memory_mb"],
        "Área de Cobertura (Cover Area)": metrics["cover_area"]
    }

    # Exibição com st.metric
    cols = st.columns(len(flat_metrics))
    for i, (label, value) in enumerate(flat_metrics.items()):
        cols[i].metric(label, round(value, 3) if isinstance(value, float) else value)

    # Área de perfil
    st.markdown("#### 📌 Área de Perfil por Snippet")
    profile_df = pd.DataFrame({
        "Snippet": list(range(1, len(metrics["profile_area"]) + 1)),
        "Área de Perfil": metrics["profile_area"]
    })
    st.dataframe(profile_df, use_container_width=True)

    # Série do perfil mínimo (opcional: para debug ou análise visual)
    st.markdown("#### 🧬 Perfil Mínimo (Min Profile)")
    min_profile_df = pd.DataFrame({
        "Índice": list(range(len(metrics["min_profile_area"]))),
        "Distância": metrics["min_profile_area"]
    })
    st.line_chart(min_profile_df.set_index("Índice"))
