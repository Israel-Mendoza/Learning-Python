from time import sleep as timer
from random import choice, randint
import pytz
from datetime import datetime


class BankAccount:
    _interest_rate = 1.05
    _transaction_id = 5000100

    def __init__(self, account_number, fname, lname, user_tz):
        self._account_number = account_number
        self._fname = fname
        self._lname = lname
        self._full_name = None
        self._tz = user_tz
        self._balance = 0

    @classmethod
    def get_txn_id(cls):
        return cls._transaction_id

    @classmethod
    def add_txn(cls):
        cls._transaction_id += 1

    @property
    def account_number(self):
        return self._account_number

    @property
    def first_name(self):
        return self._fname

    @first_name.setter
    def first_name(self, new_fname):
        """Sets the _fname attribute and clears the cached _full_name one"""
        if isinstance(new_fname, str) and len(new_fname) > 0:
            setattr(self, "_fname", new_fname)
            self._full_name = None

    @property
    def last_name(self):
        return self._lname

    @last_name.setter
    def last_name(self, new_lname):
        """Sets the _lname attribute and clears the cached _full_name one"""
        if isinstance(new_lname, str) and len(new_lname) > 0:
            setattr(self, "_lname", new_lname)
            self._full_name = None

    @property
    def full_name(self):
        if self._full_name:
            return self._full_name
        else:
            setattr(self, "_full_name", f"{self.first_name} {self.last_name}")
            return self._full_name

    @property
    def tz(self):
        return self._tz

    @tz.setter
    def tz(self, user_tz):
        """
        Changes the tz of the account instance
        Args:
            tz_offset [int]: The time offset in hours
            tz_name [str] The desired name of the timezone
        """
        self._tz = user_tz

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        """
        Deposit method adds the passed amount to the balance attribute
        Args:
            amount [float]: The amount to be added to the balance.
                            A positive number
        Return:
            A Transaction object with the transaction information.
        """
        type(self).add_txn()
        dt_str = datetime.now(pytz.utc).strftime('%Y%m%d%H%M%S')
        txn_id = type(self).get_txn_id()
        if amount > 0:
            print(f"Depositing ${float(amount):.2f} to account {self.account_number}")
            self._balance += amount
            txn_confirmation = f"D-{self.account_number}-{dt_str}-{txn_id}"
        else:
            print("Deposits must be positive amounts only!")
            txn_confirmation = f"X-{self.account_number}-{dt_str}-{txn_id}"
        return txn_confirmation

    def withdraw(self, amount):
        """
        Withdraw method subtracts the passed amount from the balance attribute
        if the balance is greater.
        Args:
            amount [float]: The amount to be subtracted from the balance.
                            A positive number lesser than the balance.
        Return:
            A Transaction object with the transaction information.
        """
        type(self).add_txn()
        dt_str = datetime.now(pytz.utc).strftime('%Y%m%d%H%M%S')
        txn_id = type(self).get_txn_id()
        if 0 < amount < self.balance:
            print(f"Withdrawing  ${float(amount):.2f} from account {self.account_number}")
            self._balance -= amount
            txn_confirmation = f"W-{self.account_number}-{dt_str}-{txn_id}"
        elif amount > self.balance:
            print(f"Unable to withdraw amount from account {self.account_number}. Insufficient funds!")
            txn_confirmation = f"X-{self.account_number}-{dt_str}-{txn_id}"
        else:
            print(f"Unable to withdraw a negative amount. Please try again...")
            txn_confirmation = f"X-{self.account_number}-{dt_str}-{txn_id}"
        return txn_confirmation

    def apply_interest(self):
        """
        Apply Interest method applies the class defined interest rate to the account by multipying the balance by the rate.
        Return:
            A Transaction object with the transaction information.
        """
        type(self).add_txn()
        dt_str = datetime.now(pytz.utc).strftime('%Y%m%d%H%M%S')
        txn_id = type(self).get_txn_id()
        return f"I-{self.account_number}-{dt_str}-{txn_id}"

    @staticmethod
    def transaction_lookup(txn_id, user_tz):
        txn_type, acc_num, dt_str, txn_num = txn_id.split("-")
        dt_obj = datetime.strptime(dt_str, "%Y%m%d%H%M%S").replace(tzinfo=pytz.utc)
        return Transaction(txn_type, acc_num, dt_obj, user_tz, txn_num)


class Transaction:

    def __init__(self, txn_type, account_num, dt_utc_obj, tz_obj, txn_num):
        self._txn_type = {"D": "Deposit",
                          "W": "Withdrawal",
                          "I": "Applied Interest",
                          "X": "Declined transaction"}[txn_type]
        self._account_num = account_num
        self._tz = tz_obj
        self._dt_local_obj = dt_utc_obj.astimezone(tz_obj)
        self._txn_num = txn_num

    @property
    def account_number(self):
        return self._account_num

    @property
    def transaction_code(self):
        return self._txn_type

    @property
    def transaction_id(self):
        return self._txn_num

    @property
    def time(self):
        dt_str = self._dt_local_obj.strftime('%Y-%m-%d %X')
        return f"{dt_str} ({self._tz})"

    def display_transaction(self):
        print(f"Account #{self.account_number}")
        print(f"Transaction #{self.transaction_id}: {self.transaction_code}")
        print(f"Local time: {self.time}")


preferred_tz = pytz.timezone("Europe/Moscow")

my_account = BankAccount(39294021, "Israel", "Mendoza", preferred_tz)

f1 = my_account.deposit
f2 = my_account.withdraw
f3 = my_account.apply_interest

f_list = [f1, f2, f3]
txn_list = []

for i in range(20):
    temp_f = choice(f_list)
    txn = None
    if temp_f.__name__ in ["deposit", "withdraw"]:
        txn = temp_f(randint(1, 10000))
        print(txn)
        txn = BankAccount.transaction_lookup(txn, preferred_tz)
        txn_list.append(txn)
    else:
        txn = temp_f()
        print(txn)
        txn = BankAccount.transaction_lookup(txn, preferred_tz)
        txn_list.append(txn)
    timer(0.3)

print(f"\nFinal balance: {my_account.balance}\n")

for t in txn_list:
    t.display_transaction()
    print()


