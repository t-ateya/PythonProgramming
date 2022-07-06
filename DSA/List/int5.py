#Question 5: Is Unique: Implement an algorithm to determine if a list has all unique characters using python list

def isUnique(my_list):
    """Returns True if a list is unique. False otherwise"""
    temp = []
    unique = True
    for element in my_list:
        if my_list.count(element) >1 :
            temp.append(element)
            unique = False
    return f"{unique}, The duplicate element is {temp}"


def isNotDuplicate(list):
    temp = []
    for element in list:
        if element in temp:
            print(element)
            return False
        else:
            temp.append(element)
    return True


myList = [1, 20, 30, 44, 5, 56,  57, 8, 10,19, 31, 12, 13, 14, 35, 16, 27, 58,20, 19,19, 21]
my_list = [1, 2, 3,3]
print(isUnique(myList))
print(isUnique(my_list))

print(isNotDuplicate(my_list))
#print(myList.count(20))
