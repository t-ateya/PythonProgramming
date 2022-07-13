
def length_of_last_word(strns):
    """Returns the length of last word in  string"""
    if strns == "":
        return 0
    new_list = [word for word in strns.split()]
    return len(new_list[-1])

#print(length_of_last_word("ateya terence arrey m"))
print(length_of_last_word("   world   "))
