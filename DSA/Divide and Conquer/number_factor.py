"""
    Number Factor
    Problem Statement:
    Given N, find the number of ways to express N as sum of 1, 3, and 4.

    Example 1
        -N = 4
        -Number of ways = 4
        
        -Explanation: There are 4 ways we can express N: {4}, {1, 3}, {3,1}, {1,1,1,1}

    Example 2
        -N = 5
        -Number of ways = 6
        
        -Explanation: There are 6 ways we can express N: {4,1}, {1, 4}, {1,3,1}, {3,1,1},{1,1,3},{1,1,1,1}
"""

def number_factor(n):
    if n in (0, 1,2):
        return 1
    elif n == 3:
        return 2
    else:
        subP1= number_factor(n-1)
        subP2= number_factor(n-3)
        subP3= number_factor(n-4)
        return subP1 + subP2 + subP3

print(number_factor(4))