"""
House Robber Problem
    Problem Statement:
    - Given N number of houses along the street with some amount of money
    - Adjacent houses cannot be stolen
    - Find the maximum amount that can be stolen
"""

def houseRobberTopDown(houses, currentIndex, tempDict):
    if currentIndex >= len(houses):
        return 0
    else:
        if currentIndex not in tempDict:
            stealFirstHouse = houses[currentIndex] + houseRobberTopDown(houses, currentIndex+2, tempDict)
            skipFirstHouse = houseRobberTopDown(houses, currentIndex+1, tempDict)
            tempDict[currentIndex] = max(stealFirstHouse, skipFirstHouse)
        return tempDict[currentIndex]


def houseRobberBottomUp(houses, currentIndex):
    tempArray = [0]*(len(houses) + 2)
    for i in range(len(houses)-1, -1, -1):
        tempArray[i]= max(houses[i]+tempArray[i+2], tempArray[i+1])
    return tempArray[0]

houses = [6,7,1,30,8,2,4]
houses1 = [5,7,8,9,10,11,20]
#print(houseRobberTopDown(houses1, 0, {}))
print(houseRobberBottomUp(houses, 0))