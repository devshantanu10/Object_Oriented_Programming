class Bank_Account:
    def __init__(self, owner , balance = 0):
        self.owner = owner
        self.balance = balance
    
    def account_info(self):
        print(f"Owner: {self.owner}")
        print(f"Balance: {self.balance}")
    
    def deposit(self, amount):
        self.balance += amount





        