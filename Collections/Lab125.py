# Collection -

# list, dic, tuple, set, OrderedDict - Data Type

normal_tuple = (1, 2, 3)
# normal_tuple[1] = 4   # tuples are immutable

print(normal_tuple[0])


# Print details by using collections
from collections import namedtuple

Person = namedtuple("Person", ["name", "age", "gender"])


person = Person(name= "Krishna", age=25, gender="M")


print("Name", person.name)
print("Age", person.age)
print("Gender", person.gender)


# Print details by using class
class Person2:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def print_details(self):
        print(f"Person details {self.name} {self.age} {self.gender}")


person2 = Person2("Krishna", 25, "M")
person2.print_details()
