def user_forgot_password():
    username = input("Enter your username: ")
    if username == "admin":
        password = input("Enter your password: ")
        if password == "password":
            print("Your password has been reset successfully.")
        else:
            print("Incorrect password. Please try again.")
    else:
        print("Invalid username. Please try again.")