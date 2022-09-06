def timed(fn):
    from time import perf_counter
    from functools import wraps

    @wraps(fn)
    def inner(*args, **kwargs):
        elapsed_total = 0
        elapsed_count = 0

        for i in range(10):
            print("Running iteration...{}".format(i))
            start = perf_counter()
            result = fn(*args, **kwargs)
            end = perf_counter()
            elapsed = end - start 
            elapsed_total += elapsed
            elapsed_count += 1

        args_ = [str(a) for a in args]
        kwargs_ = ["{0}={1}".format(k,v) for (k, v) in kwargs.items()]
        all_args = args_ + kwargs_
        args_str = ','.join(all_args)

        elapsed_avg = elapsed_total / elapsed_count

        print("{0}({1}) took {2:.6f}s to run".format(fn.__name__, args_str, elapsed_avg))

        return result
    
    return inner

#@timed
def calc_recursive_fib(n):
    if n <= 2:
        return 1
    else:
        return calc_recursive_fib(n-1) + calc_recursive_fib(n-2)

#calc_recursive_fib(6)

@timed
def fib_recursive(n):
    return calc_recursive_fib(n)

#print(fib_recursive(35))

@timed
def fib_loop(n):
    fib_1 = 1
    fib_2 = 1
    for _ in range(3, n+1):
        fib_1, fib_2 = fib_2, fib_1 + fib_2
    
    return fib_2

print(fib_loop(35))

from functools import reduce

@timed
def fib_reduce(n):
    initial = (1, 0)
    dummy = range(n)
    fib_n = reduce(lambda prev, n: (prev[0] + prev[1], prev[0]),
                            dummy, initial)
    return fib_n[0]

print(fib_reduce(35))