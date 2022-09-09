
"""
    Background Information
      A regular strictly convex polygon is a polygon that has the following xtics:
        - All interior angles are less than 180 degrees. i.e strictly convex
        - All sides have equal length i.e regular

        For a regular strictly convex polygon with
            - n edges (= n vertices)
            - R circumradius
            

        interior angle = (n-2)*(180/n)
        edge length s = 2Rsin(pi/n)
        apothem a = Rcos(pi/n)  #apothem is the distance from central point to the middle of the edge
        area = 1/2*nsa
        perimeter = ns

        Goal 1
         
         Create a Polygon class

         Initializer
            - number of vertices/edges
            - circumradius

        Properties
            - # edges
            - # vertices
            - interior angle
            - edge length
            - apothem
            - area
            - perimeter

        Functionality
         - a proper representation(__repr__)
         - implements equality (==) based on # 
         vertices and circumradius (__eq__)
         - implements > based on number of vertices only (__gt__)


    Goal 2
    implement a Polygon sequence type:

    Initializer
        - number of vertices for largest polygon in the sequence
        - common circumradius for all polygons

    Properties
        - max efficiency polygon: returns the Polygon with the highest area: perimeter ratio

    Functionality
        - functions as a sequence type (__getitem__)
        - supports the len( function(__len__))

"""

# Goal 1

import math


class Polygon:
    def __init__(self, n, R) :
        self._n = n
        if n < 3:
            raise ValueError("Polygon must have at least three sides.")
        self._R = R

    def __repr__(self) -> str:
        return f"Polygon(n={self._n}, R={self._R})"
 
    @property
    def number_vertices(self):
        return self._n

    @number_vertices.setter
    def number_vertices(self, n):
        if n <= 2:
            raise ValueError("The number of vertices MUST be greater than 2")
        self._n = n

    @number_vertices.deleter
    def number_vertices(self, n):
        del self._n
        
    @property
    def circumradius(self):
        return self._R

    @circumradius.setter
    def circumradius(self, R):
        if R < 0:
            raise ValueError("The circumradius, R cannot be negative")
        self._R = R

    @circumradius.deleter
    def circumradius(self, R):
        del self._R

    @property
    def number_edges(self):
        return self._n
    
    @property
    def interior_angle(self):
        return (self._n-2)*(180 / self._n)

    @property
    def side_length(self):
        return 2* self._R*math.sin(math.pi / self._n)

    @property
    def apothem(self):
        return self._R*math.cos(math.pi / self._n)

    @property
    def area(self):
        return  1/2*self._n*self.side_length*self.apothem

    @property
    def perimeter(self):
        return self._n * self.side_length

    def __eq__(self, other) -> bool:
        if isinstance(other, Polygon):
            return self._n == other._n and self._R == other._R

        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.number_vertices > other.number_vertices 

        return NotImplemented


#Implementing Polygon sequence

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

    def __getitem__(self, s):
        return self._polygons[s]
    
    @property
    def max_efficiency_polygon(self):
        sorted_polygons = sorted(self._polygons, key=lambda p : p.area/p.perimeter, reverse=True)
        return sorted_polygons[0]







        

        

