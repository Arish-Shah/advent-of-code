from collections import Counter

lines = open("input.txt").read().splitlines()

left, right = [], []
part1, part2 = 0, 0

for line in lines:
    l, r = line.split()
    left.append(int(l))
    right.append(int(r))

left.sort()
right.sort()

for (l, r) in zip(left, right):
    part1 += abs(l - r)

print("part 1:", part1)

count = Counter(right)

for l in left:
    if l in count:
        part2 += (l * count[l])

print("part 2:", part2)
