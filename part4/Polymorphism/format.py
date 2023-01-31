class Person:
    def __init__(self, name, dob):
        self._name = name 
        self._dob = dob 

    @property
    def name(self):
        return self._name 

    def dob(self):
        return self._dob 

    def __repr__(self):
        return f"Person(name={self.name}, dob={self.dob.isoformat()})"

    def __str__(self):
        print('__str__ called...')
        return f'Person({self.name})'

    def __format__(self, date_format_spec):
        print("__format__ called..")
        dob = format(self.dob, date_format_spec)
        return f'Person(name={self.name}, dob={dob})'

from datetime import date 

p = Person('Alex', date(1900, 10, 20))
