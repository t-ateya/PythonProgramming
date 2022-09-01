class Rectangle:
    #__(double underscore is called dunder)
    def __init__(self, width, height):
        self.width = width 
        self.height = height 
    

    #getter
    @property
    def width(self):
        return self._width

    #setter
    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError("Width must be positive.")
        else:
            self._width = width

    @property
    def height(self):
        return self._height

    #setter
    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError("height must be positive.")
        else:
            self._height = height

    def area(self):
        return self._width + self._height

    def perimeter(self):
        return 2 * (self._width + self._height)

    def to_string(self):
        return "Rectangle: width={0}, height = {1}".format(self._width, self._height)

    def __str__(self):
        return 'Rectangle: with={0}, height = {1}'.format(self._width, self._height)

    def __repr__(self):
        return "Rectangle({0}, {1})".format(self._width, self._height)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self._width == other._width and self._height == other._height
        return False
        

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        return NotImplemented
        



r1 = Rectangle(-10, 2000)
r2 = Rectangle(100, 20000)

#print(r1 == r2)
print(r1 < r2)
print(r2 > r1)
str(r1)
print(r1.to_string())
print(r1)
