# 🧭 Pathfinding Visualizer

Um visualizador interativo de algoritmos de busca em grafos (Dijkstra e A*) com interface gráfica feita em **Pygame**.  
Permite criar mapas personalizados, salvar/carregar mapas, exportar imagens e visualizar passo a passo o funcionamento dos algoritmos.

---

## ✨ Funcionalidades

- Visualização dos algoritmos **Dijkstra** e **A\***.
- Interface gráfica com **Pygame**.
- Criação de mapas interativos com obstáculos.
- **Salvar** e **carregar** mapas (`.json`).
- **Exportar imagem** do mapa atual (`.png`).
- **Executar algoritmos** com animação em tempo real.
- **Limpar caminhos** ou **resetar o mapa**.
- Bateria completa de **testes automatizados** com `pytest` e `unittest`.

---

## 🧱 Estrutura do Projeto

```
pathfinding-visualizer/
├── algorithms/
│   ├── astar.py
│   ├── dijkstra.py
│   └── utils.py
├── grid/
│   ├── grid_builder.py
│   └── node.py
├── utils/
│   ├── heuristics.py
│   ├── map_io.py
│   └── networkx_adapter.py
├── tests/
│   ├── test_astar.py
│   ├── test_dijkstra.py
│   ├── test_grid_builder.py
│   ├── test_integration_algorithms.py
│   ├── test_main.py
│   └── test_map_io.py
├── logs/
│   └── test_report.log
├── main.py
├── config.py
├── saved_map.json
├── manhattan_map.json
├── README.md
└── .gitignore
```

---

## 🚀 Como Executar o Visualizador

### 1. Clone o repositório

```bash
git clone https://github.com/vbarbosa/pathfinding-visualizer.git
cd pathfinding-visualizer
```

### 2. Crie o ambiente virtual e instale as dependências

```bash
python -m venv venv
venv\Scripts\activate   # Windows
# ou
source venv/bin/activate   # Linux/macOS

pip install -r requirements.txt
```

> Se o `requirements.txt` ainda não existir, crie com:
```txt
pygame
pytest
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

> Logs de teste serão gerados automaticamente em:
```
logs/test_report.log
```

---

## 🖱️ Controles e Botões

- **Clique esquerdo**: define início, fim e paredes.
- **Clique direito**: remove blocos.
- **Botões da interface**:
  - `Rodar algoritmo`
  - `Limpar caminhos`
  - `Resetar tudo`
  - `Salvar mapa`
  - `Carregar mapa`
  - `Carregar dummy`
  - `Exportar imagem`

---

## 🧠 Algoritmos

### ✅ Dijkstra
- Sem heurística
- Garante o caminho mais curto

### ✅ A*
- Usa heurística de Manhattan
- Garante o caminho mais curto

---

## 📂 Git: comandos úteis

### Inicializar (já feito)

```bash
git init
git add .
git commit -m "Commit inicial"
```

### Vincular ao GitHub

```bash
git remote add origin git@github.com:vbarbosa/pathfinding-visualizer.git
git branch -M main
git push -u origin main
```

> ⚠️ Se houver conflitos:
```bash
git pull origin main --allow-unrelated-histories
# resolva conflitos se existirem
git add .
git commit -m "Resolve merge conflict"
git push
```

### Forçar push (último recurso)

```bash
git push --force
```

---

## 👨‍💻 Autor

Vinicius Barbosa Maria  
📧 vbarbosa.maria@gmail.com  
🖥️ Projeto pessoal para fins didáticos e aprendizado.
