# Car
# Objects - Tesla, Lambo

class Car:
    name = None
    color = None
    model = None
    speed = None
    engine_type = None

# self is a special variable that is used within the context of OOP.
# It is a reference to the instance of a class
# access and manipulate the attributes and methods of that reference

    def start(self):
        print("Starting")

    def drive(self):
        print("Drive")

    def car_break(self):
        print("Break")

    def who_is_driving(self):
        print("I am driving " + self.name)


tesla_obj_ref = Car()  # Instance of a class - Object
tesla_obj_ref.name = "Tesla"  # Instance of a class - Object

lambo_obj_ref = Car()
lambo_obj_ref.name = "Lambo"


tesla_obj_ref.who_is_driving()
lambo_obj_ref.who_is_driving()


