lines = open("input.txt").read().strip().splitlines()

deers: dict[str, tuple[int, int, int]] = {}
distances: dict[str, int] = {}
points: dict[str, int] = {}

for line in lines:
    line = line.split()
    # name = speed, fly, rest
    deers[line[0]] = (int(line[3]), int(line[6]), int(line[13]))
    distances[line[0]] = 0
    points[line[0]] = 0

for i in range(2503):
    for deer in deers:
        state = i % (deers[deer][1] + deers[deer][2])
        if state < deers[deer][1]:
            distances[deer] += deers[deer][0]
    max_dist = max(distances.values())
    for deer in distances:
        if distances[deer] == max_dist:
            points[deer] += 1


part1 = max(distances.values())
part2 = max(points.values())
print(part1)
print(part2)
