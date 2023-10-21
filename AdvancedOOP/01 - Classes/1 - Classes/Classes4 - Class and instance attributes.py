"""Working with class and instance attributes"""

# Classes and instances have a "namespace" 
# where they store the attributes they hold. 
# When we ask an instance to return an attribute 
# that is not in its namespace,
# it asks the superclass for it instead.
# These namespaces are contained in the __dict__ attribute.


class BankAccount:
    apr = 1.2


# Check BankAccount's namespace where the "apr" attribute must be available
print(f"BankAccount's namespace:")
for k in BankAccount.__dict__:
    print(f"BankAccount.{k}: {BankAccount.__dict__[k]}")
# BankAccount.__module__: __main__
# BankAccount.apr: 1.2
# BankAccount.__dict__: <attribute '__dict__' of 'BankAccount' objects>
# BankAccount.__weakref__: <attribute '__weakref__' of 'BankAccount' objects>
# BankAccount.__doc__: None

# Instantiating BankAccount
acc1 = BankAccount()
acc2 = BankAccount()

# Confirm the namespace is empty:
print(f"{acc1.__dict__ = }, {acc2.__dict__ = }\n")
# acc1.__dict__ = {}, acc2.__dict__ = {}

# Instances request nonlocal attributes to BankAccount
print(f"{acc1.apr = }")  # Takes the apr attribute from the BankAccount class
# acc1.apr = 1.2
print(f"{acc2.apr = }\n")  # Takes the apr attribute from the BankAccount class
# acc1.apr = 1.2

# Adding attributes to the BankAccount class:
setattr(BankAccount, "account_type", "savings")

# Check BankAccount's namespace where the "account_type" attribute must be available
for k in BankAccount.__dict__:
    if k == "apr" or k == "account_type":
        print(f"BankAccount.{k}: {BankAccount.__dict__[k]}")
# BankAccount.apr: 1.2
# BankAccount.account_type: savings

# Instances request nonlocal attributes to BankAccount
print(f"{acc1.account_type = }")
# acc1.account_type = 'savings'
print(f"{acc2.account_type = }")
# acc2.account_type = 'savings'

# Modifying a class attribute through one of the instance:
acc2.apr = 1.3
print(f"{acc1.__dict__ = }, {acc2.__dict__ = }")
# acc1.__dict__ = {}, acc2.__dict__ = {'apr': 1.3}

# The BankAccount will not see the changes:
for k in BankAccount.__dict__:
    if k == "apr" or k == "account_type":
        print(f"BankAccount.{k}: {BankAccount.__dict__[k]}")
# BankAccount.apr: 1.2
# BankAccount.account_type: savings

# Deleting an attribute from the instance's namespace
delattr(acc2, "apr") # Or "del acc2.apr"
print(f"{acc1.__dict__ = }, {acc2.__dict__ = }")
# acc1.__dict__ = {}, acc2.__dict__ = {}

# The instance can still get the attribute from the class
print(f"{acc2.apr = }")
# acc2.apr = 1.2

# Setting attributes using the namespace's dictionary:
acc1.__dict__["bank_name"] = "Chase"
# Also done:
# acc1.bank_name = "Chase"
# setattr(acc1, "bank_name", "Chase")
acc2.__dict__["is_open"] = False
# Also done:
# acc1.is_open = False
# setattr(acc1, "is_open", False)

# Retrieving the new attributes:
print(f"{getattr(acc1, 'bank_name', None) = }")
print(f"{acc2.is_open = }")
# getattr(acc1, 'bank_name', None) = 'Chase'
# acc2.is_open = False

"""Attributes with spaces in between"""

# There are two ways to add attributes with spaces to an instance:
setattr(acc2, "bank name", "BB&T")
acc2.__dict__["branch name"] = "Belt Line"

# Checking the instance's namespace:
print(acc2.__dict__)
# {'is_open': False, 'bank name': 'BB&T', 'branch name': 'Belt Line'}

# Retrieving an attribute with spaces in its name
print(f"{getattr(acc2, 'bank name', None) = }")
# getattr(acc2, 'bank name', None) = 'BB&T'
print(f"{acc2.__dict__['branch name'] = }")
# acc2.__dict__['branch name'] = 'Belt Line'
