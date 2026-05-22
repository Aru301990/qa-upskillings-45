class BankAccount:

    def __init__(self, account_holder, balance=0):

        self.account_holder = account_holder
        self.__balance = balance


    def deposit(self, amount):

        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")

        else:
            print("Invalid deposit amount")


    def withdraw(self, amount):

        if amount <= self.__balance:

            self.__balance -= amount
            print(f"Withdrawn: {amount}")

        else:
            print("Insufficient balance")


    def get_balance(self):
        return self.__balance   