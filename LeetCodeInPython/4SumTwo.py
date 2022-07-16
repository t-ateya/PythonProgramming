"""
    #454
    Given four lists A, B, C, D of integer values, compute how many tuples (i,j,k,l) there are such that:
    A[i] + B[j] + C[k] + D[l] is zero.
"""
from typing import List
class Solution:
    def fourSumCount(self, A:list[int], B:List[int], C:List[int], D:list[int]):
        m = {}
        ans = 0
        lA = len(A)
        lB = len(B)
        lC = len(C)
        lD = len(D)

        for i in range(lA):
            x = A[i]
            for j in range(lB):
                y = B[j]

                if (x+y not in m):
                    m[x+y] = 0
                m[x+y] += 1
                
        for i in range(0, lC):
            x = C[i]
            for j in range(lD):
                y = D[j]
                target = -(x+y)
                if (target in m):
                    ans += m[target]
        return ans
                