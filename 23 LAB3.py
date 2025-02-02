class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must not be overdrawn.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance: {self.balance}")
            else:
                print("Insufficient funds! Withdrawal denied.")
        else:
            print("Withdrawal amount must not be overdrawn.")


owner_name = input("Enter the account owner's name: ")
initial_balance = float(input("Enter the initial balance: "))

account = Account(owner_name, initial_balance)

while True:
    print("\nChoose an option:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check balance")
    print("4. Exit")
    
    choice = input("Enter choice (1/2/3/4): ")

    if choice == '1':
        deposit_amount = float(input("Enter amount to deposit: "))
        account.deposit(deposit_amount)

    elif choice == '2':
        withdraw_amount = float(input("Enter amount to withdraw: "))
        account.withdraw(withdraw_amount)

    elif choice == '3':
        print(f"Current balance: {account.balance}")

    elif choice == '4':
        break

