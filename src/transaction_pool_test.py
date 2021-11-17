import transactions as txn
import transaction_pool as txpool
import pytest

from wallet import Wallet

def test_add_txn():
    pool = txpool.Pool()
    txn1 = txn.Transaction("sender", "reciever", 10, 1)
    txn2 = txn.Transaction("sender", "reciever", 20, 1)

    pool.addTransaction(txn1)
    assert pool.length() == 1
    pool.addTransaction(txn2)
    assert pool.length() == 2
    with pytest.raises(ValueError) as e_info:
        pool.addTransaction(txn1)

def test_secure_pool():

    securePool = txpool.SecurePool()
    alice = Wallet()
    exchange = Wallet()

    tx = txn.Transaction(exchange.publicKey, alice.publicKey,10, txn.TransactionType.EXCHANGE)
    assert securePool.addTransaction(tx) == True
    assert securePool.length() == 1

    unsignedTx =  txn.Transaction("sender", "reciever", 10, 1)
    assert securePool.addTransaction(unsignedTx) == False
    assert securePool.length() == 1

def test_delete():
    pool = txpool.Pool()
    txn1 = txn.Transaction("sender", "reciever", 10, 1)
    txn2 = txn.Transaction("sender", "reciever", 20, 1)
    pool.addTransaction(txn1)
    pool.addTransaction(txn2)
    assert pool.length() == 2
    pool.delete([txn1])
    assert pool.length() ==1
    with pytest.raises(KeyError) as e_info:
        pool.get(txn1)
    assert pool.get(txn2) is not None