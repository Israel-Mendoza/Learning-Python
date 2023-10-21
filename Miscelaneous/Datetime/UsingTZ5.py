import pytz
from datetime import datetime


class Transaction:

    def __init__(self, txn_type, acc_num, dt_utc, txn_num, preferred_tz):
        self._transaction_type = {
            "D": "Deposit",
            "W": "Withdrawal",
            "I": "Applied Interest",
            "X": "Declined transaction"}[txn_type]
        self._account_number = acc_num
        self._local_datetime = dt_utc.replace(tzinfo=pytz.utc).astimezone(tz=preferred_tz)
        self._transaction_number = txn_num

    @property
    def transaction_type(self):
        return self._transaction_type

    @property
    def account_number(self):
        return self._account_number

    @property
    def local_time(self):
        return self._local_datetime

    @property
    def local_time_str(self):
        return f'{self._local_datetime.strftime("%A %B %d, %Y")} at ' \
               f'{self._local_datetime.strftime("%I:%M:%S %p")}'

    @property
    def transaction_number(self):
        return self._transaction_number

    def display_transaction(self):
        print(f'Account #{self.account_number}')
        print(f'Transaction #{self.transaction_number}: "{self.transaction_type}"')
        print(f'Local time: {self.local_time_str}')


def txn_look_up(txn_code, preferred_tz):
    txn_type, acc_num, dt_str, txn_num = txn_code.split("-")
    dt_utc = datetime.strptime(dt_str, "%Y%m%d%H%M%S")
    return Transaction(txn_type, acc_num, dt_utc, txn_num, preferred_tz)


my_tz = pytz.timezone("America/Mexico_City")

t1 = "D-39452021-20200227031459-9558"
t2 = "W-39452021-20200226222512-9557"
t3 = "I-39452021-20200225033225-9556"
t4 = "X-39452021-20200224111531-9555"

my_transactions = [t1, t2, t3, t4]

for t in my_transactions:
    temp = txn_look_up(t, my_tz)
    temp.display_transaction()
    print()
