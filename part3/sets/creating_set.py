s = {c for c in 'python'}
ss = set("python")
#print(s)
#print(ss)

s1 = {'a', 'b', 'c'}
s2 = {10, 20, 30}

s = {*s1, *s2}
#print(s)

s2 = {'b', 'c', 'd'}
s = {*s1, *s2}
#print(s)

l = [*s1, *s2]
#print(l)

def averager(*args):
    total = 0 
    for arg in args:
        total += arg
    return total / len(args)

args = {20, 10, 30}
#print(averager(*args))

s = "abcdefghijklmnopqrstuvwxyz"
distinct = set(s)

def scorer(s):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    s = s.lower()
    distinct = set(s)
    effective = distinct & alphabet
    return len(effective) / len(alphabet)