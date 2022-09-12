"""
    Iterating over the return value of a callable(callable simply means a function)

    The second form of the iter() function:
        iter(callable, sentinel)

    This will return an iterator that will:
        call the callable when next() is called
            and either raise StopIteration if the result is equal to the sentinel value or return the result otherwise.
"""

def counter():
    i = 0 
    
    def inc():
        nonlocal i 
        i += 1
        return i 
    return inc

class CallableIterator:
    def __init__(self, callable_, sentinel):
        self._callable_ = callable_
        self.sentinel = sentinel
        self.is_consumed = False

    def __iter__(self):
        return self 

    def __next__(self):
        if self.is_consumed:
            raise StopIteration
        else:
            result = self._callable_()
            if result == self.sentinel:
                self.is_consumed = True 
                raise StopIteration
            return result


def countdown(start = 10):
    def run():
        nonlocal start 
        start -=1
        return start 
    return run



cnt = counter()

print(type(cnt)) #cnt is a function i.e a callable

"""
for _ in range(10):
   # print(cnt())
   pass
"""

cnt_iter = CallableIterator(cnt, 5)

"""


for _ in range(5):
    #print(next(cnt_iter))
    pass 

for counter in cnt_iter:
    print(counter)
"""

#print(help(iter))
#print(next(cnt_iter))

cnt_itera = iter(cnt, 5)

"""
for c in cnt_itera:
    #print(c)
    pass 
"""

import random 

random.seed(0)
#seed ensures that the random number is repeatable
"""
for i in range(10):
    print(i, random.randint(0,10))



random_iter = iter(lambda : random.randint(0, 10), 8)
random.seed(0)

for num in random_iter:
    print(num)



take_off = countdown(10)
for _ in range(15):
    print(take_off())
"""

take_off = countdown(10)
take_off_iter = iter(take_off, -1)
for num in take_off_iter:
    print(num)

