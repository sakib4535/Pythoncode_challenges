# Encapsulation

class mobile:

    def __init__(self):
        self.__maxprice = 30000  # private attributes that cant change

    def sell(self):
        print("Selling price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):   # setter function takes price as parameter
        self.__maxprice = price

m = mobile()
m.sell()

m.setMaxPrice(40000)
m.sell()

###############################################

class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Encapsulated attribute
        self.__balance = balance  # Encapsulated attribute

    def deposit(self, amount):
        self.__balance += amount  # Update balance attribute
        print(f"Deposit of {amount} successfully made. New balance is {self.__balance}.")

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount  # Update balance attribute
            print(f"Withdrawal of {amount} successfully made. New balance is {self.__balance}.")
        else:
            print(f"Insufficient funds. Balance is {self.__balance}.")

    def get_balance(self):
        return self.__balance  # Accessor method to get the balance attribute

    def get_account_number(self):
        return self.__account_number  # Accessor method to get the account number attribute

    def set_balance(self, balance):
        self.__balance = balance  # Mutator method to set the balance attribute

    def set_account_number(self, account_number):
        self.__account_number = account_number  # Mutator method to set the account number attribute


# Creating an instance of the BankAccount class
my_account = BankAccount("990-551-66890", 1000)

# Trying to access the encapsulated attribute directly (will result in an AttributeError)
# print(my_account.__balance)

# Accessing the encapsulated attribute using the accessor method
print(f"My account balance is {my_account.get_balance()}")
