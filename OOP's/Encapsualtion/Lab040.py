# Public - Variable - Don't Mention anything
# Protected - _
# Private - __

# Variable and Function


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        if name == "Ram":
            print("Dont set the name")
        else:
            self.__name = name

    def print_details(self):
        print("Your details", self.__name, self.__age)


krishna = Person("Krishna", 25)  # It will call the  __init__ with name,age
print(krishna.get_name())
print(krishna.get_age())

krishna.print_details()
# print(krishna.__name)  # private cant access

# How to change it Get and Set ?
# Fetch - Get
# Set the value  - Constructor

krishna.set_name("Ram")

name1 = krishna.get_name()
print(name1)

krishna.print_details()
