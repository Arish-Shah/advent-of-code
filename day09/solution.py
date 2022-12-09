lines = open("example", "r").readlines()

hx = hy = tx = ty = 0
ss: list[list[tuple[int, int]]] = [[(0, 0)] for _ in range(10)]
def get_next_hop(hy, hx, ty, tx):
    dy = hy - ty
    dx = hx - tx

    if dy == 2:
        return (hy - 1, hx)
    elif dy == -2:
        return (hy + 1, hx)
    elif dx == 2:
        return (hy, hx - 1)
    elif dx == -2:
        return (hy, hx + 1)
    return (ty, tx)

for line in lines:
    d, n = line.split()
    n = int(n)
    for _ in range(n):
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
            if i == 5:
                print(head_y, head_x, tail_y, tail_x)

print(len(set(ss[1])))
print(len(set(ss[9])))
