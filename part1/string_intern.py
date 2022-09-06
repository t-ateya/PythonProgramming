import sys 
import time 

a = sys.intern("hello world")
b = sys.intern("hello world")
c = "hello world"

"""
print(id(a), id(b), id(c))

print(a is b)
print(a is c)
print(c is b)
"""

def compare_using_equals(n):
    a = "a long string that is not interned"*200
    b = "a long string that is not interned"*200

    for _ in range(n):
        if a == b:
            pass

def compare_using_interning(n):
    a = sys.intern("a long string that is not interned"*200)
    b = sys.intern("a long string that is not interned"*200)

    for _ in range(n):
        if a is b:
            pass

start = time.perf_counter()
compare_using_equals(10000000)
end = time.perf_counter()
print("equality:", end - start)


start = time.perf_counter()
compare_using_interning(10000000)
end = time.perf_counter()
print("interning:", end - start)
