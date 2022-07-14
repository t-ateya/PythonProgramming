"""
  #217
    Given an array, find out if the array contains duplicates
    Return true if any number appears twice in the array, otherwise it should return false

"""
from collections import defaultdict


class Solution:
    def containsDup(self, arr:list[int])->bool:
        m = defaultdict(int)
        for i in arr:
            if i in m:
                return True 
            m[i] = 1
        return False

sol = Solution()
arr = [2,3,4,5,5]

print(sol.containsDup(arr))
