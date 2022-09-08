"""
    slicing relies on indexing. It only works with mutable(used to extract and assign data) and immutable sequnces(used to extract data).


l = [1, 2, 3, 4, 5]
l[0:2] = ('a', 'b', 'c', 'd', 'e')

#print(l)

s = slice(0, 2)

l = [1, 2, 3, 4, 5]
#print(l[s])

l = ["a", "b", "c", 'd', 'e', 'f']
print(l[3:100])

print(l[-3: -1])

l[0:6:2]

l[-1:-4:-1]

l[::]
l[1::2]
l[::2]

"""

s = slice(0,2)
print(type(s))

print(s.start)
print(s.stop)
print(s.step)

def get_data(data):
    for row in data:
        first_name = row[0:51]
        last_name = row[51:101]
        ssn = row[101:111]
    return first_name, last_name, ssn


def get_user_data(data):
    range_first_name = slice(0, 51)
    range_last_name = slice(51, 101)
    range_ssn = slice(101, 111)

    for row in data:
        first_name = row[range_first_name]
        last_name = row[range_last_name ]
        ssn = row[range_ssn]
    return first_name, last_name, ssn


range_first_name = slice(0, 51)
range_last_name = slice(51, 101)
range_ssn = slice(101, 111)

l = "python"

s1 = slice(0, 6, 2)
s1 = slice(None, 4)

l[s1]

l[3:0:-1]
l[3::-1]
l[3:-1:-1]
l[3:-100:-1]

s =slice(1, 5)
s.indices(10)
s.indices(4)