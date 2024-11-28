"""
what is datatypes in python?

Datatypes in Python are the different types of data that can be stored in variables. There are several built-in data types in Python, such as integers, floats, complex, strings, lists, tuples, dictionaries, sets,range and None. Each data type has its own specific characteristics and operations that can be performed on it.

Syntax of datatypes:
var_name = value

"""

# Example of different data types in Python:

# Integer data type: 
int_var = 10
print(type(int_var)) # <class 'int'>

# Float data type:
float_var = 10.5
print(type(float_var)) # <class 'float'>

# Complex data type:
complex_var = 10 + 5j
print(type(complex_var)) # <class 'complex'>

# String data type:

string_var = "Hello, World!"
print(type(string_var)) # <class 'str'>

# List data type:

list_var = [1, 2, 3, 4, 5]
print(type(list_var)) # <class 'list'>

# Tuple data type:

tuple_var = (1, 2, 3, 4, 5)
print(type(tuple_var)) # <class 'tuple'>

# Dictionary data type:

dict_var = {"name": "John", "age": 30}
print(type(dict_var)) # <class 'dict'>

# Set data type:

set_var = {1, 2, 3, 4, 5}
print(type(set_var)) # <class 'set'>

# Range data type:

range_var = range(1, 11)
print(type(range_var)) # <class 'range'>

# None data type:

none_var = None
print(type(none_var)) # <class 'NoneType'>


# Example of type casting:

# Implicit type conversion

x = 10
y = 20.345634
z = x + y

print(z) # 30.345634

# Explicit type conversion

# x = 10
# y = str(x)
# print(type(y))

# num = "10"
# y = int(num)
# print(type(y))

num = "67dsmhgkhj"
y = float(num)
# print(y) # ValueError: could not convert string to float: '67dsmhgkhj'