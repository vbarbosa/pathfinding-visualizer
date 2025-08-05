
import unittest
from algorithms.dijkstra import dijkstra
from algorithms.astar import astar
from grid.grid_builder import make_grid, update_neighbors
from config import ROWS

class DummyWin:
    def __call__(self): pass

class TestIntegrationAlgorithms(unittest.TestCase):
    def setUp(self):
        self.grid = make_grid()
        self.start = self.grid[0][0]
        self.end = self.grid[ROWS - 1][ROWS - 1]
        self.start.make_start()
        self.end.make_end()
        update_neighbors(self.grid)

    def test_run_dijkstra(self):
        dijkstra(DummyWin(), self.grid, self.start, self.end)

    def test_run_astar(self):
        astar(DummyWin(), self.grid, self.start, self.end)
