#Q6: Permutation. Find out if two strings are permutations of each other. That is, they have same chars but in different order

def isPermutation(list1, list2):
    """Returns True if list1 is permutation of list2"""
    if len(list1) != len(list2):
        return False
    else:
        for i in list1:
            if i not in list2:
                return False
    return True
list1 = ['a', 'c', 'b']
list2 = ['c', 'a', 'b']
print(isPermutation(list1, list2))

def permutation(list1, list2):
    if len(list1) != len(list2):
        return False
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    else:
        return False

print(permutation(list1, list2))