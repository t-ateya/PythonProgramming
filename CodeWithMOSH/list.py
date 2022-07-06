from operator import le


letters = ["a", "b", "c", "d"]
matrix = [[0, 1], [2, 4], [5, 6]]
zeros = [0]*5
combined = zeros+letters
numbers = list(range(20))
chars = list("Hello great programmer")
print(combined)
print(zeros)
print(numbers)
print(chars)

letters[0] = 'A'
print(letters[0:3])
print(letters[::2])

# Print even numbers
print("even numbers: ", numbers[::2])
print("numbers in reverse order: ", numbers[::-1])


# List unpacking
numbs = [1, 4, 6, 9, 7, 10]
first, second, *other, last = numbs
print(first)
print(second)
print(other)
print(last)

# Looping over lists
letters = ["a", "b", "c"]
for letter in enumerate(letters):
    print(letter[0], letter[1])

# Better approach
# enumerate funct is used to get the index
for index, let in enumerate(letters):
    print(index, let)

# Add
letters.append("d")  # adds element to the end of the list
letters.insert(3, "p")

# Remove
letters.pop()  # Remove elt at the end of the list
letters.pop(2)  # Removing a letter at a specific index
del letters[0:3]
# letters.remove("d")
letters.clear()  # removes all the objs on list


# Finding objs in a list
chars = ["l", "o", "v", "e"]
print(chars.count("o"))

if "o" in chars:
    print(chars.index("o"))

# Sorting elements
nu = [4, 6, 7, 1, 19]
nu.sort()
print("sorted", nu)
nu.sort(reverse=True)
print("reversed: ", nu)

print(sorted(nu, reverse=True))

items = [
    ("Product1", 11),
    ("Product2", 1),
    ("Product3", 14),
    ("Product4", 10)

]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)
