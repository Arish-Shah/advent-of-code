from sys import argv
from copy import copy

levels = open(argv[1]).read().splitlines()
beams = set([(0, levels[0].index("S"))])
part1, part2 = 0, 0

for level in levels[1:]:
    news = set()
    for beam in beams:
        new = (beam[0]+1, beam[1])
        if level[new[1]] == "^":
            l, r = (new[0], new[1]-1), (new[0], new[1]+1)
            news.add(l)
            news.add(r)
            part1 += 1
        else:
            news.add(new)
    beams = news

print("part1:", part1)

// TODO:
paths = {(0, levels[0].index("S")): 0}

while len(paths) > 0:
    head, count = paths.popitem()
    new = (head[0]+1, head[1])
    if new[0] >= len(levels):
        print("collision")
        continue

# while len(paths) > 0:
    # head = paths.pop(0)
    # new = (head[0]+1, head[1])
    # if new[0] >= len(levels):
    #     part2 += 1
    #     continue
    # if levels[new[0]][new[1]] == "^":
    #     l, r = (new[0], new[1]-1), (new[0], new[1]+1)
    #     paths.extend([l, r])
    # else:
    #     paths.append(new)

print("part2:", part2)
