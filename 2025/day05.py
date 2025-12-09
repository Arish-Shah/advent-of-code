from sys import argv

text = open(argv[1]).read().strip()
fresh, available = map(lambda x: x.split(), text.split("\n\n"))

fresh = list(map(lambda x: list(map(int, x.split("-"))), fresh))
available = list(map(int, available))
part1 = 0

for a in available:
    for l, h in fresh:
        if a >= l and a <= h:
            part1 += 1
            break

sorted_fresh = sorted(fresh)
final, current = [sorted_fresh.pop(0)], 0

while len(sorted_fresh) > 0:
    for item in sorted_fresh:
        if final[current][1] >= item[0]:
            popped = sorted_fresh.pop(0)
            final[current][1] = max(final[current][1], popped[1])
            break
    else:
        final.append(sorted_fresh.pop(0))
        current += 1

print("part1:", part1)

part2 = sum(map(lambda x: x[1]-x[0], final)) + len(final)
print("part2:", part2)
