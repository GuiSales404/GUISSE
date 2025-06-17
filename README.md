# 🧠 GUISSE - Graphical User Interface for Snippet Selection and Evaluation

Este repositório disponibiliza a interface gráfica do **GUISSE**, uma ferramenta interativa para:
- Seleção de *snippets* em séries temporais via diferentes algoritmos (incluindo RS4 e Snippet-Finder)
- Visualização interativa de resultados
- Comparação e análise de métricas de desempenho

## 📁 Estrutura do Repositório

```bash
├── app/                 # Aplicação principal em Streamlit (dividida por páginas)
├── exemplo.zip          # Exemplo de resultados para visualização
├── requirements.txt     # Dependências Python para executar a aplicação
├── README.md            # Este arquivo
└── LICENSE              # Licença do projeto
````

## 🚀 Como executar o projeto

1. Clone este repositório:

```bash
git clone https://github.com/SeuUsuario/RS4-GUI.git
cd RS4-GUI
```

2. (Opcional) Crie um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute a aplicação Streamlit:

```bash
streamlit run app/home.py
```

## 🧩 Funcionalidades principais

* **Execução customizada** dos algoritmos RS4, Snippet-Finder e métodos de clusterização.
* Upload e processamento de séries temporais.
* Visualização interativa dos *snippets* sobrepostos à série.
* Ajuste de limiar de similaridade (threshold) para comparação visual.
* Geração e download automático dos resultados em `.zip`.
* Comparação de métricas como tempo de execução, memória usada, área de cobertura, etc.

## 📦 Exemplo de uso

Você pode usar o arquivo `exemplo.zip` incluso no repositório para testar a interface sem executar o algoritmo novamente.
