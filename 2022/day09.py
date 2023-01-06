lines = open("input.txt").read().strip().splitlines()

def get_add(d):
    if d < 0:
        return -1
    return 1

def get_next_hop(hy, hx, ty, tx):
    dy = ty - hy
    dx = tx - hx

    if abs(dy) == 2:
        ty = hy + get_add(dy)
        if abs(dx) == 1:
            return ty, hx

    if abs(dx) == 2:
        tx = hx + get_add(dx)
        if abs(dy) == 1:
            return hy, tx

    return ty, tx

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
