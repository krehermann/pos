#from Crypto.Hash import SHA256
from Crypto.Hash import SHA256
import json
import jsonpickle
#import bytes
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
import pickle
def hash(data) -> SHA256.SHA256Hash:
    # is pickle backward compatable?
    jsonStr = json.dumps(data, default=lambda x: x.__dict__)
    
    return SHA256.new(bytes(jsonStr, 'utf-8'))

def signatureValidate(signature: str, data, publicKey:str) -> bool:
    signatureBytes = bytes.fromhex(signature)
    dataHash = hash(data)
    publicKeyRSA = RSA.importKey(publicKey)
    isValid = False
    try:
        PKCS1_v1_5.new(publicKeyRSA).verify(dataHash,signatureBytes)
        isValid = True
    except ValueError as ve:
        print("invalid transaction")
    return isValid

def encode(data) -> str:
    jsonpickle.set_encoder_options('simplejson')
    return jsonpickle.encode(data, unpicklable=True)


def decode(data:str, classes=None):
    jsonpickle.set_decoder_options('simplejson')
    return jsonpickle.loads(data)

def keyFromFile(filePath) -> RSA.RsaKey:
    with open(filePath, 'r') as keyFile:
        data = keyFile.read()
        return RSA.importKey(data)