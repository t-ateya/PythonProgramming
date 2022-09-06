#lambda [parameter list]: expression. 
#The parameter list is optional
"""
    Examples.
        lambda x: x**2
        lambda x, y : x + y #the lambda function takes in x,y and returns x + y
        lambda : 'hello'
        lambda s: s[::-1].upper()
        type(lambda x: x**2)

        my_func = lambda x : x**2
        my_func(3) ->9

        def apply_func(x, fn):
            return fn(x)

        apply_func(3, lambda x: x**2) ->9
        apply_func(2, lambda x: x + 5) ->7
        apply_func('abc', lambda x: x[1:]*3) ->bcbcbc


"""
g = lambda x, y = 10: x+ y
print(g(2))

f = lambda x, *args, y, **kwargs : (x, args, y, kwargs)
h = lambda x, *args, y, **kwargs : (x, *args, y, kwargs)
print(f(1, 'a', 'b', 2, y=100, a=10, b=20))
print(h(1, 'a', 'b', 2, y=100, a=10, b=20))

def apply_func(x, fn):
    return fn(x)

print(apply_func(5, lambda x:x**2))

def apply_func(fn, *args, **kwargs):
    return fn(args, kwargs)