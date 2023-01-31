from math import sqrt

class Vector:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y 

    def __repr__(self):
        return f'Vector(x={self.x}, y={self.y})'

    def __eq__(self, other):
        print("__eq__ called...")
        if isinstance(other, tuple):
            other = Vector(*other)
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return NotImplemented

    def __abs__(self):
        return sqrt(self.x** 2 + self.y**2)

    def __lt__(self, other):
        if isinstance(other, tuple):
            other = Vector(*other)
        if isinstance(other, Vector):
            return abs(self) < abs(other)

    def __le__(self, other):
        return self == other or self < other


v1 = Vector(0, 0)
v2 = Vector(1, 1)

print(v1 < v2)
print(v2 < v1)

# v1 = Vector(10, 11)
# print(v1 == (10, 11))
# print((10, 11) == v1)


from functools import total_ordering

@total_ordering
class Number:
    def __init__(self, x) -> None:
        self.x = x 
    def __eq__(self, other) -> bool:
        print('__eq__ called ...')
        if isinstance(other, Number):
            return self.x == other.x
        return NotImplemented

    def __lt__(self, other):
        print("__lt__called")
        if isinstance(other, Number):
            return self.x < other.x 
        return NotImplemented

a = Number(1)
b = Number(2)
c = Number(1)

print(a < b)
print(a <= b)
print(a == b)

