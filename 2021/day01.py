lines = list(map(int, open("input.txt").readlines()))

part1 = part2 = 0 

for i in range(len(lines)-1):
    if lines[i+1] > lines[i]:
        part1 += 1

prev_w = sum([lines[0], lines[1], lines[2]])
for i in range(len(lines)-2):
    w = sum([lines[i], lines[i+1], lines[i+2]])
    if w > prev_w:
        part2 += 1
    prev_w = w

print(part1)
print(part2)
