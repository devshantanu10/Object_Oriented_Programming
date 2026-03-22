class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def acc_info(self):
        print(f"Owner: {self.owner}")
        print(f"Balance: {self.balance}")

    def deposit(self, amount):
       self.balance += amount
       print(f"Deposited{amount} . New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
           print("Insufficient balance")
           self.balance -= amount
        else:
            print(f"withdraw{amount}.New balance:{self.balance}")
        


b1 = BankAccount("Shantanu", 1000)
b1.acc_info()
b1.deposit(500)
b1.withdraw(5000)
b1.acc_info()