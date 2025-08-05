
import unittest
import os
from utils.map_io import save_map, load_map
from grid.grid_builder import make_grid
from config import ROWS

class TestMapIO(unittest.TestCase):
    def test_save_and_load(self):
        grid = make_grid()
        start = grid[1][1]
        end = grid[2][2]
        grid[3][3].make_wall()
        start.make_start()
        end.make_end()

        save_map(grid, start, end)
        self.assertTrue(os.path.exists("saved_map.json"))

        grid2, start2, end2 = load_map("saved_map.json")
        self.assertEqual(start2.get_pos(), (1, 1))
        self.assertEqual(end2.get_pos(), (2, 2))
        self.assertTrue(grid2[3][3].is_wall())
