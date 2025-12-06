from sys import argv
from itertools import product

diagram = list(map(list, open(argv[1]).read().splitlines()))

part1, part2 = 0, 0

def get_adj(r, c, height, width):
    adj = list(product([r-1, r, r+1], [c-1, c, c+1]))
    adj.remove((r, c))
    adj = filter(lambda x: x[0] >= 0 and x[0] < height and x[1] >= 0 and x[1] < width, adj)
    return list(adj)

def get_accessible(diagram: list[list[str]]):
    indices = []
    for r in range(len(diagram)):
        for c in range(len(diagram[0])):
            if diagram[r][c] != "@":
                continue
            rolls = 0
            for adj_r, adj_c in get_adj(r, c, len(diagram), len(diagram[0])):
                if diagram[adj_r][adj_c] == "@": rolls += 1
            if rolls < 4: indices.append((r, c))
    return indices

indices = get_accessible(diagram)
part1 = part2 = len(indices)
while len(indices) != 0:
    for index in indices:
        diagram[index[0]][index[1]] = "."
    indices = get_accessible(diagram)
    part2 += len(indices)

print("part1:", part1)
print("part2:", part2)
