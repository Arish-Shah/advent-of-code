f = open(0).read().strip().split("\n")

def mul(d: dict[str, int]):
    return d["red"]*d["green"]*d["blue"]

counts = {"red": 12, "green": 13, "blue": 14}

part1, part2 = 0, 0
for game in f:
    ID, subsets = game.split(": ")
    flag, mins = True, {"red": 0, "green": 0, "blue": 0}
    for subset in subsets.split("; "):
        for bag in subset.split(", "):
            count, color = bag.split(" ")
            if int(count) > counts[color]:
                flag = False
            if mins[color] < int(count):
                mins[color] = int(count)
    if flag: part1 += int(ID.split(" ")[1])
    part2 += mul(mins)
print(part1, part2)
