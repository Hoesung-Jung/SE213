def calcPath(inserted_map, x, y):
    a = 0
    b = 0
    if x == len(inserted_map) - 1 and y == len(inserted_map) - 1:
        return 1
    if x + inserted_map[y][x] < len(inserted_map):
        a = calcPath(inserted_map, x + inserted_map[y][x], y)
    if y + inserted_map[y][x] < len(inserted_map):
        b = calcPath(inserted_map, x, y + inserted_map[y][x])
    return a + b