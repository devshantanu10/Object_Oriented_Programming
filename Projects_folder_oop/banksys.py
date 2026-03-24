class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def show_balance(self):
        print(f"{self.owner}'s Balance: {self.balance}")


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name):
        if name in self.accounts:
            print("Account already exists!")
        else:
            self.accounts[name] = BankAccount(name)
            print("Account created!")

    def get_account(self, name):
        return self.accounts.get(name, None)


# ---- Main Program ----
bank = Bank()

while True:
    print("\n1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter your name: ")
        bank.create_account(name)

    elif choice in ["2", "3", "4"]:
        name = input("Enter your name: ")
        account = bank.get_account(name)

        if not account:
            print("Account not found!")
            continue

        if choice == "2":
            amount = int(input("Enter amount: "))
            account.deposit(amount)

        elif choice == "3":
            amount = int(input("Enter amount: "))
            account.withdraw(amount)

        elif choice == "4":
            account.show_balance()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")