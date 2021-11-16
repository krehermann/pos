import os, sys
import requests
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from server import TransactionMessage
from wallet import Wallet
from transactions import TransactionType
import utils

if __name__ == "__main__":
    alice = Wallet()
    bob= Wallet()
    exchange = Wallet()

    print("alice pub", alice.publicKey)
    txn = exchange.newTransaction(alice.publicKey, 10, TransactionType.EXCHANGE)

    url = "http://127.0.0.1:5001/transaction"
    msg = {"transaction": utils.encode(txn)}
    resp = requests.post(url,json=msg)
    if resp.status_code != 201:
        print("resp err", resp.content)