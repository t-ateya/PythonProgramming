user_name = {
    'bob':{
        "username": "Bob",
        "password": "ateya"
    }
}

def check_user(username, passw):
    user = user_name.get(username, None)
    if user and user['password'] == passw:
        return user

print(check_user("bob", "ateya"))