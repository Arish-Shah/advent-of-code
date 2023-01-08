puzzle = 33100000
house = 1

def get_divisors(n):
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            yield i
    yield n

while True:
    gifts = sum(get_divisors(house))
    print(house, gifts)
    if gifts >= int(puzzle / 10):
        break
    house += 1

print(house)
