
import pygame
import os
import tkinter as tk
from tkinter import filedialog
from datetime import datetime

from config import *
from grid.grid_builder import make_grid, update_neighbors
from algorithms.dijkstra import dijkstra
from algorithms.astar import astar
from utils.map_io import save_map, load_map, load_dummy_map

INFO_WIDTH = 240
WINDOW_WIDTH = WIDTH + INFO_WIDTH
FONT_SIZE = 18
MESSAGE_DURATION = 2500  # milissegundos

BUTTONS = {
    "Dijkstra": (WIDTH + 20, 40, 200, 30),
    "A*": (WIDTH + 20, 80, 200, 30),
    "Rodar algoritmo": (WIDTH + 20, 140, 200, 30),
    "Limpar caminhos": (WIDTH + 20, 180, 200, 30),
    "Resetar tudo": (WIDTH + 20, 220, 200, 30),
    "Salvar mapa": (WIDTH + 20, 280, 200, 30),
    "Carregar mapa": (WIDTH + 20, 320, 200, 30),
    "Carregar dummy": (WIDTH + 20, 360, 200, 30),
    "Exportar imagem": (WIDTH + 20, 400, 200, 30)
}

def draw_button(win, rect, text, font, active=False, clicked=False):
    if clicked:
        color = (180, 180, 255)
    elif active:
        color = (180, 220, 180)
    else:
        color = (200, 200, 200)
    pygame.draw.rect(win, color, rect)
    pygame.draw.rect(win, BLACK, rect, 2)
    txt = font.render(text, True, BLACK)
    win.blit(txt, (rect[0]+10, rect[1]+5))

def draw_grid(win, grid, font, algo, message=None, clicked_button=None):
    win.fill(WHITE)
    for row in grid:
        for node in row:
            node.draw(win)

    for i in range(ROWS + 1):
        pygame.draw.line(win, GRAY, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE))
        pygame.draw.line(win, GRAY, (i * CELL_SIZE, 0), (i * CELL_SIZE, WIDTH))

    pygame.draw.rect(win, (245, 245, 245), (WIDTH, 0, INFO_WIDTH, WIDTH))
    txt = font.render("Algoritmo: " + algo.upper(), True, BLACK)
    win.blit(txt, (WIDTH + 10, 10))

    for name, rect in BUTTONS.items():
        active = (name.lower() == algo.lower())
        clicked = (name == clicked_button)
        draw_button(win, rect, name, font, active, clicked)

    legend = [
        "Legenda:",
        "Verde: Inicio",
        "Vermelho: Fim",
        "Preto: Obstaculo",
        "Amarelo: Caminho"
    ]
    for idx, line in enumerate(legend):
        txt = font.render(line, True, BLACK)
        win.blit(txt, (WIDTH + 10, 460 + idx * (FONT_SIZE + 2)))

    if message:
        txt = font.render("INFO: " + message, True, BLUE)
        win.blit(txt, (WIDTH + 10, 580))

    pygame.display.update()

def get_clicked_pos(pos):
    x, y = pos
    if x >= WIDTH:
        return None, None
    return y // CELL_SIZE, x // CELL_SIZE

def handle_button_click(pos):
    x, y = pos
    for name, rect in BUTTONS.items():
        rx, ry, rw, rh = rect
        if rx <= x <= rx+rw and ry <= y <= ry+rh:
            return name
    return None

def log_event(text):
    os.makedirs("logs", exist_ok=True)
    with open("logs/events.log", "a") as f:
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        f.write(f"{timestamp} {text}\n")

def export_image(win):
    try:
        root = tk.Tk()
        root.withdraw()
        filepath = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if filepath:
            sub = pygame.Surface((WIDTH, WIDTH))
            sub.blit(win, (0, 0), (0, 0, WIDTH, WIDTH))
            pygame.image.save(sub, filepath)
            log_event(f"Imagem exportada para {filepath}")
            return "Imagem exportada!"
    except Exception as e:
        log_event(f"Erro ao exportar imagem: {e}")
        return "Erro ao exportar imagem."
    return None

