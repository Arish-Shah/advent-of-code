from functools import cmp_to_key

pairs = open("input", "r").read().strip().split("\n\n")

def cmp(l, r):
    if type(l) is int and type(r) is int:
        if l < r:
            return 1
        elif l > r:
            return -1
        else:
            return 0
    elif type(l) is int:
        l = [l]
    elif type(r) is int:
        r = [r]

    for x, y in zip(l, r):
        ret = cmp(x, y)
        if ret != 0:
            return ret
    if len(l) < len(r):
        return 1
    elif len(l) > len(r):
        return -1
    else:
        return 0

s = []
lists = [[[2]], [[6]]]
for i, p in enumerate(pairs):
    l, r = [eval(x) for x in p.split("\n")]
    lists.extend([l, r])
    res = cmp(l, r)
    if res == 1:
        s.append(i + 1)
part1 = sum(s)

lists.sort(key=cmp_to_key(lambda l, r: cmp(l, r)), reverse=True)

indices = [i + 1 for i in range(len(lists)) if lists[i] == [[2]] or lists[i] == [[6]]]
part2 = indices[0] * indices[1]
print(part1)
print(part2)
