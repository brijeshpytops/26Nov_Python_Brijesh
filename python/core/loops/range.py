"""
range(stop+1)
range(start, stop+1)
range(start, stop+1, step+1)
"""

# left to right:

# print(range(10)) # range(0, 10)  default start with zero
# print(range(1, 10)) # range(1, 10) start with given position
# print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list(range(1,11))) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list(range(1,11,2))) # [1, 3, 5, 7, 9]
# print(list(range(1,11,3))) # [1, 3, 5, 7, 9]
# print(list(range(-5,6)))

# right to left:
# print(list(range(0, -6, -1))) # step value must be negative
# print(list(range(0, -11, -2))) # step value must be negative
# print(list(range(0, -11, -3))) # step value must be negative