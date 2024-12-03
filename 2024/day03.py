from re import findall

text = open("input.txt").read().strip()

def enabled(mem: str):
    sum = 0
    for item in findall("mul\\(\\d+,\\d+\\)", mem):
        x, y = map(int, item.replace("mul(", "").replace(")", "").split(","))
        sum += x*y
    return sum

part1 = enabled(text)
print("part 1:", part1)

part2 = 0
for dont in text.split("don't"):
    if text.startswith(dont):
        part2 += enabled(dont)
    else:
        for do in dont.split("do")[1:]:
            part2 += enabled(do)

print("part 2:", part2)
