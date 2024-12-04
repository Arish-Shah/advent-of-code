from re import findall

ls = open("input.txt").read().splitlines()
part1, part2 = 0, 0

def calc(l: list[str]):
    ltr, rtl = 0, 0
    for line in l:
        ltr += len(findall("XMAS", line))
        rtl += len(findall("SAMX", line))
    return ltr + rtl

def transpose(m: list[str]):
    t = ["" for _ in range(len(m[0]))]
    for i in range(len(t)):
        for j in range(len(m)):
            t[i] += m[j][i]
    return t

part1 = calc(ls) + calc(transpose(ls))

for i in range(len(ls)):
    for j in range(len(ls[0])):
        if ls[i][j] == "X":
            if i-3 >= 0 and j-3 >= 0:
                if ls[i-1][j-1] == "M" and ls[i-2][j-2] == "A" and ls[i-3][j-3] == "S": part1 += 1
            if i-3 >= 0 and j+3 < len(ls[0]):
                if ls[i-1][j+1] == "M" and ls[i-2][j+2] == "A" and ls[i-3][j+3] == "S": part1 += 1
            if i+3 < len(ls) and j-3 >= 0:
                if ls[i+1][j-1] == "M" and ls[i+2][j-2] == "A" and ls[i+3][j-3] == "S": part1 += 1
            if i+3 < len(ls) and j+3 < len(ls[0]):
                if ls[i+1][j+1] == "M" and ls[i+2][j+2] == "A" and ls[i+3][j+3] == "S": part1 += 1

print("part 1: ", part1)

for i in range(len(ls)):
    for j in range(len(ls[0])):
        if ls[i][j] == "A":
            if i-1 >= 0 and j-1 >= 0 and i+1 < len(ls) and j+1 < len(ls[0]):
                if ls[i-1][j-1] == "M" and ls[i+1][j+1] == "S":
                    if ls[i-1][j+1] == "M" and ls[i+1][j-1] == "S":
                        part2 += 1
                    elif ls[i-1][j+1] == "S" and ls[i+1][j-1] == "M":
                        part2 += 1
                elif ls[i-1][j-1] == "S" and ls[i+1][j+1] == "M":
                    if ls[i-1][j+1] == "M" and ls[i+1][j-1] == "S":
                        part2 += 1
                    elif ls[i-1][j+1] == "S" and ls[i+1][j-1] == "M":
                        part2 += 1

print("part 2: ", part2)
