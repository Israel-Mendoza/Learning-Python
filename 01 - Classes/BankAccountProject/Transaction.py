import pytz
from datetime import datetime


class BankTransaction:

    txn_start = 1000

    def __init__(self, bank_account_number: int, txn_type: str, amount: float, preferred_tz):
        BankTransaction.txn_start += 1
        self.bank_account_number = bank_account_number
        self.transaction_type = txn_type
        self._amount = amount
        self._txn_time = datetime.now(pytz.utc)
        self._id = BankTransaction.txn_start
        self._preferred_tz = preferred_tz

    @property
    def bank_account_number(self):
        """The Bank Account where the Transaction was triggered"""
        return self._bank_account_number

    @bank_account_number.setter
    def bank_account_number(self, value: int):
        if isinstance(value, int):
            self._bank_account_number = value
        else:
            raise ValueError("Bank Account must be a valid BankAccount number")

    @property
    def transaction_type(self):
        """The type of the transaction"""
        return self._type

    @transaction_type.setter
    def transaction_type(self, value: str):
        value = value.strip().lower()
        if "deposit" in value:
            self._type = 'D'
        elif "with" in value:
            self._type = 'W'
        elif "interest" in value:
            self._type = 'I'
        else:
            self._type = 'X'

    @property
    def amount(self):
        """The amount of the transaction in positive number"""
        return self._amount

    @amount.setter
    def amount(self, value: float):
        self._amount = abs(value)

    @property
    def transaction_id(self) -> str:
        """The transaction ID code"""
        date = f"{self._txn_time.year}{self._txn_time.month}{self._txn_time.day}"
        time = f"{self._txn_time.hour}{self._txn_time.minute}{self._txn_time.second}"
        txn_id = f"{self.transaction_type}-{self.bank_account_number}-{date}{time}"
        return txn_id

    def __repr__(self):
        if self.transaction_type == "D":
            return f"Deposit on account {self.bank_account_number} on " \
                   f"{self._txn_time.astimezone(self._preferred_tz)}"
        elif self.transaction_type == "W":
            return f"Withdrawal from account {self.bank_account_number} on " \
                   f"{self._txn_time.astimezone(self._preferred_tz)}"
        elif self.transaction_type == "I":
            return f"Applied Interest on account {self.bank_account_number} on " \
                   f"{self._txn_time.astimezone(self._preferred_tz)}"
        else:
            return f"Unsuccessful transaction on account {self.bank_account_number} on " \
                   f"{self._txn_time.astimezone(self._preferred_tz)}"
