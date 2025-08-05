
import networkx as nx

def generate_nx_grid(grid):
    G = nx.Graph()
    for row in grid:
        for node in row:
            if not node.is_wall():
                for neighbor in node.neighbors:
                    if not neighbor.is_wall():
                        G.add_edge((node.row, node.col), (neighbor.row, neighbor.col), weight=1)
    return G
