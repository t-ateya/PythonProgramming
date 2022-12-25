"""
    A set is an unordered collection of distinct objects.

    Frozen sets are the immutable equivalent of sets
    - Sets are not hashbale but frozenset is hashable
    - A frozenset can therefore be used as a dictionary key since it's hashable

"""

s = set([1, 2, 3])
print(s)

d = {"a":1, "b":2}
s = set(d)
print(s)

