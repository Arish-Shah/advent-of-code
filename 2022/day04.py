lines = open("./input.txt", "r").read().strip().split("\n")

part1 = 0
part2 = 0

for line in lines:
    elf1, elf2 = line.split(",")
    elf1_start, elf1_end = [int(n) for n in elf1.split("-")]
    elf2_start, elf2_end = [int(n) for n in elf2.split("-")]
    if (elf1_start >= elf2_start and elf1_end <= elf2_end) or \
        (elf2_start >= elf1_start and elf2_end <= elf1_end):
            part1 += 1

    if (elf2_start <= elf1_end and elf2_start >= elf1_start) or \
            (elf1_start <= elf2_end and elf1_start >= elf2_start):
                part2 += 1

print(part1)
print(part2)
