from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self, voice):
        pass

# obj = Animal() # Can't instantiate abstract class Animal without an implementation for abstract method 'sound'   


class Dog(Animal):
    def sound(self, voice):
        return f"{voice}"
    
class Cat(Animal):
    def sound(self, voice):
        return f"{voice}"
    

obj = Dog()
print(obj.sound("wof!"))

obj = Cat()
print(obj.sound("meow!"))