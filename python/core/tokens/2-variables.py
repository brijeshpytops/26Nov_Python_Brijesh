"""
What is variable in python?

Variable is a named storage location used to store data values. They are declared with a specific data type, and their values can be changed. Variables in Python are dynamically typed, meaning they can hold values of different data types during their lifetime.

syntax of variable:

variable_name = value

Here are some examples of variables in Python:

1. Integer variable: int_var = 10
2. Floating-point variable: float_var = 3.14
3. String variable: str_var = "Hello, World!"
4. Boolean variable: bool_var = True or False

In this code, we have defined four variables: int_var, float_var,bool_var, and str_var. We assigned the values 10, 3.14,  "Hello, World!" and True respectively to these variables.
"""

# num = 10
# num = 20
# print(num)

# num1 = 10
# num2 = 10

# print(id(num1))
# print(id(num2))

# num1 = num2 = 10
# print(num1, num2)

# num1, num2 = 10, 20
# print(num1, num2)

# num1 = int(input("Enter a num1: ")) # always return value as a string by default
# num2 = int(input("Enter a num2: "))
# print(num1, num2) # 10 20
# print(type(num1), type(num2)) # <class 'int'> <class 'int'>

num1, num2= input("Enter a num1 and num2 sep by '|' ").split('|')

# Enter a num1 and num2 sep by '|' 1020 # ValueError: not enough values to unpack (expected 2, got 1)

# Enter a num1 and num2 sep by '|' 10|20
print(num1)
print(num2) 
10
20