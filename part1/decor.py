"""
    In general, a decorator function:
    -takes a function as an argument
    -returns a closure
    -The closure usually accepts any combination of parameters
    -runs some code in the inner function (closure)
    -the closure function calls the original function using the arguments passed to the closure
    -returns whatever is returned by that function call

    def counter(fn):
        count = 0
        def inner(*args, **kwargs):
            nonlocal count
            count +=1
            print('{0} was called {1} times'.format(fn.__name__, count))
            return fn(*args, **kwargs)
        return inner



    @counter 
    def mult(a, b, c=1):
        return a * b *c                same as:    mult = counter(mult)


"""

def counter(fn):
    #inner() is closure that has 2 free variables; counter and fn
    #*args and **kwargs arguments to inner() and thus are not local to inner(). There4, they're not free variables
        count = 0
        def inner(*args, **kwargs):
            nonlocal count
            count +=1
            print('{0} was called {1} times'.format(fn.__name__, count))
            return fn(*args, **kwargs)
        inner.__name__ = fn.__name__
        inner.__doc__ = fn.__doc__
        return inner #returns a closure

def add(a:int, b:int = 0):
    """
        adds two variables
    """
    return a + b

def mult(a : int, b: int, c : int = 1, *, d):
    """multiplies three values"""
    return a * b * c * d

def my_func(s: str, i:int)->str:
    return s * i 

my_func = counter(my_func)




add = counter(add)
add(20, 30)



from functools import wraps

def counter(fn):
    #inner() is closure that has 2 free variables; counter and fn
    #*args and **kwargs arguments to inner() and thus are not local to inner(). There4, they're not free variables
        count = 0
        def inner(*args, **kwargs):
            nonlocal count
            count +=1
            print('{0} was called {1} times'.format(fn.__name__, count))
            return fn(*args, **kwargs)
        inner = wraps(fn)(inner)
        return inner #returns a closure