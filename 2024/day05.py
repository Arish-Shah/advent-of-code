rules, update = open("input.txt").read().strip().split("\n\n")

rules = [*map(lambda x: [*map(int, x.split("|"))], rules.splitlines())]
update = [*map(lambda x: [*map(int, x.split(","))], update.splitlines())]

part1, part2 = 0, 0

correct: list[list[int]] = []
incorrect: list[list[int]] = []

for pages in update:
    flag = True
    for (before, after) in rules:
        if before in pages and after in pages:
            if pages.index(before) > pages.index(after):
                flag = False
                break
    correct.append(pages) if flag else incorrect.append(pages)

for pages in correct:
    part1 += pages[int(len(pages)/2)]

print("part 1:", part1)

# bubble sort
for pages in incorrect:
    for i in range(len(pages)):
        for j in range(i+1, len(pages)):
            for (before, after) in rules:
                if before in pages and after in pages:
                    bi = pages.index(before)
                    ai = pages.index(after)
                    if bi > ai:
                        temp = pages[bi]
                        pages[bi] = pages[ai]
                        pages[ai] = temp

for pages in incorrect:
    part2 += pages[int(len(pages)/2)]

print("part 2:", part2)
