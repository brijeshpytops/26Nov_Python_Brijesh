"""
foor loop in python:

theory:

for loop is used to iterate over a sequence (list, tuple, string) or other iterable objects. It allows you to perform a specific block of code for each item in the sequence.

syntax:

for variable in sequence:
    statements
"""

name = "python"
# for ch in name:
#     print(ch)

# for ch in name:
#     print(ch, end="")

# num = 10
# for num in range(1, num+1): 
#     print(num)


# num = 10
# for num in range(1, num+1): 
#     if num % 2 == 0:
#         print("even: ", num)
#     else:
#         print("odd: ", num)

# num = 5
# for row in range(1, num+1):
#     for col in range(1,num+1):
#         print("*", end=" ")
#     print()


# num = 5
# for row in range(1, num+1):
#     for col in range(1,row+1):
#         print("*", end=" ")
#     print()





# num = 5
# for row in range(1, num+1):
#     for col in range(1,row+1):
#         print("*", end=" ")
#     print()
# for row in range(1, num+1):
#     for col in range(1,num-row+1):
#         print("*", end=" ")
#     print()


# num = 5
# for row in range(1, num+1):
#     for col in range(1,row):
#         print(" ", end=" ")
#     for col in range(1,num-row+2):
#         print("*", end=" ")
#     print()


# num = 5
# for row in range(1, num+1):
#     for col in range(1,num-row+1):
#         print(" ", end=" ")
#     for col in range(1,row+1):
#         print("*", end=" ")
#     for col in range(1,row):
#         print("*", end=" ")
#     print()
# for row in range(1, num+1):
#     for col in range(1,row+1):
#         print(" ", end=" ")
#     for col in range(1,num-row+1):
#         print("*", end=" ")
#     for col in range(1,num-row):
#         print("*", end=" ")
#     print()

#        *
#       * *
#      * * *
#     * * * *
#    * * * * *
# num = 6
# for row in range(num):
#     print(" "*(num-row)," *"*row)

# for ch in "python":
#     print(ch)

# name = "python"

# ch = iter(name)

# print(next(ch))
# print(next(ch))
# print(next(ch))
# print(next(ch))
# print(next(ch))
# print(next(ch))
# print(next(ch))


# def simple_generator():
#     yield 1
#     yield 2
#     yield 3

# num = simple_generator()
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))