
rate_per_minute = [0.07, 0.12, 0.05]

RATE_CATEGORY = ["Daytime", "Evening", "Off-Peak"]
Category = []
Length = []
Cost =  []

COST = 0

def get_time_category():
    
    """Returns the time category from the usdr"""
    try: 
        user_choice = int(input("""Select the time of the phone call:  
            1. 6am to 5:59 pm
            2. 6pm to 11:59pm
            3. 12am to 5:59am
            4. End
            """))
    except ValueError:
        print("You must enter an integer")
    else:
        return user_choice

def display():
    print ("{:<10} {:<10} {:<10}".format('Category', 'Length', 'Cost'))
    for index in range(len(Category)):
        print("{:<10} {:<10} ${:<10.2f}".format(Category[index], Length[index],  Cost[index]))
    

def cal_call_cost():

    while True:
        user_choice= get_time_category()
        if user_choice == 4:
            display()
            return 
        if user_choice not in [1, 2, 3, 4]:
            print("Must enter 1, 2, or 3\n")
            continue 
            
        call_length = int(input("Enter the length of the call in minutes: "))
        if user_choice == 1:
            COST =  (rate_per_minute[user_choice-1])*call_length
            Category.append(RATE_CATEGORY[0])
            Cost.append(COST)
            Length.append(call_length)
            
            
        elif user_choice == 2:
            COST =  (rate_per_minute[user_choice-1])*call_length
            Category.append(RATE_CATEGORY[1])
            Cost.append(COST)
            Length.append(call_length)
            
            
        elif user_choice == 3:
            COST = (rate_per_minute[user_choice-1])*call_length
            Category.append(RATE_CATEGORY[2])
            Cost.append(COST)
            Length.append(call_length)
            
           
cal_call_cost()

