
"""
    Given a word, determine how many letters are in the middle of the word
"""
def middle_char_length(word):
    """Returns the number of letters in the middle of a word"""
    return len(word[1:-1])

print(middle_char_length("JESUS"))