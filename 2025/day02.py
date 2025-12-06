from sys import argv

ranges = open(argv[1]).read().strip().split(",")
part1, part2 = 0, 0

for r in ranges:
    l, r = [*map(int, r.split("-"))]
    for ID in range(l, r+1):
        strID = str(ID)
        lenStrID = len(strID)
        if lenStrID % 2 == 0:
            if strID[:int(lenStrID/2)] == strID[int(lenStrID/2):]:
                part1 += ID
        for i in range(1, int(lenStrID/2)+1):
            pattern = strID[:i]
            count = strID.count(pattern)
            if lenStrID == len(pattern)*count:
                part2 += ID
                break

print("part1:", part1)
print("part2:", part2)
