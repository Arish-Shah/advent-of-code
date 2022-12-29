line = open("input.txt").read().strip()

s = { "x": 0, "y": 0, "v": set() }
r = { "x": 0, "y": 0, "v": set() }

s["v"].add((0, 0))
r["v"].add((0, 0))

for i, dir in enumerate(line):
    if i % 2 == 0:
        c = s
    else:
        c = r

    if dir == ">":
        c["x"] += 1
    elif dir == "<":
        c["x"] -= 1
    elif dir == "v":
        c["y"] += 1
    elif dir == "^":
        c["y"] -= 1
    c["v"].add((c["x"], c["y"]))

print(len(set(list(s["v"]) + list(r["v"]))))
