import re

f = open(0).read().strip().split("\n")

def is_part(row, col, length):
    a = [(row, col-1), (row, col+length)]
    for i in range(col-1, col+length+1):
        a.extend([(row-1, i), (row+1, i)])
    return len(list(filter(lambda z: z != ".", map(lambda y: f[y[0]][y[1]],
            filter(lambda x: -1 not in x and x[0] < len(f) and x[1] < len(f[0]), a))))) > 0

part1 = 0
for r in range(len(f)):
    n, s = "", None
    for c in range(len(f[0])):
        if f[r][c].isdigit():
            n += f[r][c]
            if s == None: s = c
        elif n != "":
            if is_part(r, s, len(n)): part1 += int(n)
            n, s = "", None

print(part1)
