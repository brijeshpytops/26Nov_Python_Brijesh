"""
What is list in python?

List : Ordered, Mutable, Duplicates value are allowed, indexing and slicing

List is a collection of items in Python. Lists are ordered, changeable, and allow duplicate values. Lists in Python are denoted by square brackets [].

syntax:

list_name = [item1, item2, item3...]
list_name = list()
"""

# nums = [1,2,3,4]
# print(len(nums))

# print(type(nums))

# nums = list()
# print(type(nums))


# int array_name[size] = { val1, val2, ...valn};

# mix_list = [10, 20, 34.567, 'python', 243 + 87j, (12+4+45*456)]

# print(mix_list)


# Access elements of a list

vegs = [
    'carrot',  # 0 -6
    'potato',  # 1 -5
    'onion',   # 2 -4
    'tomato',  # 3 -3
    'pepper',  # 4 -2
    'garlic'   # 5 -1
]

# print(vegs)

# Indexing (+/-)
# print(vegs[3])
# print(vegs[4])
# print(vegs[-1])
# print(vegs[-1+3])

# Slicing ([:], [start:], [start:end], [start:end:step]) (+/-)


# print(vegs[:])
# print(vegs[2:])
# print(vegs[1:4])
# print(vegs[::2])

# print(vegs[-1:-4:-1])

mummy = ['milk', 'butter-milk', 'tomato', 'onion']
aunty = mummy * 2 # replica
my_list = ['drinks']
sister = ['chocolate']

mix_list = mummy + aunty + my_list + sister # concat
# print(mix_list)

# List methods
nums = [1,2,3,4,5]
# print(dir(nums))


nums = [1,2,3,4,5]
new_nums = [5,6,7,8,9,10]

# Add
# nums.append(new_nums) # [1, 2, 3, 4, 5, [5, 6, 7, 8, 9, 10]]
# nums.extend(new_nums) # [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10]
# nums.insert(2, new_nums) # [1, 2, [5, 6, 7, 8, 9, 10], 3, 4, 5]

# update
# nums[2] = 33

# delete

# del nums[2]
# nums.clear()
# nums.pop()
# nums.pop(2)
# nums.remove(5)

# print(nums.index(5))

# nums = [1,2,1,2,3,4,5,1,3,4,1,4,1,6,1,4,1,1]
# print(nums.count(1))
# nums.reverse()
# nums.sort()
# nums.sort(reverse=True)
# print(nums)

# nums = [1,2,3,4,5]
# copy_nums = nums
# copy_nums1 = nums.copy()

# print(id(nums))
# print(id(copy_nums))
# print(id(copy_nums1))

# nums = [
#     1,2,3,4,5,
#      [6,7,8,9,[
#          [10,11,12,13,14,15]
#      ]]
# ]

# print(nums[-1])
# print(nums[-1][-1])
# print(nums[-1][-1][-1])
# print(nums[-1][-1][-1][-1])



