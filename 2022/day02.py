w = ["AY", "BZ", "CX"]
d = ["AX", "BY", "CZ"]
l = ["AZ", "BX", "CY"]

def get_result(e, p):
    s = e + p

    if s in w:
        return 6
    elif s in d:
        return 3
    else:
        return 0

def get_sel(e, result):
    if result == 6:
        arr = w
    elif result == 3:
        arr = d
    else:
        arr = l

    for item in arr:
        if item.startswith(e):
            return item[1]

def get_value(sel):
    if sel in ["A", "X"]:
        return 1
    elif sel in ["B", "Y"]:
        return 2
    else:
        return 3

def get_result_value(result):
    if result == "X":
        return 0
    elif result == "Y":
        return 3
    else:
        return 6

def main():
    file = open("./input.txt")

    part1 = 0
    part2 = 0

    for line in file.read().strip().split("\n"):
        e, p = line.split(" ")
        part1 += get_value(p) + get_result(e, p)
        sel = get_sel(e, get_result_value(p))
        part2 += get_value(sel) + get_result(e, sel)

    print(part1)
    print(part2)

    file.close()

if __name__ == "__main__":
    main()
