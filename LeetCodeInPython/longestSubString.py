"""
    Given a string, find the length of the longest substring without repeating characters.
"""

class Solution:
    def lengthOfLongestSubString(self, s:str)->int:
        m = {}
        left = 0
        right = 0
        longest = 0
        n = len(s)
        while (left<n and right < n):
            char = s[right]
            if (char in m):
                left = max(left, m[char] + 1)
            m[char] = right
            longest = max(longest, right-left+1)
            right +=1
        return longest

sol = Solution()
s = "fivestarreview"

print(sol.lengthOfLongestSubString(s))