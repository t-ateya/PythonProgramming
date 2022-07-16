"""
  #Medium 49
    Given an array of strings. Group the anagrams together. An anagram is a word that is formed by 
    re-arranging the letters of a different word i.e Anagrams are words formed by re-arranging the letters in a given word.
"""
class Solution:
    def findHash(self, s):
        return ''.join(sorted(s))

    def groupAnagrams(self, strs: list[str])->list[list[str]]:
        result = []
        m = {}

        for s in strs:
            hashed = self.findHash(s)
            if (hashed not in m):
                m[hashed] = []
            m[hashed].append(s)

        for val in m.values():
            result.append(val)
        
        return result

sol = Solution()
anagram = ["ate", "eat", "tea", "play", "plan", "bat", "tab"]
print(sol.groupAnagrams(anagram))

