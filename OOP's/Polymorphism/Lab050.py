# Polymorphism - object-oriented programming (OOP)
# object -> behave differently based on the class.

class Shape:
    def area(self):
        print("Area of shape")


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        # return 2 * self.length + 2 * self.width
        super().area()


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


shape1 = Rectangle(2, 1)
# print(shape1.area())
shape1.area()

shape2 = Circle(4)
print(shape2.area())

shape3 = Shape()
shape3.area()
