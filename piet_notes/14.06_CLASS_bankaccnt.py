class BankAccount:
    def __init__(self, bla) -> None:
        self.balance = bla

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount
    

my_bank = BankAccount(100)
# print(my_bank.balance)
my_bank.withdraw(1000)
# print(my_bank.balance)
my_bank.deposit(900)
# print(my_bank.balance)
        
class BankAccount2:
    def __init__(self, bla) -> None:
        self.balance = bla
        self.limit = -500

    def withdraw(self, amount):
        if self.balance - amount > self.limit:
            self.balance -= amount

    def deposit(self, amount):
        self.balance += amount
    

my_bank = BankAccount2(100)
print(my_bank.balance)
my_bank.withdraw(1000)
print(my_bank.balance)
my_bank.deposit(900)
print(my_bank.balance)

class BankAccount3:
    def __init__(self, bla) -> None:
        self.balance = bla
        self.limit = 0

    def withdraw(self, amount, limit):
        self.limit = limit
        if self.balance - amount > self.limit:
            self.balance -= amount
        else:
            print('limit reached')

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print('negatives not allowed')


my_bank = BankAccount3(100)
print(my_bank.balance)
my_bank.withdraw(1000, -600)
print(my_bank.balance)
my_bank.deposit(-900)
print(my_bank.balance)