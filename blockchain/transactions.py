import time
import uuid

class transaction:
    """ Transaction class
    """
    def __init__(self,senderPublicKey, recieverPublicKey,amount, type):
        self.senderPublicKey = senderPublicKey
        self.recieverPublicKey = recieverPublicKey
        self.amount = amount
        self.type = type
        self.createdAt = time.time()
        self.id = uuid.uuid4().hex
        self.signature = ''

