from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
import utils
import transactions as tx
import json

import block
class Wallet:
    def __init__(self):
        self._keyPair = RSA.generate(2048)
        self._signer = PKCS1_v1_5.new(self._keyPair)
    
    @property
    def publicKey(self):
        return self._keyPair.publickey().exportKey('PEM').decode('utf-8')

    def sign(self, data):
        hashed = utils.hash(data)
        return self._signer.sign(hashed).hex()

    def newTransaction(self, reciever, amount, type):
        txn = tx.Transaction(self.publicKey, reciever, amount, type)
        signature = self.sign(txn.payload)
        txn.signature = signature
        assert utils.signatureValidate(signature, txn.payload, self.publicKey)
        return txn

    def toJSON(self):
        return json.dumps(self, default=lambda x: x.__dict__)
        

    def forgeBlock(self, payload: block.Payload) -> block.Block:
        forged = block.Block(payload)
        signature = self.sign(payload)
        forged.sign(signature)
        assert utils.signatureValidate(signature, payload, self.publicKey)
        return forged