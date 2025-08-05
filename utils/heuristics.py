def manhattan(a, b):
    return abs(a.row - b.row) + abs(a.col - b.col)

def euclidean(a, b):
    return ((a.row - b.row)**2 + (a.col - b.col)**2)**0.5