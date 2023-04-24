"""
Problem: Create a simple banking system that consists of two classes, Account and Bank.
The Account class will represent a bank account with a balance, account number, and account holder name,
and will have methods to deposit and withdraw funds. The Bank class will manage multiple accounts,
and will have methods to create new accounts, get an account by account number, and calculate the total balance of all accounts.

"""

class Account:
    def __init__(self, account_number, account_holder, initial_balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient Fund")
        self.balance -= amount

# Define Bank Class

class Bank:

    def __init__(self):
        self.accounts = []
    def create_account(self, account_number, account_holder, initial_balance=0):
        account = Account(account_number, account_holder, initial_balance)
        self.accounts.append(account)
        return account
    def get_account(self, acount_number):
        for account in self.accounts:
            if account.account_number == acount_number:
                return account
        raise ValueError

    def total_balance(self):
        total = 0
        for account in self.accounts:
            total += account.balance
        return total

# Create a bank object and some accounts
bank = Bank()
account1 = bank.create_account(123, "Shah", 1000)
account2 = bank.create_account(456, "Poran", 500)

# Deposit and withdraw funds from the accounts
account1.deposit(500)
account2.withdraw(200)

# Print the account details and total balance
print(account1.account_holder, account1.balance)
print(account2.account_holder, account2.balance)
print("Total balance:", bank.total_balance())
