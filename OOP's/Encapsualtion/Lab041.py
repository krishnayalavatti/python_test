class Password:

    def __init__(self, password):
        self.__password = password
        self.public_var = 10

    def get_password(self, is_auth):
        if is_auth:
            return self.__password
        else:
            print("Error")

    def set_password(self, password):
        if len(password) > 10:
            self.__password = password
        else:
            print("Weak Password")

    def print_len(self):
        print("Your password len is", len(self.__password))


pwd = Password("Groot")

print(pwd.public_var)

pwd.print_len()
psa = pwd.get_password(False)
print(psa)


# pwd.__password

pwd.set_password("IAmGroot")
pwd.print_len()