def main():
    os.makedirs("logs", exist_ok=True)
    pygame.init()
    win = pygame.display.set_mode((WINDOW_WIDTH, WIDTH))
    pygame.display.set_caption("Pathfinding Visualizer")
    font = pygame.font.SysFont("consolas", FONT_SIZE)

    grid = make_grid()
    start = None
    end = None
    algo = "dijkstra"
    has_run = False
    run = True
    last_message = None
    message_time = 0

    clicked_button = None
    while run:
        now = pygame.time.get_ticks()
        if last_message and now - message_time > MESSAGE_DURATION:
            last_message = None

        draw_grid(win, grid, font, algo, last_message, clicked_button)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                action = handle_button_click(pos)
                clicked_button = action
                if action:
                    if action == "Dijkstra":
                        algo = "dijkstra"
                        log_event("Algoritmo alterado para Dijkstra")
                    elif action == "A*":
                        algo = "astar"
                        log_event("Algoritmo alterado para A*")
                    elif action == "Rodar algoritmo":
                        if start and end:
                            # 🧹 Limpa caminhos anteriores
                            for row in grid:
                                for node in row:
                                    if node.is_closed() or node.is_open() or node.is_path():
                                        node.reset()
                            update_neighbors(grid)
                            if algo == "dijkstra":
                                dijkstra(lambda: draw_grid(win, grid, font, algo), grid, start, end)
                            else:
                                astar(lambda: draw_grid(win, grid, font, algo), grid, start, end)
                            last_message = "Algoritmo executado."
                            message_time = now
                            log_event("Algoritmo executado.")
                    elif action == "Limpar caminhos":
                        for row in grid:
                            for node in row:
                                if node.is_closed() or node.is_open() or node.is_path():
                                    node.reset()
                        last_message = "Caminhos limpos."
                        message_time = now
                        log_event("Caminhos limpos.")
                    elif action == "Resetar tudo":
                        grid = make_grid()
                        start, end = None, None
                        has_run = False
                        last_message = "Mapa reiniciado."
                        message_time = now
                        log_event("Mapa resetado.")
                    elif action == "Salvar mapa":
                        save_map(grid, start, end)
                        last_message = "Mapa salvo."
                        message_time = now
                        log_event("Mapa salvo.")
                    elif action == "Carregar mapa":
                        try:
                            root = tk.Tk()
                            root.withdraw()
                            filepath = filedialog.askopenfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
                            if filepath:
                                grid, start, end = load_map(filepath)
                                update_neighbors(grid)
                                has_run = False
                                last_message = "Mapa carregado."
                                message_time = now
                                log_event(f"Mapa carregado: {filepath}")
                            else:
                                last_message = "Carregamento cancelado."
                                message_time = now
                        except Exception as e:
                            last_message = "Erro ao carregar."
                            log_event(f"Erro ao carregar mapa: {e}")
                            message_time = now
                    elif action == "Carregar dummy":
                        grid, start, end = load_dummy_map()
                        update_neighbors(grid)
                        has_run = False
                        last_message = "Mapa dummy carregado."
                        message_time = now
                        log_event("Mapa dummy carregado.")
                    elif action == "Exportar imagem":
                        msg = export_image(win)
                        last_message = msg
                        message_time = now
                    continue

                row, col = get_clicked_pos(pos)
                if row is not None and col is not None:
                    node = grid[row][col]
                    if not start:
                        start = node
                        node.make_start()
                    elif not end and node != start:
                        end = node
                        node.make_end()
                    elif node != start and node != end:
                        node.make_wall()

            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos)
                if row is not None and col is not None:
                    node = grid[row][col]
                    node.reset()
                    if node == start:
                        start = None
                    elif node == end:
                        end = None

    pygame.quit()

if __name__ == "__main__":
    main()
