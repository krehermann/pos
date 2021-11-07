import transactions as txn
import transaction_pool as txpool
import pytest

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

    