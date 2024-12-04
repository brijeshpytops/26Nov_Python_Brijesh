"""
Dictionary : orederd, mutable, duplicate keys are not allowed, unindexed, slicing not allowed

syntax:

dict_name = {key1: value1, key2: value2, key3: value3...}

dict_name = dict()
"""

person = {
    "name": "John", 
    "age": 30, 
    "city": "New York"
    }

# print(person)
# print(person["name"])

# person["name"] = "brijesh"

# print(person)

contacts = {
    "John": ["1234567890", "6372686783"],
    "Jane": "9876543210",
    "Bob": {
        "home": "1234567890",
        "work": "9876543210"
    }
}

# print(contacts["John"][1])

# contacts["Jane"] = ["9876543210", "6372686783"]

# print(contacts["Bob"]["work"])

# p1 = {
#     "color":"black"
# }

# p2 = {
#     "name": "Jane",
#     "age": 28,
#     "city": "Los Angeles"
# }

# mDict = p1 + p2 # TypeError: unsupported operand type(s) for +: 'dict' and 'dict'

# print(mDict)

# mDict = {**p1, **p2}

# print(mDict)


# dictionary methods

# print(dir(contacts))

car = {
    "brand": "Toyota",
    "model": "Camry",
    "year": 2020
}

# print(car['brand'])
# print(car.get('model'))

# print(car.keys())
# print(car.values())
# print(car.items())

keys = list(car.keys())
values = list(car.values())

# for key in keys:
#     print(key)

# for value in values:
#     print(value)

# for key, value in car.items():
#     print(key, value)

# print(keys)
# print(values)

# print(list(zip(keys, values)))

# num1 = [1,2,3,4,5, 6,7,8,9]
# num2 = [11,22,33,44,55]
# num3 = [111,222,333,444,555]
# print(list(zip(num1, num2, num3)))

# car = {
#     "brand": "Toyota",
#     "model": "Camry",
#     "year": 2020,
#     # "color": "black"
# }

# car.pop('year')
# car.popitem()
# car.setdefault("color", "red")
# new_data = {'color': "red", "price": "20L"}
# car.update(new_data)
# print(car)

# items = ['tomato', 'potato', 'onion']
# price =  50

# products = {}

# print(products.fromkeys(items, price))

users = []
flag = True
while flag:
    user = {
        "name": input("Enter name: "),
        "age": int(input("Enter age: "))
    }
    users.append(user)
    choice = input("Do you want to add more users? (yes/no): ") 

    print(users)
    if choice.lower() == "yes":
        flag = True
    else:
        flag = False

