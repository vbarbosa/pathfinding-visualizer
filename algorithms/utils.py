
import json
import time

def reconstruct_path(came_from, current, draw, export_path=False):
    path = []
    while current in came_from:
        current = came_from[current]
        current.make_path()
        path.append((current.row, current.col))
        draw()
    path.reverse()
    if export_path:
        with open("path_result.json", "w") as f:
            json.dump(path, f, indent=4)
