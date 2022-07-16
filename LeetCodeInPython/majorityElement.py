"""
    #169
    Given an array of integers of size N, find the majority element of the array.
"""
class Solution:
    def majorityElement(self, nums:list[int])->int:
        m = {}
        for num in nums:
            m[num] = m.get(num,0)+1

            """
            if num in m:
                m[num] +=1 
            else:
                m[num] =1
            """
        
        for num in nums:
            if m[num] > len(nums)//2:
                return num 

s = Solution()
arr = [2,3,4,5,5,5,5]
print(s.majorityElement(arr))