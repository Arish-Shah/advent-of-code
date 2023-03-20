lines = open("input.txt").read().splitlines()

x1, y1 = 0, 0
x2, y2 = 0, 0
aim = 0

for line in lines:
    d, v = line.split(" ")
    v = int(v)
    if d == "forward":
        x1 += v
        x2 += v
        y2 += (aim*v)
    elif d == "down":
        y1 += v
        aim += v
    else:
        y1 -= v
        aim -= v

part1 = x1*y1
part2 = x2*y2

print(part1)
print(part2)
