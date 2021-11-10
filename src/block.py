import time
import transactions as txn
from typing import List
import json

class Payload:
    """
    Payload: represents the content of block


    transactions: list of transactions
    forger: string. public key of entity that created the block. TODO this should be validated and/or not a string
    previousHash: string. hexdigest of hash of previous block. TODO validation of some sort
    """
    def __init__(self,transactions:List[txn.Transaction], forger:str, previousHash:str) -> None:
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

    @property
    def payload(self):
        return self._payload

    def toJSON(self):
        return json.dumps(self, default=lambda x: x.__dict__)
        
    def sign(self, signature:str) -> None:
        """

        signature: string. rsa signature of the block. todo: validate format?
        """
        self.signature = signature

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Block):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.payload.time == o.payload.time and \
            self.payload.transactions == o.payload.transactions and \
                self.payload.forger == o.payload.forger and \
                    self.payload.previousHash == o.payload.previousHash 


    def equals(self, other) -> bool:
        return self.payload == other.payload