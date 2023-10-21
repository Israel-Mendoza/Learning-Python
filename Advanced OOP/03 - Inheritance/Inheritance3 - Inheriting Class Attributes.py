from __future__ import annotations


class Account:

    apr: float = 3.0

    def __init__(self, account_number: int, initial_balance: int | float) -> None:
        self.account_number: int = account_number
        self.balance: int | float = initial_balance
        self.account_type: str = "Generic account"

    def calculate_interest(self) -> str:
        # The apr shown will be the class attribute, regardless of the instance info
        return f"Calculating interest on account {self.account_type}: {type(self).apr}"


class SavingsAccount(Account):

    # Class attribute is overriden:
    apr: float = 5.0

    def __init__(self, account_number: int, initial_balance: int | float) -> None:  # Deliberately missing super()
        self.account_number: int = account_number
        self.balance: int | float = initial_balance
        self.account_type: str = "Savings account"


a: Account = Account(10001, 500)
s: SavingsAccount = SavingsAccount(10002, 500)

# Expecting "3.0" as the apr.
print(a.calculate_interest())
# Calculating interest on account Generic account: 3.0

# Expecting "5.0" as the apr
print(s.calculate_interest())
# Calculating interest on account Savings account: 5.0

# Overriding the class apr attribute using an instance
# Do not do this!!!
s.__class__.apr = 1000
print(s.calculate_interest())
# Calculating interest on account Savings account: 1000

# Confirming that the class apr attribute has been overriden
s2: SavingsAccount = SavingsAccount(12334, 1000)

print(s2.calculate_interest())
# Calculating interest on account Savings account: 1000

# But the base class' apr property remains as 3.0:
print(a.calculate_interest())
# Calculating interest on account Generic account: 3.0
