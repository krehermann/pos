
import p2p
import transaction_pool
from transactions import Transaction
import wallet

import blockchain as bc
import utils

class Node:
    def __init__(self, host='localhost', port=50050) -> None:
        self._host = host
        self._port = port
        self._p2p = p2p.P2PNode(host,port)
        self._wallet = wallet.Wallet()
        self._transaction_pool = transaction_pool.Pool()

        self._blockchain = bc.Chain()


    @property
    def blockchain(self):
        return self._blockchain

    @property
    def pool(self):
        return self._transaction_pool

    def start(self):
        self._p2p.start()

    def handleTransaction(self, txn:Transaction) -> bool:
        wasAdded=False
        if utils.signatureValidate(txn.signature, txn.payload, txn.payload.senderPublicKey):
            try:
                self._transaction_pool.addTransaction(txn)
                wasAdded = True
            except ValueError as ve:
                print("transaction not added ", ve)
        return wasAdded