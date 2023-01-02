lines = open("input.txt", "r").readlines()

grid = []
part1 = 0
part2 = 0

for line in lines:
    line = line.replace("\n", "")
    grid.append([])
    for n in line:
        grid[-1].append(int(n))

part1 += ((len(grid) * 2) + (len(grid[0]) * 2) - 4)

for i in range(1, len(grid) - 1):
    for j in range(1, len(grid[i]) - 1):
        current = grid[i][j]
        t = b = l = r = False
        st = sb = sl = sr = 0

        for k in range(i - 1, -1, -1):
            st += 1
            if grid[k][j] >= current:
                t = True
                break
        for k in range(i + 1, len(grid)):
            sb += 1
            if grid[k][j] >= current:
                b = True
                break
        for k in range(j - 1, -1, -1):
            sl += 1
            if grid[i][k] >= current:
                l = True
                break
        for k in range(j + 1, len(grid[i])):
            sr += 1
            if grid[i][k] >= current:
                r = True
                break
        
        part2 = max(part2, st * sb * sl * sr)

        if not t or not b or not l or not r:
            part1 += 1

print(part1)
print(part2)
