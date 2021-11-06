from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
import utils

class Wallet:
    def __init__(self):
        self._keyPair = RSA.generate(2048)
        self._signer = PKCS1_v1_5.new(self._keyPair)

    def sign(self, data):
        hashed = utils.hash(data)
        return self._signer.sign(hashed)