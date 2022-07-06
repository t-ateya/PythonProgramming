"""
    The Longest Palindromic Subsequence (LPS)

    Problem Statement:
    -S is a given string
    -Find the longest palindromic subsequence (LPS)
    -Subsequence: a sequence that can be driven from another sequence by deleting some elements by deleting some elements without changing the order of them
    -Palindrome is a string that reads the same backward as well as forward

    Example 1:
    - S = "ELRMENMET"
    - Output = 5
    LPS: "EMEME"

    Subproblems:
    Option1 = 2 + f(2,8)
    Option1 = 0 + f(1,8)    => max(Option1, Option2, Option3)
    Option1 = 0 + f(2,9)


    Example 2:
    - S = "AMEEWMA"
    - Output = 6
    - LPS: "AMEEMA"
"""

def find_LPS(s, start_index, end_index):
    if start_index > end_index:
        return 0
    if start_index == end_index:
        return 1
    if s[start_index] == s[end_index]:
        return 2 + find_LPS(s, start_index+1, end_index-1)
    else:
        option1 = find_LPS(s, start_index, end_index-1)
        option2 = find_LPS(s, start_index+1, end_index)
        return max(option1, option2)

print(find_LPS("AMEEWMA", 0, 6))