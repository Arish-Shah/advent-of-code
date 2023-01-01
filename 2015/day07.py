lines = open("input.txt").read().strip().splitlines()

for line in lines:
    lhs, rhs = line.split(" -> ")
    print(lhs, rhs)
