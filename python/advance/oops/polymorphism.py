# method overloading
    # compile-time polymorphisum
        # - static binding
# method overriding
    # run-time polymorphisum
        # - dynamic binding

# class Math:
#     def add(self, a , b):
#         return a + b
    
#     def add(self, a, b, c):
#         return a + b + c
    
# obj = Math()

# print(obj.add(10, 20)) # TypeError: Math.add() missing 1 required positional argument: 'c'

# print(obj.add(10, 20, 30)) # 60


# class Math:
#     def add(self, *args):
#         return sum(args)
    
# obj = Math()

# print(obj.add(10, 20)) # 30

# print(obj.add(10, 20, 30)) # 60


    
# a = 10
# a = 20
# print(a)


# class Math1:
#     def info(self):
#         return "I am from parent class"
    
# class Math2(Math1):
#     def info(self):
#         print(super().info())
#         return "I am from child class"
    
# obj = Math2()

# print(obj.info()) # I am from child class
    
