class CreditCard:

    def __init__(self, customer, bank, account, limit):
        """

        :param customer: the name of customer
        :param bank: the name of the bank
        :param account: account identifier.
        :param limit: credit limit(dollars)

        """

        self._customer = customer
        self._bank = bank
        self._account = account
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        return self._customer

    def get_bank(self):
        return self._bank
    def get_account(self):
        return self._account

    def get_limit(self):
        return self._limit

    def get_balance(self):
        return self._balance

    def charge(self, price):
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        self._balance -= amount


if __name__ == "__main__":

    wallet = []
    wallet.append(CreditCard("Hasnain Imtiaz", "dhaka Savings", "4567 3452 7623 2121", 3500))
    wallet.append(CreditCard("Hasnain Imtiaz", "baridhara Savings", "2131 4144 4121 5646", 13000))
    wallet.append(CreditCard("Hasnain Imtiaz", "Forex Savings", "6543 5354 6543 6331", 7000))

    for val in range(1,17):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)

    for c in range(3):
        print("Customer= ", wallet[c].get_customer())
        print("Bank= ", wallet[c].get_bank())
        print("Account= ", wallet[c].get_account())
        print("Limit= ", wallet[c].get_limit())
        print("Balance = ", wallet[c].get_balance())
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print("Your Account Have New Balance= ", wallet[c].get_balance())
        print()




