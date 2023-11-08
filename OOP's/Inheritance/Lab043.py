# Single Inheritance - 90% we will use
# Use the properties, variables and methods of your base class or parent class by the sub class or child class


class Father:
    bank_bal = 100

    def one_bhk(self):
        print("Use it")


class Son(Father):
    pass


s = Son()
s.one_bhk()   # Accessing parent class method from child class object
print(s.bank_bal)  # Accessing parent class variable from child class object
