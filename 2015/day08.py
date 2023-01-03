lines = open("input.txt").read().strip().splitlines()

s = 0
m = 0
e = 0

for line in lines:
    s += len(line)
    m += len(eval(line))
    line = "\"" + line.replace("\\", "\\\\").replace("\"", "\\\"") + "\""
    e += len(line)

part1 = s - m
part2 = e - s
print(part1)
print(part2)
