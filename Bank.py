import random

# Initialize a dictionary to store user account information
accounts = {}

class BankAccount:
    def __init__(self, account_number, owner, balance=0.0, passcode=""):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        self.passcode = passcode

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount, passcode):
        if amount > 0 and amount <= self.balance and passcode == self.passcode:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance

# Function to create a new bank account
def create_account():
    account_number = str(random.randint(100000, 999999)) # Generate a 6-digit account number
    while account_number in accounts:
        account_number = str(random.randint(100000, 999999)) # Ensure uniqueness
    owner = input("Enter your name: ")
    passcode = input("Enter a passcode for your account: ")
    initial_balance = float(input("Enter initial balance: $"))
    account = BankAccount(account_number, owner, initial_balance, passcode)
    accounts[account_number] = account
    print(f"Account created successfully. Your account number is: {account_number}")

# Function to perform a deposit
def deposit():
    account_number = input("Enter your account number: ")
    if account_number in accounts:
        account = accounts[account_number]
        amount = float(input("Enter the deposit amount: $"))
        if account.deposit(amount):
            print(f"Deposit of ${amount} was successful. New balance: ${account.get_balance()}")
        else:
            print("Invalid deposit amount.")
    else:
        print("Account not found.")

# Function to perform a withdrawal
def withdraw():
    account_number = input("Enter your account number: ")
    if account_number in accounts:
        account = accounts[account_number]
        passcode = input("Enter your passcode: ")
        amount = float(input("Enter the withdrawal amount: $"))
        if account.withdraw(amount, passcode):
            print(f"Withdrawal of ${amount} was successful. New balance: ${account.get_balance()}")
        else:
            print("Invalid passcode, insufficient funds, or invalid withdrawal amount.")
    else:
        print("Account not found.")

# Function to check account balance
def check_balance():
    account_number = input("Enter your account number: ")
    if account_number in accounts:
        account = accounts[account_number]
        print(f"Account balance for {account.owner}: ${account.get_balance()}")
    else:
        print("Account nor found.")

# Main Loop
while True:
    print("\nBank Menu:")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Quit")

    choice = input("Select an option (1/2/3/4/5): ")

    if choice == "1":
        create_account()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        check_balance()
    elif choice == "5":
        print("Thank you for using our bank program. Have a good day!")
        break
    else:
        print("Invalid choice. Please select a valid option.")