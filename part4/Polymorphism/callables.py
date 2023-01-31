"""
    Any object can be made to emulate the callable by implementing a __call__ method

"""

class Person:
    def __call__(self, name):
        return f'Hello {name}'