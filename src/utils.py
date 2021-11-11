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
    return  PKCS1_v1_5.new(publicKeyRSA).verify(dataHash,signatureBytes)

def encode(data) -> str:
    #jsonpickle.
    #return pickle.dumps(data)
    jsonpickle.set_encoder_options('simplejson')
    return jsonpickle.encode(data, unpicklable=True)
    #return json.dumps(data)

def decode(data:str, classes=None):
    #return pickle.loads(data)
    #print("trying to decode ", data)
    #return jsonpickle.decode(data, classes=classes, keys=True)
   # if isinstance(data,dict):
    #    return data.
    jsonpickle.set_decoder_options('simplejson')
    return json.loads(data)