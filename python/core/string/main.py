"""
What is string in python?

String is a sequence of characters enclosed in single quotes, double quotes, or triple quotes. Strings in Python are immutable, meaning their values cannot be changed once they are created.

"""

str_name = 'python'
str_name = "python"
str_name = """python"""
str_name = '''python'''

# print(type(str_name))
# print(len(str_name))

# string element accessing

# indexing (+/-)

# print(str_name[0])

# slicing ([:], [start:stop-1], [start:stop-1:step-1])

# print(str_name[:3])
# print(str_name[2:])
# print(str_name[2:5])
# print(str_name[::-1])
# print(str_name[::2])

# string concatenation (+)

# fname = "brijesh"
# lname = "gondaliya"

# fullname = fname + " " + lname

# print(fullname)

# string replica

# star = "*" * 3
# print(star)

# for ch in "python":
#     print(ch)

# string methods 

# print(dir(""))

name = "ToPS TecHNoloGY Pvt. LTd."

# print(name.lower())
# print(name.upper())
# print(name.capitalize())
# print(name.title())
# print(name.swapcase())


# print(name.startswith("TOP"))

# print(name.endswith("Ltd."))


# print(name.find("Tec"))

# print(name.index("Tec"))

# print(name.replace("Tec", "Tech"))

# print(name.count("Tec"))

# print(name.split())

# password = "#@$#^&%"

# print(password.isalnum())
# print(password.isalpha())
# print(password.isdigit())
# print(not password.isalnum())

# string formatting

name = "java"
price = 34.5666
pages = 300
# print("book name is python and book price is 34.5666 and total pages is 300")
# print(f"book name is {name} and book price is {price} and total pages is {pages}")
# print("book name is {} and book price is {} and total pages is {}".format(name, price, pages))
# print("book name is {1} and book price is {0} and total pages is {2}".format(name, price, pages))
# print("book name is %s and book price is %.2f and total pages is %d" % (name, price, pages))


# Task:

technologies = [
    "python",
    "java",
    "javascript",
    "c++",
    "ruby",
    "swift",
    "go",
    "php",
    "rust"
    "kotlin",
    "perl",
    "haskell"
]
# ("tech_name", total_length, vowel_length, consonent_length, speicel_symbol_length)
# data = [
#     ("python", 6, 1, 5, 0),
#     ("java", 4, 2, 2, 0),
#     ("javascript", 10, 2, 8, 0),
#     ("c++", 3, 1, 2, 0),
#     ("ruby", 4, 1, 3, 0),
#     ("swift", 4, 2, 2, 0),
#     ("go", 2, 1, 1, 0),
#     ("php", 3, 1, 2, 0),
#     ("rust", 4, 1, 3, 0),
#     ("kotlin", 5, 2, 3, 0),
#     ("perl", 4, 1, 3, 0),
#     ("haskell", 7, 2, 5, 0)
# ]