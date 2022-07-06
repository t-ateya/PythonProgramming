"""
    Instructions:
    You are going to write a program that tests the compatibility between two people.We're going to use the super scientific
    method recommended by BuzzFeed

    To work out the love score between two people:
      Take both people's names and check for the number of times the letters in the word TRUE occurs.
      Then check for the number of times the letters in the word LOVE occurs. Then combine the number to make a 2 digit number

      -For Love Scores  less than 10 or greater than 90, the message should be:
       "Your score is x, you go together like coke and mentos"

       -For Love Scores between 40 and 50, the message should be:\
           "Your score is y, you are alright together."

        Otherwise, the message should be their score. e.g:
         "Your score is z."
         e.g
         name1 = "Angela Yu"
         name2 = "Jack Bauer"

         T occurs 0 times
         R occurs 1 time
         U occurs 2 times
         E occurs 2 times
         total = 5

         L occurs 1 time
         O occurs 0 times
         V occurs 0 times
         E occurs 2 times
         Total = 3

         Love Score = 53
         Print: "your love score is 53." 

         Hint!!!
         1. The lower() function changes all the letters in a string to lowercase 
         2. The count() function will give you the number of times a letter occurs in a string 
         
"""

# Solution

# 1. Get user input
print("Welcome to the love calculator!")
name1 = input("What is your name?\n")
name2 = input("What is your lover's name?\n")
combined_name = name1 + name2
lower_case_name = combined_name.lower()

# 2. Total occurrence of TRUE
t = lower_case_name.count("t")
r = lower_case_name.count("r")
u = lower_case_name.count("u")
e = lower_case_name.count("e")

true = t + r + u + e
#print(f"Total occurrence of TRUE: {true}")

# 3. Total occurrence of LOVE
l = lower_case_name.count("l")
o = lower_case_name.count("o")
v = lower_case_name.count("v")
e = lower_case_name.count("e")

love = l + o + v + e
#print(f"Total occurrence of LOVE: {love}")

love_score = int(str(true) + str(love))
#print("love score: ", love_score)

# 4. Printing out love results
if (love_score < 10) or (love_score) > 90:
    print(f"Your score is {love_score},you go together")
elif (40 <= love_score <= 50):
    print(f"Your score is {love_score}, you are alright together")
else:
    print(f"Your score is {love_score}")
