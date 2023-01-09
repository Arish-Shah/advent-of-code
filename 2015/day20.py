puzzle = 33100000
house = 1
part1 = part2 = 0
found1 = found2 = False

def get_divisors1(n):
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            yield i
    yield n

def get_divisors2(n):
    for i in range(1, int(n / 2) + 1):
        if n % i == 0 and n / i <= 50:
            yield i
    yield n

while True:
    gifts1 = sum(get_divisors1(house)) * 10
    gifts2 = sum(get_divisors2(house)) * 11
    if gifts1 >= puzzle and not found1:
        found1 = True
        part1 = house
    if gifts2 >= puzzle and not found2:
        found2 = True
        part2 = house
        break
    house += 1
    print(house)

print(part1)
print(part1)
