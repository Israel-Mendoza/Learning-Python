from Transaction import BankTransaction


class BankAccount:

    interest_rate = 1.05

    def __init__(self, first_name: str, last_name: str, account_number: int, initial_balance: float, preferred_tz):
        self._first_name = first_name
        self._last_name = last_name
        self._account_number = account_number
        self._transaction_list = []
        self._is_active = True
        self.preferred_tz = preferred_tz
        self._balance = 0
        self.deposit(initial_balance)

    @property
    def fist_name(self) -> str:
        """Account holder's first name"""
        return self._first_name

    @property
    def last_name(self) -> str:
        """Account holder's last name"""
        return self._last_name

    @property
    def full_name(self) -> str:
        """The account holder's full name"""
        return f"{self.fist_name} {self.last_name}"

    @property
    def account_number(self) -> int:
        """The account holder's account number"""
        return self._account_number

    @property
    def balance(self) -> float:
        """The balance in the account"""
        return float(self._balance)

    @property
    def preferred_tz(self):
        """The account holder's preferred timezone object"""
        return self._preferred_tz

    @preferred_tz.setter
    def preferred_tz(self, value):
        self._preferred_tz = value

    @property
    def transaction_list(self) -> list:
        """The account holder's transaction list"""
        return self._transaction_list

    def deposit(self, deposit_amount: float):
        """Adds the passed deposit_amount to the current instance balance"""
        if isinstance(deposit_amount, float) or isinstance(deposit_amount, int):
            deposit_amount = abs(float(deposit_amount))
            self._balance += deposit_amount
            self._transaction_list.append(
                BankTransaction(self.account_number, "Deposit", deposit_amount, self.preferred_tz)
            )
            print(f"${deposit_amount:.2f} successfully deposited to account no. {self.account_number}. "
                  f"Final balance: ${self.balance:.2f}")
        else:
            try:
                deposit_amount = abs(float(deposit_amount))
                self._balance += deposit_amount
                self._transaction_list.append(
                    BankTransaction(self.account_number, "Deposit", deposit_amount, self.preferred_tz)
                )
                print(f"${deposit_amount:.2f} successfully deposited to account no. {self.account_number}. "
                      f"Final balance: ${self.balance:.2f}")
            except ValueError:
                print(f"We are sorry, but the entered amount is not valid...")

    def withdraw(self, withdrawal_amount: float):
        """Withdraws the passed withdrawal_amount from the current instance balance"""
        if isinstance(withdrawal_amount, float) or isinstance(withdrawal_amount, int):
            withdrawal_amount = abs(float(withdrawal_amount))
            if withdrawal_amount < self.balance:
                self._balance -= withdrawal_amount
                self._transaction_list.append(
                    BankTransaction(self.account_number, "Withdrawal", withdrawal_amount, self.preferred_tz)
                )
                print(f"${withdrawal_amount:.2f} successfully withdrawn from account no. {self.account_number}. "
                      f"Final balance: ${self.balance:.2f}")
            else:
                print(f"Insufficient funds!!! Amount attempted: ${withdrawal_amount:.2f}")
                self._transaction_list.append(
                    BankTransaction(self.account_number, "X", withdrawal_amount, self.preferred_tz)
                )
        else:
            try:
                withdrawal_amount = abs(float(withdrawal_amount))
                if withdrawal_amount < self.balance:
                    self._balance -= withdrawal_amount
                    self._transaction_list.append(
                        BankTransaction(self.account_number, "Withdrawal", withdrawal_amount, self.preferred_tz)
                    )
                    print(f"${withdrawal_amount:.2f} successfully withdrawn from account no. {self.account_number}. "
                          f"Final balance: ${self.balance:.2f}")
                else:
                    print(f"Insufficient funds!!! Amount attempted: ${withdrawal_amount:.2f}")
                    self._transaction_list.append(
                        BankTransaction(self.account_number, "X", withdrawal_amount, self.preferred_tz)
                    )
            except ValueError:
                print(f"We are sorry, but the entered amount is not valid...")

    def apply_interest(self):
        self._balance *= self.interest_rate
        self._transaction_list.append(
            BankTransaction(self.account_number, "Applied Interest", 0, self.preferred_tz)
        )
        print(f"Applied interest on account no. {self.account_number}. Final balance: ${self.balance:.2f}")

    def __str__(self):
        """String representation of the bank account"""
        return f"Account information: {self.full_name} - Acc: {self.account_number} - " \
               f"Current balance: ${self.balance:.2f}"
