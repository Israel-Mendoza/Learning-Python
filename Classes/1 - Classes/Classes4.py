# Working with class and instance attributes


class BankAccount:
    apr = 1.2


# Check BankAccount's namespace where the "apr" attribute must be available
print(f"BankAccount's namespace:")
for k in BankAccount.__dict__:
    print(f"BankAccount.{k}: {BankAccount.__dict__[k]}")
print()

# Instantiating BankAccount
acc1 = BankAccount()
acc2 = BankAccount()

# Confirm the namespace is empty:
print(f"'acc1' and 'acc2' namespaces are empty: {acc1.__dict__}, {acc2.__dict__}\n")

# Instances request nonlocal attributes to BankAccount
print(f"Although the namespaces are empty, they contain the 'apr' attribute:")
print(f"acc1.apr = {acc1.apr}")  # Takes the apr attribute from the BankAccount class
print(f"acc2.apr = {acc2.apr}\n")  # Takes the apr attribute from the BankAccount class

# Adding attributes to the BankAccount class:
setattr(BankAccount, "account_type", "savings")

# Check BankAccount's namespace where the "account_type" attribute must be available
print(f"Added the 'account_type' attribute to the BankAccount class:")
for k in BankAccount.__dict__:
    if k == "apr" or k == "account_type":
        print(f"BankAccount.{k}: {BankAccount.__dict__[k]}")
print()

# Instances request nonlocal attributes to BankAccount
print(f"Although the namespaces are empty, they contain the 'account_type' attribute:")
print(f"acc1.account_type = {acc1.account_type}")
print(f"acc2.account_type = {acc2.account_type}\n")

# Modifying a class attribute through one of the instance:
acc2.apr = 1.3
print(f"'acc1' and 'acc2' namespaces: {acc1.__dict__}, {acc2.__dict__}\n")

# The BankAccount will not see the changes:
print(f"The attribute modification through the instance doesn't change the class;")
for k in BankAccount.__dict__:
    if k == "apr" or k == "account_type":
        print(f"BankAccount.{k}: {BankAccount.__dict__[k]}")
print()

# Deleting an attribute from the instance's namespace
delattr(acc2, "apr")
print(f"Deleted the 'apr' attribute from the 'acc2' instance.")
print(f"'acc1' and 'acc2' namespaces: {acc1.__dict__}, {acc2.__dict__}")
print(f"Although the attribute was deleted, it's still inherited from the class:")
print(f"acc2.apr = {acc2.apr}\n")

# Setting attributes using the namespace's dictionary:
acc1.__dict__["bank_name"] = "Chase"
acc2.__dict__["is_open"] = False

# Retrieving the new attributes:
print(f"acc1.bank_name: {getattr(acc1, 'bank_name', None)}")
print(f"acc2.is_open: {acc2.is_open}")

# ---> OPTIONAL <---
# Adding attributes with spaces in between
setattr(acc2, "bank name", "BB&T")
print(acc2.__dict__)
print(getattr(acc2, "bank name", None))
