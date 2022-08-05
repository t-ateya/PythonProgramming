users = [
        (0, "Bob", "password"),
        (1, "Rolf", "bob123"),
        (2, "Jose", "longpassword"),
        (3, "username", "1234")
]


user_mapping = {user[1]:user for user in users}

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")
_, username, password = user_mapping[username_input]

if password_input == password :
    print("Your details are correct")
else:
    print("Your details are incorrect")

#print(user_mapping["Bob"])