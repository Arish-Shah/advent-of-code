from itertools import combinations

containers = list(map(int, open("input.txt").readlines()))
repeats = []
part1 = 0
ways = {}

for i in range(len(containers)):
    if containers[i] in containers[i+1:]:
        repeats.append(containers[i])

for i in range(len(containers)):
    ways[i] = 0
    for c in combinations(containers, i):
        if sum(c) == 150:
            part1 += 1
            ways[i] += 1
    if ways[i] == 0:
        del ways[i]

part2 = ways[min(ways)]

print(part1)
print(part2)
