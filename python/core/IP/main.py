# task-1] create a function to convert text into another patterns

# Example:

# enter something: PytHOn TeCHNoloGY
# 1. create a function to conver givent text into the lower_case: python technology
# 2. create a function to conver givent text into the upper_case: PYTHON TECHNOLOGY
# 3. create a function to conver givent text into the title_case: Python Technology
# 4. create a function to conver givent text into the capitalize_case: Python technology
# 5. create a function to conver givent text into the swap_case: pYThoN tEchnOLOgy

# hint: 
# print(chr(65))
# print(ord('A'))

# Task - 2: calculate length of any iterable object without using any built-in functions

# Task - 3: create a function for bus ticket generation


# text = "python TechNOlogy"

# def UpperCase(ch):
#     if (ord(ch) >= 97 and ord(ch) <= 122):
#         return chr(ord(ch) - 32)
    
# def LowerCase(ch):
#     if ord(ch) >= 65 and ord(ch) <= 90:
#         return chr(ord(ch) + 32)
    
# swapcase = ""

# for ch in text:
#     if ord(ch) >= 65 and ord(ch) <= 90:
#         swapcase += LowerCase(ch)
#     elif (ord(ch) >= 97 and ord(ch) <= 122):
#         swapcase += UpperCase(ch)
#     else:
#         swapcase += ch

# print(swapcase)


# def TitleCase(text):
#     words = text.split(" ")
#     for index, word in enumerate(words):
#         words[index] = words[index].capitalize()
#     return " ".join(words)


# text = input("Enter a text")

# print(TitleCase(text))
