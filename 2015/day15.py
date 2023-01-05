from itertools import permutations

lines = open("input.txt").read().strip().splitlines()

ings: list[tuple[int, int, int, int, int]] = []
ratios = []

for line in lines:
    line = line.split(": ")
    ings.append(tuple(map(int, [n.split(" ")[1] for n in line[1].split(", ")])))

for p in permutations(range(1, 100), len(ings)):
    if sum(p) == 100:
        ratios.append(p)

part1 = part2 = 0

for ratio in ratios:
    c = d = f = t = cal = 0
    for i, r in enumerate(ratio):
        c += r * ings[i][0]
        d += r * ings[i][1]
        f += r * ings[i][2]
        t += r * ings[i][3]
        cal += r * ings[i][4]
    c = max(c, 0)
    d = max(d, 0)
    f = max(f, 0)
    t = max(t, 0)
    cal = max(cal, 0)
    part1 = max(part1, c * d * f * t)
    if cal == 500:
        part2 = max(part2, c * d * f * t)

print(part1)
print(part2)
