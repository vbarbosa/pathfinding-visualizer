import unittest
import pygame
from grid.grid_builder import make_grid
from config import WIDTH, ROWS, CELL_SIZE, WHITE, BLACK
from utils.map_io import save_map, load_map
import os

class TestGridAndMap(unittest.TestCase):
    def test_make_grid_dimensions(self):
        grid = make_grid()
        self.assertEqual(len(grid), ROWS)
        self.assertEqual(len(grid[0]), ROWS)

    def test_node_positions(self):
        grid = make_grid()
        for i in range(ROWS):
            for j in range(ROWS):
                self.assertEqual(grid[i][j].get_pos(), (i, j))

    def test_save_and_load_map(self):
        grid = make_grid()
        start = grid[0][0]
        end = grid[ROWS-1][ROWS-1]
        start.make_start()
        end.make_end()
        for i in range(5, 10):
            grid[i][5].make_wall()

        save_map(grid, start, end)
        self.assertTrue(os.path.exists("saved_map.json"))

        loaded_grid, loaded_start, loaded_end = load_map("saved_map.json")
        self.assertEqual(loaded_start.get_pos(), start.get_pos())
        self.assertEqual(loaded_end.get_pos(), end.get_pos())
        for i in range(5, 10):
            self.assertTrue(loaded_grid[i][5].is_wall())

if __name__ == "__main__":
    unittest.main()
