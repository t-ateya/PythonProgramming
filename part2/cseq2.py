
import numbers

class Point():
    def __init__(self, x, y) -> None:
        if isinstance(x, numbers.Real) and isinstance(y, numbers.Real):
            self._pt = (x, y)
        else:
            raise TypeError ("Point co-ordinates must be real numbers.")
        
    def __repr__(self) -> str:
        return f"Point(x={self._pt[0]}, y={self._pt[1]})"

    #Let's make a point a seq by defining the len and getitem methods

    def __len__(self):
        return len(self._pt)

    
    def __getitem__(self, index):
        return self._pt[index]
    
        

class Polygon:
    def __init__(self, *pts) -> None:
        if pts:
            self._pts = [Point(*pt) for pt in pts]
        else:
            self._pts = []

    def __repr__(self) -> str:
        pts_str = ','.join([str(pt) for pt in self._pts])
        return f"Polygon({pts_str})"

    #Let's make a Polygon a sequence by defining len and getitem methods
    def __len__(self):
        return len(self._pts)

    def __getitem__(self, s):
        return self._pts[s]

    #does not mutate the polygon i.e the id of the sum is diff from individual polygons
    def __add__(self, other):
        if isinstance(other, Polygon):
            new_pts = self._pts + other._pts
            return Polygon(*new_pts)
        else:
            raise TypeError("Can only concatenate with another Polygon")

    def append(self, pt):
        self._pts.append(Point(*pt))

    def insert(self, i, pt):
        self._pts.insert(i, Point(*pt))

    def extend(self, pts):
        if isinstance(pts, Polygon):
            self._pts += pts._pts
        else:
            points = [Point(*pt) for pt in pts]
            self._pts += points

    #in-place concatenation: does mutate the polygon
    """
    def __iadd__(self, other):
        if isinstance(other, Polygon):
            points= other._pts
        else:
            points = [Point(*pt) for pt in other]

        self._pts += points
        return self 
    """
    
    #in-place concatenation: does mutate the polygon
    def __iadd__(self, other):
        self.extend(other)
        return self 
            



"""
p1 = Point(10, 2.5)
print(p1)
p2 = Point('abc', 25)
print(p2)


p1 = Point(10, 2)
x, y = p1 

p2 = Point(*p1)
print(x)
print(y)
"""


"""
p = Polygon((0,0), Point(1,1), [2,3], {5,6})
print(p)

p1 = Polygon(Point(x=0, y=0),Point(x=1, y=1),Point(x=2, y=3),Point(x=5, y=6))

print(p1)

p2 = Polygon((0,0), (1,1), (2,2))

print(p2)

print(p2[0:2])
print(p[0])

print(p[::-1])
"""

p1 = Polygon((0,0), (1,1))
p2 = Polygon((2,2), (3,3))

#print(p1 + p2)


#in-place concatenation
#print(id(p1))
p1 += p2   #p1 == p1__iadd(p2)
#print(p1)
#print(id(p1))

p1 = Polygon((0,0), (1,1))
p1 += [(2,2), (3,3), [1,4], Point(7,6)]
#print(p1)

# Testing append and extend

p1 = Polygon((0,0), (1,1))
p2 = Polygon((2,2), (3,3))

p1.append([10, 10])
p1.append(Point(5,5))

p1.insert(1, Point(-1, -1))

p1.extend(p2)
p1.extend([(-100, -100), Point(8,8)])
print(p1)




