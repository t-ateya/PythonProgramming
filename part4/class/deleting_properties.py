class Person:
    def __init__(self, name):
        self._name = name 

    def get_name(self):
        print('getter...')
        return self._name

    def set_name(self, value):
        print('setter...')
        self._name = value 

    def del_name(self):
        print('deleter...')
        del self._name

    name = property(fget=get_name, fset=set_name, fdel=del_name, doc='Person name')


p = Person('Guido')
    

class Person:
    def __init__(self, name):
        self._name = name 

    @property
    def name(self):
        """Person name"""
        print("getter...")
        return self._name

    @name.setter
    def name(self, value):
        print("setter...")
        self._name = value 

    @name.deleter
    def name(self):
        print("deleter...")
        del self._name


p = Person('Alex')

print(p.__dict__)
del p.name 

print(p.__dict__)


p.name = 'Guido'

print(p.__dict__)

