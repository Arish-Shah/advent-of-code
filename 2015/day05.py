lines = open("input.txt").read().strip().splitlines()

part1 = part2 = 0

def is_nice1(line):
    vc = 0
    for c in line:
        if c in "aeiou":
            vc += 1
    if vc < 3:
        return False
    if "ab" in line or "cd" in line or "pq" in line or "xy" in line:
        return False
    for i in range(len(line) - 1):
        if line[i] == line[i + 1]:
            return True
    return False

def is_nice2(line):
    f = False
    for i in range(len(line) - 1):
        char = line[i:i+2]
        if char in line[i+2:]:
            f = True
    if not f:
        return False
    for i in range(len(line) - 2):
        left = line[i]
        right = line[i + 2]
        if left == right:
            return True
    return False

for line in lines:
    if is_nice1(line):
        part1 += 1
    if is_nice2(line):
        part2 += 1

print(part1)
print(part2)
