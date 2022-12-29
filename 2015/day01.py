line = open("input.txt").read().strip()

part1 = 0
part2 = 0
basement_reached = False

for i, item in enumerate(line):
    if item == "(":
        part1 += 1
    elif item == ")":
        part1 -= 1

    if part1 == -1 and not basement_reached:
        part2 = i + 1
        basement_reached = True

print(part1)
print(part2)
