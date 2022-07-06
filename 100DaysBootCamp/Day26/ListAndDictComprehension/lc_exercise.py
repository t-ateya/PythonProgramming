

numbers =[1, 1, 2, 3, 5, 8, 13, 21, 34, 55 ]

#ex1
def square_numbers(numbers_list):
    """Returns a list of square numbers"""
    return [n**2 for n in numbers_list]

#print(square_numbers(numbers))

#ex2
def even_numbers(numbers_list):
    """Returns a list of even numbers"""
    return [x for x in numbers_list if x%2==0]
#print(even_numbers(numbers))


#ex3.
with open("file1.txt", "r") as f1:
    list1 = f1.readlines()

with open("file2.txt", "r") as f2:
    list2 = f2.readlines()

result = [int(n) for n in list1 if n in list2]
print(result)

