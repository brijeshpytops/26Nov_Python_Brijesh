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

num = 5
for row in range(1, num+1):
    for col in range(1,row+1):
        print("*", end=" ")
    print()

for num in range(6):
    print("* "*num)


# * * * * *
# * * * *
# * * *
# * *
# *

num = 5
for row in range(1, num+1):
    for col in range(1,num-row+2):
        print("*", end=" ")
    print()


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


num = 5
for row in range(1, num+1):
    for col in range(1,row):
        print(" ", end=" ")
    for col in range(1,num-row+2):
        print("*", end=" ")
    print()

#         *
#       * *
#     * * *
#   * * * *
# * * * * *


num = 5
for row in range(1, num+1):
    for col in range(1,num-row+1):
        print(" ", end=" ")
    for col in range(1,row+1):
        print("*", end=" ")
    print()

num = 6
for row in range(num):
    print(" "*(num-row),"*"*row)


#         *
#       * *
#     * * *
#   * * * *
# * * * * *
#   * * * *
#     * * *
#       * *
#         *


num = 5
for row in range(1, num+1):
    for col in range(1,num-row+1):
        print(" ", end=" ")
    for col in range(1,row+1):
        print("*", end=" ")
    print()
for row in range(1, num+1):
    for col in range(1,row+1):
        print(" ", end=" ")
    for col in range(1,num-row+1):
        print("*", end=" ")
    print()


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
num = 6
for row in range(num):
    print(" "*(num-row)," *"*row)