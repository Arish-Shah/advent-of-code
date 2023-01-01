lines = open("input.txt").read().strip().splitlines()

lights1 = [[0 for _ in range(1000)] for _ in range(1000)]
lights2 = [[0 for _ in range(1000)] for _ in range(1000)]
part1 = part2 = 0

for line in lines:
    line = line.split(" ")
    if "on" in line or "off" in line:
        state = line[1]
        s = line[2]
        e = line[4]
    else:
        state = line[0]
        s = line[1]
        e = line[3]

    sx, sy = [int(n) for n in s.split(",")]
    ex, ey = [int(n) for n in e.split(",")]

    for i in range(sx, ex + 1):
        for j in range(sy, ey + 1):
            if state == "on":
                lights1[i][j] = 1
                lights2[i][j] += 1
            elif state == "off":
                lights1[i][j] = 0
                temp = lights2[i][j] - 1
                lights2[i][j] = max(temp, 0)
            else:
                lights1[i][j] = 1 if lights1[i][j] == 0 else 0
                lights2[i][j] += 2

for i in range(1000):
    for j in range(1000):
        part1 += lights1[i][j]
        part2 += lights2[i][j]

print(part1)
print(part2)
