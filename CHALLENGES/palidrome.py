"""
    Write a program to find out if a string is a palindrome
    Palindrom is a word that can be read in forward and reverse orders e.g civic, level
"""

def is_palindrom(strn):
    """Returns true if a string is a palindrome and False otherwise"""
    if len(strn) == 1:
        return True 
    
    left_pointer = 0
    right_pointer = len(strn) - 1
    while left_pointer <= right_pointer:
        if strn[left_pointer] != strn[right_pointer]:
            return False

        left_pointer +=1
        right_pointer -=1
    return True 

s1 = "Ateya"
s2 = "civic"
s3 = "level"

print(is_palindrom(s1))
print(is_palindrom(s2))
print(is_palindrom(s3))