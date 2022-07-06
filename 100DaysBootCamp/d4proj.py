import random

paper = '''
     _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|
'''
scissors = '''
     ____
  / __ \
 ( (__) |___ ___
  \________,'   """""----....____
   _______<  () dd       ____----'
  / __   __`.___-----""""
 ( (__) |
  \____/
'''

rock = '''
                                                        
                                  88                    
                                  88                    
                                  88                    
8b,dPPYba,  ,adPPYba,   ,adPPYba, 88   ,d8 8b       d8  
88P'   "Y8 a8"     "8a a8"     "" 88 ,a8"  `8b     d8'  
88         8b       d8 8b         8888[     `8b   d8'   
88         "8a,   ,a8" "8a,   ,aa 88`"Yba,   `8b,d8'    
88          `"YbbdP"'   `"Ybbd8"' 88   `Y8a    Y88'     
                                               d8'      
                                              d8'  
'''

game_images = [rock, paper, scissors]
user_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors\n"))

if (user_choice >= 3 or user_choice < 0):
    print("You typed an invalid number, you lose!")
else:

    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)

    print("Computer chose: ")
    print(game_images[computer_choice])

    if (user_choice == 0 and computer_choice == 2):
        print("You Win!")
    elif computer_choice > user_choice:
        print("You Lose!")
    elif user_choice > computer_choice:
        print("You Win!")
    elif user_choice == computer_choice:
        print("It's a tie!")
    else:
        print("You typed an invalid number, you lose!")

    print(computer_choice)
