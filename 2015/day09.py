from itertools import permutations

lines = open("input.txt").read().strip().splitlines()

loc = set()
dist = {}

for line in lines:
    line = line.split()
    f, t, d = line[0], line[2], line[4]
    loc.add(f)
    loc.add(t)
    dist[f + t] = int(d)
    dist[t + f] = int(d)

per = permutations(loc, len(loc))
part1 = part2 = None

for p in per:
    d = 0
    for i in range(len(loc) - 1):
        d += dist[p[i] + p[i+1]]
    part1 = d if part1 is None else min(part1, d)
    part2 = d if part2 is None else max(part2, d)

print(part1)
print(part2)
