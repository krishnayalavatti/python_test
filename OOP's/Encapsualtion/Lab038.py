class MyClass:

    def __int__(self):
        self.__private_toilet = "Private Toilet Only Allowed"
        self._protected_attribute = 42
        self.public_var = 55

    def __private_method(self):
        return "This is a private method."


obj = MyClass()
obj.public_var = 10
print(obj.public_var)
