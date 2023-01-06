import copy

lines = open("input.txt").read().strip().split("\n\n")

d = {}
part1 = ""
part2 = ""

crates = lines[0].split("\n")
crates.reverse()

for stack in crates[0].split("  "):
    d.setdefault(int(stack.strip()), [])

for stack in crates[1:]:
    i = 0
    while True:
        try:
            i = stack.index("[", i) + 1
            d[int(i / 4) + 1].append(stack[i])
        except:
            break

d2 = copy.deepcopy(d)

for op in lines[1].rstrip().split("\n"):
    n, f, t = [int(x) for i, x in enumerate(op.split(" ")) if i % 2 == 1]
    for i in range(n):
        r = d[f].pop()
        d[t].append(r)

    r = d2[f][len(d2[f]) - n:]
    d2[f] = d2[f][0:len(d2[f]) - n]
    d2[t].extend(r)

for i in d:
    part1 += d[i][len(d[i]) - 1]
    part2 += d2[i][len(d2[i]) - 1]

print(part1)
print(part2)
