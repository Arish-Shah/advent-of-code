from hashlib import md5

puzzle = "yzbqklnj"
part1 = part2 = 0
part1_found = part2_found = False

for i in range(10000000):
    b = (puzzle + str(i)).encode()
    h = md5(b).hexdigest()

    if not part1_found and h.startswith("00000"):
        part1 = i
        part1_found = True

    if not part2_found and h.startswith("000000"):
        part2 = i
        part2_found = True

print(part1)
print(part2)
