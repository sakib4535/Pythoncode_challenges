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

class PredatoryCreditCard(CreditCard):

    """This is and extension to Credit Card that compounds interest and fee"""

    def __init__(self, customer, bank, account, limit, apr):
        super().__init__(customer, bank, account, limit)
        self._apr = apr

    def charge(self, price):
        success = super().charge(price)
        if not success:
            self._balance += 5
        return success

    def process_month(self):
        if self._balance > 0:
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor

if __name__ == "__main__":
    cc1 = CreditCard("Hasnain Imtiaz", "Dhaka Savings", "4567 3452 7623 2121", 3500)
    cc2 = PredatoryCreditCard("Hasnain Imtiaz", "Baridhara Savings", "2131 4144 4121 5646", 13000, 0.0825)

    # Use Credit Card Intances
    for val in range(1,17):
        cc1.charge(val)
    print(f"Balance for {cc1.get_customer()} is {cc1.get_balance()}")
    while cc1.get_balance() > 100:
        cc1.make_payment(100)
        print(f"New Balance for {cc1.get_customer()} is {cc1.get_balance()}")
        cc2.process_month()
        print(f"Balance for {cc2.get_customer()} after processing a month is {cc2.get_balance()}")


