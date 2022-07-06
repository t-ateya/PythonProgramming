# step 1
import random

# Challeng part  2

"""
world_list = ["ardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and
# assign it to the variable called chosen_word.
chosen_word = random.choice(world_list)

# Testing code
print(f"The Solution is: {chosen_word}")

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()
# TODO-3 - Check if the letter the user guessed (guess)
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
    #TODO-1: -Create an empty list called display
    For each letter in the chosen word, add a "_" to 'display'

    #So if the chosen word was "apple", display should be
    ["_", "_", "_", "_", "_"] with 5  "_" representing each letter to guess.

    #TODO-2: Loop through each position in the chosen_word:
    If the letter at the position matches  'guess' then reveal that letter in the display at that position.
    e.g If the user guessed "p" and the chosen word was "apple", then the display should be ["_","p","p", "_", "_"]

"""

world_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(world_list)
print(f"The Solution is: {chosen_word}")

display = []
word_length = len(chosen_word)

for letter in chosen_word:
    display.append("_")

print("display: ", display)

end_of_game = False
while not end_of_game:

    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = letter

    print("display: ", display)

    if "_" not in display:
        end_of_game = True
