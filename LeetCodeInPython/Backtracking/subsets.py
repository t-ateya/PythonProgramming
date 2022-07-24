"""
    Medium #78
    Given a set of distinct integers, nums, return all possible subsets.

    Note: The solution set must not contain duplicate subsets.
"""
class Solution:
    def solution(self, nums, ans, curr, index):
        if (index > len(nums)):
            return 
        ans.append(curr[:])

        for i in range(index, len(nums)):
            if (nums[i] not in curr):
                curr.append(nums[i])
                self.solution(nums, ans, curr, i)
                curr.pop()

    def subsets(self, nums:list[int]) ->list[list[int]]:
        ans = []
        curr = []
        self.solution(nums, ans, curr,0)
        return ans 