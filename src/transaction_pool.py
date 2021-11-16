from typing import List
import json
import utils
import transactions as txn

class Pool:
    def __init__(self) -> None:
        self._transactions = {}

    def addTransaction(self, transaction: txn.Transaction) -> None:
        if transaction.payload.id not in self._transactions:
            self._transactions[transaction.payload.id] = transaction
        else:
            raise ValueError("transaction %s already exists", transaction.payload.id)
    
    def length(self) -> int:
        return len(self._transactions.keys())

    def transactions(self) -> List[txn.Transaction]:
        return list(self._transactions.values())

    def delete(self, transactions:List[txn.Transaction]):
        for tx in transactions:
            # delete tx
            self._transactions.pop(tx.id,None)
    
    def get(self, transaction: txn.Transaction) -> txn.Transaction:
        return self._transactions[transaction.payload.id]
            
    def toJSON(self):
        return json.dumps(self, default=lambda x: x.__dict__)



class SecurePool(Pool):
    def __init__(self) -> None:
        super().__init__()
    

    def addTransaction(self, transaction: txn.Transaction) -> None:
        wasAdded=False
        try:
            if utils.signatureValidate(transaction.signature, transaction.payload, transaction.payload.senderPublicKey):
                try:
                    super().addTransaction(transaction)
                    wasAdded = True
                except ValueError as ve:
                    print("transaction not added ", ve)
        except ValueError as e:
            print("addTransaction:", e)
        return wasAdded