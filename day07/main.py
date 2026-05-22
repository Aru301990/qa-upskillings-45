from bank_account import BankAccount
from person import Person


# Bank Account Demo

account = BankAccount("Aruna", 1000)

account.deposit(500)

account.withdraw(300)

print("Current Balance:", account.get_balance())


print("\n------------------\n")


# Person Demo

person = Person("Aruna", 25)

person.introduce()

person.set_age(26)

print("Updated Age:", person.get_age())