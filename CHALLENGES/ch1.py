"""
    Write a program that calulates the length of the last word in a sentence
"""

def len_last_word(sentence):
    """Returns the length of the last word in a sentence"""
    *others, last = sentence.split()
    print(others)
    return len(last)

print(len_last_word("I love my parents"))