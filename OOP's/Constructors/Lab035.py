#  Constructors

class Car:
    name = "Thor"  # Class Variable

    def __init__(self, make, model):  # Default Constructor
        self.make = make  # Instance Variable
        self.model = model  # Instance Variable
        # print("I am First", self.name)
        print("I am First")

    def start_engine(self):
        # print("Starting a car", self.make, self.model)
        print("Starting a car", self.make,self.model)


car1 = Car("TATA", "Nexon")
car2 = Car("Mahindra", "Thor")
car1.start_engine()  # With Instance Variable
car2.start_engine()

# car1 = Car()
# car1.start_engine()  # With class Variable


# print(id(car1))
# print(id(car2))

#  Object is created a Special Function is called automatically __int__()
#  All the attribute Object you can initilize - add some initial value to them