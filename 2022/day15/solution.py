lines = open("example", "r").read().strip().split("\n")

class Point:
    def __init__(self, *args):
        if len(args) == 1:
            self.x, self.y = args[0]
        else:
            self.x, self.y = args

    def __repr__(self):
        return "({}, {})".format(self.x, self.y)

    def get_tuple(self):
        return (self.x, self.y)

def dist(p1: Point, p2: Point):
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)

def get_x(s: Point, d, y):
    rhs = d - abs(y - s.y)
    return s.x - rhs, s.x + rhs

def no_beacon_points(s: Point, d, y):
    points: set[tuple[int, int]] = set()
    for i in range(d, 0, -1):
        if abs(y - s.y) <= i:
            x1, x2 = get_x(s, i, y)
            points.add((x1, y))
            points.add((x2, y))
    return points

n = []
part1_y = 10
for line in lines:
    s, b = [Point(tuple(map(lambda x: int(x), part[part.index("at")+3:]
            .replace("x=", "")
            .replace(" y=", "")
            .split(",")))) for part in line.split(": ")]
    d = dist(s, b)
    n.extend(no_beacon_points(s, d, part1_y))
    if b.get_tuple() in n:
        n.remove(b.get_tuple())

print(len(set(n))) # part1
