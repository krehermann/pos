
import p2p
import transaction_pool
from transactions import Transaction
import wallet

import blockchain as bc
import utils

class Node:
    def __init__(self, host='localhost', port=50050, peer=None,peerHost=None, peerPort=None, debug=False) -> None:
        self._host = host
        self._port = port
 
        self._wallet = wallet.Wallet()
        self._transaction_pool = transaction_pool.SecurePool()
        self._p2p = p2p.P2PNode(host,port,txn_pool=self._transaction_pool, peer=peer,peerHost=peerHost, peerPort=peerPort, debug=debug)
        self._blockchain = bc.Chain()


    @property
    def blockchain(self):
        return self._blockchain

    @property
    def pool(self):
        return self._transaction_pool

    @property
    def p2p(self):
        return self._p2p

    def start(self):
        self._p2p.start()
