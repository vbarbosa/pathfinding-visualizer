
import unittest
from algorithms.dijkstra import dijkstra
from grid.grid_builder import make_grid, update_neighbors
from config import ROWS

class DummyWin:
    def __call__(self): pass

class TestDijkstra(unittest.TestCase):
    def test_dijkstra_executes(self):
        grid = make_grid()
        start = grid[0][0]
        end = grid[ROWS - 1][ROWS - 1]
        start.make_start()
        end.make_end()
        update_neighbors(grid)
        try:
            dijkstra(DummyWin(), grid, start, end)
        except Exception as e:
            self.fail(f"Dijkstra algorithm raised an exception: {e}")
