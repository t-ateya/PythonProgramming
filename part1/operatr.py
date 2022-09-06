
l = [2, 3, 4]

#reduce(lambda a, b: a*b, l)

"""
    Examples:

    concat(s1, s2)

    contains(s, val)

    countOf(s, val)

    getitem(s, i)

    setitem(s, i, val)

    delitem(s, i)

    Item Getters

    itemgetter(i) e.g f = itemgetter(1)
                      s = [1,2,3]
                      f(s)->2
                      s = 'python'
                      f(s) -> 'y'

    l = [1, 2, 3, 4, 5, 6]

    s = 'python'

    f = itemgetter(1, 3, 4)

    f(l) -> (2, 4, 5)
    f(s) -> ('y', 'h', 'o')

    Attribute Getter


import operator as op

print(op.add(1, 2))
print(op.mul(2, 3))

s = [1, 2, 3]
item = op.getitem(s, 1, 0)
#print(item)

my_list = [1, 2, 3, 4]
print(my_list)
op.setitem(my_list, 1, 100)

"""
