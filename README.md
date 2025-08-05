# 🧭 Pathfinding Visualizer

Um visualizador interativo de algoritmos de busca em grafos (Dijkstra e A*) com interface gráfica feita em Pygame. Permite criar mapas personalizados, salvar/carregar mapas, exportar imagens e visualizar passo a passo o funcionamento dos algoritmos.

---

## ✨ Funcionalidades

- Visualização dos algoritmos **Dijkstra** e **A\***.
- Interface gráfica com **Pygame**.
- Criação de mapas interativos com obstáculos.
- **Salvar** e **carregar** mapas (`.json`).
- **Exportar imagem** do mapa atual (`.png`).
- **Executar algoritmos** com animação em tempo real.
- **Limpar caminhos** ou **resetar o mapa**.
- Bateria completa de **testes automatizados** com `pytest`.

---

## 🧱 Estrutura do Projeto

```
pathfinding_visualizer/
├── algorithms/
│   ├── astar.py
│   └── dijkstra.py
├── grid/
│   ├── grid_builder.py
│   └── node.py
├── utils/
│   └── map_io.py
├── tests/
│   ├── test_astar.py
│   ├── test_dijkstra.py
│   ├── test_grid_builder.py
│   ├── test_integration_algorithms.py
│   ├── test_main.py
│   └── test_map_io.py
├── logs/
│   └── test_report.log
├── config.py
├── main.py
└── README.md
```

---

## 🚀 Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/pathfinding_visualizer.git
cd pathfinding_visualizer
```

### 2. Instale as dependências

```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Linux/macOS

pip install -r requirements.txt
```

> Ou crie um `requirements.txt` contendo:
```txt
pygame
```

### 3. Execute o programa

```bash
python main.py
```

---

## 🧪 Executando os Testes

### Com `pytest` (recomendado):

```bash
pytest tests/
```

### Com `unittest`:

```bash
python -m unittest discover -s tests
```

Logs de teste ficam salvos em:

```
logs/test_report.log
```

---

## 🖱️ Controles e Botões

- **Clique esquerdo**: define início, fim e paredes.
- **Clique direito**: remove blocos.
- **Botões**:
  - `Rodar algoritmo`: executa o algoritmo.
  - `Limpar caminhos`: remove apenas caminhos.
  - `Resetar tudo`: limpa tudo.
  - `Salvar mapa`: salva o `.json`.
  - `Carregar mapa`: carrega o `.json`.
  - `Carregar dummy`: mapa de teste.
  - `Exportar imagem`: `.png`.

---

## 🧠 Algoritmos

### ✅ Dijkstra
- Sem heurística.
- Caminho mais curto garantido.

### ✅ A*
- Usa heurística de Manhattan.
- Caminho mais curto garantido.

---

## 👨‍💻 Autor

Vinicius Barbosa Maria  
📧 vbarb_ihzzadu@...  
🖥️ Projeto pessoal para fins didáticos.
