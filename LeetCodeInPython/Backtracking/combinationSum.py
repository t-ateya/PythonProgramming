"""
    Medium #39
    Given a set of positive candidatees numbers (without duplicates) and a target number 
    Find all unique combinations of candidates where the candidates numbers sum to target.
    Note: 1. The same repeated number may be chosen from candidates unlimited number of times.
          2. The solution set must not contain duplicate combinations.
"""
class Solution:

    def solution(self, candidates, ans, cur, target, index, sum1):
        if (sum1 == target):
            ans.append(cur[:])
        elif (sum1 < target):
            n = len(candidates)
            for i in range(index, n):
                cur.append(candidates[i])
                self.solution(candidates, ans, cur, target, i, target, sum1+candidates[i])
                cur.pop()
        return 

        
    def combinationSum(self, candidates:list[int], target:int)->list[list[int]]:
        ans = []
        cur = []
        self.solution(candidates,ans,cur,target, 0, 0)
        return ans 