import networkx as nx

lines = open("input.txt", "r").readlines()

grid = []
G = nx.DiGraph()
start = None
starts = []
end = None

def get_neighbours(t):
    n = []
    r, c = t
    w = grid[r][c]

    if r - 1 >= 0 and grid[r - 1][c] - w <= 1:
        n.append((r - 1, c))
    if r + 1 < len(grid) and grid[r + 1][c] - w <= 1:
        n.append((r + 1, c))
    if c - 1 >= 0 and grid[r][c - 1] - w <= 1:
        n.append((r, c - 1))
    if c + 1 < len(grid[0]) and grid[r][c + 1] - w <= 1:
        n.append((r, c + 1))

    return n

for row, line in enumerate(lines):
    grid.append([])
    for col, ch in enumerate(line.strip()):
        G.add_node((row, col))
        if ch == "a":
            starts.append((row, col))
        elif ch == "S":
            ch = "a"
            start = (row, col)
        elif ch == "E":
            ch = "z"
            end = (row, col)
        grid[-1].append(ord(ch))

for node in G.nodes():
    for n in get_neighbours(node):
        G.add_edge(node, n)

part1 = len(nx.shortest_path(G, start, end)) - 1
part2 = part1

for start in starts:
    try:
        part2 = min(len(nx.shortest_path(G, start, end)) - 1, part2)
    except:
        pass

print(part1)
print(part2)
