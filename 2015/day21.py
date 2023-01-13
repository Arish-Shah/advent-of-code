from itertools import product

boss = [int(n.split(": ")[1]) for n in open("input.txt").read().splitlines()]

w = {(4, 0): 8, (5, 0): 10, (6, 0): 25, (7, 0): 40, (8, 0): 74}
a = {(0, 1): 13, (0, 2): 31, (0, 3): 53, (0, 4): 75, (0, 5): 102}
r = {(1, 0): 25, (2, 0): 50, (3, 0): 100, (0, 1): 20, (0, 2): 40, (0, 3): 80}

def win(boss: list[int], player: list[int]):
    player_chance = True
    bhp, php = boss[0], player[0]
    while php > 0 and bhp > 0:
        if player_chance:
            damage = player[1] - boss[2]
            if damage <= 0: damage = 1
            bhp -= damage
        else:
            damage = boss[1] - player[2]
            if damage <= 0: damage = 1
            php -= damage
        player_chance = not player_chance
    return True if bhp <= 0 else False

items = set()

for item in w:
    items.add((item, None, None, None))
for item in product(w, r):
    items.add((item[0], None, item[1], None))
for item in product(w, r, r):
    if item[1] != item[2]: items.add((item[0], None, item[1], item[2]))
for item in product(w, a):
    items.add((item[0], item[1], None, None))
for item in product(w, a, r):
    items.add((item[0], item[1], item[2], None))
for item in product(w, a, r, r):
    if item[2] != item[3]: items.add((item[0], item[1], item[2], item[3]))

part1 = None
part2 = None
for item in items:
    w1 = item[0]
    a1 = item[1]
    r1 = item[2]
    r2 = item[3]

    cost = w[w1]
    player = [100, w1[0], w1[1]]

    if a1 != None:
        cost += a[a1]
        player[1] += a1[0]
        player[2] += a1[1]
    if r1 != None:
        cost += r[r1]
        player[1] += r1[0]
        player[2] += r1[1]
    if r2 != None:
        cost += r[r2]
        player[1] += r2[0]
        player[2] += r2[1]
    if win(boss, player):
        part1 = cost if part1 is None else min(cost, part1)
    else:
        part2 = cost if part2 is None else max(cost, part2)

print(part1)
print(part2)
