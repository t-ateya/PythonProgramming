
#1. Mod function
def mod (number, tableSize):
    return number % tableSize


#2. ASCII function
def modASCII(string, tableSize):
    """ord() function returns the number representing and ASCII Char"""
    total = 0
    for i in string:
        total += ord(i)
    return total % tableSize

print(ord("a"))


