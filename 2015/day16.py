lines = open("input.txt").read().strip().splitlines()

d = {"children": 0, "cats": 1, "samoyeds": 2, "pomeranians": 3, "akitas": 4, 
     "vizslas": 5, "goldfish": 6, "trees": 7, "cars": 8, "perfumes": 9}
out = [3, 7, 2, 3, 0, 0, 5, 3, 2, 1]

m = None
part1 = None
for line in lines:
    index = int(line.split(": ")[0].split()[1])
    line = line[line.index(":")+2:].split(", ")
    sd = 0
    for item in line:
        thing, value = item.split(": ") 
        sd += abs(out[d[thing]] - int(value))
    if m is None or sd < m:
        m = sd
        part1 = index

print(part1)
