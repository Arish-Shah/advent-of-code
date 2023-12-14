f = open(0, "r").read().strip().split("\n")

def replacer(line: str):
    return line.replace("one", "o1e")\
            .replace("two", "t2o")\
            .replace("three", "t3e")\
            .replace("four", "f4r")\
            .replace("five", "f5e")\
            .replace("six", "s6x")\
            .replace("seven", "s7n")\
            .replace("eight", "e8t")\
            .replace("nine", "n9e")

def summer(f: list[str]):
    return sum(map(lambda x: int(x[0]+x[-1] if len(x) > 1 else x[0]*2),
                map(lambda x: [*filter(lambda y: y.isdigit(), x)],
                    map(lambda x: [*x], f))))


part1 = summer(f)
print(part1)

f = map(lambda x: replacer(x), f)
part2 = summer([*f])
print(part2)
