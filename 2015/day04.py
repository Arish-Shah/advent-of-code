from hashlib import md5

puzzle = "yzbqklnj"
part1 = part2 = 0

for i in range(10000000):
    b = (puzzle + str(i)).encode()
    h = md5(b).hexdigest()
    if h.startswith("000000"):
        n = i
        break

print(part1)
print(part2)
