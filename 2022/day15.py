lines = open("input.txt").read().splitlines()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def get_tuple(self):
        return (self.x, self.y)

    def no_beacon_points(self, d, y):
        points = set()
        for i in range(1, d+1):
            if abs(self.y - y) <= i:
                rhs = i - abs(self.y - y)
                points.add((self.x + rhs, y))
                points.add((self.x - rhs, y))
        return points

points = set()
for line in lines:
    data = [tuple(map(int, part[part.index("x="):].replace("x=", "").replace("y=", "").split(", "))) for part in line.split(": ")]
    s = Point(*data[0])
    b = Point(*data[1])
    d = s.dist(b)
    for p in s.no_beacon_points(d, 10):
        if b != p:
            points.add(p)

print(len(points))
