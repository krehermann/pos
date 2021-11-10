#from Crypto.Hash import SHA256
from Crypto.Hash import SHA256
import json
#import bytes
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

def hash(data) -> SHA256.SHA256Hash:
    # is pickle backward compatable?
    jsonStr = json.dumps(data, default=lambda x: x.__dict__)
    
    return SHA256.new(bytes(jsonStr, 'utf-8'))

def signatureValidate(signature: str, data, publicKey:str) -> bool:
    signatureBytes = bytes.fromhex(signature)
    dataHash = hash(data)
    publicKeyRSA = RSA.importKey(publicKey)
    return  PKCS1_v1_5.new(publicKeyRSA).verify(dataHash,signatureBytes)