lines = open("input.txt").read().strip().splitlines()

out = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0, 
     "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1}

m1 = m2 = None
part1 = part2 = None
for line in lines:
    index = int(line.split(": ")[0].split()[1])
    line = line[line.index(":")+2:].split(", ")
    sd1 = sd2 = 0
    flag = True
    for item in line:
        thing, value = item.split(": ") 
        diff = out[thing] - int(value)
        sd1 += abs(diff)

        if thing in ["cats", "trees"]:
            if diff >= 0:
                flag = False
        elif thing in ["pomeranians", "goldfish"]:
            if diff <= 0:
                flag = False
        else:
            sd2 += abs(diff)

    if m1 is None or sd1 < m1:
        m1 = sd1
        part1 = index

    if flag and (m2 is None or sd2 < m2):
        m2 = sd2
        part2 = index

print(part1)
print(part2)
