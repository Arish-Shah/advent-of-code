import copy

inputs = open("input.txt", "r").read().strip().split("\n\n")

monkeys = {}
part1 = []
items = []
divs = []

def operation(old, sign, op) -> int:
    if op == "old":
        op = old
    op = int(op)
    if sign == "+":
        return old + op
    else:
        return old * op

def return_operation_lambda(sign, op):
    return lambda old: operation(old, sign, op)

def get_answer(l):
    v = sorted(list(l), reverse=True)
    return v[0] * v[1]

def return_test_lambda(arr):
    return lambda n: arr[1] if bool(n % arr[0] == 0) else arr[2]

for i, input in enumerate(inputs):
    monkeys.setdefault(i, {})
    part1.append(0)
    lines = [line.strip() for line in input.split("\n")][1:]
    test = []
    for line in lines:
        attr, param = line.split(": ")
        if attr.startswith("Starting items"):
            items.append([int(n) for n in param.split(", ")])
        elif attr.startswith("Operation"):
            sign, op = param.replace("new = old ", "").split(" ")
            monkeys[i]["o"] = return_operation_lambda(sign, op)
        elif attr.startswith("Test"):
            div = int(param.replace("divisible by ", ""))
            test.append(div)
            divs.append(div)
        elif attr.startswith("If true"):
            num = int(param.replace("throw to monkey ", ""))
            test.append(num)
        elif attr.startswith("If false"):
            num = int(param.replace("throw to monkey ", ""))
            test.append(num)
            monkeys[i]["t"] = return_test_lambda(test)

part2 = copy.copy(part1)
items2 = copy.deepcopy(items)
modulo = 1
for div in divs:
    modulo *= div

for round in range(20):
    for i in monkeys:
        part1[i] += len(items[i])
        while items[i]:
            worry_level = items[i].pop(0)
            new_worry_level = int(monkeys[i]["o"](worry_level) // 3)
            to = monkeys[i]["t"](new_worry_level)
            items[to].append(new_worry_level)

for round in range(10000):
    print(round, part2)
    for i in monkeys:
        part2[i] += len(items2[i])
        while items2[i]:
            worry_level = items2[i].pop(0)
            new_worry_level = monkeys[i]["o"](worry_level) % modulo
            to = monkeys[i]["t"](new_worry_level)
            items2[to].append(new_worry_level)

print(get_answer(part1))
print(get_answer(part2))
