#from Crypto.Hash import SHA256
from Crypto.Hash import SHA256
import pickle

def hash(data):
    # is pickle backward compatable?
    bytes = pickle.dumps(data)
    return SHA256.new(bytes)