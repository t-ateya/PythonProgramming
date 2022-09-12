"""
    The starting point for this project is the Polygon class and the Polygon sequence type we created in project 1

    Goal 1:
    Refactor the Polygon class so that all the calculated properties are lazy properties, i.e they should still be calculated properties, but they should not 
    have to get calculated more than once(since we made out polygon class 'immutable').

    Goal 2:
    Refactor the Polygon(sequence) type, into an iterable. Make sure also that the elements in the iterator are computed lazily i.e you can
    no longer use a list as an underlying storage mechanism for your polygons

    You'll need to implement both iterable and an iterator. 


"""

import math

#Note: Polygon is immutable since it does not implement setter property. So we assign new values to any of the polygon attributes.
class Polygon:
    def __init__(self, n, R) :
        if n < 3:
            raise ValueError("Polygon must have at least three sides.")
        self._n = n
        self._R = R

        self._interior_angle = None 
        self._side_length = None 
        self._apothem = None 
        self._area = None 
        self._perimeter = None 


    def __repr__(self) -> str:
        return f"Polygon(n={self._n}, R={self._R})"

    
 
    @property
    def circumradius(self):
        return self._R

    @property
    def number_edges(self):
        return self._n

    @property
    def number_vertices(self):
        return self._n
    
    @property
    def interior_angle(self):
        if not self._interior_angle:
            self._interior_angle = (self._n-2)*(180 / self._n)
        return self._interior_angle

    @property
    def side_length(self):
        if self._side_length is None:
            self._side_length = 2* self._R*math.sin(math.pi / self._n)
        return self._side_length

    @property
    def apothem(self):
        if not self._apothem:
            self._apothem = self._R*math.cos(math.pi / self._n)
        return self._apothem

    @property
    def area(self):
        if self._area is None:
            self._area = 1/2*self._n*self.side_length*self.apothem
        return  self._area

    @property
    def perimeter(self):
        if not self._perimeter:
            self._perimeter = self._n * self.side_length
        return self._perimeter 

    def __eq__(self, other) -> bool:
        if isinstance(other, Polygon):
            return self._n == other._n and self._R == other._R

        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.number_vertices > other.number_vertices 

        return NotImplemented


#Implementing Polygon sequence
class PolygonIterator:
    def __init__(self, m, R):
        if m < 3:
            raise ValueError("m must be at least 3")
        self._m = m
        self._R = R 
        self._index = 3

    def __iter__(self):
        return self 

    def __next__(self):
        if self._index > self._m:
            raise StopIteration
        else:
            poly = Polygon(self._index, self._R)
            self._index +=  1
            return poly

class Polygons:
    def __init__(self, m, R):
        if m < 3:
            raise ValueError("m must be at least 3")
        self._m = m
        self._R = R 
        self._polygons = [Polygon(i,R) for i in range(3, m + 1)]

    def __len__(self):
        """Returns the number of polygons in the sequence"""
        return self._m - 2

    def __repr__(self) -> str:
        return f'Polygon(m={self._m}, R={self._R})'

    def __iter__(self):
        return PolygonIterator(self._m, self._R)

    @property
    def max_efficiency_polygon(self):
        sorted_polygons = sorted(PolygonIterator(self._m, self._R), key=lambda p : p.area/p.perimeter, reverse=True)
        return sorted_polygons[0]

    
