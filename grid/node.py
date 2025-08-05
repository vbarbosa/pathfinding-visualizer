from config import *

class Node:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.x = col * CELL_SIZE
        self.y = row * CELL_SIZE
        self.color = WHITE
        self.neighbors = []

    def get_pos(self):
        return self.row, self.col

    # Estado atual
    def is_closed(self):
        return self.color == RED

    def is_open(self):
        return self.color == GREEN

    def is_wall(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == ORANGE

    def is_end(self):
        return self.color == TURQUOISE

    def is_path(self):
        return self.color == YELLOW

    # Alterações de estado
    def reset(self):
        self.color = WHITE

    def make_start(self):
        self.color = ORANGE

    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = GREEN

    def make_wall(self):
        self.color = BLACK

    def make_end(self):
        self.color = TURQUOISE

    def make_path(self):
        self.color = YELLOW

    # Desenha o nó na tela
    def draw(self, win):
        import pygame
        pygame.draw.rect(win, self.color, (self.x, self.y, CELL_SIZE, CELL_SIZE))

    # Atualiza vizinhos válidos (sem parede) para algoritmos
    def update_neighbors(self, grid):
        self.neighbors = []

        if self.row < ROWS - 1 and not grid[self.row + 1][self.col].is_wall():  # baixo
            self.neighbors.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].is_wall():  # cima
            self.neighbors.append(grid[self.row - 1][self.col])

        if self.col < ROWS - 1 and not grid[self.row][self.col + 1].is_wall():  # direita
            self.neighbors.append(grid[self.row][self.col + 1])

        if self.col > 0 and not grid[self.row][self.col - 1].is_wall():  # esquerda
            self.neighbors.append(grid[self.row][self.col - 1])
