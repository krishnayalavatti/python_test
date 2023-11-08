class BankAccount:
    def __init__(self):
        self.balance = 0  # Instance Variable (You can access it cvia only Object)
        self.__private_var = 100

    def deposit(self, amount):  # Public function
        # self.balance = self.balance + amount
        self.balance += amount
        print("You deposited", self.balance)

    def _withdraw(self, amount):  # Protected
        self.balance -= amount
        print("You withdrawn", self.balance)

    def __show_balance(self):  # Private
        print("Your Bal", self.balance)

    def is_auth_true_show_bal(self, isAuth):
        if isAuth:
            self.__show_balance()
        else:
            print("You are not auth")


customer = BankAccount()
customer.deposit(100)
customer._withdraw(10)   # Dont use this, Its a Bad practice
# customer.__show_balance()  # we can't access private variables outside the class
# customer.is_auth_true_show_bal(True)
customer.is_auth_true_show_bal(False)

customer._BankAccount__private_var = 100  # Bad Practice in python
print(customer._BankAccount__private_var)
