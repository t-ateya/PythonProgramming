class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y+other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y-other.y)


point = Point(1, 2)
other = Point(11, 20)
print(point + other)
print(point - other)
