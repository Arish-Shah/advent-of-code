from sys import argv

lines = open(argv[1]).read().splitlines()
part1, part2 = 0, 0

def find(bank, size):
    pass

for line in lines:
    bank = list(line)
    largest = 0
    for i in range(len(bank)):
        for j in range(i+1, len(bank)):
            joltage = int(bank[i]+bank[j])
            if joltage > largest:
                largest = joltage
    part1 += largest

print("part1:", part1)
