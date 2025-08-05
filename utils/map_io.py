import json
import os
import sys
from grid.grid_builder import make_grid
from config import ROWS

def resource_path(relative_path):
    """Resolve o caminho do arquivo, compatível com PyInstaller."""
    base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
    return os.path.join(base_path, relative_path)

def save_map(grid, start, end, path="saved_map.json"):
    """Salva o mapa atual em um arquivo JSON."""
    data = {
        "start": start.get_pos() if start else None,
        "end": end.get_pos() if end else None,
        "walls": [node.get_pos() for row in grid for node in row if node.is_wall()]
    }

    try:
        with open(os.path.join(os.getcwd(), path), "w") as f:
            json.dump(data, f)
    except Exception as e:
        print(f"Erro ao salvar mapa: {e}")

def load_map(path="saved_map.json"):
    """Carrega um mapa salvo e retorna (grid, start, end)."""
    full_path = resource_path(path)
    if not os.path.exists(full_path):
        raise FileNotFoundError(f"Arquivo não encontrado: {path}")

    try:
        with open(full_path, "r") as f:
            data = json.load(f)

        grid = make_grid()
        start = end = None

        wall_positions = set(map(tuple, data.get("walls", [])))
        start_pos = tuple(data.get("start")) if data.get("start") else None
        end_pos = tuple(data.get("end")) if data.get("end") else None

        for row in grid:
            for node in row:
                pos = node.get_pos()
                if pos in wall_positions:
                    node.make_wall()
                elif start_pos and pos == start_pos:
                    node.make_start()
                    start = node
                elif end_pos and pos == end_pos:
                    node.make_end()
                    end = node

        return grid, start, end

    except Exception as e:
        print(f"Erro ao carregar mapa: {e}")
        raise

def load_dummy_map():
    """Carrega um mapa de exemplo para testes."""
    grid = make_grid()
    start = grid[0][0]
    end = grid[ROWS - 1][ROWS - 1]
    start.make_start()
    end.make_end()

    for i in range(10, 20):
        grid[i][15].make_wall()

    return grid, start, end
