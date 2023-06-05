import pytz
from Bank import Bank
from time import sleep
from random import randint, choice

# Creating a Bank object
banamex = Bank("CitiBanamex")

# Setting up my preferred timezone:
mx_tz = pytz.timezone("America/Mexico_City")

# Creating a BankAccount object from the existent Bank object
my_account = banamex.create_account("Israel", "Mendoza", 5000, mx_tz)

# Appending the deposit, withdraw, and apply interest methods to a list to
# juggle them in the loops below
transactions = [my_account.deposit, my_account.withdraw, my_account.apply_interest]

for i in range(0, 25):
    method = choice(transactions)
    if method is transactions[2]:   # If method is apply interest
        method()                    # Apply interest doesn't take arguments
    else:
        method(randint(0, 5000))    # Deposit and withdrawals do take arguments
    # Sleeping half a second between each transaction,
    # to make sure the transactions ID will have different values
    sleep(.5)

# Looping through the transactions list ans printing the IDs
for txn in my_account.transaction_list:
    print(txn.transaction_id)

# Using the last txn value left by the loop to test the
# "transaction_lookup" method in the bank instance
last_txn = banamex.transaction_lookup(txn.transaction_id)

# Print the object return by the last test:
print(last_txn)
