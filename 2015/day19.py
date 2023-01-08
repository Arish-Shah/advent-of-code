from random import shuffle
from re import finditer

s, m = open("input.txt").read().strip().split("\n\n")

reps: list[tuple[str, str]] = []
d = set()
mc = str(m)
part1 = part2 = 0

for rep in s.splitlines():
    rep = rep.split(" => ")
    reps.append((rep[0], rep[1]))

for (key, value) in reps:
    if key in m:
        for i in finditer(key, m):
            d.add(m[:i.start()] + value + m[i.end():])
part1 = len(d)

shuffle(reps)
while mc != "e":
    tmp = mc
    for key, value in reps:
        if value not in mc:
            continue
        mc = mc.replace(value, key, 1)
        part2 += 1

print(part1)
print(part2)
