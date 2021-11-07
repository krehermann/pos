import time
import uuid

class Payload:
    
    def __init__(self,senderPublicKey, recieverPublicKey,amount, type):
        self.senderPublicKey = senderPublicKey
        self.recieverPublicKey = recieverPublicKey
        self.amount = amount
        self.type = type
        self.createdAt = time.time()
        self.id = uuid.uuid4().hex

    def toJSON(self):
        return self.__dict__

class Transaction:
    """ Transaction class
    """
    def __init__(self,senderPublicKey, recieverPublicKey,amount, type):
        self._payload = Payload(senderPublicKey,recieverPublicKey,amount,type)
        self._signature = ''

    @property
    def payload(self):
        return self._payload

    @property
    def signature(self):
        return self._signature
        
    @signature.setter 
    def signature(self, value):
        self._signature = value

    def toJSON(self):
        return self.__dict__