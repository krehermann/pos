#import pytest
import transactions as tx

def test_transaction():
    txn = tx.Transaction("sender", "reciever",10,1)
    assert txn.senderPublicKey == "sender"
    assert txn.recieverPublicKey == "reciever"
    assert txn.amount == 10 
    assert txn.type == 1
    
