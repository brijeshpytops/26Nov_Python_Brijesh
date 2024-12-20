"""
What is encapsulation int python?

Encapsulation is the bundling of data and methods into a single unit called an object. It is the process of hiding the internal implementation details of an object and only exposing its public interface. This allows developers to work with objects in a more intuitive and organized manner.

Advantages of encapsulation:

1. Encapsulation provides a level of protection against unauthorized modifications and access to the object's data.
2. It promotes code reusability and reduces the likelihood of bugs.
3. It improves code maintainability and readability by hiding complex implementation details.

"""

# class ATM:
#     def __init__(self, card_number, pin): 
#         self.card_number = card_number # Public
#         self.__pin = pin # Private
#         self.__balance = 0

#     def display_data(self):
#         print(f"Card Number: {self.card_number}")
#         print(f"Pin: {self.__pin}")
#         print(f"Balance: {self.__balance}")

# brijesh = ATM(11111, 1234)
# brijesh.display_data()
# print(brijesh.__pin) # AttributeError: 'ATM' object has no attribute '__pin'
# print(brijesh._ATM__pin) # using Namemangling system
