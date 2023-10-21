from types import MethodType
import pytz
from Bank import Bank
from time import sleep
from random import randint, choice
from BankAccount import BankAccount
from Transaction import BankTransaction

# Creating a Bank object
banamex: Bank = Bank("CitiBanamex")

# Setting up my preferred timezone:
mx_tz = pytz.timezone("America/Mexico_City")

# Creating a BankAccount object from the existent Bank object
my_account: BankAccount = banamex.create_account("Israel", "Mendoza", 5000, mx_tz)

# Appending the deposit, withdraw, and apply interest methods to a list to
# juggle them in the loops below
transactions: list[MethodType] = [my_account.deposit, my_account.withdraw, my_account.apply_interest]

for i in range(0, 25):
    method: MethodType = choice(transactions)
    if method is transactions[2]:   # If method is "apply interest"
        method()                    # Apply interest doesn't take arguments
    else:
        method(randint(0, 5000))    # Deposit and withdrawals do take arguments
    # Sleeping half a second between each transaction,
    # to make sure the transactions ID will have different values
    sleep(.5)

# Looping through the transactions list and printing the IDs
txn: BankTransaction = my_account.transaction_list[0] if my_account.transaction_list else None
for txn in my_account.transaction_list:
    print(txn.transaction_id)

# Using the last txn value left by the loop to test the
# "transaction_lookup" method in the bank instance
last_txn: BankTransaction = banamex.transaction_lookup(txn.transaction_id)

# Print the object return by the last test:
print(last_txn)
