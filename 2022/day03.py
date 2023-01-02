lines = open("./input.txt").read().strip().split("\n")

def letter_sum(letters):
    s = 0
    for letter in letters:
        sub = 38 if letter.isupper() else 96
        s += (ord(letter) - sub)
    return s

common1: list[str] = []
common2: list[str] = []

for line in lines:
    first = line[0:int(len(line) / 2)]
    second = line[int(len(line) / 2):len(line)]
    s = set()
    for letter in first:
        if letter in second:
            s.add(letter)
    common1.extend(s)
part1 = letter_sum(common1)
print(part1)

for i in range(0, len(lines), 3):
    grp = lines[i:i + 3]
    s = set()
    for letter in grp[0]:
        if letter in grp[1] and letter in grp[2]:
            s.add(letter)
    common2.extend(s)

part2 = letter_sum(common2)
print(part2)
