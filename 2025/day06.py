from sys import argv
from math import prod

T = lambda m: [[m[i][j] for i in range(len(m))] for j in range(len(m[0]))]
R = lambda o, m: sum(m) if o == "+" else prod(m)

text = open(argv[1]).read().splitlines()
ops = text.pop(-1).split()
rtl = [[]]

sptext = T(list(map(lambda x: list(map(int, x.split())), text)))
part1 = sum([R(ops[i], sptext[i]) for i in range((len(ops)))])
print("part1:", part1)

for j in range(len(text[0])-1, -1, -1):
    temp = ""
    for i in range(len(text)):
        temp += text[i][j]
    temp = temp.strip()
    if temp != "": rtl[-1].append(int(temp))
    else: rtl.append([])

rtl = list(reversed(rtl))
part2 = sum([R(ops[i], rtl[i]) for i in range(len(ops))])
print("part2:", part2)
