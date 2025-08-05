
import unittest
from grid.grid_builder import make_grid
from config import ROWS

class TestGridBuilder(unittest.TestCase):
    def test_grid_dimensions(self):
        grid = make_grid()
        self.assertEqual(len(grid), ROWS)
        self.assertTrue(all(len(row) == ROWS for row in grid))
