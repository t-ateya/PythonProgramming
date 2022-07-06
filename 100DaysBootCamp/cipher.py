from art import logo
from operator import index
import string
# Part 1: Encryption


def caesar(text, shift, direction):
    number_of_alphabets = 26
    cipher_text = ""
    if direction == "decode":
        shift *= -1
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift) % number_of_alphabets
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        else:
            cipher_text += letter

    print(f" Here's the {direction}d result:  {cipher_text}")


print(logo)
alphabet = list(string.ascii_lowercase)
should_continue = True
while should_continue:
    text = input("Type your message: \n").lower()
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    shift = int(input("Type the shift number:\n"))
    caesar(text=text, shift=shift, direction=direction)
    result = input("Type 'yes' if you want to go again. Otherwise 'no' \n")
    if result == "no":
        should_continue = False
        print("Goodbye")

# TODO1- Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# TODO 2: Inside the 'encrypt' function, shift each letter of the text forwards in the alphabet by the
# shift amount and print the encrypted text.


def encrypt(plain_text, shift_amount):
    number_of_alphabets = 26
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = (position + shift_amount) % number_of_alphabets
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is: {cipher_text}")
    return cipher_text, shift_amount


def decrypt(cipher_text, shift):
    number_of_alphabets = 26
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = (position - shift) % number_of_alphabets
        new_letter = alphabet[new_position]
        plain_text += new_letter
    print(f"The decrypted text is: {plain_text}")


if direction == "encode":
    pass
    #encrypt(text, shift)
elif direction == "decode":
    pass
    #decrypt(text,shift )
else:
    pass
    #print("Wrong Input!!!, Please type encode or decode")


# Part 3: Combine encrypt and decrypt into a single function called caesar()


#caesar(text=text, shift=shift, direction=direction)

# Part 4 of the the caesar cipher
# TODO-3: Import and print the logo from art.py when the progrm starts
# print(logo)
# To DO 4: Can you figure out a way to ask if they want to restart the cipher text?
