puzzle = 3113322113
sp = str(puzzle)
part1 = part2 = None

for i in range(50):
    temp_sp = ""
    count = 1
    curr = sp[0]

    for ch in sp[1:]:
        if ch == curr:
            count += 1
        else:
            temp_sp += (str(count) + curr)
            count = 1
            curr = ch
    
    temp_sp += (str(count) + curr)
    sp = temp_sp

    if i == 39:
        part1 = len(sp)
    if i == 49:
        part2 = len(sp)

print(part1)
print(part2)
