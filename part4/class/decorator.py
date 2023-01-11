def my_decorator(fn):
    print("decorating function")
    def inner(*arg, **kwargs):
        print("running decorated function")
        return fn(*arg, **kwargs)
    return inner 


def undecorated_function(a, b):
    print('running original function')
    return a + b


decorated_func = my_decorator(undecorated_function)
#`print(decorated_func(1, 2))

@my_decorator
def my_func(a, b):
    print('running original function')
    return a + b

#print(my_func(1, 2))


class Person:
    def __init__(self, name) -> None:
        self._name = name 

    @property
    def name(self):
        """The Person's name"""
        return self._name

    @name.setter
    def name(self, name):
        self._name = name 


p = Person("Ateya")


print("================================================")
print(help(Person.name))