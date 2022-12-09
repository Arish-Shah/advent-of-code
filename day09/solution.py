lines = open("input", "r").readlines()

def get_next_hop(hy, hx, ty, tx):
    dy = ty - hy
    dx = tx - hx

    if dy == -2:
        ty = hy - 1
        if abs(dx) == 1:
            tx = hx
    if dy == 2:
        ty = hy + 1
        if abs(dx) == 1:
            tx = hx
    if dx == -2:
        tx = hx - 1
        if abs(dy) == 1:
            ty = hy
    if dx == 2:
        tx = hx + 1
        if abs(dy) == 1:
            ty = hy

    return (ty, tx)

hy = hx = ty = tx = 0
ss: list[list[tuple[int, int]]] = [[(0, 0)] for _ in range(10)]

for line in lines:
    d, n = line.split()
    n = int(n)
    for i in range(n):
        if d == "U":
            hy += 1
        elif d == "D":
            hy -= 1
        elif d == "R":
            hx += 1
        elif d == "L":
            hx -= 1

        ss[0].append((hy, hx))

        for i in range(1, 10):
            head_y, head_x = ss[i - 1][-1]
            tail_y, tail_x = ss[i][-1]
            ss[i].append(get_next_hop(head_y, head_x, tail_y, tail_x))

print(len(set(ss[1]))) # part1
print(len(set(ss[9]))) # part2
