def logged(fn):
    from functools import wraps
    from datetime import datetime, timezone

    @wraps(fn)
    def inner(*args, **kwargs):
        run_dt = datetime.now(timezone.utc)
        result = fn(*args, **kwargs)
        print("{0}: called {1}".format(run_dt, fn.__name__))
        
        return result
    
    return inner


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


@logged
def func_1():
    pass 

@logged
def func_2():
    pass 
#func_1()

@timed
@logged
def fact(n):
    from operator import mul 
    from functools import reduce

    return reduce(mul, range(1, n+1))

fact(3)
#print(fact(3))



