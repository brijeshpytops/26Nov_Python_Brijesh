# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *


# num = 5
# for row in range(1, num+1):
#     for col in range(1,num+1):
#         print("*", end=" ")
#     print()


# *
# * *
# * * *
# * * * *
# * * * * *

# num = 5
# for row in range(1, num+1):
#     for col in range(1,row+1):
#         print("*", end=" ")
#     print()

# for num in range(6):
#     print("* "*num)


# * * * * *
# * * * *
# * * *
# * *
# *

# num = 5
# for row in range(1, num+1):
#     for col in range(1,num-row+2):
#         print("*", end=" ")
#     print()


# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *



# num = 5
# for row in range(1, num+1):
#     for col in range(1,row+1):
#         print("*", end=" ")
#     print()
# for row in range(1, num+1):
#     for col in range(1,num-row+1):
#         print("*", end=" ")
#     print()


# * * * * *
#   * * * *
#     * * *
#       * *
#         *


# num = 5
# for row in range(1, num+1):
#     for col in range(1,row):
#         print(" ", end=" ")
#     for col in range(1,num-row+2):
#         print("*", end=" ")
#     print()

#         *
#       * *
#     * * *
#   * * * *
# * * * * *


# num = 5
# for row in range(1, num+1):
#     for col in range(1,num-row+1):
#         print(" ", end=" ")
#     for col in range(1,row+1):
#         print("*", end=" ")
#     print()

# num = 6
# for row in range(num):
#     print(" "*(num-row),"*"*row)


#         *
#       * *
#     * * *
#   * * * *
# * * * * *
#   * * * *
#     * * *
#       * *
#         *


# num = 5
# for row in range(1, num+1):
#     for col in range(1,num-row+1):
#         print(" ", end=" ")
#     for col in range(1,row+1):
#         print("*", end=" ")
#     print()
# for row in range(1, num+1):
#     for col in range(1,row+1):
#         print(" ", end=" ")
#     for col in range(1,num-row+1):
#         print("*", end=" ")
#     print()


#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *



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



# digit's patterns

# 11111
# 00000
# 11111
# 00000
# 11111

num = 5

# for row in range(1, num+1):
#     for col in range(1, num+1):
#         if row % 2 == 0:
#             print("0", end=" ")
#         else:
#             print("1", end=" ")
#     print()

# 10101
# 10101
# 10101
# 10101
# 10101

# num= 5
# for row in range(1, num+1):
#     for col in range(1, num+1):
#         if col % 2 == 0:
#             print("0", end=" ")
#         else:
#             print("1", end=" ")
#     print()

# 1
# 22
# 333
# 4444
# 55555

# num= 5
# for row in range(1, num+1):
#     for col in range(1, row+1):
#         print(row, end=" ")
#     print()

# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15


# num= 5
# g_var = 1
# for row in range(1, num+1):
#     for col in range(1, row+1):
#         print(g_var, end=" ")
#         g_var += 1
#     print()


# alphabet's patterns

# 0-255 ASCII

# A - 65
# Z - 90

# a - 97
# z - 122

# print(chr(65))
# print(chr(90))
# print(chr(97))
# print(chr(122))


# A
# B C
# D E F
# G H I J
# K L M N O

# num= 5
# g_var = 1
# for row in range(1, num+1):
#     for col in range(1, row+1):
#         print(chr(g_var+64), end=" ")
#         g_var += 1
#     print()


# * * * * *
# *       *
# *       *
# *       *
# * * * * *

# num= 5
# for row in range(1, num+1):
#     for col in range(1, num+1):
#         if row == 1 or row == num or col == 1 or col == num:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# * * * * * * *
# *   *   *   *
# * * *   *   *
# *       *   *
# * * * * *   *
# *           *
# * * * * * * *

num = 3

# * * *
#  * 1 *
#   * * *
#   * * *
#  * 2 *
# * * *
# * * *
#  * 3 *
#   * * *
#   * * *
#  * 4 *
# * * *
# * * *
#  * 5 *
#   * * *


# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1


#     1 
#    1 2 
#   1 2 3 
#  1 2 3 4 
# 1 2 3 4 5


# 1 2 3 4 5
#  6 7 8 9
#   10 11 12
#    13 14
#     15


# * * * * * * * 
# * *       * * 
# *   *   *   * 
# *     *     * 
# *   *   *   * 
# * *       * * 
# * * * * * * *



# * * * * * 
#   *       * 
#     *       * 
#       *       * 
#         * * * * *
                         