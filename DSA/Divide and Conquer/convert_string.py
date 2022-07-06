"""
    Convert String
    Problem Statememt:
        - S1 and S2 are given strings
        - Convert S2 to S1 using delete, insert or replace operations
        - Find minimum count of edit operations

    Example 1:
    - S1 = "catch"
    - S2 = "carch"
    - Output = 1
    - Explanation: Replace "r" with "t"

    Example 2
    -S1 = "table"
    - S2 = "tbres"
    - Output = 3
    - Explanation: Insert "a" to second position, replace "r" with "l" and delete "s"


"""

def find_min_operation(s1, s2, index1, index2):
    if index1 == len(s1):
        return len(s2) - index2 
    if index2 == len(s2):
        return len(s1)-index1
    if s1[index1] == s2[index2]:
        return find_min_operation(s1, s2, index1 +1, index2 +1)
    else:
        deleteOp = 1 + find_min_operation(s1, s2, index1, index2+1)
        insertOp = 1 + find_min_operation(s1, s2, index1+1, index2)
        replaceOp = 1 + find_min_operation(s1, s2, index1+1, index2+1)
        return min(deleteOp, insertOp, replaceOp)


print(find_min_operation("table", "tbrlett", 0, 0))