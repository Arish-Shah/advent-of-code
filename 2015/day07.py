lines = open("input.txt").read().strip().splitlines()

signals = {}
seen = []
ops = {"AND": "&", "OR": "|", "LSHIFT": "<<", "RSHIFT": ">>", "NOT": "~"}

def done():
    for wire in signals:
        if signals[wire] == None:
            return False
    return True

def reset():
    for line in lines:
        lhs = line.split(" -> ")[1]
        signals[lhs] = None
    seen.clear()

def solve():
    while True:
        if done():
            break

        for i, line in enumerate(lines):
            if i not in seen:
                lhs, wire = line.split(" -> ")
                lhs = lhs.split()
                if len(lhs) == 3:
                    op = ops[lhs[1]]
                    x = signals[lhs[0]] if not lhs[0].isdigit() else int(lhs[0])
                    y = signals[lhs[2]] if not lhs[2].isdigit() else int(lhs[2])
                    if x != None and y != None:
                        signals[wire] = eval(str(x) + op + str(y))
                        continue
                if len(lhs) == 2:
                    op = ops[lhs[0]]
                    x = signals[lhs[1]] if not lhs[1].isdigit() else int(lhs[1])
                    if x != None:
                        signals[wire] = eval(op + str(x))
                        continue
                if len(lhs) == 1:
                    x = signals[lhs[0]] if not lhs[0].isdigit() else int(lhs[0])
                    if x != None:
                        signals[wire] = x
                        continue


reset()
solve()
part1 = signals["a"]
print(part1)

reset()
signals["b"] = part1
seen = [89] # remove the line that sets b
solve()
print(signals["a"])
