def user_login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Database connection and authentication logic here
    if username == "admin" and password == "password":
        return True
    else:
        return False