import time
import uuid
import json
from enum import Enum

class Payload:
    
    def __init__(self,senderPublicKey, recieverPublicKey,amount, type):
        self.senderPublicKey = senderPublicKey
        self.recieverPublicKey = recieverPublicKey
        self.amount = amount
        self.type = type
        self.createdAt = time.time()
        self.id = uuid.uuid4().hex

    def toJSON(self):
        return json.dumps(self, default=lambda x: x.__dict__)

class TransactionType(str,Enum):
    TRANSFER = "TRANSFER"
    EXCHANGE = "EXCHANGE"



class Transaction:
    """ Transaction class
    """
    def __init__(self,senderPublicKey, recieverPublicKey,amount, type: TransactionType):
        self._payload = Payload(senderPublicKey,recieverPublicKey,amount,type)
        self._signature = ''

    @property
    def payload(self):
        return self._payload

    @property
    def id(self):
        return self._payload.id
        
    @property
    def signature(self):
        return self._signature

    @property
    def type(self):
        return self._payload.type
        
    @signature.setter 
    def signature(self, value):
        self._signature = value

    def toJSON(self):
        #TODO this serializes private _paload. Seems like it ought to serialize payload instead
        return json.dumps(self, default=lambda x: x.__dict__)
        
    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Transaction):
            return False
        return self.payload.id == o.payload.id