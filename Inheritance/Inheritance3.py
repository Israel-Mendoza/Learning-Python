class Account:

    apr = 3.0

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        self.account_type = "Generic account"

    def calculate_interest(self):
        # The apr shown will be the class attribute, regardless of the instance info
        return f"Calculating interest on account {self.account_type}: {type(self).apr}"


class SavigsAccount(Account):

    apr = 5.0

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        self.account_type = "Savings account"


a = Account(10001, 500)
s = SavigsAccount(10002, 500)

# Expecting "3.0" as the apr.
print(a.calculate_interest())
# Expecting "5.0" as the apr
print(s.calculate_interest())

# Overriding the class apr attribute using an instance
# Do not do this!!!
s.__class__.apr = 1000
print(s.calculate_interest())

# Confirming that the class apr attribute has been overriden
s2 = SavigsAccount(12334, 1000)
print(s2.calculate_interest())
