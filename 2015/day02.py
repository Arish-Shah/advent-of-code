lines = open("input.txt").read().strip().splitlines()

part1 = 0
part2 = 0

for line in lines:
    l, w, h = map(int, line.split("x"))
    part1 += 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)
    part2 += 2*min(l+w, w+h, h+l) + l*w*h

print(part1)
print(part2)
