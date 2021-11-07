
import transactions as txn
class Pool:
    def __init__(self) -> None:
        self._transactions = {}

    def addTransaction(self, transaction: txn.Transaction) -> None:
        if transaction.payload.id not in self._transactions:
            self._transactions[transaction.payload.id] = transaction
        else:
            raise ValueError("transaction already exists")
    
    def length(self) -> int:
        return len(self._transactions.keys())