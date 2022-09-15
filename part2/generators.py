"""
    Generator: A type of iterator
    Generator functions: generate generators. i.e they return a generator when called.They're not generators themselves.
    Generator expressions: A more comprehension syntax. A more coincise way of creating generators.

    Performance consideration of generators vs list comprehensions

yield:
    It emits a value, the function is effectively suspended (but it retains its current state)
    Calling next on the function resumes running the function right after the yield statement.
    if function returns something instead of yielding(finishes running) -> Stop Iteration exception
    Example below




def song():
    print("Line 1")
    yield "I am a lumber jack and I'M OK"
    print("line 2")
    yield "I sleep all night and I speek all day"

lines = song()
line = next(lines)
line = next(lines)
line = next(lines)
"""

#print(line)

"""
    Generators
      A function that uses the yield statement, is called a generator function
    Example:
        def my_func():
            yield 1
            yield 2
            yield 3
        my_func is just a regular function. Calling my_func() returns a generator object

    Generators are iterators
    gen = my_func()
    next(gen)


def my_func():
    yield 1
    yield 2
    yield 3

gen = my_func()
print(next(gen))
print(next(gen))
print(next(gen))
"""
import math 
#Example of using yield key word in creating iterators.
class FactIter:
    def __init__(self, n):
        self._n = n
        self.index = 0

    def __iter__(self):
        return self  

    def __next__(self):
        if self.index >= self._n:
            raise StopIteration
        else:
            result = math.factorial(self.index)
            self.index += 1
            return result

fact = FactIter(5)
print(next(fact))
print(next(fact))
print(next(fact))
print(next(fact))
print(next(fact))
print(next(fact))