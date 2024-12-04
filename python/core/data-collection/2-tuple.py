"""
What is tuple in python?

Tuple : Ordered, Immutable, Duplicates value are allowed, indexing and slicing

Tuple is a collection of items in Python. Unlike lists, tuples are immutable, meaning they cannot be changed after they are created. Tuples in Python are denoted by parentheses ().

syntax:

tuple_name = (item1, item2, item3...)

tuple_name = tuple()

comma_tuple = 10,23

"""

# nums = (1,2,3,4,5)
# nums = tuple()
# nums = 10,
# print(type(nums))

# Access elements of a tuple

# nums = (1,2,3,4,5)

# print(nums[0]) # 1

# print(nums[-1]) # 5

# Slicing a tuple

# print(nums[1:3]) # (2, 3)

# print(nums[::-1]) # (5, 4, 3, 2, 1)

# Concatenation of tuples

# nums1 = (1,2,3)
# nums2 = (4,5,6)

# print(nums1 + nums2) # (1, 2, 3, 4, 5, 6)

# Immutable nature of tuples

# nums[0] = 10 # This will give error as tuples are immutable

# print(nums)

# nums = [1,2,3,4,5]

# t_nums = tuple(nums)

# print(t_nums)

# nums = (1,2,3,4,5)
# l_nums = list(nums)
# l_nums[1] = 22
# print(tuple(l_nums))