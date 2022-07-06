"""
    The Longest Common Subsequence (LCS)
    Problem Statement
    - S1 and S2 are given strings
    - Find the length of the longest subsequence which is common to both strings.
    - Subsequence: a sequence that can be driven from another sequence by deleting some elements without changing the order of them

    Example
    - S1 = "elephant"
    - S2 = "erepat"
    - Output = 5
    - Longest String = "eepat"

    Subproblems:
    Option1 = 1 + f(2,8:2,7)  #8 being length of S1 and 7 length of S2, 2 the second char in S1
    Option2 = 0 + f(3,8 :2,7 )           =>max(option1, option2, option3)
    Option3 = 0 + f(2,8:3,7)


"""


def find_LCS(s1, s2, index1, index2):
    if index1 == len(s1) or index2 == len(s2):
        return 0
    if s1[index1] == s2[index2]:
        return 1 + find_LCS(s1, s2, index1 +1, index2+1)
    else:
        option1 = find_LCS(s1, s2, index1+1, index2)
        option2 = find_LCS(s1, s2, index1, index2+1)
        return max(option1, option2)

print(find_LCS("elephantu", "eretpatu", 0, 0))


