
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

    def __setitem__(self, s, value):
        #s stands for slice
        try:
            rhs = [Point(*pt) for pt in value]  #rhs ==right hand side
            is_single = False
        except TypeError:
            try:
                rhs = Point(*value)
                is_single = True 
            except TypeError:
                raise TypeError("Invalid Point or Iterable of Points")
        
        if (isinstance(s, int) and is_single) \
            or (isinstance(s, slice) and not is_single):
                self._pts[s] = rhs 
        else:
            raise TypeError("Incompatible index/slice assignment")

        
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
    def __iadd__(self, other):
        self.extend(other)
        return self 

    def __delitem__(self, s):
        del self._pts[s]

    def pop(self, index=-1):
        return self._pts.pop(index)

    def clear(self):
        self._pts.clear()
            




p = Polygon((0,0), (1,1), (2,2), (3,3), Point(4,4))
print(p)

#print(p[0:2])

#p[0:2] = [(10, 10), Point(20, 20), [30, 30]]

#print(p[0:2])


#p[0] = Point(-11,-11) #invokes __setitem__ internally

#p[0] = [Point(10,10), Point(20,20)]

#p[0] = [(0,0), (1,1)]

#p[0:2] = Point(0,0)
#p[0] = ("a", "b")

#del p[0]
#del p[0:2]


#print("pop: ", p.pop(1))

p.clear()

print(p)




