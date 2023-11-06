class Person:
    def __init__(self):
        print("Can I Use You?")


    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("You Created an Object with name and age")


    def printDetails(self):
        print("your details are", self.name, self.age)


    def printDetails2(self):
        print("Your details are", self.name*2)


krishna = Person("krishna", 25)
krishna.printDetails()

ram = Person("ram", 28)
krishna.printDetails()

#  We can not use two constructors if we use also it will call only one constructor