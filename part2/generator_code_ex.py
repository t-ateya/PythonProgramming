import math

class FactorialIter:
    def __init__(self, n) -> None:
        self._n = n
        self._index = 0

    def __iter__(self):
        return self 

    def __next__(self):
        if self._index >= self._n:
            raise StopIteration
        else:
            result = math.factorial(self._index)
            self._index += 1
            return result

""" 
fact_iter = FactorialIter(5)
print(list(fact_iter))      
print(list(fact_iter))      
print(next(fact_iter))   #Throws an exception
"""

#Using closure to achieve closure
def fact():
    i = 0
    def inner():
        nonlocal i 
        result = math.factorial(i)
        i += 1
        return result
    return inner


f = fact()
for _ in range(5):
    print(f())

f = fact()
fact_iter = iter(f, math.factorial(5))
print(list(fact_iter))


#####################Using yield key word#####################
def my_func():
    print('line 1')
    yield 'Flying'
    print('line 2')
    yield 'Circus'

f = my_func()
print(type(f))

print('__iter__' in dir(f))
print('__next__' in dir(f))
print(iter(f) is f)

print(f.__next__())
print(next(f))
#print(next(f))

def silly():
    yield 'this'
    yield 'ministry'