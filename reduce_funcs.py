"""
    Reducing functions in python are functions that recombine an iterable recursively, ending up with a single return value
"""
from msilib import sequence


l = [5, 8, 6, 10, 9]
_max = lambda x, y : x if x > y else y

def max_sequence(seq):
    result = seq[0]
    for x in seq[1:]:
        result = _max(result, x)
    return result


_min = lambda x, y : x if x <y else y
def min_sequence(seq):
    result = seq[0]
    for x in seq[1:]:
        result = _min(result, x)
    return result

_add = lambda a, b: a + b

def add_sequence(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = _add(result, x)
    return result


def _reduce(fn, sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = fn(result, x)
    return result


def _reduces(fn, sequence, initial):
    result = initial
    for x in sequence[1:]:
        result = fn(result, x)
    return result


print(max_sequence(l))
print(min_sequence(l))
print(add_sequence(l))

print(_reduce(_min, l))
print(_reduces(lambda a, b : a+b, l, 0))
