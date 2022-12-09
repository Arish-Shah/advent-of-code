lines = open("example", "r").readlines()

def get_next_hop(hy, hx, ty, tx):
    dy = hy - ty
    dx = hx - tx

    if dy == 2:
        ty += 1
        if abs(dx) == 1:
            tx = hx
    elif dy == -2:
        ty -= 1
        if abs(dx) == 1:
            tx = hx
    elif dx == 2:
        tx += 1
        if abs(dy) == 1:
            ty = hy
    elif dx == -2:
        tx -= 1
        if abs(dy) == 1:
            ty = hy
    return ty, tx

m = ["."]
hx = hy = tx = ty = 0
part1 = 0

for line in lines:
    d, n = line.split()
    n = int(n)
    for i in range(n):
        if d == "U":
            hy -= 1
        elif d == "D":
            hy += 1
        elif d == "L":
            hx -= 1
        elif d == "R":
            hx += 1

        if hy == -1:
            m.insert(0, "." * len(m[0]))
            hy = 0
            ty += 1
        if hy == len(m):
            m.append("." * len(m[0]))
        if hx == -1:
            for x in range(len(m)):
                m[x] = "." + m[x]
            hx = 0
            tx += 1
        if hx == len(m[0]):
            for x in range(len(m)):
                m[x] = m[x] + "."

        ty, tx = get_next_hop(hy, hx, ty, tx)
        m[ty] = m[ty][:tx] + "#" + m[ty][tx + 1:]

for row in m:
    for col in row:
        if col == "#":
            part1 += 1

print(part1)
