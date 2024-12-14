def user_register():
    """
    This function is used to register a new user.
    """
    print("Registration Form:")
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    confirm_password = input("Confirm your password: ")

    if password == confirm_password:
        print("Registration successful!")
    else:
        print("Passwords do not match. Please try again.")
        user_register()

    