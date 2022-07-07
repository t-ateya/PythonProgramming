"""
    Dynamic Programming - Number Factor Problem
    
    Problem Statement:
    Given N, find the number of ways to express N as a sum of 1, 3 and 4

    Example 1
        -N =4
        -Number of ways = 4
"""

def numberFactor(n):
    tb = [1,1,1,2]
    for i in range(4, n+1):
        tb.append(tb[i-1] + tb[i-3] + tb[i-4])
    return tb[n]

def number_factor_TopDown(n, temp_dict):
    """Top Down Approach"""
    if n in (0,1,2):
        return 1
    elif n == 3:
        return 2
    else:
        if n not in temp_dict:
            subP1 = number_factor_TopDown(n-1, temp_dict)
            subP2 = number_factor_TopDown(n-3, temp_dict)
            subP3 = number_factor_TopDown(n-4, temp_dict)
            temp_dict[n] = subP1 + subP2 + subP3
        return temp_dict[n]


def number_factor_bottom_up(n):
    """Bottom Up Approach. Performs better"""
    tempArray = [1,1,1,2]
    for i in range(4, n+1):
        tempArray.append(tempArray[i-1] + tempArray[i-3] + tempArray[i-4])
    return tempArray[n]

print(number_factor_TopDown(5, {}))
print(number_factor_bottom_up(5))