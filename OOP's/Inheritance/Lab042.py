# Parent - Child
# Father -> son
# GF -> F -> S
# 1BHK -> 1 BHK -> 1BHK

# Single Inheritance

class Animal:

    def speak(self):
        print("Animals can speak")


class Dog(Animal):
    pass


dog = Dog()
dog.speak()
