def fib_recursive(n):
    if n <=1:
        return 1
    return fib_recursive(n-1) + fib_recursive(n-2)

#print([fib_recursive(x) for x in range(7)])


from timeit import timeit
#duration = timeit('fib_recursive(30)', globals=globals(), number=10)
#print(duration)


#Using memoization to improve fib
from functools import lru_cache
@lru_cache
def fib_recursive(n):
    if n <=1:
        return 1
    return fib_recursive(n-1) + fib_recursive(n-2)

from timeit import timeit
#duration = timeit('fib_recursive(5000)', globals=globals(), number=10)
#print(duration)
#NB: Recursive call can always exceed maximum depth. So avoid recursion for large n

#A better approach in calculating fib number using non-recursive method: for loop
#[1,1, 2, 3, 5]
def fib(n):
    fib_0 = 1
    fib_1 = 1
    for x in range(n-1):
        fib_0, fib_1 = fib_1, fib_0 + fib_1
    return fib_1

#print([fib(x) for x in range(7)])

from timeit import timeit
duration = timeit('fib(5000)', globals=globals(), number=10)
#print(duration)


class FibIter:
    def __init__(self, n):
        self._n = n 
        self._index = 0

    def __iter__(self):
        return self 

    def __next__(self):
        if self._index >= self._n:
            raise StopIteration 
        else:
            result = fib(self._index)
            self._index += 1
            return result

fib_iter = FibIter(7)
for x in fib_iter:
    #print(x)
    pass 



#Best Approach: Using generator function

def fib_gen(n):
    fib_0 = 1
    yield fib_0
    fib_1 = 1
    yield fib_1
    for i in range(n-2):
        fib_0, fib_1 = fib_1, fib_0 + fib_1
        yield fib_1 

gen = fib_gen(7)
for num in gen:
    print(num)

from timeit import timeit
duration = timeit('list(fib_gen(5000))', globals=globals(), number=10)
print(duration)
