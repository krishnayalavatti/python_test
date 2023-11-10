# Abstraction - OOPs
# Hiding the details and showing the what is required

# hide the implementation and show only the important details

# to represent complex systems by simplifying and hiding unnecessary details

# ABC -> ? Abstract Base Class
# Abstract base Methods

from abc import ABC, abstractmethod


class Animal(ABC):
    # def __init__(self, name):
    #     self.name = name

    @abstractmethod
    def sound(self):
        pass


class Cat(Animal):
    def sound(self):
        return "Meow"


class Dog(Animal):
    def sound(self):
        return "Bow bo"


cat = Cat()
print(cat.sound())

dog = Dog()
print(dog.sound())
