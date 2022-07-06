#Write a function to find the missing number in a given integer array from 1 to 100
def missingNumber(myList, totalCount):
    sum_of_first_totCount_terms = totalCount*(totalCount + 1)/2
    missig_item = sum_of_first_totCount_terms - sum(myList)
    return int(missig_item)

def missingNumberMethod2(myList, totalCount):
    expectedSum = totalCount * ((totalCount + 1) / 2)
    actualSum = 0
    for i in myList:
        actualSum += i
    return int(expectedSum - actualSum)

myList = [1, 2, 3, 4, 6]
print(missingNumber(myList, 6))