import streamlit as st
import json
import os

class SimpleTranslationSystem:
    def __init__(self):
        self.translations_file = "app/translations.json"
        self.translations = self.load_translations()
        
        # Inicializar estado da tradução
        if 'translate_enabled' not in st.session_state:
            st.session_state.translate_enabled = False
        if 'target_language' not in st.session_state:
            st.session_state.target_language = 'pt'
    
    def load_translations(self):
        """Carregar traduções pré-definidas"""
        if os.path.exists(self.translations_file):
            try:
                with open(self.translations_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                pass
        
        # Traduções padrão
        return {
            "pt": {
                "Home": "Home",
                "Visualizador": "Visualizador", 
                "Algoritmos": "Algoritmos",
                "Métricas": "Métricas",
                "🧠 GUISSE - Graphical User Interface for Snippet Selection and Evaluation": "🧠 GUISSE - Graphical User Interface for Snippet Selection and Evaluation",
                "Uma ferramenta interativa para seleção de snippets em séries temporais via diferentes algoritmos, visualização interativa de resultados e análise comparativa de métricas de desempenho.": "Uma ferramenta interativa para seleção de snippets em séries temporais via diferentes algoritmos, visualização interativa de resultados e análise comparativa de métricas de desempenho.",
                "Visualizador de Resultados": "Visualizador de Resultados",
                "Algoritmos Parametrizados": "Algoritmos Parametrizados", 
                "Comparador de Métricas": "Comparador de Métricas",
                "Pensado para fornecer indicadores e recomendações para a melhoria da saúde dos seus usuários, ajudando as linhas de pesquisa a captar dados para análise.": "Pensado para fornecer indicadores e recomendações para a melhoria da saúde dos seus usuários, ajudando as linhas de pesquisa a captar dados para análise.",
                "A prática que visa integrar o desenvolvimento, a operação e a manutenção de sistemas de aprendizado de máquina de forma eficiente e escalável.": "A prática que visa integrar o desenvolvimento, a operação e a manutenção de sistemas de aprendizado de máquina de forma eficiente e escalável.",
                "O Kubeflow é um framework open source do Kubernetes usado no desenvolvimento, gerenciamento e execução de cargas de trabalho de machine learning (ML).": "O Kubeflow é um framework open source do Kubernetes usado no desenvolvimento, gerenciamento e execução de cargas de trabalho de machine learning (ML).",
                "Visualização dos Snippets": "Visualização dos Snippets",
                "Explore e analise os resultados dos algoritmos de clustering de séries temporais": "Explore e analise os resultados dos algoritmos de clustering de séries temporais",
                "Bem-vindos ao GUISSE": "Bem-vindos ao GUISSE",
                "Esta é uma demonstração do sistema de tradução automática.": "Esta é uma demonstração do sistema de tradução automática.",
                "Funcionalidades": "Funcionalidades",
                "• Tradução em tempo real": "• Tradução em tempo real",
                "• Cache inteligente": "• Cache inteligente", 
                "• Múltiplos idiomas": "• Múltiplos idiomas",
                "Como usar": "Como usar",
                "1. Ative o toggle na sidebar": "1. Ative o toggle na sidebar",
                "2. Escolha o idioma desejado": "2. Escolha o idioma desejado",
                "3. Veja a tradução automática": "3. Veja a tradução automática",
                "Sistema de tradução funcionando perfeitamente!": "Sistema de tradução funcionando perfeitamente!",
                "GUISSE - Clustering Parametrizável": "GUISSE - Clustering Parametrizável",
                "Execute algoritmos avançados de clustering em séries temporais com parâmetros customizáveis": "Execute algoritmos avançados de clustering em séries temporais com parâmetros customizáveis",
                "Algoritmos Avançados": "Algoritmos Avançados",
                "K-Shape, HDBSCAN, Hierarchical e outros algoritmos de clustering de ponta.": "K-Shape, HDBSCAN, Hierarchical e outros algoritmos de clustering de ponta.",
                "Parâmetros Flexíveis": "Parâmetros Flexíveis",
                "Configure todos os parâmetros dos algoritmos para otimizar seus resultados.": "Configure todos os parâmetros dos algoritmos para otimizar seus resultados.",
                "Resultados Detalhados": "Resultados Detalhados",
                "Obtenha métricas completas e arquivos prontos para visualização.": "Obtenha métricas completas e arquivos prontos para visualização.",
                "Processamento finalizado!": "Processamento finalizado!",
                "Prévia de Métricas da Última Série Processada": "Prévia de Métricas da Última Série Processada",
                "Área de Perfil por Snippet": "Área de Perfil por Snippet",
                "Snippet": "Snippet",
                "Área de Perfil": "Área de Perfil",
                "Perfil Mínimo (Min Profile)": "Perfil Mínimo (Min Profile)",
                "Índice": "Índice",
                "Opções de Execução": "Opções de Execução",
                "Usar resultados da execução do algoritmo": "Usar resultados da execução do algoritmo",
                "Performance Analysis": "Performance Analysis",
                "Analise tempo de execução, memória e qualidade dos clusters.": "Analise tempo de execução, memória e qualidade dos clusters.",
                "Visualizações": "Visualizações",
                "Gráficos interativos para facilitar a interpretação dos resultados.": "Gráficos interativos para facilitar a interpretação dos resultados.",
                "Visualização Interativa": "Visualização Interativa",
                "Explore os snippets extraídos com gráficos interativos e análises detalhadas.": "Explore os snippets extraídos com gráficos interativos e análises detalhadas.",
                "Análise Detalhada": "Análise Detalhada",
                "Examine cada snippet individualmente com informações de contexto e métricas.": "Examine cada snippet individualmente com informações de contexto e métricas.",
                "Resultados Comparativos": "Resultados Comparativos",
                "Compare diferentes algoritmos e suas respectivas extrações de snippets.": "Compare diferentes algoritmos e suas respectivas extrações de snippets.",
                "Resultados carregados a partir do arquivo local.": "Resultados carregados a partir do arquivo local.",
                "Arquivo 'resultados.zip' não encontrado.": "Arquivo 'resultados.zip' não encontrado.",
                "Resultados carregados com sucesso!": "Resultados carregados com sucesso!",
                "Arquivo ZIP inválido.": "Arquivo ZIP inválido.",
                "Pasta de Avaliação:": "Pasta de Avaliação:",
                "Selecione a Série:": "Selecione a Série:",
                "Selecione os Métodos:": "Selecione os Métodos:",
                "Carregar Métricas": "Carregar Métricas",
                "Método": "Método",
                "Métrica": "Métrica",
                "Valor": "Valor",
                "Tabela de Métricas": "Tabela de Métricas",
                "Gráficos Comparativos": "Gráficos Comparativos",
                "Métricas Comparativas": "Métricas Comparativas",
                "Compare o desempenho dos diferentes algoritmos de clustering através de métricas detalhadas": "Compare o desempenho dos diferentes algoritmos de clustering através de métricas detalhadas",
                "Compare o desempenho de diferentes algoritmos com métricas detalhadas.": "Compare o desempenho de diferentes algoritmos com métricas detalhadas.",
                "Tamanho da subsequência:": "Tamanho da subsequência:",
                "k mínimo:": "k mínimo:",
                "k máximo:": "k máximo:",
                "Quantidade de Snippets:": "Quantidade de Snippets:",
                "Selecione os métodos:": "Selecione os métodos:",
                "Como deseja fornecer a série temporal?": "Como deseja fornecer a série temporal?",
                "Selecionar existente": "Selecionar existente",
                "Fazer upload": "Fazer upload",
                "Selecione séries para processar:": "Selecione séries para processar:",
                "Faça upload de um arquivo .txt com a série temporal": "Faça upload de um arquivo .txt com a série temporal",
                "Executar Clusterizações": "Executar Clusterizações",
                "min_cluster_size para HDBSCAN": "min_cluster_size para HDBSCAN",
                "batch_size para MiniBatchKMeans": "batch_size para MiniBatchKMeans",
                "Valor de Threshold": "Valor de Threshold",
                "Diferença máxima permitida ponto a ponto entre o snippet e o trecho da série.": "Diferença máxima permitida ponto a ponto entre o snippet e o trecho da série.",
                "Iniciar": "Iniciar",
                "Série original carregada com sucesso!": "Série original carregada com sucesso!",
                "Selecione os Métodos a Comparar:": "Selecione os Métodos a Comparar:",
                "Pasta de Avaliação:": "Pasta de Avaliação:",
                "Selecione a Série:": "Selecione a Série:",
                "Arquivo 'resultados.zip' não encontrado no diretório do projeto.": "Arquivo 'resultados.zip' não encontrado no diretório do projeto.",
                "O arquivo fornecido não é um arquivo ZIP válido.": "O arquivo fornecido não é um arquivo ZIP válido.",
                "Nenhuma pasta encontrada no arquivo ZIP extraído.": "Nenhuma pasta encontrada no arquivo ZIP extraído.",
                "Shapes dos Snippets": "Shapes dos Snippets",
                "Snippets sobrepostos na Série": "Snippets sobrepostos na Série",
                "Resultados carregados a partir do arquivo local.": "Resultados carregados a partir do arquivo local.",
                "Envie o arquivo .zip com os resultados:": "Envie o arquivo .zip com os resultados:"
            },
            "en": {
                "Home": "Home",
                "Visualizador": "Visualizer",
                "Algoritmos": "Algorithms", 
                "Métricas": "Metrics",
                "🧠 GUISSE - Graphical User Interface for Snippet Selection and Evaluation": "🧠 GUISSE - Graphical User Interface for Snippet Selection and Evaluation",
                "Uma ferramenta interativa para seleção de snippets em séries temporais via diferentes algoritmos, visualização interativa de resultados e análise comparativa de métricas de desempenho.": "An interactive tool for selecting snippets in time series via different algorithms, interactive visualization of results and comparative analysis of performance metrics.",
                "Visualizador de Resultados": "Results Visualizer",
                "Algoritmos Parametrizados": "Parameterized Algorithms",
                "Comparador de Métricas": "Metrics Comparator", 
                "Pensado para fornecer indicadores e recomendações para a melhoria da saúde dos seus usuários, ajudando as linhas de pesquisa a captar dados para análise.": "Designed to provide indicators and recommendations for improving the health of your users, helping research lines to capture data for analysis.",
                "A prática que visa integrar o desenvolvimento, a operação e a manutenção de sistemas de aprendizado de máquina de forma eficiente e escalável.": "The practice that aims to integrate the development, operation and maintenance of machine learning systems in an efficient and scalable way.",
                "O Kubeflow é um framework open source do Kubernetes usado no desenvolvimento, gerenciamento e execução de cargas de trabalho de machine learning (ML).": "Kubeflow is an open source Kubernetes framework used in the development, management and execution of machine learning (ML) workloads.",
                "Visualização dos Snippets": "Snippets Visualization",
                "Explore e analise os resultados dos algoritmos de clustering de séries temporais": "Explore and analyze the results of time series clustering algorithms",
                "Bem-vindos ao GUISSE": "Welcome to GUISSE",
                "Esta é uma demonstração do sistema de tradução automática.": "This is a demonstration of the automatic translation system.",
                "Funcionalidades": "Features",
                "• Tradução em tempo real": "• Real-time translation",
                "• Cache inteligente": "• Smart cache",
                "• Múltiplos idiomas": "• Multiple languages", 
                "Como usar": "How to use",
                "1. Ative o toggle na sidebar": "1. Enable the toggle in the sidebar",
                "2. Escolha o idioma desejado": "2. Choose the desired language",
                "3. Veja a tradução automática": "3. See the automatic translation",
                "Sistema de tradução funcionando perfeitamente!": "Translation system working perfectly!",
                "GUISSE - Clustering Parametrizável": "GUISSE - Parameterizable Clustering",
                "Execute algoritmos avançados de clustering em séries temporais com parâmetros customizáveis": "Execute advanced clustering algorithms on time series with customizable parameters",
                "Algoritmos Avançados": "Advanced Algorithms",
                "K-Shape, HDBSCAN, Hierarchical e outros algoritmos de clustering de ponta.": "K-Shape, HDBSCAN, Hierarchical and other cutting-edge clustering algorithms.",
                "Parâmetros Flexíveis": "Flexible Parameters",
                "Configure todos os parâmetros dos algoritmos para otimizar seus resultados.": "Configure all algorithm parameters to optimize your results.",
                "Resultados Detalhados": "Detailed Results",
                "Obtenha métricas completas e arquivos prontos para visualização.": "Get comprehensive metrics and files ready for visualization.",
                "Processamento finalizado!": "Processing completed!",
                "Prévia de Métricas da Última Série Processada": "Preview of Metrics from Last Processed Series",
                "Área de Perfil por Snippet": "Profile Area per Snippet",
                "Snippet": "Snippet",
                "Área de Perfil": "Profile Area",
                "Perfil Mínimo (Min Profile)": "Minimum Profile (Min Profile)",
                "Índice": "Index",
                "Opções de Execução": "Execution Options",
                "Usar resultados da execução do algoritmo": "Use results from algorithm execution",
                "Performance Analysis": "Performance Analysis",
                "Analise tempo de execução, memória e qualidade dos clusters.": "Analyze execution time, memory and cluster quality.",
                "Visualizações": "Visualizations",
                "Gráficos interativos para facilitar a interpretação dos resultados.": "Interactive charts to facilitate results interpretation.",
                "Visualização Interativa": "Interactive Visualization",
                "Explore os snippets extraídos com gráficos interativos e análises detalhadas.": "Explore extracted snippets with interactive charts and detailed analysis.",
                "Análise Detalhada": "Detailed Analysis",
                "Examine cada snippet individualmente com informações de contexto e métricas.": "Examine each snippet individually with context information and metrics.",
                "Resultados Comparativos": "Comparative Results",
                "Compare diferentes algoritmos e suas respectivas extrações de snippets.": "Compare different algorithms and their respective snippet extractions.",
                "Resultados carregados a partir do arquivo local.": "Results loaded from local file.",
                "Arquivo 'resultados.zip' não encontrado.": "'resultados.zip' file not found.",
                "Envie o arquivo .zip com os resultados:": "Upload the .zip file with results:",
                "Resultados carregados com sucesso!": "Results loaded successfully!",
                "Arquivo ZIP inválido.": "Invalid ZIP file.",
                "Pasta de Avaliação:": "Evaluation Folder:",
                "Selecione a Série:": "Select Series:",
                "Selecione os Métodos:": "Select Methods:",
                "Carregar Métricas": "Load Metrics",
                "Método": "Method",
                "Métrica": "Metric",
                "Valor": "Value",
                "Tabela de Métricas": "Metrics Table",
                "Gráficos Comparativos": "Comparative Charts",
                "Métricas Comparativas": "Comparative Metrics",
                "Compare o desempenho dos diferentes algoritmos de clustering através de métricas detalhadas": "Compare the performance of different clustering algorithms through detailed metrics",
                "Compare o desempenho de diferentes algoritmos com métricas detalhadas.": "Compare the performance of different algorithms with detailed metrics.",
                "Tamanho da subsequência:": "Subsequence Size:",
                "k mínimo:": "Minimum k:",
                "k máximo:": "Maximum k:",
                "Quantidade de Snippets:": "Number of Snippets:",
                "Selecione os métodos:": "Select Methods:",
                "Como deseja fornecer a série temporal?": "How would you like to provide the time series?",
                "Selecionar existente": "Select Existing",
                "Fazer upload": "Upload File",
                "Selecione séries para processar:": "Select series to process:",
                "Faça upload de um arquivo .txt com a série temporal": "Upload a .txt file with the time series",
                "Executar Clusterizações": "Execute Clustering",
                "min_cluster_size para HDBSCAN": "min_cluster_size for HDBSCAN",
                "batch_size para MiniBatchKMeans": "batch_size for MiniBatchKMeans",
                "Valor de Threshold": "Threshold Value",
                "Diferença máxima permitida ponto a ponto entre o snippet e o trecho da série.": "Maximum allowed point-to-point difference between snippet and series segment.",
                "Iniciar": "Start",
                "Série original carregada com sucesso!": "Original series loaded successfully!",
                "Selecione os Métodos a Comparar:": "Select Methods to Compare:",
                "Pasta de Avaliação:": "Evaluation Folder:",
                "Selecione a Série:": "Select Series:",
                "Arquivo 'resultados.zip' não encontrado no diretório do projeto.": "'resultados.zip' file not found in the project directory.",
                "O arquivo fornecido não é um arquivo ZIP válido.": "The provided file is not a valid ZIP file.",
                "Nenhuma pasta encontrada no arquivo ZIP extraído.": "No folders found in the extracted ZIP file.",
                "Shapes dos Snippets": "Snippet Shapes",
                "Snippets sobrepostos na Série": "Snippets Overlaid on Series",
                "Resultados carregados a partir do arquivo local.": "Results loaded from local file."
            }
        }
    
    def save_translations(self):
        """Salvar traduções"""
        try:
            os.makedirs(os.path.dirname(self.translations_file), exist_ok=True)
            with open(self.translations_file, 'w', encoding='utf-8') as f:
                json.dump(self.translations, f, ensure_ascii=False, indent=2)
        except:
            pass
    
    def translate_text(self, text, target_lang='pt'):
        """Traduzir texto usando dicionário pré-definido"""
        if not text or not text.strip():
            return text
            
        if target_lang in self.translations:
            return self.translations[target_lang].get(text, text)
        
        return text
    
    def create_toggle_ui(self):
        """Criar interface do toggle de tradução"""
        # Garantir que o session_state seja inicializado primeiro
        if 'translate_enabled' not in st.session_state:
            st.session_state.translate_enabled = False
        if 'target_language' not in st.session_state:
            st.session_state.target_language = 'pt'
            
        with st.container():
            st.markdown("### 🌍 Translation System")
            
            # Toggle principal
            enabled = st.toggle(
                "Enable Translation",
                value=st.session_state.translate_enabled,
                key="translation_toggle_simple"
            )
            
            st.session_state.translate_enabled = enabled
            
            if enabled:
                # Traduzir para pt-br
                st.session_state.target_language = 'pt'
                st.info("📝 Traduzindo para: Português")
            else:
                # Mostrar em inglês
                st.session_state.target_language = 'en'
                st.info("Exibindo em Inglês (original)")
    
    def t(self, text):
        """Função helper para tradução"""
        # Garantir que o session_state seja inicializado
        if 'translate_enabled' not in st.session_state:
            st.session_state.translate_enabled = False
        if 'target_language' not in st.session_state:
            st.session_state.target_language = 'pt'
        # Se o toggle estiver ativado, traduz para pt-br
        if st.session_state.translate_enabled:
            return self.translate_text(text, 'pt')
        # Se desativado, exibe em inglês
        return self.translate_text(text, 'en')

# Instância global do sistema de tradução
simple_translation_system = SimpleTranslationSystem()

def create_translation_toggle():
    """Criar toggle de tradução na sidebar"""
    with st.sidebar:
        st.markdown("---")
        simple_translation_system.create_toggle_ui()
        st.markdown("---")

def t(text):
    """Função de tradução simplificada para uso nas páginas"""
    return simple_translation_system.t(text)
