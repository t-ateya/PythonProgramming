"""
#268
    Given an array containing n ditinct numbers taken from 0, 1, 2, 3, ..,n
    find the number that is missing from the array
"""
#My Solution

class Solution:
    def findMissingItem(self, nums:list[int])->int:
        n = len(nums)
        intended_sum= n*(n+1)/2
        actual_sum = sum(nums)
        return int (intended_sum - actual_sum)



nums = [0, 3, 1, 2, 5]
sol = Solution()
print(sol.findMissingItem(nums))

