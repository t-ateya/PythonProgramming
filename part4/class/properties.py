"""
    The property class
    property is a class (type)

    ->constructor has a few parameters:
        fget -> specifies the function to use to get instance property value
        fset -> specifies the function to use to set the instance property value
        fdel -> specifies the function to call when deleting the instance property
        doc -> a string representing the docstring for the property
"""
class Person:
    """This is a Person object"""
    def __init__(self, name) -> None:
        self.set_name(name)

    def get_name(self):
        return self._name

    def set_name(self, value):
        if isinstance(value, str) and len(value.strip()) > 0:
            self._name = value 
        else:
             raise ValueError('name must be a non-empty string')

p = Person('Alex')

try:
    p.set_name(100)
except ValueError as ex:
    print(ex)