file = open("./input", "r").read().strip().split("\n")

def find_marker(line, n):
    for i in range(0, len(line), 1):
        if len(set(line[i:i + n])) == n:
            return i + n

for line in file:
    print(find_marker(line, 4))
    print(find_marker(line, 14))
