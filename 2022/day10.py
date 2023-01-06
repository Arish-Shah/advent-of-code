lines = open("input.txt", "r").read().strip().splitlines()

X = 1
x = []
c = 0
part1 = 0
cycles = [20, 60, 100, 140, 180, 220]

def check(c, X):
    x.append(X)
    if c in cycles:
        return X * c
    return 0

for line in lines:
    if line.strip() == "noop":
        c += 1
        part1 += check(c, X)
    else:
        n = int(line.split(" ")[1])
        for _ in range(2):
            c += 1
            part1 += check(c, X)
        X += n

print(part1)

# part 2
for i in range(len(x)):
    crt_i = i % 40
    sprite = [x[i] - 1, x[i], x[i] + 1]

    if crt_i in sprite:
        print("#", end="")
    else:
        print(".", end="")
    if crt_i == 39:
        print()
