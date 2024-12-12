"""
what are functions in python and their types:

Functions in Python are reusable blocks of code that perform a specific task. They take input parameters, perform a sequence of operations, and return a result. Functions can have different types, such as built-in functions, user-defined functions, and lambda functions.

Types of functions:

1. Built-in functions: These are predefined functions provided by Python and available for use without importing any module. Examples include print(), len(), type(), input(), range(), etc.

2. User-defined functions: These are functions defined by the programmer using the def keyword. They can take any number of input parameters and return a result.

3. Lambda functions: These are small anonymous functions that can be defined inline without using the def keyword. They are commonly used in combination with other functions to create more concise and readable code.

syntax:

def function_name(parameter1, parameter2,...):
    statements

function call
function_name(val1, val2,...)
"""

# num1 = 10
# num2 = 20
# total = num1 + num2
# print(total)

# num3 =  30
# num4 = 40
# total = num3 + num4
# print(total)

# def add(num1, num2):
#     # print(num1 + num2)
#     return num1 + num2

# add(10, 20)
# total = add(30, 40)
# print(total)

# def add(num1, num2, num3,num4):
#     return num1 + num2 + num3 + num4

# print(add(10,20,30, 40))

# function para types:
# 1] positional para/args

# def add(num1, num2, num3,num4):
#     return num1 + num2 + num3 + num4

# print(add(10,20,30)) # TypeError: add() missing 1 required positional argument: 'num4'


# 2] default/keyword parameters/arguments
# def bill(tomato, potato=30, book= 50):
#     return tomato + potato + book

# print(bill(50))
# print(bill(50,50))

# 3] variable length para/args
# *args
# **kwargs

# def add(*nums):
#     # print(type(nums))
#     print(sum(nums))

# add(10,20,30,40,50, 60, 70)

# def bill(**products):
#     # print(type(products))
#     total = 0
#     for key, value in products.items():
#         total += value
#     return total

# print(bill(tomato=50, potato=30, book=50, pen=500))

# add = lambda x,y,z:x+y+z
# print(add(10,20,30))




# num = 10 # global var
# def test():
#     global num
#     num = 20 
#     # num = 10 # local var
#     print(num)

# test()
# print(num)


# nums = [1,2,3,4,5,6,7,8,9,10]

# for index, num in enumerate(nums):
#     nums[index] = num*num

# print(nums)


# print(list(num*num for index, num in enumerate([1,2,3,4,5,6,7,8,9,10])))

# print(list(map(lambda num:num*num, [1,2,3,4,5,6,7,8,9,10])))

# nums = [1,2,3,4,5,6,7,8,9,10]

# def is_even(num):
#     return num % 2 == 0

# print(list(filter(is_even, nums)))

# print(list(filter(lambda num:num % 2 == 0, nums)))
# print(list(filter(lambda num:num % 2 != 0, nums)))


# def Outer_lower_func(func):
#     def Inner_lower_func():
#         res = func().lower()
#         print(res)
#         return res
#     return Inner_lower_func

# def Outer_upper_func(func):
#     def Inner_upper_func():
#         res = func().upper()
#         print(res)
#         return res
#     return Inner_upper_func
# @Outer_upper_func
# @Outer_lower_func
# def text():
#     return input("Enter a something: ")

# print(text())


