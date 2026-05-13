# Current Account Class
class CurrentAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")

        else:
            self.balance -= amount
            print("Withdrawal successful")
            print("Remaining balance:", self.balance)


# Example
current = CurrentAccount(1000)
current.withdraw(300)




# Savings Account Class
class SavingsAccount:
    def __init__(self, balance):
        self.balance = balance
        self.withdraw_limit = 100

    def withdraw(self, amount):
        if amount > self.withdraw_limit:
            print("Cannot withdraw more than $100")

        elif amount > self.balance:
            print("Insufficient balance")

        else:
            self.balance -= amount
            print("Withdrawal successful")
            print("Remaining balance:", self.balance)


# Example
savings = SavingsAccount(500)
savings.withdraw(50)
savings.withdraw(150)



# Normal Account Class
class NormalAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposit successful")
        print("Current balance:", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")

        else:
            self.balance -= amount
            print("Withdrawal successful")
            print("Remaining balance:", self.balance)


# Example
normal = NormalAccount(200)
normal.deposit(100)
normal.withdraw(50)
