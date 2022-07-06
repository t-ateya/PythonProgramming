#Given a list, write a function to get the first, second best scores from the list
def firstSecond(myList):
    newList = sorted(myList)
    first = newList[-1]
    second = newList[-2]
    return first, second


myList = [84, 85, 86, 87, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0]

print(firstSecond(myList))