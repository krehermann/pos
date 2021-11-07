#from Crypto.Hash import SHA256
from Crypto.Hash import SHA256
import pickle

from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

def hash(data):
    # is pickle backward compatable?
    bytes = pickle.dumps(data)
    return SHA256.new(bytes)

def signatureValidate(signature: str, data, publicKey:str) -> bool:
    signatureBytes = bytes.fromhex(signature)
    dataHash = hash(data)
    publicKeyRSA = RSA.importKey(publicKey)
    return  PKCS1_v1_5.new(publicKeyRSA).verify(dataHash,signatureBytes)