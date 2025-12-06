from sys import argv

lines = open(argv[1]).read().splitlines()

numbers = [x for x in range(0, 100)]
part1, part2 = 0, 0
current = 50

for line in lines:
    direction, amount = line[:1], int(line[1:])
    for _ in range(amount):
        if direction == "L": current -= 1
        if direction == "R": current += 1

        if current < 0: current += 100
        if current > 99: current -= 100

        if current == 0:
            part2 += 1
    if current == 0:
        part1 += 1

print("part1:", part1)
print("part2:", part2)
