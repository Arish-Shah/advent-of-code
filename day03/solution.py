lines = open("./input").read().strip().split("\n")

part1 = 0
part2 = 0

for line in lines:
    first = [line[n] for n in range(0, int(len(line) / 2))]
    second = [line[n] for n in range(int(len(line) / 2), len(line))]
    for inter in list(set(first).intersection(second)):
        if inter.isupper():
            part1 += (ord(inter) - 38)
        else:
            part1 += (ord(inter) - 96)
print(part1)

for i in range(0, len(lines), 3):
    group = lines[i:i + 3]
    for inter in list(set(group[0]).intersection(group[1]).intersection(group[2])):
        if inter.isupper():
            part2 += (ord(inter) - 38)
        else:
            part2 += (ord(inter) - 96)

print(part2)

