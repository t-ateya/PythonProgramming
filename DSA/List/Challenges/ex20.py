#Write a function to find all pairs of an integer array whose sum equal to a given number

def pairSum(myList, sum):
    results = []
    for i in range(len(myList)):
        for j in range(i+1, len(myList)):
            if myList[i] + myList[j] == sum:
                pairs = (str(myList[i]) +"+"+ str(myList[j]))
                results.append(pairs)
    return results


def pairSumMethod2(myList, sum):
    result = []
    for i in range(len(myList)):
        for j in range(i+1,len(myList)):
            if myList[i] + myList[j] == sum:
                result.append(str(myList[i]) +"+"+ str(myList[j]))
    return result

myList = [3,4, 5, 2, 6,1,8]
print(pairSum(myList,7))
print(pairSumMethod2(myList,7))

