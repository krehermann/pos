
class AccountStatement:
    def __init__(self, account:str, balance=0) -> None:
        self._id = account
        self._balance = balance

    @property
    def balance(self):
        return self._balance


class AccountBook:
    def __init__(self) -> None:
        self._balances = {}

    def create(self, account: str, balance =0) -> None:
        """
        account: hex of public key
        """

        if account not in self._balances.keys():
            self._balances[account] = balance
    
    def list(self):
        return self._balances.keys()

    def get(self, account:str) -> AccountStatement:
        if account not in self._balances.keys():
            raise ValueError
        balance = self._balances[account]
        return AccountStatement(account, balance)



    def update(self, account:str, amount):
        if account not in self._balances.keys():
            raise ValueError
        newAmount = self._balances[account] + amount
        if newAmount < 0:
            raise ValueError
        self._balances[account] = newAmount