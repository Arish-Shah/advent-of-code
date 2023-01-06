lines = open("input.txt").read().strip().split("\n\n")

cal = []
for elf in lines:
    cal.append(sum([int(n) for n in elf.split("\n")]))
cal.sort(reverse=True)

print(cal[0])
print(sum(cal[0:3]))
