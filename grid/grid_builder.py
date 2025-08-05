
from .node import Node
from config import ROWS

def make_grid():
    return [[Node(i, j) for j in range(ROWS)] for i in range(ROWS)]

def update_neighbors(grid):
    for row in grid:
        for node in row:
            node.update_neighbors(grid)
