"""
    #medium 17
    Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

"""
class Solution:
    def backtracking(self, ans, m, digits, combination, index):
        if (index > len(digits)):
            return 
        if (len(combination) == len(digits)):
            ans.append(combination[:])
            return 
        
        currDigit = digits[index]
        currString = m[currDigit]

        for i in range(len(currString)):
            self.backtracking(ans, m, digits, combination+currString[i], index + 1)


    def letterCombination(self, digits : str)->list[str]:

        ans = []
        if (len(digits) == 0):
            return ans 
        
        m = {}
        m['2'] = "abc"
        m['3'] = "def"
        m['4'] = "ghi"
        m['5'] = "jkl"
        m['6'] = "mno"
        m['7'] = "pqrs"
        m['8'] = "tuv"
        m['9'] = "wxyz"

        self.backtracking(ans, m, digits, "", 0)

        return ans 
