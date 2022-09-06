
def fib(n):
    print("Calculating fib({0})".format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)

#fib(10)

class Fib:
    def __init__(self) -> None:
        self.cache = {1: 1, 2: 1}

    def fib(self, n):
        if n not in self.cache:
            print("Calculating {0}".format(n))
            self.cache[n] = self.fib(n-1) + self.fib(n-2)

        return self.cache[n]

f = Fib()

#print(f.fib(10))



########## Using closure ==============
def fib():
    cache = {1:1, 2: 1}

    def calc_fib(n):
        if not n in cache:
            print("Calculating {0}".format(n))
            cache[n] = calc_fib(n-1) + calc_fib(n-2)
        return cache[n]

    return calc_fib  #closure

f = fib()
#print(f(10))


######### Using decorator ==============
def memoize(fn):
    cache = dict()

    def inner(n):
        if not n in cache:
            cache[n] = fn(n)
        return cache[n]

    return inner 

@memoize
def fib(n):
    print("Calculating fib({0})".format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)

#fib(5)


from functools import lru_cache  #least recently used cache

@lru_cache
def fib(n):
    print("Calculating fib({0})".format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)


@lru_cache(maxsize=8)
def fib(n):
    print("Calculating fib({0})".format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)

fib(12)


