import numbers


numbers = [1, 3, 6, 9]
print(numbers)
print(*numbers)  # unpacking operator
values = [*range(5), *"Hello"]
print(values)

first = [1, 3]
second = [2]
value = [*first, "a", *second, *"Hello ateya arrey"]
print(value)

# unpacking dictionary
third = {"x": 1}
fourth = {"x": 10, "y": 2}
combined = {**third, **fourth, "z": 1}
print(combined)
