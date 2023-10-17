from BankAccount import BankAccount


class Bank:

    def __init__(self, bank_name: str):
        self._bank_name = bank_name
        self._last_account_number = 1_001_000
        self._active_accounts = []
        self._inactive_accounts = []

    @property
    def active_accounts(self) -> list:
        """The list containing the active accounts in this instance"""
        return self._active_accounts

    @property
    def inactive_accounts(self) -> list:
        """the list containing the inactive accounts in this instance"""
        return self._inactive_accounts

    def create_account(self, first_name: str, last_name: str, initial_deposit: float, preferred_tz) -> BankAccount:
        self._last_account_number += 1
        new_account = BankAccount(first_name, last_name, self._last_account_number, initial_deposit, preferred_tz)
        self._active_accounts.append(new_account)
        return new_account

    def delete_account(self, account_number: int):
        if isinstance(account_number, int):
            if account_number in self._active_accounts:
                self._active_accounts.remove(account_number)
                self._inactive_accounts.append(account_number)
                print(f"Account number <{account_number}> was successfully removed...")
            else:
                print(f"Account <{account_number}> does not exist...")
        else:
            try:
                account_number = int(account_number)
                if account_number in self._active_accounts:
                    self._active_accounts.remove(account_number)
                    self._inactive_accounts.append(account_number)
                    print(f"Account number <{account_number}> was successfully removed...")
                else:
                    print(f"Account <{account_number}> does not exist...")
            except ValueError:
                print("Please provide a valid account number and try again...")

    def transaction_lookup(self, transaction_id: str):
        _, account_num, _ = transaction_id.split("-")
        account_num = int(account_num)
        account = self.account_lookup(account_num)
        if account:
            for txn in account.transaction_list:
                if txn.transaction_id == transaction_id:
                    return txn
            return None
        else:
            print("Account does not exist...")

    def account_lookup(self, account_number: int) -> BankAccount:
        for account in self.active_accounts:
            if account_number == account.account_number:
                return account
        return None
