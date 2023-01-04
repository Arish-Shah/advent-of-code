from json import loads

contents = open("input.txt").read().strip()
part1 = part2 = 0

def read1(obj):
    global part1
    if isinstance(obj, int):
        part1 = part1 + obj
    elif isinstance(obj, list):
        for item in obj:
            read1(item)
    elif isinstance(obj, dict):
        for item in obj:
            read1(obj[item])

def read2(obj):
    global part2
    if isinstance(obj, int):
        part2 = part2 + obj
    elif isinstance(obj, list):
        for item in obj:
            read2(item)
    elif isinstance(obj, dict):
        if "red" not in obj.values():
            for item in obj:
                read2(obj[item])

obj = loads(contents)
read1(obj)
read2(obj)
print(part1)
print(part2)
