numbers = [1, 1, 2, 3, 4]
first = set(numbers)
second = {6, 8, 4}
second.add(5)
second.add(7)
print("len: ", len(second))

print(first | second)
print(first & second)
print(first - second)
print(first ^ second)

if 1 in first:
    print("Yes")
