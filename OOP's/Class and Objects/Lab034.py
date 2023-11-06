# Taking input from user

class Car:
    color=None
    model=None

    def car_details(self):
        print("Your car details is",self.color,self.model)


car_color = input("Enter your car color")
car_model = input("Enter your car model")


car_obj_ref = Car()
car_obj_ref.color=car_color
car_obj_ref.model=car_model

# obj ref we can call the function
car_obj_ref.car_details()