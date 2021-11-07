from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
import utils
import transactions as tx

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
        assert signatureValidate(signature, txn.payload, self.publicKey)
        return txn


def signatureValidate(signature: str, data, publicKey:str) -> bool:
    signatureBytes = bytes.fromhex(signature)
    dataHash = utils.hash(data)
    publicKeyRSA = RSA.importKey(publicKey)
    return  PKCS1_v1_5.new(publicKeyRSA).verify(dataHash,signatureBytes)