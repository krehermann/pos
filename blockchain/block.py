import time
import transactions as txn
from typing import List
import json

class Payload:
    """
    Payload: represents the content of block


    transactions: list of transactions
    forger: string. public key of entity that created the block. TODO this should be validated and/or not a string
    previousHash: string. value of hash of previous block. TODO validation of some sort
    """
    def __init__(self,transactions:List[txn.Transaction], forger:str, previousHash) -> None:
        self.transactions = transactions
        self.forger = forger
        self.previousHash = previousHash
        self.time = time.time()

    def toJSON(self):
        return json.dumps(self, default=lambda x: x.__dict__)

class Block:
    """
    Block: payload + signature
    """

    def __init__(self,payload:Payload) -> None:
        self._payload = payload #Payload(transactions,forger,previousHash)
        self.signature = ''

    def toJSON(self):
        return json.dumps(self, default=lambda x: x.__dict__)
        
    def sign(self, signature:str) -> None:
        """

        signature: string. rsa signature of the block. todo: validate format?
        """
        self.signature = signature