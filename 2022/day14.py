lines = open("input.txt", "r").read().strip().split("\n")

def cal_sand(rocks, max_y, block=False):
    r = set(rocks)
    sand = 0

    while True:
        fall = False
        sand_x, sand_y = (500, 0)
        
        while True:
            next_sand_x, next_sand_y = sand_x, sand_y + 1
            if (next_sand_x, next_sand_y) in r:
                next_sand_x, next_sand_y = sand_x - 1, sand_y + 1
                if (next_sand_x, next_sand_y) in r:
                    next_sand_x, next_sand_y = sand_x + 1, sand_y + 1
                    if (next_sand_x, next_sand_y) in r:
                        r.add((sand_x, sand_y))
                        if block and (500, 0) in r:
                            sand += 1
                            fall = True
                        break
                    else:
                        sand_x, sand_y = next_sand_x, next_sand_y
                else:
                    sand_x, sand_y = next_sand_x, next_sand_y
            else:
                sand_x, sand_y = next_sand_x, next_sand_y

            if sand_y > max_y:
                fall = True
                break
        if fall:
            break
        else:
            sand += 1
    return sand

rocks = set()

for line in lines:
    l = list(map(lambda x: tuple(int(t) for t in x.split(",")), 
        [s for s in line.split(" -> ")]))
    for i in range(len(l) - 1):
        curr_x, curr_y = l[i]
        next_x, next_y = l[i + 1]

        rocks.add(l[i])
        rocks.add(l[i + 1])

        if curr_x != next_x:
            diff = next_x - curr_x
            step = 1 if next_x > curr_x else -1
            for i in range(curr_x, next_x, step):
                rocks.add((i, curr_y))
        else:
            diff = next_y - curr_y
            step = 1 if next_y > curr_y else -1
            for i in range(curr_y, next_y, step):
                rocks.add((curr_x, i))

max_y = max([y for _, y in rocks])
part1 = cal_sand(rocks, max_y)

max_x = max([x for x, _ in rocks])
min_x = min([x for x, _ in rocks])
max_y = max_y + 2

# probably bad way to do this (1000 instead of infinity)
for i in range(min_x - 1000, max_x + 1000):
    rocks.add((i, max_y))

part2 = cal_sand(rocks, max_y, block=True)

print(part1)
print(part2)
