"""

what is class or object ?

# class is a blueprint or template for creating objects. Objects are instances of a class.

class:
syntax:

class ClassName:
    block of code

object:
syntax:

object_name = ClassName()
"""

# name = "brijesh"
# age = 17

# def run():
#     return "I can run."

# print(name)
# print(age)
# print(run())

# class Person:
#     name = "brijesh"
#     age = 17

#     def run(yoyo):
#         return "I can run."
    
# b = Person()
    
# print(b.name)
# print(b.age)
# print(b.run())


# class Person:
#     name = input("Enter your name:")
#     age = int(input("Enter your age: "))

#     def run(yoyo):
#         return "I can run."
    
# b = Person()
    
# print(b.name)
# print(b.age)
# print(b.run())

# j = Person()
    
# print(j.name)
# print(j.age)
# print(j.run())


class Person:
    def __init__(self, name, age):
        self.n = name
        self.a = age

    def run(self):
        return "I can run."
    
# b = Person("brijesh", 27)
    
# print(b.n)
# print(b.a)
# print(b.run())

# j = Person("jay", 24)
    
# print(j.n)
# print(j.a)
# print(j.run())
# while True:
#     p = Person(input("Enter your name: "), int(input("Enter your age: ")))
#     print(p.n)
#     print(p.a)
#     print(p.run())

