class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # class method
    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
point.draw()
#print(point.x, point.y)
#print("type: ", type(point))
#print(isinstance(point, Point))

# Class vs Instance methods
point2 = Point.zero()
point2.draw()
