from copy import copy, deepcopy

l1 = [list(n) for n in open("input.txt").read().strip().splitlines()]
l2 = deepcopy(l1)
lc = deepcopy(l1)

def update(l, y, x):
    neighbors = [(y-1, x-1), (y-1, x), (y-1, x+1), (y, x-1), (y, x+1), (y+1, x-1), (y+1, x), (y+1, x+1)]
    neighbors_copy = set(copy(neighbors))
    count = 0
    for n in neighbors:
        if -1 in n or len(l) in n:
            neighbors_copy.remove(n)
    for n in neighbors_copy:
        if l[n[0]][n[1]] == "#": count += 1
    if l[y][x] == "#":
        if count in [2, 3]: return "#"
        else: return "."
    else:
        if count == 3: return "#"
        else: return "."

def count_on(l):
    count = 0
    for y in range(len(l)):
        for x in range(len(l[0])):
            if l[y][x] == "#": count += 1
    return count

def update_corners(l):
    for (y, x) in [(0, 0), (0, len(l)-1), (len(l)-1, 0), (len(l)-1, len(l)-1)]:
        l[y][x] = "#"

for _ in range(100):
    for y in range(len(l1)):
        for x in range(len(l1[0])):
            lc[y][x] = update(l1, y, x)
    l1 = deepcopy(lc)

part1 = count_on(l1)

update_corners(l2)
for _ in range(100):
    for y in range(len(l1)):
        for x in range(len(l1[0])):
            lc[y][x] = update(l2, y, x)
    l2 = deepcopy(lc)
    update_corners(l2)

part2 = count_on(l2)
print(part1)
print(part2)
