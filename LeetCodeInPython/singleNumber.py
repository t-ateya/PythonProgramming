"""
#136
    Given a non-empty array of integers, every element appears twice except one, find it.
"""

#My Solution
class Solution1:
    def findSingleNumber(self, arr):
        """Returns a non-repetitive number"""

        return [item for item in arr if arr.count(item) == 1][0]
        

#Tutor's solution
class Solution:
    def findSingleN(self, A):
        return 2*sum(set(A)) - sum(A)

        


sol = Solution()
arr = [2, 2, 4, 3,3, 4,6, 5,5, 6,7]
#print(sol.findSingleNumber(arr))
print(sol.findSingleN(arr))