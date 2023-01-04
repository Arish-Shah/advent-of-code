from itertools import permutations

lines = open("input.txt").read().strip().splitlines()

people = set()
happy = {}
part1 = part2 = None

for line in lines:
    line = line.replace("lose ", "-").replace("gain ", "").replace(".", "").split()
    f, h, t = line[0], line[2], line[9]
    people.add(f)
    people.add(t)
    happy[f + t] = int(h)

arrs = permutations(people, len(people))

for arr in arrs:
    h = 0
    for i in range(len(arr)):
        left, right = i-1, i+1
        if left == -1: left = len(arr) - 1
        if right == len(arr): right = 0
        h = h + happy[arr[i] + arr[left]] + happy[arr[i] + arr[right]]
    part1 = h if part1 is None else max(part1, h)

print(part1)
