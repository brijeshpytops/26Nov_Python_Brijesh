"""
What are operators and operands in python?

Operators are used to perform operations on variables/operands and values. They are classified into arithmetic, assignment, comparison, logical, bitwise, membership, and identity operators.

Arithmetic operators: +, -, *, /, //, %, **
Assignment operators: =, +=, -=, *=, /=, //=, %=, **=
Comparison operators: ==,!=, <, >, <=, >=
Logical operators: and, or, not
Membership operators: in, not in
Identity operators: is, is not
Bitwise operators: &, |, ^, ~, <<, >>


"""

# Arithmetic operators: +, -, *, /, //, %, **

# num1 = 10
# num2 = 20

# res = num1 + num2

# print("Addition:", res)

# res = num1 - num2

# print("Subtraction:", res)

# res = num1 * num2

# print("Multiplication:", res)

# num1 = 10
# num2 = 5
# res = num1 / num2

# print("Division:", res)

# res = num1 // num2

# print("Floor Division:", res)

# res = num1 % num2

# print("Modulus:", res)

# res = num1 ** num2

# print("Exponentiation:", res)

# Assignment/Shorthand operators: =, +=, -=, *=, /=, //=, %=, **=

# num = 10

# # num = num + 20
# num += 20
# print(num)

# num -= 20
# print(num)

# num *= 2

# print(num)

# num /= 2

# print(num)

# num //= 2

# print(num)

# num %= 2

# print(num)

# num **= 2

# print(num)

# Comparison operators: ==,!=, <, >, <=, >=

# num1 = 10
# num2 = 20

# print(num1 < num2) # True

# print(num1 > num2) # False

# print(num1 == num2) # False

# print(num1 != num2) # True

# print(num1 <= num2) # True

# print(num1 >= num2) # False


# Logical operators: and, or, not

# A B C and or
# T T T T   T
# F T T F   T
# T F T F   T
# T T F F   T
# F F F F   F

# A not
# T F
# F T


# c1 = True
# c2 = False
# c3 = 2 < 34.787 # True
# c4 = True and False or( 23.62876 < 27657) # True
# # print(c4)

# print(c1 and c2) # False

# print(c1 or c2) # True

# print(not c1) # False
# print(not c4) # False

# Membership operators: in, not in

# name = "Python"
# print("p" in name) # False

# print("P" in name) # True

# print('y' not in name) # False

# print("to" in name) # False

# print("tho" in name) # True

# Identity operators: is, is not

# - value must be same
# - datatype must be same
# - id must be same

# num1 = 10

# num2 = num1

# num3 = 10

# num4 = "10"

# print(num1 is num2) # True

# print(num1 is num3) # True

# print(num1 is not num4) # True


# Bitwise operators: &, |, ^, ~, <<, >> 

# print(3 & 5)
# print(3 | 5)
# print(3 ^ 5)
# print(~ 3)

# x = 7
# x = x << 2
# x = x << 3
# print(x)