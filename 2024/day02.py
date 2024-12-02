lines = open("input.txt").read().splitlines()

def is_safe(l: list[int]):
    s = "i" if l[0] < l[1] else "d"
    for i in range(0, len(l)-1):
        x, y = l[i], l[i+1]
        diff = abs(x-y)
        if diff not in [1, 2, 3]: return 0
        if s == "i" and x > y: return 0
        if s == "d" and y > x: return 0
    return 1

data = list(map(lambda x: list(map(int, x.split())), lines))
part1 = sum(map(is_safe, data))
print("part 1:", part1)

removed_data = []

for l in data:
    removed_data.append([])
    for i in range(len(l)):
        removed_data[-1].append(l[:i] + l[i+1:])

tol = []
for l in removed_data:
    tol.append(1 if 1 in list(map(is_safe, l)) else 0)

part2 = sum(tol)
print("part 2:", part2)
