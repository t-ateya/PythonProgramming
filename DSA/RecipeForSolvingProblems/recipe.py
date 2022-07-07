"""
    1. Undertand the Problem
        a) Can we restate the problem in our own words?
        b) What are the inputs that go into the problem?
        c) What are the outputs that come from the problem?
        d) Can the outputs be determined from the inputs? In other words, do we have enough information to solve this problem?
        e) What should I label the important piece of data that are the part of a problem?
    2. Explore Examples
        a) Start with simple examples
                #Step 1 - Simple Example
                charCount("bbbb")
                  Ans: {b:4}
                charCount("hello")
                    Ans: {h:1, e:1, l:2, o:1}
        b) Progress to more complex examples
             Complex examples: charCount("My name is Ateya Arrey")
        c) Explore examples with empty
                charCount("")
        d) Explore the example with invalid iputs
                    charCount(1)
    3. Break it Down
        - Write out the steps that you need to take
        def charCount(strn):
            #declare and object to return at the end
            #loop over the string
                If the char is letter and it is in our object, add one to the value
                If the char is letter and is in not in our object, add char to our object with the value of 1
            # return an object
    4. Solve/Simplify
            Solve the problem if you can
            Simplify the 
            Simplify the problem
                - Find the core difficulty
                - Temporarily ignore that difficulty
                - Write a simplified solution
                - Then incorporate that difficulty
    5. Look Back and Refactor
            -Can we check the result?
            -Can we drive the result differently? i.e is there another solution?
            -Can we understand it at a glance?
            -Can we use the result or method for some other problem?
            -Can we improve the performance of your solution?
            -How other people solve this problem?
"""

def char_count(letters):
    """Returns the number of times a letter appears in a group of letters"""
    temp_dict = {}
    try:
        for char in letters:
            temp_dict.update([(char,letters.count(char))])
    except TypeError as err:
        return f"Sorry!!!, error occurred:  {err}"
    else:
        return temp_dict

def charCount(strn):
    """returns the number of char counts"""
    temp = {}
    for char in strn.lower():
        if isinstance(char, str) and not(char.isspace()):
            if char not in temp.keys():
                temp[char] = 1
            else:
                temp[char] +=1
    return temp


def char_count2(letters):
    """Returns the number of times a letter appears in a group of letters"""
    temp_dict = {}
    temp_dict1={temp_dict.update([(char,letters.count(char))]) for char in letters}
    return temp_dict1
    

def word_count(sentence):
    """Returns the number of times a word appears in a sentence."""
    temp_dict = {}
    for word in sentence.split():
        temp_dict.update([(word,sentence.count(word))])
    return temp_dict


sentence = "I am in love with you for you are the best in my life to love"
#print(word_count(sentence))
#print(charCount("bbbuvwx   BxXuU"))
print(charCount(1))

"""
print(char_count("My name is ateya arrey"))
print(char_count(""))
print(char_count(1))
"""